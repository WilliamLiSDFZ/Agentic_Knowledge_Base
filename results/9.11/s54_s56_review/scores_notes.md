# S54–S56 07xx 完成批：评分与图表审计

只读检查本地 fetch 文件；未重新评分、未修改原始结果、分析脚本或集群。数据来自 `/Users/william/nautilus/results/scores.csv`，不是 AKB/results/scores.csv。

## 最新三对

| Seed | A K1 | F K1 | F−A K1 | A K4 | F K4 | F−A K4 |
|---|---:|---:|---:|---:|---:|---:|
|54|0.93388|0.92639|−0.00749|0.93629|0.93452|−0.00177|
|55|0.92604|0.92831|+0.00227|0.93588|0.93624|+0.00036|
|56|0.92613|0.92545|−0.00068|0.93036|0.93650|+0.00614|

K1 均值 −0.0019667，95% t CI [−0.0144013,+0.0104679]；K2 +0.0007533 [−0.0096999,+0.0112066]；K3 +0.0019267 [−0.0096480,+0.0135014]；K4 +0.0015767 [−0.0085908,+0.0117441]。

以上只有三对，t 区间的分布假设缺少检验能力，不能宣称有效/无效或叠加收益。多 K 为事后探索，不要把最有利 K 当成预注册结果。K1 是依据公共 holdout 选择的单个最佳候选，并非在私有测试集上挑最高分。

F56 的 K1→K4 提升 +0.01105，而 A56 +0.00423。最新结果最值得关注的信号是融合收益，单模型收益不稳定。后续逐候选私榜诊断显示，这也包含公共 holdout 漏选更强单候选的补救，不能仅称为多样性收益；详见文末补充。F55 的 K6 0.93597 比 K4 0.93624 略低；F56 的 K6 0.93686 比 K4 0.93650 略高，不能笼统说越多越好。

## 可信度与预算口径

- 最新六个 run 为 20260911_071931_base54、072108_base55、072344_base56、072611_anaf55、072611_anaf56、072808_anaf54。库存 verdict 全 ok，完整约 12h；groups.csv 对应 draw16/17/18，无借基线。
- 全部评分为 `jubias-continuous-auc-v1`，grader SHA256 `000e216bc0faea8041e11a7f4dccc873e84f18c9d0a27f00bf5ebddb7b0dcd61`，mlebench_version=1.0.0。mlebench_commit 空白，因此可证相同 grader hash，不能从该表恢复准确仓库 commit。整个 scores.csv 无重复 run/variant/K 行。
- 每对 A/F 的 contract_id、split.npz hash 完全一致，公共训练与测试文件 hash 也相同。当前 summary 开头的“arms hold out different data”是旧流程说明，不适用于这三个配对；公共 holdout 分数仍不是最终私有评分。
- 六个 best_solution submission 与自身 manifest SHA256 全匹配；best_submission 和 top1 ensemble 都有 97320 行、id 逐行相同，预测最大差异 <1e−16，仅 CSV 重序列化数值精度，未发现拿错最佳输出。
- A54 在 V100 32GB，其余 A10（此前 live GPU 报告及快照）。时间预算相同不代表计算资源相同；S54 是硬件混杂的配对，不能直接将其下降归因 analogy。仅看同卡 S55/S56 样本则只剩两对，更不足以得出稳定效果。
- ensemble 的 cum_hours 是所纳入候选各自完整执行耗时之和，不是找到这组候选的总实验时间；六个实验均已经花约12h，包括失败、LLM、预处理及未入选候选成本。不要把 K4 的约5–7h视为实验只花这么久。
- 默认扫 K=1,2,3,4,6，不含5。A54/A55/A56/F54 都有至少7个 scoreable 候选，缺 K6 因 top6 执行耗时分别 9.06786/9.36385/9.60259/9.33915h，超过9h ensemble cap；F55/F56 top6为8.74337/7.26499h，所以有K6。不是 fetch 漏文件。

## 当前总图不能直接代表新版本

主 summary F−A 为 n=6、+0.02631：混合 S51–53 旧协议与 S54–56 新协议，包含 S51 借来的 20260901_192139_jubias-base-s42（0.77717）；F51 0.92207 带来 +0.14490，主导总体正均值。S51 原 A 20260910_022351 没有 submission 已 invalid，不能把借基线当真配对。旧 S53 的 +0.03652 和 S52 −0.01766 也来自旧执行协议。这个汇总不能回答最新修复后的效果。

图 `analogy_score_F` 会排除借基线于均值/CI，但仍将旧 S52/S53 与当前3对混合；它是5个真实配对的跨版本统计，也不是当前3对结论。一般效果图/summary 则纳入借基线并标记 unpaired，两张图平均值不同是统计口径不同。

00xx 旧中断批和06xx 启动失败批共12个均 invalid，未计入主效果图；没有将旧失败启动与最新实验重复计算。最新6个无整 run 生存者筛选；候选失败应作为 run 成本计入，而非仅从有效候选改进均值推断因果。

`analogy_summary.csv` 存在一处真实映射缺陷：旧 invalid `20260911_005107_jubias-anaf-s54` 与 `...s55` 的 control_run 空，但 score_effect_vs_A 被填为最新同 seed 的 −0.00749/+0.00227。`scripts/plot_analogy.py:694` 用 label 末尾 seed 匹配分数，跨运行重复 seed 时误贴。此字段不代表旧 run 得到该成绩。图表中流程图已过滤 verdict==ok，因此此误贴主要影响汇总 CSV 的解释；未修改。

## 证据路径

- 原始评分：`/Users/william/nautilus/results/scores.csv`
- 配对与汇总：`results/9.11/groups.csv`、`run_inventory.csv`、`charts/summary.md`
- 当前六个：各自 `logs/candidate_results/summary.json`、`workspace/best_solution/manifest.json`、`workspace/ensembles_csv/`
- 硬件证据：`results/9.11/live-s54-s56-20260911_1015Z/REPORT.md:23` 及其 GPU snapshots
- 重算精确数值：同目录 `scores_audit.json`

## 补充：45 个候选的事后私榜诊断及 F56 选择偏差

`candidate_private_scores.jsonl` 对每个候选已经保存的“公共验证集最高分 snapshot”进行独立事后评分，共45个，使用同一 corrected grader；没有依据私榜改选候选内 checkpoint。root 的取证过程确认45份 submission hash 均通过。这个诊断文件不替代正式 scores.csv，不用于重写 top1、重新选 K 或继续 agent 搜索。

F56 的 `logs/candidate_results/selection.json` 明确确认：

| 公共排序 | 候选 | 类型 | 公共验证 | 事后私榜 | optimizer steps |
|---|---|---|---:|---:|---:|
|top1|4eed868ef31d4cbbad8722e4257772d9|首个 draft|0.9269353104|0.92545|1,255|
|top2|c87f0ec8e98d4e0abafdbd26384cb20c|该 draft 的 improve|0.9263956661|0.93096|4,714|

公共分数把 improve 判为下降 −0.0005396443，实际这个已保存 improve 快照的私榜高 +0.00551。正式流程按公共分数选择首个 draft 是遵守规则；事后证据表明，仅凭这一很小的公共差距放弃它作为单模型会漏掉有效改进，不能据此称该次 analogy improve 有害。

F56 的正式 ensemble：K1 0.92545 → K2 0.93353 → K3 0.93570 → K4 0.93650。K1→K2 增益 +0.00808，占 K1→K4 总增益 +0.01105 的约73.1%。K2 正是上述 top1+top2，按现行“公共验证分数×名次”权重约0.666796/0.333204。该组合比事后较强的单独 c87（0.93096）仍高 +0.00257。

因此更准确的解释是：F56 的融合同时弥补了公共排序漏选更强候选的问题，并获得了超越两者各自分数的组合收益；不能把全部+0.01105归因于架构/机制多样性，也不能全部归为候选选择错误。这是分数层面的现象，尚无子群切片和预测误差相关性证据来确定具体互补来源。c87 的训练步数也明显多于首个 draft，且 improve/draft 预算为120/90分钟，所以该候选私榜进步仍不能单独归因于所加的机制。

其他5个 run：A54/A56/F54/F55 所选 top1 都是本次已评分候选中的私榜最高；A55 的私榜最高 bd1b4e2260714dbaaf1cd1b869cc5147 为0.92612，比所选20bbfe0ac57f45e4900176b36596cdc0 的0.92604仅高0.00008。F56 是这6个 run 中明显的公共候选排序失配个案，尚不能认定存在普遍排序故障。

注意：事后私榜最高值具有选择偏差，不能把这个“如果用私榜挑”的结果替换正式组间差值/CI。正式图表与上文 K1/K4 配对统计保持原值。
