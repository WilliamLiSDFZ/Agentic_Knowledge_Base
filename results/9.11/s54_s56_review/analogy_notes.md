# F S54–56 analogy 证据审计

只读分析。原始日志、图表、生产代码、集群状态均未修改。除末尾专门标记的事后 private 复评分外，本文候选分数均为 **公开固定 validation split 的 composite AUC**，不能当作 private final grade。节点关系来自 candidate_results/candidate.json，分数来自可评分 snapshot manifest；journal.json 缺少尾部节点，未单独依赖它。代码与 cluster_sources 中不可变 solution.py 对照；三个最终获选模型源码的 SHA256 均与 best_solution/manifest.json 相符。

## 1. 首 draft 有实际干预，三个最终获选者都出自它

| Seed | 首个注入 draft 的真实实现 | 首 draft validation | 最终选中链 |
|---|---|---:|---|
| 54 | 18 个 identity-present × toxicity cell 的 EMA 风险动态加权 BCE | 0.9118066 | d24983 → f7be07（0.9100518）→ 27273be（0.9227605，选中） |
| 55 | 训练集 identity × binary-label 频次平方根逆频率权重，裁剪 1–6，重叠组取最大；weighted soft BCE | 0.9279249 | d5978 → 62fdc8（0.9280408）→ 994b5c（0.9288847，选中） |
| 56 | 负类固定缩至正类 3 倍，再按两类逆频率 WeightedRandomSampler replacement=True 做期望类别平衡 | 0.9269353 | 4eed868 首 draft 直接选中；后续 c87f0e 0.9263957，b17384 0.6927282 未获选 |

这说明本批并非“analogy 没有注入或建议完全没用上”。但不能由同一 run 内的分支选择推导因果：首 draft 优先获得执行时间，后续分支架构、预算和随机训练也不同。

S54 实现是论文启发的风险 EMA/样本权重启发式，不是论文的完整 Pareto/梯度冲突优化：每个样本的所属组权重取平均，最后仍按样本聚合 BCE（d24983 solution.py:300–411），没有求解多目标梯度组合。S55 同样不是论文的 two-stage last-layer correction，只用了其激发的加权建议。S56 的论文明确实验了 CivilComments；这属于直接相邻领域的方法迁移，不能标作明显的远域发现。

## 2. improve 存在收益，但建议到实现并不一一对应

已注册 improve 19 个：12 个产生可评分结果，3 个极早失败、2 个 timeout、2 个未执行。12 个可评分子节点相对各自父节点 6 升 6 降，非独立试验，也混入尾部预算不足，不能将该比例视为方法胜率。

- S54 最佳 27273be 增加 `BCE + 0.05 * pairwise ranking`，按 overall/subgroup/BPSN/BNSP 抽取本 batch 正负对；保留 200 步 head warm-up。源报告同时提出 FIFO 和 representation editing，planner 明确拒绝 memory bank，本次提升对应一个更简化的 loss 干预（solution.py:414–509、839–845）。
- S55 最佳 994b5c 将排序对扩展至当前 effective batch 与容量 256 的 detached FIFO，0.075 ranking 辅助项，确保至少一个端点为当前模型可求导 logit。相较父节点约 +0.000844（solution.py:307–440、567–570、878–883）。CONTACCUM 从对比学习迁到排序，属于真实机制层面迁移，但仍非源论文完整算法复现。
- S56 c87f0e 的最终 analogy 报告只保留 adversarial debiasing 和 influence-guided last-layer correction；planner/代码最后实现的是 `0.5 BCE + 0.5 within-batch ranking`，没有落实这两条报告机制。这条变化不能直接归因于所引的两篇论文。
- S54 e66f9b 读到 representation-editing 建议，最后实现 head warm-up + 最后四层解冻，分数从 0.902627 到 0.915616。它利用的是计算分配思路，非 scale/bias representation editing。
- S56 580ae5 报告提出 frozen backbone + soft prefix/classifier，planner进一步变成只训练新 classifier；实际从 pretrained ModernBERT 载入并冻结全部模型，仅解冻 classifier（solution.py:381–395）。19,002 步后只有 0.821563，低于父 0.909731。后续 f61ccb 解冻末层 + final norm 后到 0.832325。这是过强简化/适应容量不足的实例，不能说所有冻结/PEFT 方法都无效。

## 3. 一个明确的排序方向 bug，解释“看起来有害”的具体来源

S56 b1738447ec61460dbe32f74c6978e42b 的不可变源码：

`cluster_sources/20260911_072611_jubias-anaf-s56/b1738447ec61460dbe32f74c6978e42b/solution.py`

- `_sample_direction` 第 417–419 行始终返回 `softplus(stored_logits - sampled_current_logits)`。
- `_cell_loss` 第 436–449 行也把“当前负例、缓存正例”送入该函数，未翻转正负方向。
- 对当前正例+缓存负例，该公式正确；对当前负例+缓存正例，应为 `softplus(current_negative - stored_positive)`，现在反向鼓励抬高负例分数。

纯算术检查：缓存正例 2、当前负例从 −2 升至 −1，错误 loss 从 4.018 降至 3.049（被奖励），正确 loss 应从 0.018 升至 0.049（被惩罚）。没有执行训练或运行候选完整脚本。

它不是只跑几步：总 5,206 次 optimizer update，三次 validation 0.692728、0.692127、0.689752。上一个当前 batch ranking 候选为 0.926396。该符号错误是确定的实现问题；它很可能是暴跌的重要原因，尚不能定量证明解释了全部差值。S55 994b5c 对两种方向均正确使用 `negative_values - positive_values`（solution.py:406–435），其 FIFO 结果并未崩溃。因此将结果概括为“FIFO/类比有害”会掩盖真正问题。

## 4. 两个极低分并未真正检验新机制

- S55 c3270863 0.517030 只训练 5 步。新 adaptive ranking multiplier 明确每 200 步才更新（solution.py:634、1033–1034），从未执行核心干预。run 剩余总时间 + 预处理/初始化 + 完整验证/导出耗尽可训练窗口。不能据此否定 adaptive weighting。
- S54 1d927b42 0.475552 也只训练 5 步。源码的确新增 frozen DeBERTa + representation scale/bias（solution.py:266–292），但缺少充分训练预算，这不是有效的 representation editing 效果试验。
- F54 a06dcf6a、F55 9199e398 在 run 尾部 timeout，不能用于机制效用判断。

## 5. 全文功能工作了，瓶颈不主要是阅读预算

23 次调用，共成功打开 45 次（21 篇去重），49 次 read 返回 187 个 chunk、261,287 字符；analogy 耗时合计 2,650 秒，约每 run 13–16 分钟。单次仅 0–3 次 read，明显未用满 12 次调用/40k 字符预算。

43 条最终机制：20 `full_text`、2 `mixed`、21 `abstract_only`。7 次报告完全退回摘要级：S55 invocation 1/2/6，S56 2/3/4/6。S55 首 draft 虽然阅读了 13,183 字符，最终两条建议仍都是 abstract_only。

全文访问失败 24 次：21 download_error、2 unavailable、1 timeout，反复失败的主要是 OpenReview 来源（如 xnhvvtztld、aqj9ifxrl6）。不要把打开失败和引用失败混为一谈。

22/23 次报告出现 `quote not found in text returned to this episode`，累计 88 条拒绝信息；部分建议被完全删除，部分用摘要引文重新提交。很多是 AUCSeg 等已成功打开并阅读的论文。因此“开到全文”≠“最终建议有全文证据”。引用校验按空白归一后的字面匹配；此审计未恢复所有被拒绝原始 submit 参数，不能断言全是错误引文或全是 Markdown 格式误杀。值得进一步检查引文选择与 PDF 抽取格式，但不宜直接放松校验。

## 6. 报告比旧版更审慎，但假设验证环节仍缺一截

报告一般列明 source assumptions / target fit / limitations / rejection criterion，且承认 group accuracy 与 AUC 不同、identity 重叠、反事实替换未必保标签等限制。这是进步。

然而很多最小验证方案要求“相同配置 BCE 对照、每个 subgroup/BPSN/BNSP AUC、弱组变化、queue coverage、吞吐量”，实际候选主要只看总 composite 与日志 optimizer steps。前几个首 draft 未实现逐组 AUC 打印或对照分支；runtime snapshot 只给总分，报告的 rejection criterion 未形成实际决策闭环。S56 FIFO 出错后，后续 planner 将其称为 memory collapse，却没有识别方向 bug，因此错误结果继续污染方法判断。

另外，draft packet 仍向 analogy 描述每个 solution 6 小时，若干 improve 报告/plan 沿用 1 小时；实际任务配置是 draft 90 分钟、后续 120 分钟，且最后候选还受剩余 run deadline 截短。错误资源上下文可能推高冻结/简化建议的优先级。

## 7. 分析优先级建议（未改代码）

比继续加阅读预算更优先的是：让候选开始前感知实际剩余预算；为新 loss 做正负对方向/梯度的廉价语义检查；区分未跑到干预触发点、实现错误、充分训练后低效三类失败；把 per-slice diagnostic 与实际采用/拒绝原因回传给 analogy。保留父节点最佳 artifact 已经发挥作用，低分探索没有覆盖三个最终获选结果。

用户 `MLEvolve/example_analogy_draft.md` 仍对应旧 S48 的 `20260907_200046_jubias-anad-s48/logs/analogy/draft_001.md`，只额外补了一个结束代码围栏，不属于此次 S54–56。


## 8. Root 补取候选预测后的 private 复评分（事后诊断，不用于运行中选模）

`candidate_private_scores.jsonl` 使用连续 AUC grader 只读评分候选已存在预测，没有重跑模型。

| Seed / 分支 | Public validation 轨迹 | 对应 private 轨迹 |
|---|---|---|
| F54 主分支 | 0.911807 → 0.910052 → **0.922761 选中** | 0.91679 → 0.91451 → **0.92639** |
| F55 主分支 | 0.927925 → 0.928041 → **0.928885 选中** | 0.92728 → 0.92798 → **0.92831** |
| F56 主分支 | **0.926935 选中** → 0.926396 → 0.692728 | **0.92545** → 0.93096 → 0.69590 |

F56 特别关键：c87 的 ranking 改动 public 只低 0.000540，private 实际高 0.00551；它被 runtime 合理地按预设 public 标准淘汰，不能因此断言这步对真实泛化无益。另一方面 b173 的方向错误 public 和 private 同时大幅退化，支持实际训练机制受损。该事后检查看到的是本次 private split，不能改用 private 选模型或调参，也不证明未来 run 的效果。

## 9. 瓶颈诊断有证据不足/模板化问题

- F55 invocation 2 将“Identity mention remains an unconstrained predictive shortcut”当瓶颈，其 evidence 仅引用任务背景中的通用 identity-toxicity 偏差和当前方法未显式 invariance；没有该候选的 identity probe、BPSN 缺口、错误样本或分组 score histogram。
- F56 invocation 2 同样断言“Identity mentions can remain a predictive shortcut”，证据是任务描述和当前 plan 只有 normalization/sampling/fine-tuning。可以作为待检验假设，不能当已观测的该模型瓶颈。
- F56 invocation 4 当前模型已经 0.5 BCE + 0.5 ranking，报告仍把首要问题写成“training surrogate is primarily pointwise”；下一条“metric-critical comparisons scarce”仅由 plan 存在 ranking、预算耗尽、总分略降推断，没有实际每个组的 pair coverage 统计。合理猜想被直接升级成改动依据。

因此下一步更值得让 analogy 读取 **真实 subgroup/BPSN/BNSP AUC、排序错误样本、每类pair有效率、实际阶段耗时和剩余预算**，并显式分开 observed facts / hypotheses / validation test。当前全文阅读改善了来源可追溯性，但无法替代对目标候选的诊断；即使找到很好的论文，错误或未经验证的目标瓶颈也会把方法送往错误位置。
