S60–S62 实验复核（2026-09-15）
================================

**P0 的报告交付修复有效，但这批没有显示稳定的最终成绩收益。** 两个完整 A/F 配对一负一正；F62 最高分候选明确拒绝了当轮 analogy 建议，改用了任务预训练模型，不能把这部分增益直接归给类比机制。更具体的剩余问题是：部分报告虽然成功返回，关键机制仍因引文排版差异或输出预算被删除。

本次只分析已有结果、代码和落盘，并通过 CPU dev Pod 只读核查 PVC；未修改程序、评分器、Job 或 UPDATELOG，未重新评分。原有 `results/9.14` 图表保留。本目录保存独立复核结果。

**样本与成绩口径**

本地共有八个相关目录。早期 A60 `045451`、F62 `043431` 是未完成尝试，单独列出；当前可比较的是五个完成 run 加一个不完整 F60。没有借用别的 seed/batch 作为配对。

| Seed | A 最新目录时间 | F 最新目录时间 | A private k=1 | F private k=1 | F−A |
|---|---|---|---:|---:|---:|
| S60 | 071735 | 051428，未完成 | 0.91786 | 缺失 | 不计算 |
| S61 | 062456 | 070847 | 0.93073 | 0.90872 | **−0.02201** |
| S62 | 070227 | 070253 | 0.92186 | 0.93360 | **+0.01174** |

目录均以 `20260914_` 开头。完整路径和八次尝试的 inventory 在 [summary.json](/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.14/s60_s62_review/summary.json) 中。

两个有效配对的 k=1 均值差为 **−0.005135**。这只是描述值，n=2 不支持稳定收益或稳定有害的统计结论。扩大 ensemble 没有改变各 seed 的方向：

| k | S61 F−A | S62 F−A | 两对均值 |
|---|---:|---:|---:|
| 1 | −0.02201 | +0.01174 | −0.005135 |
| 2 | −0.02080 | +0.00999 | −0.005405 |
| 3 | −0.01950 | +0.01229 | −0.003605 |
| 4 | −0.01609 | +0.01164 | −0.002225 |

F61/F62 没有 k=6 是时间上限所致：前六个入选候选的累计计费时长分别为 **9.8599 h / 9.1606 h**，超过原 ensemble 的 9 h cap，并非都没有六个可用候选。不应把 A 的 k=6 与 F 的 k=4 混比。

成绩直接来自现有 [scores.csv](/Users/william/nautilus/results/scores.csv) 的 `capped` 行；本目录复制了这五个 run 的 23 行到 [private_scores.csv](/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.14/s60_s62_review/private_scores.csv)。全部为 `jubias-continuous-auc-v1`，grader SHA256 一致：`000e216bc0faea8041e11a7f4dccc873e84f18c9d0a27f00bf5ebddb7b0dcd61`。下面讨论候选变化时使用的是 public validation，不与 private 成绩混用。

![S60–S62 配对成绩和 ensemble 差值](/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.14/s60_s62_review/comparison.png)

**F60 并非只漏了 fetch**

CPU dev Pod 上 `/workspace/MLEvolve/runs` 也只有同样八个目录，没有找到较晚的 F60 重跑。F60 的 runtime 有两个候选注册记录，但 **0 个已发布快照、无 journal、无 selection**，没有可恢复的评分结果。

候选 execution 记录中一个为 `failed / RuntimeError`，约 975 秒；另一个停留在 `running`。主日志只延续到 06:01 左右，约 47 分钟，停止时第三个 draft 仍在生成。由于原实验 Pod/Job 已不存在，无法从现有材料确定是手动停止、节点问题还是其他 run 级退出原因。候选错误不能直接当成 Pod 消失原因。详情和相对文件路径见 [candidate_analysis.json](/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.14/s60_s62_review/candidate_analysis.json)。

**P0：整份报告不再丢失，但机制交付仍不完整**

统计最新 F60/F61/F62，排除早期重复 F62：

| Run | analogy 调用 | 完整接受 | 部分接受 | 无报告 | 首拒后成功纠正 |
|---|---:|---:|---:|---:|---:|
| F60，不完整 run | 1 | 0 | 1 | 0 | 0 |
| F61 | 6 | 1 | 5 | 0 | 3 |
| F62 | 8 | 0 | 8 | 0 | 2 |
| 合计 | **15** | **1** | **14** | **0** | **5** |

所有调用都有 `report_schema_revision=2`、首次提交截止第 12 轮；首次提交实际在第 9–12 轮，纠错在第 12–14 轮完成。没有发现 runtime evidence 路径错误。仅看完成 run 也为 **14/14 非空**，不是依赖 F60 的一次调用才成立。与上批 20/26 非空相比，交付指标明显改善，但两批样本不同，不能据此推断成绩提升。

按每次调用**最后一次提交**计，模型提出 33 个机制，最终交付 **17 个**：9 个被证据/源码校验删除，7 个被 12,000 字符预算删除。仅看完成的 F61/F62，则为 30 个提出、16 个交付、8 个校验删除、6 个预算删除。

`accepted_partial` 会立即结束 episode。因此“有一个机制幸存”有时意味着更重要的另一个机制失去纠错机会。例如正式 F62 draft 在第 11 轮删除了采样机制，只保留软标签建议，剩余轮次没有再用于修复那条采样机制。

**一个明确的误拒来源是 Markdown 排版。** 全部提交有 32 次 `paper_quote_not_returned`，逐条与当次提交之前实际返回的工具文本比对后，11 次仅差 `**加粗**`、`_斜体_` 等强调标记。另 19 次存在文本改写、删节、公式或 PDF 提取顺序差异，2 次是 abstract 失配，不能一概视为排版问题。

例如 F62 draft 已读取 AUCSeg 的 `p006-c007`，工具返回 `at least one sample from each class` 这段时带有加粗标记；提交引用去掉标记，就被拒绝。至少三项最终删除机制的全部引文问题都可由强调标记差异解释，涉及 metric-cell sampling 和 cross-batch memory。

当前 [report_v2.py](/Users/william/Documents/project/python/MLEvolve/engine/analogy/report_v2.py:180) 只统一空白再做子串匹配。原始引用、工具先后顺序、每次提交和删除原因均保存在 [analogy_delivery.json](/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.14/s60_s62_review/analogy_delivery.json)；可追到 [F62 draft context](/Users/william/nautilus/results/20260914_070253_jubias-anaf-gpt56sol-s62/logs/analogy/draft_001.context.json)。这支持一个范围明确的后续修复方向：处理不改变文字含义的排版差异，而不是允许改写后的引文通过。

全文和源码工具确实在用。15 次 analogy 全部读过全文，共 51 次 `read_paper`，返回正文 312,650 字符；12 次 improve 全部查询源码，`read_candidate_code` 调用 99 次，其中 97 次成功。最终 17 个机制却有 9 个仅引用 abstract、5 个引用全文、3 个混合引用，说明“读过全文”与“全文依据进入最终建议”仍有明显差距。

累计模型 input 7,682,259 tokens、output 178,965 tokens；这些是多轮请求累计值，不是独立文献量。各 episode 耗时之和约 87.23 分钟，存在并行，不能当作 GPU 空闲时长。

**F62 的最高分主要来自模型选择，不能直接归为当轮类比收益**

F62 top-1 快照对应 `ff36137ccbc24a639318142f7a4f49ac`，public **0.954566**，private **0.93360**。其 [best_solution.py](/Users/william/nautilus/results/20260914_070253_jubias-anaf-gpt56sol-s62/logs/best_solution.py:594) 使用 `unitary/unbiased-toxic-roberta`。父节点的 DeBERTa-v3-large 只有 5 次 optimizer updates，public 0.481629。

[该轮 handoff](/Users/william/nautilus/results/20260914_070253_jubias-anaf-gpt56sol-s62/logs/analogy/handoffs/ff36137ccbc24a639318142f7a4f49ac.json) 明确拒绝 analogy 的 proxy-evaluation 建议，选择保留完整指标并替换为任务预训练模型。因此不能把这次巨大上升直接计为被采纳类比机制的收益；这也不排除 F 臂更早的提示对整个搜索轨迹有间接影响。

该权重的官方说明将其对应到 Jigsaw Unintended Bias 任务，而非仅通用语言预训练。[Hugging Face 模型卡](https://huggingface.co/unitary/unbiased-toxic-roberta) 因而带来两项需要区分的解释：更接近任务的先验可能提高成绩；原任务训练数据也可能与本实验从 public train 划出的内部验证集重叠，使候选选择乐观。尚未逐条核对该权重的训练成员。

我核实了集群实际安装的 MLE-bench `prepare.py`：`public/train.csv` 来自原始 `train.csv`，private 评分来自原始 `test_private_expanded.csv`。**目前没有证据确认 private test 泄漏**，不能仅凭任务预训练模型就宣布该 private 分数无效。这里首先是归因和 public 验证独立性问题。

同一高分模型后来加入论文启发的 FIFO memory，public 从 **0.954566 降到 0.953629**，队列和更新均有运行证据。排除整个任务预训练分支后，F62 最高 public 仍是最初 draft 的 0.922872；这只是已有候选内部观察，未生成任何“剔除后 private 成绩”。

**F61：类比诊断确实修好了实现，但主要是在追回先前损失**

F61 第一 draft public **0.911762**。加入 cell memory bank 后降为 **0.903203**：ranking 只在第 4 个梯度累积 microbatch 执行；前三个只执行 BCE，采样还存在优先 current rows、忽略 bank 的问题。

下一次 analogy 通过读取父源码定位这些问题，后续最佳候选 `0a060fbe…` 的实际计数为 `ranking_calls_by_microbatch=[909,909,909,909]`，各 microbatch 梯度覆盖率均为 1，public 回升到 **0.912938**。这是“诊断有据、实现改变、运行观测改变、分数回升”的有效案例，但相对最初 draft 的净增益只有 **+0.001176**。

证据在 [诊断 context](/Users/william/nautilus/results/20260914_070847_jubias-anaf-gpt56sol-s61/logs/analogy/62b4b50bec1d41dc80f9cc9b28bc0653_004.context.json) 和 [最终代码](/Users/william/nautilus/results/20260914_070847_jubias-anaf-gpt56sol-s61/logs/best_solution.py:2341)。A61 的最佳 public 为 0.930682，使用 DeBERTa-v3-small；F61 最佳仍是 ModernBERT-large。当前候选的模型选择和单位预算训练效率，可能比这条 ranking 细化更影响最终差距。

**不能再用上一批“动态权重没有更新”解释所有下降**

F62 的 `86e9091f…` 采用顺序乘法动态权重，运行记录有 32,266 次 alpha 更新，权重约 0.009259–0.148058、归一化熵 0.793585，EMA 和分组计数也在变化。然而 public 从父节点 **0.920234 降到 0.913687**。这次至少有明确的状态活动证据，应进一步区分目标是否匹配、更新噪声和额外计算开销，不能直接套用之前 boolean indexing 写入副本的解释。

两个完成 F run 中，声明采纳 analogy 的 6 个 improve 子节点为 **3 升、3 降**。其中最大的正向变化把仅训练 5 步的欠训练分支改成轻量实现，训练更新变为 23,547 次；这种挽救收益不等于在强 baseline 上的增益，不能简单平均成“类比质量分”。全部八条 improve 父子关系在 `candidate_analysis.json` 中。

**运行与资源方面**

五个完成 run 的日志均延续约 12 小时并生成 ensemble；没有在这些主日志中发现 rate-limit 中止迹象。候选预算结束不等于 run 失败：F61 的六个可评分候选全部以预算结束保存结果，说明之前的可评分快照机制在发挥作用。

生成代码仍会消耗预算：F61 一个 draft 在约 3,468 秒后发生 scatter dtype 不匹配；A 臂还出现 BCE+autocast、重复 backward、动态 padding 拼接、CPU/CUDA 混用等错误。这些是候选实现问题，不能归因于 P0 报告路径。

F61/F62 的验证与导出累计耗时分别约 **4.21 h / 4.51 h**；其中包含必要推理与结果保存，不等于 GPU 闲置。硬件也没有统一：已核实 A61 为 V100、F61 为 A10，F62 为 V100。因此固定 wall-clock 下的候选数量、训练步数与 backbone 选择存在额外差异。

**对下一步的判断**

现有证据支持先解决“正确读到的依据能否完整交付、交付的机制是否改善强父节点”这两个具体问题，继续单纯增加阅读预算的依据较弱。优先考虑对强调标记做保守归一化，并让 partial 交付明确保留机制优先级、给被删核心机制有限纠错机会；长度问题可优先精简报告组织，而非无条件提高所有上下文预算。

验证效果时，更有辨识力的是固定一个强父候选、固定 backbone/权重来源与 GPU，将其 ordinary improve 与 analogy improve 配对比较，观察同一预算下的 public/private 改变，并单独记录冷启动模型选择的收益。当前整轮 A/F 差值仍有价值，但不足以分辨上述来源。S60 需要新的完整 F 结果才能补成三对；现有残留结果不能恢复为完成实验。

以上仅为分析建议，本次没有实施任何代码或实验配置更改。
