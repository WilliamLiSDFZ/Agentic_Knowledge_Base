import json
import subprocess
from pathlib import Path

DEST = Path('/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.11/s54_s56_review')
audit=json.loads((DEST/'runtime_audit.json').read_text())
jobs=[]
for run in audit['runs']:
 for c in run['rows']:
  s=c.get('selected_snapshot')
  if s:
   jobs.append({'run':run['name'],'label':run['label'],'node_id':c['node_id'],'parent_id':c.get('parent_id'),'stage':c['stage'],'snapshot':s})
script='''
import json,sys,hashlib,io
from pathlib import Path
sys.path.insert(0,'/workspace/MLEvolve')
from utils.mlebench_patch import grading_metadata
from mlebench.registry import registry
from mlebench.utils import load_answers,read_csv
import pandas as pd
cid='jigsaw-unintended-bias-in-toxicity-classification'
meta=grading_metadata(cid)
print(json.dumps({'type':'provenance',**meta}),flush=True)
competition=registry.set_data_dir(Path('/workspace/data/mlebench')).get_competition(cid)
answers=load_answers(competition.answers)
jobs=JOB_LIST
for job in jobs:
 s=job.pop('snapshot')
 row={**job,'snapshot_id':s['snapshot_id'],'validation_score':s['metric'],'optimizer_steps':s['optimizer_steps']}
 p=Path('/workspace/MLEvolve/runs')/job['run']/'workspace/candidate_results/candidates'/job['node_id']/'snapshots'/s['snapshot_id']/'submission.csv'
 try:
  data=p.read_bytes()
  digest=hashlib.sha256(data).hexdigest()
  row['submission_sha256']=digest
  if digest!=s['files']['submission.csv']:raise ValueError('submission hash mismatch')
  frame=read_csv(p)
  row['private_score']=float(competition.grader(frame,answers))
 except Exception as e:row['error']=str(e)
 print(json.dumps({'type':'candidate',**row}),flush=True)
'''.replace('JOB_LIST',repr(jobs))
cmd=['kubectl','--context','nautilus','-n','ecepxie','exec','mlevolve-agentic-knowledge-base-dev-cpu','--','/workspace/MLEvolve/.venv/bin/python','-u','-c',script]
with (DEST/'candidate_private_scores.jsonl').open('w') as output:
 proc=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
 count=0
 for line in proc.stdout:
  output.write(line);output.flush()
  try:
   data=json.loads(line)
   if data.get('type')=='candidate':
    count+=1
    print(f"{count}/{len(jobs)} {data['label']} {data['node_id'][:8]} val={data['validation_score']:.5f} private={data.get('private_score',data.get('error'))}",flush=True)
  except Exception:pass
 stderr=proc.stderr.read()
 status=proc.wait()
 if stderr:print(stderr)
 if status:raise SystemExit(status)
print('Completed post-run scoring; no cluster files changed.')
