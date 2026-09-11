"""Read-only analysis of the captured S54-S56 live diagnostics."""
import datetime as dt
import json
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent
TZ = ZoneInfo('America/Los_Angeles')
def readlines(name):
    return [json.loads(line) for line in (ROOT / name).read_text().splitlines() if line]

history = {row['kind']: row for row in readlines('gpu_history.jsonl')}
averages = {s['metric']['pod']: float(s['value'][1]) for s in history['average']['result']['data']['result']}
compact = readlines('compact_logs.jsonl')
summary = {'gpu_average_percent': averages, 'closed_at_five_steps': [], 'events_by_run': {}, 'errors': readlines('candidate_errors.jsonl')}
for run in compact:
    nodes = []
    for nid, raw in run['events'].items():
        events = [json.loads(line) for line in raw.splitlines() if line]
        smoke = next((e for e in events if e['event'] == 'smoke_passed'), None)
        validation = [e for e in events if e['event'] == 'validation']
        closed = next((e for e in events if e['event'] == 'worker_finished'), None)
        published = [e for e in events if e['event'] == 'snapshot_published']
        training = next((e for e in events if e['event'] == 'training_started'), None)
        row = {'node': nid, 'preparation_minutes': training['elapsed_seconds'] / 60 if training else None,
               'first_validation': validation[0] if validation else None,
               'best_published_metric': max((e['metric'] for e in published), default=None),
               'closed': closed}
        if smoke and validation:
            row['smoke_validation_overestimate'] = smoke['estimated_validation_seconds'] / validation[0]['duration_seconds']
            row['initial_reserve_minutes'] = 1.5 * (2 * smoke['estimated_validation_seconds'] + smoke['estimated_test_seconds']) / 60
        if closed and validation and max(e['optimizer_steps'] for e in validation) == 5:
            summary['closed_at_five_steps'].append({'run': run['run'], **row})
        nodes.append(row)
    summary['events_by_run'][run['run']] = nodes
(ROOT / 'summary.json').write_text(json.dumps(summary, indent=2))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
series = history['range']['result']['data']['result']
fig, axes = plt.subplots(3, 2, figsize=(15.5, 8.2), sharex=True, sharey=True)
start = dt.datetime.fromtimestamp(history['range']['start'], TZ)
end = dt.datetime.fromtimestamp(history['range']['end'], TZ)
for seed, pair in zip((54, 55, 56), axes):
    for arm, tag, ax in zip(('A', 'F'), ('base', 'anaf'), pair):
        item = next(s for s in series if f'-{tag}-s{seed}-' in s['metric']['pod'])
        pod = item['metric']['pod']
        values = [(dt.datetime.fromtimestamp(t, TZ), float(v)) for t, v in item['values']]
        xs, ys = zip(*values)
        color = '#287ca5' if arm == 'A' else '#d27b31'
        ax.plot(xs, ys, color=color, lw=1, alpha=0.45)
        smoothed = [sum(ys[max(0, i-4):i+1]) / len(ys[max(0, i-4):i+1]) for i in range(len(ys))]
        ax.plot(xs, smoothed, color=color, lw=2)
        ax.set_title(f'{arm} S{seed}  |  mean over recorded samples: {averages[pod]:.1f}%', fontsize=11, loc='left')
        ax.set_ylim(-3, 105)
        ax.set_xlim(start, end)
        ax.set_yticks((0, 50, 100))
        ax.grid(alpha=0.18)
        ax.spines[['top', 'right']].set_visible(False)
        if seed == 56 and arm == 'F':
            stopped = dt.datetime.fromisoformat('2026-09-11T01:06:48+00:00').astimezone(TZ)
            ax.axvspan(stopped, end, color='#d0d0d0', alpha=0.35)
            ax.axvline(stopped, color='#9a4d48', ls='--', lw=1)
            ax.text(0.23, 0.52, 'Pod removed; later measurements unavailable\nJob failed at 18:06 PDT', transform=ax.transAxes,
                    color='#6a5553', fontsize=11, ha='left')
        ax.xaxis.set_major_locator(mdates.MinuteLocator(byminute=(0, 30), tz=TZ))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M', tz=TZ))
        if arm == 'A': ax.set_ylabel('GPU utilization (%)')
        if seed == 56: ax.set_xlabel('September 10, 2026 — PDT')
fig.suptitle('Jigsaw S54–S56 GPU utilization since startup', x=0.06, ha='left', fontsize=17)
fig.text(0.06, 0.915, 'Prometheus DCGM metrics · thin line: 1-minute samples · thick line: trailing 5-sample mean', fontsize=10, color='#666666')
fig.text(0.06, 0.02, 'High GPU utilization includes validation and prediction export; it does not imply useful training progress. Gaps are not treated as zero.', fontsize=10, color='#666666')
fig.subplots_adjust(left=0.06, right=0.98, top=0.87, bottom=0.09, hspace=0.4, wspace=0.16)
fig.savefig(ROOT / 'gpu_history.png', dpi=160)
plt.close(fig)
print(json.dumps({'closed_at_five_steps': len(summary['closed_at_five_steps']), 'gpu_averages': averages}, indent=2))
