# S57–S59 最新 Sol 实验复核

分析日期：2026-09-13。对象为 2026-09-12 08:12–08:24 UTC 启动的六个 GPT-5.6 Sol A/F run，不包含此前 GPT-6 或早先失败重启的 run。完整运行名与逐项统计在 [summary.json](/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.12/s57_s59_review/summary.json)。

**结论：这一批 F 臂有一致的正向分数信号，但现有证据不能把收益归因于 improve 阶段提出的动态重加权机制。** 两个最佳 F 候选的动态权重实际上没有更新；另一个最佳 F 候选对应的 improve analogy 没有成功交付报告。值得保留 F 方向继续验证，但当前最值得改进的是报告交付、实现诊断和机制生效检查。

## 1. 单独看这批结果，F 比历史总图表现得更积极

以下为 private held-out 分数；K=1 表示依据已有 public validation 排名选出的单个候选，不是在 private 分数上挑最优。评分版本均为 `jubias-continuous-auc-v1`，grader SHA256 一致。

| Seed | A：K=1 | F：K=1 | F−A | 说明 |
|---|---:|---:|---:|---|
| 57 | 0.91985 | 0.93170 | +0.01185 | A 为保存预测的事后恢复结果 |
| 58 | 0.92028 | 0.92938 | +0.00910 | 两臂正常完成 |
| 59 | 0.91606 | 0.92644 | +0.01038 | 两臂正常完成 |

仅用正常完成的 S58/S59，K=1 平均差为 **+0.00974**；计入恢复的 S57 为 **+0.01044**。K=1、2、3、4、6 的三对差值全部为正，但 S58/S59 的优势在集成更多候选时总体减小。

| K | S57：F−A（恢复 A） | S58：F−A | S59：F−A | 正常完成两对均值 |
|---:|---:|---:|---:|---:|
| 1 | +0.01185 | +0.00910 | +0.01038 | +0.00974 |
| 2 | +0.01105 | +0.00536 | +0.00144 | +0.00340 |
| 3 | +0.01188 | +0.00439 | +0.00183 | +0.00311 |
| 4 | +0.00989 | +0.00441 | +0.00263 | +0.00352 |
| 6 | +0.00761 | +0.00621 | +0.00342 | +0.00481 |

![本批独立对比](/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.12/s57_s59_review/latest_sol_comparison.png)

现有历史图中，最新 S57 的分组借用了历史 S46 的 A，不能解释为本批同 seed 对照。历史汇总还混合模型和运行逻辑版本；其总体置信区间回答的是另一个问题。本次另外出图，保留原始图表和评分 CSV。

A57 没有最终 submission/ensemble，但留下 8 个可评分候选快照。我在 CPU dev pod 上读取这些保存预测，校验 SHA256、97,320 个唯一 ID、行顺序和预测范围，按照已有 public 排名、相同 rank/metric 权重及 9 小时累计候选预算补算。F57 的第一名交叉检查得到 0.93170，与已有 CSV 一致。恢复过程不重新训练、不使用 private 标签选模型、不修改源 run。方法与结果见 [recover_a57.py](/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.12/s57_s59_review/recover_a57.py) 和 [恢复记录](/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.12/s57_s59_review/a57_recovered_scores.json)。

这是 **2 对正常完成 + 1 对部分恢复** 的小样本，不能宣称稳定、可泛化的收益。硬件也并非完全一致：F57/F59 是 A10，F58 是 L4。最佳候选的 backbone 在 S57/S58 还分别是 A 的 ModernBERT-base 与 F 的 ModernBERT-large；因此该比较衡量整个搜索流程的结果，不能隔离某条 analogy 建议的贡献。S59 两臂最佳候选均使用 large。

## 2. 分数提升与机制生效之间存在缺口

下面的候选分数均为 **public validation**，与上表 private 分数不同。三个 F 的最佳有效候选都出现在第一次 improve；后续搜索没有超过该 run 的最佳 public 分数。

### F57：analogy 后来找对了 bug，但修正后的候选没有更高分

第一轮 improve 将 `9a77309c` 的 0.91447 提高到 `bca5f8ac` 的 **0.92732**。planner 明确选择了 persistent primal-dual cellwise AUC 机制。

然而代码使用：

```python
self.family_dual_logits[family_index, eligible].add_(delta)
```

这里的布尔高级索引产生副本，修改没有写回原始状态。运行日志也显示分组权重保持 1/9，即便各组风险不同。因而这个高分候选不能作为“动态对抗权重有效”的证据。

后续 analogy 通过代码和运行信息识别了这个问题，建议修复状态更新。子候选 `a8f33f1b` 改为 `index_add_`，加入状态变化检查，但分数为 **0.92274**，较父候选下降 **0.00457**。这说明代码读取确实带来了有效诊断；也说明修复机制与提高最终分数需要分别验证。单次下降不能证明该机制普遍有害，训练深度和预算等也需要控制。

证据：[最佳候选源码副本](/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.12/s57_s59_review/bca5f8ac.py:1027)、[修复候选源码副本](/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.12/s57_s59_review/a8f33f1b.py:1039)、[后续 analogy 落盘](/Users/william/nautilus/results/20260912_082449_jubias-anaf-gpt56sol-s57/logs/analogy/bca5f8acf43d4060b8043d60898b7b1b_004.context.json)。

### F59：把状态更新错误误诊为样本覆盖问题

第一次 improve 将 `600ef4fa` 的 0.92496 提高到 `64f9c626` 的 **0.93285**。选择的机制是对不同 metric cell 使用平滑 group-DRO 权重。

但生成代码也有相同类别的错误：

```python
accumulated_loss_sums[availability].add_(detached_losses)
availability_counts[availability].add_(1)
ema_losses[availability].mul_(decay).add_(...)
```

计数和 EMA 的修改没有写回。后续 analogy 观察到控制器不活跃，却主要沿着“有效正负样本对覆盖不足”的方向解释；planner 选择 role-complete offline batch packing。生成的 `64405410` 增强了批次覆盖，但保留上述状态错误，在 200 次 optimizer update 后触发：

```text
Role-complete controller smoke test failed: EMAs or family weights remained inactive.
```

这次候选耗时约 680 秒，没有可用快照。为了区分“缺少有效样本”与“更新没写回”，我只抽取两份候选中的控制器方法做 CPU 复现：即使提供全部 9 个有效 cell，loss 梯度也非零，保存的计数仍为 0、EMA 仍是 log(2)、权重仍是 1/9。最佳候选和 batch-packing 子候选均复现。复现环境为本地 PyTorch 2.12.1 CPU；原实验环境为 2.7.1，因此这里同时依赖源码语义与原始运行日志，而非声称重放了完整训练。

**这是本批最明确的诊断失败：报告识别了症状，却没有先验证最直接的实现原因，随后引入更复杂的采样方案。**

证据：[最佳候选源码](/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.12/s57_s59_review/64f9c626.py:1024)、[子候选保留的错误](/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.12/s57_s59_review/64405410.py:1025)、[analogy 落盘](/Users/william/nautilus/results/20260912_082449_jubias-anaf-gpt56sol-s59/logs/analogy/64f9c6261a574b3cad82168485502c72_003.context.json)、[隔离复现脚本](/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.12/s57_s59_review/check_controller_state.py)、[复现输出](/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.12/s57_s59_review/controller_reproduction.json)。

### F58：最佳提升对应的 improve analogy 没有成功交付

`c03c57a6 → 08f224fd` 将 public 分数从 **0.90914 提高到 0.92914**，是该 run 最佳候选。但该次 improve 的 analogy 最终未通过校验，报告为空，子节点没有 analogy adoption。它的初始 draft 已接收 analogy，所以也不能解释成完全没有 analogy 的收益；只能说 **这次提升不是该轮 improve 报告直接带来的**。

后续明确采用跨 batch 队列的候选为 0.92650，低于这个父候选。证据见 [该次未交付的 trace](/Users/william/nautilus/results/20260912_081346_jubias-anaf-gpt56sol-s58/logs/analogy/c03c57a6fc0c44739acab52ac4ed5bf1_002.md)。

跨三个 F run，journal 中明确记录 `selected` 的 improve 子节点共 10 个：8 个有可比较的正常 public 指标，其中 4 个上升、4 个下降，另 2 个标记为 buggy。未完成的 handoff 不计入。这个描述性统计不能替代受控消融，也不适合直接平均，因为弱分支的大幅恢复会主导均值。

## 3. 全文和代码工具已使用，报告交付仍是明显损耗

| Run | Analogy 调用 | 成功交付 | 空报告 | 累计调用耗时 |
|---|---:|---:|---:|---:|
| F57 | 8 | 7 | 1 | 44.3 分钟 |
| F58 | 10 | 6 | 4 | 54.1 分钟 |
| F59 | 8 | 7 | 1 | 44.7 分钟 |

总计 26 次，20 次成功、6 次为空（23.1%）；draft 3/3 成功，improve 17/23 成功。25/26 次调用阅读了全文，累计正文返回约 **54.2 万字符**，源码工具 ledger 共 **229 次调用**。成功报告共保留 35 个机制，其标注证据等级为 full_text 18、mixed 3、abstract_only 14；所以“启用了全文阅读”并不意味着每条最终建议都由全文支持。

模型多轮 usage 累计输入约 **1,570 万 token**、输出约 **38.7 万 token**。输入包含每轮重复发送的上下文，不等于唯一阅读量，也不是账单成本。调用耗时可能与候选训练重叠，不能直接当作 GPU 空闲时间。

**空报告的直接问题不是报告太长。** 六次失败均遇到 runtime evidence 路径校验失败，其中一次随后还遭遇论文引文无法精确匹配。五次直到第 14 轮才首次提交，已没有修正轮次；另一次在第 13 轮提交后，第 14 轮仍校验失败。

典型情况是把多个路径写在一个字符串中：

```text
public_validation.metric; public_validation.overall.auc; public_validation.power_means
```

或使用 `weakest_components[0]`，而校验器只识别单条点分路径和 `.0` 数组下标。当前一个 observed fact 的路径错误会使整个报告返回空。拒绝响应却附有通用“缩短报告”的提示，容易误导修正方向。解析到的拒绝原因没有长度超限。

交付摩擦不止六次终局失败：20 次成功中，19 次也经历过至少一次提交拒绝。代码工具另有 16 次显式错误，其中 10 次是同时传 symbol 与行范围，违反互斥规则。这里应改善工具契约和诊断信息，而不是简单放松事实/引文校验。

证据：[逐调用统计](/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.12/s57_s59_review/summary.json)、[runtime 路径校验代码](/Users/william/Documents/project/python/MLEvolve/engine/analogy/report_v2.py:56)、[整份报告返回空的位置](/Users/william/Documents/project/python/MLEvolve/engine/analogy/report_v2.py:94)。

## 4. 运行稳定性与候选浪费

| Run | Journal 候选数 | buggy 数 | Runtime 可评分候选 / 已登记候选 |
|---|---:|---:|---:|
| A57 | 9 | 2 | 8 / 11 |
| F57 | 7 | 0 | 7 / 10 |
| A58 | 9 | 1 | 8 / 11 |
| F58 | 11 | 1 | 11 / 13 |
| A59 | 10 | 1 | 9 / 12 |
| F59 | 12 | 5 | 7 / 15 |

Journal 与 runtime 是不同统计口径：runtime 还包含尚未完成回填、被中断等候选，不能把两者差值都视为代码 bug。五个正常完成 run 的 Pod 已确认 Succeeded；本批未观察到此前的 rate-limit/schema 故障反复出现。

A57 日志中出现 CUDA unspecified launch failure，之后 global memory 的 CUDA 调用也失败，最终未产出 ensemble。该 Pod 已不存在，现有材料不能确定是如何终止的，不能断言 OOM 或 eviction。保留下来的 8 份可评分快照让本次能够恢复比较，说明结果保存机制有实际价值。

F59 的生成候选仍有 autograd 重复 backward、RNG 状态 tensor 设备、正则 backreference、clamp 参数组合以及上述控制器自检等错误。它的高分来自少数早期有效候选，后续搜索可靠性还有提升空间。

## 5. 建议的下一步顺序

1. **先提高报告交付成功率。** 为 runtime evidence 提供可复制的精确路径或稳定 evidence ID；校验错误指出具体 fact、路径和修正格式；预留提交后的纠错轮次；明确源码工具 symbol/行范围互斥。保留真实引用和事实 grounding，不能靠忽略错误来提升成功率。
2. **把机制生效检查放到长训练之前。** 对动态权重、队列、EMA、采样等要求小型可执行检查：有效输入是否存在、状态前后是否变化、梯度是否经过预期分支、保存/恢复是否保持状态。检查应先区分实现错误与数据不足，再决定是否引入新算法。沿用现有候选运行/验证流程即可，不必仅为此增加 search node type。
3. **再做受控消融，区分 draft 与 improve 的贡献。** 若研究问题是 improve analogy 是否有效，固定同一父候选、backbone、split、训练与验证预算和 GPU 类型，对比普通 improve 与 analogy improve；如果要估计整个流程贡献，再独立比较 baseline、仅 draft analogy、draft+improve analogy。以 private 指标只做事后评估，不反馈给生成过程。

当前报告里的建议集中在分组 AUC、损失重加权、跨 batch 队列、采样覆盖和软标签。这些建议常常更贴近实现了，但“建议具有论文依据”“代码明确采用”“实际状态变化”“验证指标提升”仍是四个不同层次。本批最值得补的是后两个层次之间的可验证连接，而非继续增加阅读预算。

本次只新增此分析目录；未修改 MLEvolve 运行代码、UPDATELOG、原始结果、现有图表或集群实验配置。
