"""Summarize saved live replay artifacts without model calls or private scores."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent


def summarize(directory):
    rows = []
    for path in sorted(directory.glob('*.context.json')):
        name = path.name.removesuffix('.context.json')
        context = json.loads(path.read_text())
        text = (directory / (name + '.md')).read_text()
        report_section = text.split('# report\n\n', 1)[1]
        report = None
        if '\n```json\n' in report_section:
            report = json.loads(report_section.split('\n```json\n', 1)[1].rsplit('\n```', 1)[0])
        fulltext = json.loads((directory / (name + '.fulltext.json')).read_text())
        stdout = (directory / (name + '.stdout.log')).read_text()
        timing = re.search(r'tokens in/out (\d+)/(\d+) \| ([\d.]+)s', stdout)
        calls = context.get('model_calls', [])
        rows.append({
            'case': name,
            'accepted_report': report is not None and bool(report.get('mechanisms')),
            'mechanisms': [m['title'] for m in (report or {}).get('mechanisms', [])],
            'evidence_levels': [m.get('evidence_level') for m in (report or {}).get('mechanisms', [])],
            'report_chars': len(report_section.split('\n```json\n', 1)[0].strip()) if report else 0,
            'empty_reason': report_section.strip() if report is None else None,
            'model_calls': len(calls),
            'models': sorted({m.get('model') for m in calls if m.get('model')}),
            'efforts': sorted({m.get('returned_reasoning_effort') for m in calls if m.get('returned_reasoning_effort')}),
            'input_tokens_billed': sum(m.get('usage', {}).get('input_tokens', 0) for m in calls),
            'output_tokens': sum(m.get('usage', {}).get('output_tokens', 0) for m in calls),
            'reasoning_tokens': sum(m.get('usage', {}).get('output_tokens_details', {}).get('reasoning_tokens', 0) for m in calls),
            'maximum_actual_input_tokens': max((m.get('usage', {}).get('input_tokens', 0) for m in calls), default=0),
            'maximum_estimated_input_tokens': max((t['estimated_input_tokens'] for t in context['context']['turn_budgets']), default=0),
            'context_counting': context['context']['counting'],
            'code_tool_calls': len((context.get('code_reads') or {}).get('ledger', [])),
            'tool_calls': re.findall(r'^\[turn \d+\] (\w+)\(', text, re.M),
            'fulltext_documents': len(fulltext['documents']),
            'fulltext_read_calls': fulltext['read_calls'],
            'fulltext_body_chars': fulltext['body_chars'],
            'loop_seconds': float(timing.group(3)) if timing else None,
            'rejections': len(re.findall(r'"status": "rejected"', text)),
        })
    return rows


if __name__ == '__main__':
    output = {name: summarize(ROOT / name) for name in ('live', 'live_corrected') if (ROOT / name).exists()}
    (ROOT / 'live_summary.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
    for batch, rows in output.items():
        print(batch)
        for row in rows:
            print(row['case'], 'accepted=', row['accepted_report'], 'turns=', row['model_calls'],
                  'code_reads=', row['code_tool_calls'], 'chars=', row['report_chars'],
                  'actual_max_input=', row['maximum_actual_input_tokens'], 'seconds=', row['loop_seconds'])
