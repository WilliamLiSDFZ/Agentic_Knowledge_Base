import json
import subprocess
from pathlib import Path

DEST = Path('/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.11/s54_s56_review')
RUNS = ['20260911_071931_jubias-base-s54', '20260911_072108_jubias-base-s55', '20260911_072344_jubias-base-s56', '20260911_072808_jubias-anaf-s54', '20260911_072611_jubias-anaf-s55', '20260911_072611_jubias-anaf-s56']
script = '''
import json
from pathlib import Path
runs = RUN_LIST
for run in runs:
 root = Path('/workspace/MLEvolve/runs') / run / 'workspace/candidate_results/candidates'
 for p in sorted(root.iterdir()):
  if not p.is_dir(): continue
  out = {'run':run,'node_id':p.name,'files':{}}
  for name in ['solution.py','execution_spec.json','worker_finished.json','execution.json','review.json']:
   f=p/name
   if f.is_file():out['files'][name]=f.read_text()
  print(json.dumps(out),flush=True)
'''.replace('RUN_LIST', repr(RUNS))
cmd = ['kubectl','--context','nautilus','-n','ecepxie','exec','mlevolve-agentic-knowledge-base-dev-cpu','--','python3','-u','-c',script]
result = subprocess.run(cmd,capture_output=True,text=True,check=True)
count=0
for line in result.stdout.splitlines():
 data=json.loads(line)
 folder=DEST/'cluster_sources'/data['run']/data['node_id']
 folder.mkdir(parents=True,exist_ok=True)
 for name,content in data['files'].items():(folder/name).write_text(content)
 count+=1
print('Saved',count,'candidates to',DEST/'cluster_sources')
