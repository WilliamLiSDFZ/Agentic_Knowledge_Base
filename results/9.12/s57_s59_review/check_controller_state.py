"""CPU-only reproduction using two inspected loss methods, never candidate top-level code."""
import ast
import json
import math
from pathlib import Path
from types import MethodType, SimpleNamespace

import torch

folder = Path(__file__).resolve().parent
checks = []
for name in ("64f9c626", "64405410"):
    tree = ast.parse((folder / f"{name}.py").read_text())
    methods = [n for cls in tree.body if isinstance(cls, ast.ClassDef) for n in cls.body
               if isinstance(n, ast.FunctionDef) and n.name in
               {"_group_dro_family_loss", "commit_group_dro_statistics"}]
    assert len(methods) == 2
    scope = {"torch": torch}
    exec(compile(ast.Module(body=methods, type_ignores=[]), str(folder / f"{name}.py"), "exec"), scope)
    ema = torch.full((9,), math.log(2))
    weights = torch.ones(9) / 9
    sums = torch.zeros(9)
    counts = torch.zeros(9, dtype=torch.long)
    last = torch.zeros(9, dtype=torch.bool)
    obj = SimpleNamespace(identity_count=9, _queue_logits=torch.zeros(1),
                          group_dro_family_names=("subgroup",),
                          _family_buffers=lambda family: (ema, weights, sums, counts, last))
    losses = [torch.tensor((i+1)/10, requires_grad=True) for i in range(9)]
    loss, availability, _ = MethodType(scope["_group_dro_family_loss"], obj)(losses, "subgroup", True)
    loss.backward()
    before_commit = counts.tolist()
    MethodType(scope["commit_group_dro_statistics"], obj)()
    assert availability.all() and counts.eq(0).all() and not last.any()
    assert torch.equal(ema, torch.full((9,), math.log(2)))
    checks.append({"candidate": name, "available_cells_returned": int(availability.sum()),
                   "counts_before_commit": before_commit, "ema_after_commit": ema.tolist(),
                   "weights_after_commit": weights.tolist(),
                   "nonzero_loss_gradients": all(x.grad is not None and x.grad.item() > 0 for x in losses)})

x = torch.zeros(1, 3)
mask = torch.tensor([True, False, True])
x[0, mask].add_(torch.tensor([1., 2.]))
assert x.eq(0).all()
checks.append({"s57_index_update_reproduction": x.tolist()})
print(json.dumps({"device": "cpu", "torch_version": torch.__version__, "checks": checks}))
