"""Read-only analysis of the six completed/partially recovered Sol launches.

Writes only this review directory. The A57 recovery uses saved public selection,
not private-test selection; see recover_a57.py and a57_recovered_scores.json.
"""
import csv
import json
import re
from collections import Counter
from pathlib import Path

OUT = Path(__file__).resolve().parent
SOURCE = Path('/Users/william/nautilus/results')
RUNS = {
    'A57': '20260912_081234_jubias-base-gpt56sol-s57',
    'F57': '20260912_082449_jubias-anaf-gpt56sol-s57',
    'A58': '20260912_082058_jubias-base-gpt56sol-s58',
    'F58': '20260912_081346_jubias-anaf-gpt56sol-s58',
    'A59': '20260912_082030_jubias-base-gpt56sol-s59',
    'F59': '20260912_082449_jubias-anaf-gpt56sol-s59',
}


def read_json(path):
    return json.loads(path.read_text())


def submissions(lines):
    result = []
    for i, line in enumerate(lines):
        match = re.match(r'\[turn (\d+)\] submit_report\(', line)
        if not match:
            continue
        for after in lines[i + 1:i + 5]:
            if after.startswith('{'):
                response = json.loads(after)
                result.append({'turn': int(match[1]), 'status': response.get('status'),
                               'problems': response.get('problems', [])})
                break
    return result


def main():
    rows = list(csv.DictReader((SOURCE / 'scores.csv').open()))
    inventory = {r['name']: r for r in csv.DictReader((OUT.parent / 'run_inventory.csv').open())}
    recovery = read_json(OUT / 'a57_recovered_scores.json')
    summary = {'runs': {}, 'paired': {}, 'notes': [
        'A57 is post-hoc recovered from saved snapshots; the original run has no final ensemble.',
        'Private scores are rounded by the grader; public validation scores are a different split.',
        'No source run, original scores.csv, grouping or existing chart is changed.',
        'Analogy tokens sum per-request usage, including repeatedly supplied context; they are not unique text or billed cost.',
        'Summed analogy wall seconds are not equivalent to GPU idle seconds.',
    ]}
    for key, name in RUNS.items():
        run = SOURCE / name
        selected = [r for r in rows if r['run'] == name and r['variant'] == 'capped']
        for row in selected:
            assert row['metric_version'] == recovery['provenance']['metric_version']
            assert row['grader_sha256'] == recovery['provenance']['grader_sha256']
        scores = {int(r['k']): float(r['score']) for r in selected}
        if key == 'A57':
            assert not selected
            scores = {r['k']: r['score'] for r in recovery['scores']}
        j = read_json(run / 'logs/journal.json')
        nodes = {n['id']: n for n in j['nodes']}
        node_rows = []
        for n in nodes.values():
            if n['stage'] == 'root':
                continue
            parent_id = j['node2parent'].get(n['id'])
            parent = nodes.get(parent_id, {})
            value = (n.get('metric') or {}).get('value')
            parent_value = (parent.get('metric') or {}).get('value')
            adoption = n.get('analogy_adoption') or {}
            node_rows.append({
                'id': n['id'], 'stage': n['stage'], 'step': n['step'],
                'public_metric': value, 'parent': parent_id,
                'parent_public_metric': parent_value,
                'delta': value - parent_value if value is not None and parent_value is not None else None,
                'buggy': n['is_buggy'], 'valid': n['is_valid'],
                'execution_status': n.get('execution_status'),
                'analogy_report_present': bool(n.get('analogy_report')),
                'adoption': adoption.get('status'),
                'mechanism': (adoption.get('selected_mechanism') or {}).get('title'),
            })
        valid = [n for n in node_rows if n['public_metric'] is not None and n['valid'] and not n['buggy']]
        best = max(valid, key=lambda n: n['public_metric'])
        info = {'run': name, 'source': str(run), 'recovered': key == 'A57',
                'scores': scores, 'inventory': inventory[name], 'nodes': node_rows, 'best': best}
        if key.startswith('F'):
            analogy = run / 'logs/analogy'
            episodes = []
            for line in (analogy / 'index.jsonl').read_text().splitlines():
                raw = json.loads(line)
                context = read_json(analogy / Path(raw['context_trace']).name)
                ledger = (context.get('code_reads') or {}).get('ledger', [])
                episode = {k: raw.get(k) for k in (
                    'invocation', 'stage', 'parent_id', 'ok', 'reason', 'turns',
                    'in_tokens', 'out_tokens', 'seconds', 'report_chars',
                    'fulltext_body_chars', 'fulltext_read_calls', 'fulltext_papers_opened')}
                episode['trace'] = str(analogy / raw['trace'])
                episode['submissions'] = submissions((analogy / raw['trace']).read_text().splitlines())
                episode['models'] = sorted({m.get('model', '') for m in context.get('model_calls', [])})
                episode['code_calls'] = len(ledger)
                episode['code_errors'] = [r['response'].get('reason') for r in ledger
                                          if r.get('response', {}).get('status') == 'error']
                episode['mechanisms'] = [{k: m.get(k) for k in ('title', 'evidence_level', 'paper_ids')}
                                         for m in (context.get('report') or {}).get('mechanisms', [])]
                episodes.append(episode)
            info['episodes'] = episodes
        summary['runs'][key] = info
    for k in [1, 2, 3, 4, 6]:
        deltas = {str(seed): summary['runs'][f'F{seed}']['scores'][k] -
                  summary['runs'][f'A{seed}']['scores'][k] for seed in [57, 58, 59]}
        summary['paired'][k] = {'deltas': deltas,
            'mean_completed_pairs_58_59': (deltas['58'] + deltas['59']) / 2,
            'mean_including_recovered_57': sum(deltas.values()) / 3}
    episodes = [e for r in summary['runs'].values() for e in r.get('episodes', [])]
    summary['analogy_totals'] = {
        'episodes': len(episodes), 'ok': sum(e['ok'] for e in episodes),
        'with_fulltext_read': sum(e['fulltext_read_calls'] > 0 for e in episodes),
        **{k: sum(e[k] for e in episodes) for k in
           ('in_tokens', 'out_tokens', 'seconds', 'fulltext_body_chars', 'code_calls')},
        'evidence_levels': dict(Counter(m['evidence_level'] for e in episodes for m in e['mechanisms'])),
        'code_error_reasons': dict(Counter(reason for e in episodes for reason in e['code_errors'])),
        'rejection_problems': dict(Counter(p for e in episodes for s in e['submissions'] for p in s['problems'])),
        'failed_first_submit_turns': [e['submissions'][0]['turn'] if e['submissions'] else None
                                     for e in episodes if not e['ok']],
        'successful_with_rejected_attempt': sum(e['ok'] and any(s['status'] == 'rejected' for s in e['submissions'])
                                                for e in episodes),
    }
    (OUT / 'summary.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False) + '\n')
    make_chart(summary)
    print(json.dumps({'paired': summary['paired'], 'analogy': summary['analogy_totals'],
                      'best_nodes': {k: v['best'] for k, v in summary['runs'].items()}},
                     indent=2, ensure_ascii=False))


def make_chart(summary):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.1), gridspec_kw={'width_ratios': [1, 1.35]})
    colors = {57: '#0072B2', 58: '#D55E00', 59: '#009E73'}
    for seed in [57, 58, 59]:
        a, f = (summary['runs'][f'{arm}{seed}'] for arm in ['A', 'F'])
        label = f'S{seed}' + (' (A recovered)' if seed == 57 else '')
        axes[0].plot([0, 1], [a['scores'][1], f['scores'][1]], color=colors[seed], linewidth=2, label=label)
        axes[0].scatter([0], [a['scores'][1]], color=colors[seed], s=65,
                         facecolors='white' if seed == 57 else colors[seed], zorder=3)
        axes[0].scatter([1], [f['scores'][1]], color=colors[seed], s=65, zorder=3)
        ks = [1, 2, 3, 4, 6]
        axes[1].plot(ks, [f['scores'][k] - a['scores'][k] for k in ks], 'o-',
                     color=colors[seed], linewidth=2, label=label,
                     markerfacecolor='white' if seed == 57 else colors[seed])
    axes[0].set_xticks([0, 1], ['A: baseline', 'F: draft + improve analogy'])
    axes[0].set_xlim(-.18, 1.25)
    axes[0].set_ylabel('Private score at K = 1 (higher is better)')
    axes[0].set_title('Latest Sol launches: same-seed comparison')
    axes[1].axhline(0, color='#777777', linewidth=1, linestyle='--')
    axes[1].set_xticks([1, 2, 3, 4, 6])
    axes[1].set_xlabel('Top K candidates (existing public ranking, 9 h cap)')
    axes[1].set_ylabel('Private score difference: F − A')
    axes[1].set_title('Positive differences across saved ensemble sizes')
    for ax in axes:
        ax.grid(axis='y', alpha=.2)
        ax.spines[['top', 'right']].set_visible(False)
    axes[0].legend(loc='upper left', fontsize=9)
    fig.suptitle('Jigsaw Unintended Bias · S57 / S58 / S59 · GPT-5.6 Sol', fontsize=15)
    fig.text(.5, .015, 'S57 A: post-hoc recovery of saved predictions; original run did not finish. Small sample; GPU types vary.',
             ha='center', fontsize=9, color='#555555')
    fig.tight_layout(rect=(0, .055, 1, .94))
    fig.savefig(OUT / 'latest_sol_comparison.png', dpi=180)
    plt.close(fig)


if __name__ == '__main__':
    main()
