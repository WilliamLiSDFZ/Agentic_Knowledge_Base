# 9/8 图表与 S48 analogy 落盘复核

后续实施记录（同日）：用户随后授权修复。评分补丁已在 dev pod 应用，相关代码、版本检查与回归测试纳入 MLEvolve；见项目 UPDATELOG 的 2026-09-09 条目。下文“没有修改评分器”等描述指最初的诊断阶段。

复核日期：2026-09-09。结论：S48 在原图中的巨大负效应主要来自评分器将预测概率二值化；按连续预测计算竞赛 AUC，S48 的 E 组 K=1 比 A 组高 0.00355。但直接接受 analogy 的分支较弱，其候选加入集成后会降低正确口径的分数。这两件事需要区分，现有证据不能单独证明采样建议具有负因果效应。

本次只分析代码、日志和已有预测，并在集群内使用 private answers 重评分；没有重训模型、修改评分器或覆盖原始分数及图表。派生数字保存在同目录 `s48_metric_recheck.csv`。私有标签未导出。

## 证据范围与复核方法

- 图表：`results/9.8/charts/`，重点是 jubias 的 score、branches、funnel、transfer、retrieval、cost 图。
- 用户提供的 `/Users/william/Documents/project/python/MLEvolve/example_analogy_draft.md` 与 `/Users/william/nautilus/results/20260907_200046_jubias-anad-s48/logs/analogy/draft_001.md` 字节一致。
- 逐节点依据是对应 run 的 `logs/journal.json`；没有只用 best_solution.py 代表整次搜索。
- 实际集群评分器：`/workspace/MLEvolve/.venv/lib/python3.11/site-packages/mlebench/competitions/jigsaw-unintended-bias-in-toxicity-classification/grade.py`。
- 重评分对象：S48 的 A/E、S50 的 A/E、S49 的 E 已有 ensemble CSV，以及 S48 E 的四个保存候选。每份 ensemble 有 97,320 行，按 id 排序并核对答案 id 完全相等。
- 复核保留真实 toxicity 与九个 identity 在 0.5 处的二值化，但预测保留连续值。每个 identity 计算 subgroup、BPSN、BNSP AUC，分别以 p=-5 聚合，最终 overall AUC 与三个聚合项各占 0.25。把预测重新二值化后，可以复现这些提交原有的评分。

## 1. 原图的主要异常是评分口径错误

当前 grader 的 `prepare_for_metric` 在调用 ROC-AUC 前执行了：

```python
submission["toxicity"] = submission["toxicity"].apply(lambda x: 1 if x >= 0.5 else 0)
```

这会丢掉概率之间的排序信息。全部预测都低于 0.5 的模型即使排序很好，也会被压成几乎全零的输出，得到接近 0.5 的分数。真实标签需要二值化，预测不应这样处理。集群安装的代码和所查 [MLE-bench 上游代码](https://github.com/openai/mle-bench/blob/main/mlebench/competitions/jigsaw-unintended-bias-in-toxicity-classification/grade.py) 一致。

| 同批次比较，K=1 | 原 A | 原 E | 原 E−A | 连续预测 A | 连续预测 E | 连续预测 E−A |
|---|---:|---:|---:|---:|---:|---:|
| S48 | 0.76990 | 0.50045 | −0.26945 | 0.92100 | 0.92455 | +0.00355 |
| S50 | 0.50456 | 0.73548 | +0.23092 | 0.93372 | 0.91871 | −0.01501 |

S48 E 的 K=1 预测仅 8 / 97,320 个达到 0.5，但连续分数为 0.92455；S50 A 也只有 94 个达到 0.5，连续分数为 0.93372。因此原图把两个排序较好的模型画成接近随机，甚至翻转了处理效应的符号。

两个配对 draw 的修正后平均 E−A 约为 −0.00573，样本数仍只有 2，不能据此断言 analogy 总体有效或有害。S49 E 的修正分数为 0.83138，但缺少有效的同批 A，不能凑成第三个配对样本。原 summary 的 n=3 unpaired 汇总与 analogy score_E 图的 n=2 paired 汇总本就不是同一估计；两者还共同受错误评分影响。

此问题也影响同一任务其他 A/B/C/D/E 提交的解释。其他 jubias 图和基于旧方差推导的所需样本数应在统一重评分后更新；不能把本次五个 run 的复核当作已经修复全部图表。

## 2. 接受 analogy 的分支确实较弱，但不是原图中那个接近 0.5 的最佳候选

E 模式只把 report 直接注入第一个生成的 draft，即 branch 1。journal 的 step 按完成记录顺序排列，该 draft 显示为 step 2。

| 分支/节点 | 实际执行 | 结果 | 连续预测 private score |
|---|---|---|---:|
| branch 1 / step 2 | ModernBERT-large，512 tokens，weighted sampler | optimizer 首次更新 OOM | — |
| branch 1 / step 6 | debug | 6 小时超时 | — |
| branch 1 / step 7 | DistilBERT，128 tokens，编码器全冻结，weighted BCE | 有效 | 0.81432 |
| branch 1 / step 9 | 解冻最后两层，保留加权 | 有效 | 0.91133 |
| branch 1 / step 10 | 再加 subtype 辅助目标 | 有效 | 0.91103 |
| branch 2 / step 8 | DeBERTa-v3-base，冻结下六层，多任务与 ranking loss | 有效，最终 top 1 | 0.92455 |

所以原图中 E48 的 0.50045 实际对应 branch 2 的优良排序模型，而不是直接注入 report 的 draft。branch 2 没有直接获得完整 report，但其 prompt 的 Memory 包含此前的 analogy 方案；不能把它当作完全独立、完全未受影响的对照。

S48 E 的四个有效节点中，三个来自注入分支，一个来自 branch 2。整次 run 为 10 个非 root 节点、6 个 buggy；A48 也有大量 OOM/超时及 6 个 buggy 节点，不能把资源失败全部归咎于 analogy。

按 Agent 当时的本地验证分数排序并逐个加入保存候选，得到：

| K | 原评分 | 连续预测评分 |
|---:|---:|---:|
| 1 | 0.50045 | 0.92455 |
| 2 | 0.55218 | 0.92420 |
| 3 | 0.61628 | 0.92151 |
| 4 | 0.63675 | 0.91846 |

旧图看似“更多候选挽救模型”，正确口径却是加入较弱候选后逐步下降。branch 1 的 step 9、10 分数约为 0.911，step 7 仅为 0.814。这是已观察到的候选混合损失，不等价于已证明 analogy 机制本身有害。

分项也没有达到报告希望的“双向改善”：branch 1 / step 9 的 BPSN 聚合为 0.84479、BNSP 为 0.97030；branch 2 / step 8 分别为 0.90242、0.95693。前者在 BPSN 上明显更弱、BNSP 更强。BPSN 衡量“不含该身份的有毒评论”与“含该身份的无毒评论”之间的排序。这个差异值得检查，但两个模型的架构、训练和本地划分不同，不能直接当作采样导致的变化。

## 3. analogy 文本的推理与落地缺口

报告正确指出：总体 BCE 与低尾敏感的 identity 条件 AUC 不完全一致；identity 与 toxicity 的相关性可能成为捷径。它也明确提醒 naive balancing 可能有害，提出保留 uniform 混合成分，并用真实指标验证。这不是毫无根据的建议。

但它从“任务存在这种结构”跳到了“当前模型的主要瓶颈就是这种结构”，当时没有成功 baseline、每组 AUC 或误差分析支撑该诊断。第一份 draft 上的它应被理解为待验证假设。

其机制迁移还存在三层间隙：

1. **目标不等价。** Worst-group classification performance 与 subgroup/BPSN/BNSP 的排序目标并不相同。九个有重叠的 identity 群体被压缩成“任意 identity present/absent × toxic/non-toxic”四格，无法直接针对具体弱群体和具体排序对。
2. **理论方法被简化成启发式。** 初始实现采用 70% uniform 加 30% corrective mass，四格质量设为 `[0.15, 0.35, 0.15, 0.35]`（顺序是无身份无毒、有身份无毒、无身份有毒、有身份有毒），再 replacement sampling。它突出两个 identity-present 格子，但不是依据实测失败或已知目标分布推导的权重。[Importance-sampling 原论文](https://arxiv.org/html/2412.13003v1) 对子群分布和迁移条件有具体假设，不能仅凭题目就保证这里的权重有效。
3. **验证与回退没有落实。** 报告要求固定模型/head/BCE、只改 sampler，并用验证决定是否保留。实际经历了 OOM、超时、换 backbone、冻结编码器、sampler 改 weighted BCE、再加辅助任务；没有对应的成功 uniform 基线。因此既没有忠实验证原建议，也没有干净的因果对照。

其中 [The Group Robustness is in the Details](https://arxiv.org/html/2407.13957v1) 的实验本来就包括 CivilComments 毒性分类及身份属性，与该任务高度接近，不能仅凭“NeurIPS/AAAI 来源”认定为跨领域。该论文还指出 naive upsampling/upweighting 的风险；其 mixture 包括先对子群做子集选择再上采样，并非随意设 minibatch 比例即可复现。

资源方面，sampler 本身增加的开销很小。问题是报告把一个尚未验证能在预算内训练的 ModernBERT 流程判为 feasible；随后的调试大幅改动了模型。不能据此声称加权采样直接造成 OOM。

## 4. 9/8 过程图能支持什么

- **Funnel 的 valid child = 0**：实现只统计直接携带 report 的节点是否 buggy。S48 的注入 draft 失败，但其分支后来有三个有效节点；不能读成“analogy 没产生有效后代”。
- **Transfer 图**：标题为 improve nodes，实际遍历所有带 report 的节点，包含 E 的 draft；adoption 若没有 LLM 判定文件则使用关键词重叠代理。小样本、不同阶段与非独立节点不能支撑因果结论。
- **Retrieval 图**：venue mix 不是领域距离；仅两篇引用时全部落在 top 3、单个 mechanism 时标题全不重复，也不足以证明检索或类比质量。
- **Cost 图**：该次 analogy 调用约 61 秒，主要损失来自小时级训练失败与候选质量，不能把大的分数落差解释为检索延迟。
- **跨任务汇总**：9/8 的主要对比置信区间均跨零或只有一个 draw，尚没有稳定的总体正负结论；jubias 的效果及方差尤其需要先按统一正确口径重算。

## 后续优先级

1. 先修正 jubias 的预测二值化问题，重算该任务全部历史提交及图表，并统一 Agent 本地验证、离线评分的定义；真实标签与 identity 的阈值处理仍需保留。
2. 在固定 backbone、split、初始化、训练预算下比较 uniform 与建议的 mixture，分别记录 overall、九组 subgroup/BPSN/BNSP 及最终合成分数。资源可行性应先由可运行 baseline 或吞吐实测确认。
3. 把 analogy 建议明确记录为假设，要求具体受损分项、论文适用条件、实现映射、验收指标与失败后的回退。检查建议是否真正实现，区分直接注入、继承与 Memory 间接影响。
4. 区分单候选效果和融合效果；S48 当前最清楚的真实退化来自把较弱、相关的候选加入 ensemble。候选筛选只能依据允许的验证数据，不能依据本次 private 重评分进行挑选。

本次结果支持“测量错误制造了 S48 的巨大负效应；实际注入分支存在资源可行性、方法忠实度和验证设计缺口”，不支持“这份 analogy 已被证明整体有害”，也不支持“修正后 S48 略胜就证明 analogy 有效”。
