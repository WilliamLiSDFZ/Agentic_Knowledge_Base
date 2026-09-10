"""Reproduce the local S51–S53 post-run audit; never calls the cluster or an LLM."""
import collections
import csv
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import sys

import yaml

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
RUNS = Path('/Users/william/nautilus/results')
sys.path.insert(0, str(ROOT / 'scripts'))
from analyze_runs import _TagIgnoringLoader


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def classify(node):
    text = ''.join(node.get('_term_out') or [])
    if node.get('is_valid') is True and node.get('is_buggy') is False:
        return 'valid'
    if node.get('exc_type') == 'TimeoutError':
        return 'timeout'
    if 'out of memory' in text.lower():
        return 'oom'
    if 'backward through the graph a second time' in text:
        return 'checkpoint'
    return node.get('exc_type') or 'invalid'


with (RUNS / 'scores.csv').open() as handle:
    scores = [r for r in csv.DictReader(handle) if r['run'].startswith('20260910_')]
summaries = []
for path in sorted(RUNS.glob('20260910_*jubias*')):
    journal_path = path / 'logs/journal.json'
    journal = json.loads(journal_path.read_text())
    nodes = [n for n in journal['nodes'] if n['stage'] != 'root']
    cfg = yaml.load((path / 'logs/config.yaml').read_text(), Loader=_TagIgnoringLoader)
    log = (path / 'logs/MLEvolve.log').read_text()
    start = datetime.strptime(re.search(r'^\[([^,]+),', log).group(1), '%Y-%m-%d %H:%M:%S')
    valid = [n for n in nodes if classify(n) == 'valid']
    first_valid = min((datetime.fromisoformat(n['finish_time']) for n in valid), default=None)
    record = {
        'run': path.name, 'seed': cfg['agent']['seed'],
        'arm': 'F' if cfg['analogy']['enabled'] else 'A',
        'journal_sha256': digest(journal_path),
        'config': {'exec': cfg['exec'], 'parallel_search_num': cfg['agent']['search']['parallel_search_num'],
                   'time_limit': cfg['agent']['time_limit'], 'cpu_number': cfg['cpu_number'],
                   'initial_drafts': cfg['agent']['initial_drafts'],
                   'analogy': {k: cfg['analogy'].get(k) for k in ['enabled', 'draft', 'improve']},
                   'fulltext_enabled': cfg['analogy']['fulltext']['enabled']},
        'started_utc': start.isoformat(),
        'first_valid_h_from_run_start': (first_valid-start).total_seconds()/3600 if first_valid else None,
        'outcomes': dict(collections.Counter(classify(n) for n in nodes)),
        'stages': dict(collections.Counter(n['stage'] for n in nodes)),
        'completed_nodes': len(nodes),
        'completed_candidate_hours': sum(n.get('exec_time') or 0 for n in nodes)/3600,
        'failed_candidate_hours': sum(n.get('exec_time') or 0 for n in nodes if classify(n) != 'valid')/3600,
        'scores': [r for r in scores if r['run'] == path.name],
        'nodes': [], 'analogy_calls': [],
    }
    for n in nodes:
        record['nodes'].append({**{k:n.get(k) for k in ['id','stage','branch_id','metric','created_time','finish_time','exec_time']},
                               'parent_id': journal.get('node2parent', {}).get(n['id']), 'outcome': classify(n),
                               'report_titles': re.findall(r'^### (.+)', n.get('analogy_report') or '', re.M),
                               'report_evidence': re.findall(r'\*\*Evidence level\*\*: (.+)', n.get('analogy_report') or '')})
    idx = path / 'logs/analogy/index.jsonl'
    for line in idx.read_text().splitlines() if idx.exists() else []:
        call = json.loads(line)
        ft = json.loads((idx.parent / call['fulltext_trace']).read_text())
        trace = (idx.parent / call['trace']).read_text()
        injected = trace.split('## Report (as injected)')[-1].split('## Report (raw JSON)')[0]
        call['rendered_evidence_levels'] = re.findall(r'\*\*Evidence level\*\*: (.+)', injected)
        call['download_attempts'] = {k:v['status'] for k,v in ft['attempts'].items()}
        call['read_paper_ids'] = [e['arguments']['paper_id'] for e in ft['events'] if e['tool'] == 'read_paper']
        children = re.findall(r'\[improve\] ' + call['parent_id'] + r' → node ([a-f0-9]+)', log)
        call['generated_child_ids'] = children
        call['completed_child_ids'] = [n['id'] for n in nodes if n['id'] in children]
        record['analogy_calls'].append(call)
    summaries.append(record)

by_pair = {(r['seed'],r['arm']):r for r in summaries}
paired = []
for seed in [51,52,53]:
    values = {}
    for arm in ['A','F']:
        rs = [s for s in by_pair[seed,arm]['scores'] if s['variant']=='capped' and s['k']=='1' and s['score']]
        values[arm] = float(rs[0]['score']) if rs else None
    values['seed'] = seed
    values['F_minus_A'] = values['F']-values['A'] if None not in [values['A'], values['F']] else None
    paired.append(values)
all_calls = [c for r in summaries for c in r['analogy_calls']]
paired_deltas = [p['F_minus_A'] for p in paired if p['F_minus_A'] is not None]
totals = collections.Counter()
for r in summaries:
    totals.update(r['outcomes'])
audit = {'scores_sha256': digest(RUNS/'scores.csv'), 'runs': summaries, 'paired_k1': paired,
         'paired_only_mean': sum(paired_deltas)/len(paired_deltas),
         'totals': dict(totals),
         'paper_open_attempts': dict(collections.Counter(s for c in all_calls for s in c['download_attempts'].values())),
         'analogy_seconds': sum(c['seconds'] for c in all_calls),
         'fulltext_chars': sum(c['fulltext_body_chars'] for c in all_calls)}
(OUT/'audit.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2)+'\n')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, (left,right) = plt.subplots(1,2,figsize=(13.5,5.4),gridspec_kw={'width_ratios':[1,1.1]})
for i,p in enumerate(paired):
    if p['A'] is not None:
        left.plot([i-.14,i+.14],[p['A'],p['F']],color='#adb5bd',lw=1.5,zorder=1)
        left.scatter(i-.14,p['A'],color='#52585f',s=65,label='A baseline' if i==1 else None,zorder=2)
        left.text(i-.16,p['A']+.008,f"{p['A']:.5f}",ha='right',fontsize=9)
    else:
        left.text(i-.14,.757,'A: no submission',ha='center',fontsize=9,color='#a33c32')
    left.scatter(i+.14,p['F'],color='#277fbd',s=65,label='F analogy' if i==0 else None,zorder=2)
    left.text(i+.16,p['F']+.008,f"{p['F']:.5f}",ha='left',fontsize=9)
left.set(xticks=range(3),xticklabels=['S51\nno paired difference','S52\nF - A = -0.01766','S53\nF - A = +0.03652'],
         ylim=(.74,.975),xlim=(-.5,2.7),ylabel='Private score at K=1 (continuous AUC)',
         title='Only two complete A/F pairs')
left.grid(axis='y',alpha=.2)
left.legend(frameon=False,loc='upper right')
ordered=[by_pair[s,a] for s in [51,52,53] for a in ['A','F']]
offset=[0]*6
for name,color,label in [('valid','#439775','valid (all debug)'),('timeout','#d58d49','6-hour timeout'),
                         ('oom','#b85656','CUDA OOM'),('checkpoint','#8970aa','checkpoint backward error'),
                         ('AttributeError','#aaa','other error')]:
    widths=[r['outcomes'].get(name,0) for r in ordered]
    right.barh(range(6),widths,left=offset,color=color,label=label)
    offset=[a+b for a,b in zip(offset,widths)]
right.set(yticks=range(6),yticklabels=[f"{r['arm']}-S{r['seed']}" for r in ordered],
          xlabel='Completed candidate nodes in journal',title='6 valid / 41 completed candidates',xlim=(0,8.2))
right.invert_yaxis()
right.legend(frameon=False,fontsize=8,loc='upper center',bbox_to_anchor=(.5,-.22),ncol=2)
fig.suptitle('Jigsaw S51–S53: run reliability limits the analogy comparison',fontsize=13)
fig.text(.02,.02,'No borrowed baseline. Unfinished candidates are not counted as completed failures. Source: fetched results, 2026-09-10.',fontsize=8,color='#555')
fig.tight_layout(rect=(0,.10,1,.96))
fig.savefig(OUT/'paired_and_failures.png',dpi=160)
plt.close(fig)
print(json.dumps({k:v for k,v in audit.items() if k!='runs'},ensure_ascii=False,indent=2))
print('FIRST_VALID_H',[(r['seed'],r['arm'],r['first_valid_h_from_run_start']) for r in summaries])
