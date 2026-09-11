# S54–S56 完成后运行审计

只读分析本地 fetch 的六个 run。原始数据位于 `/Users/william/nautilus/results/20260911_07*_jubias-*`；逐候选证据保存在同目录 `runtime_audit.json`。未修改代码、原图、原始结果或集群。

## 口径

- 以 `logs/candidate_results/summary.json`、逐候选 `execution.json` 和 `events.jsonl` 为执行与落盘来源，`journal.json` 仅补源码/异常上下文。
- root 不算候选；registered 包含队列未执行候选；执行尝试包含启动前 AST 拒绝，不能称所有66个都训练过。
- 六个 journal 均落后于运行末尾：最后日志 stats 比 journal 多1个节点，F54 多2个。节点树不能独立作为最终计数依据。
- `budget_exhausted` 是正常主动收尾，不等于外部 `timeout`。
- 下文候选耗时是占用执行槽的墙钟时间之和，包括 CPU、I/O、验证、导出和训练，不是 GPU 活跃小时。validation/export 只统计已经完成并写入事件的阶段；硬中断中的未完成阶段不在总数中。

## 总体

75 个注册候选，66 个执行尝试，45 个完整可评分（68.2%），14 个 failed，7 个 timeout，9 个最终 queued 未执行。45 个可评分候选均产生 `worker_finished` 正常收尾事件，无本次 `finish()` 返回分数接口错误。

| Run | 注册 | journal 非root | 执行 | 完整结果 | failed | timeout | 未执行 | 首个完整结果/min | 最优公开分数 | 最优快照时间/h |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A54 | 11 | 8 | 9 | 7 | 1 | 1 | 2 | 61.07 | 0.929835 | 9.55 |
| A55 | 11 | 8 | 9 | 7 | 1 | 1 | 2 | 73.77 | 0.927630 | 9.09 |
| A56 | 14 | 11 | 12 | 7 | 4 | 1 | 2 | 93.56 | 0.924555 | 10.63 |
| F54 | 10 | 7 | 9 | 7 | 0 | 2 | 1 | 70.21 | 0.922761 | 9.44 |
| F55 | 16 | 14 | 15 | 8 | 6 | 1 | 1 | 68.77 | 0.928885 | 8.35 |
| F56 | 13 | 11 | 12 | 9 | 2 | 1 | 1 | 68.48 | 0.926935 | 1.14 |

首个完整结果/最优快照时间均相对 candidate runtime run start；最优分数是公共固定验证集，不能与 private test 或不同 seed 的 holdout 直接等同。F56 最优结果来自首个 draft，后续约11小时未超过其公开验证分数。

## 上次修复确实生效

- 49 个候选具有 smoke 估计与首次完整验证可比数据，48 个估计误差在±10%内（−9.66%～+7.40%；这48个均为 calibrated=true）。整体49个比值中位数1.00086。唯一2.008倍的是F56末尾 fusion_draft：仅剩7.37分钟、主动跳过双样本校准，不能说所有估计都已准确。
- 43 个正常收尾候选保存的最优 checkpoint 至少307步，最大20,550步；另2个是总时限尾部只训5步的候选，原因见下。
- 完整验证与后续验证间有实际训练进展，未发现旧版导出后只推进一步即再验证的常态。

## 未解决的主要运行问题

### 总时限尾部仍无有效候选准入

7 次 timeout 中6次都发生在run总截止：A54 a76b4395 只获得39.04m、A55 c17b04f9 63.11m、A56 4554586f 9.91m、F54 a06dcf6a 3.03m、F55 9199e398 8.62m、F56 3d17e0b1 7.37m。F54还有1次独立90m候选上限超时，见下一节。

F54 `1d927b42` 和 F55 `c3270863` 正常保存0.47555/0.51703结果但只训5步。两者排队204.5/145.2分钟，开始后预处理22.6/16.5分钟，完整校准后所剩时间3.4/8.8分钟，`continue_training=false`。其smoke估计分别仅+2.4%/+1.7%，不是旧版估计数倍过高复发，而是进入执行时已没有足够训练加收尾预算。

建议下一轮优先研究按剩余run预算决定是否接纳新候选、根据同模型/父候选实测推理和预处理成本预留时间；接近终点时停止生成注定排队/中断的昂贵新候选。现有“无best先完整校准”需要先判断完整验证+重载复验+test是否可能完成。

### F54 慢推理候选确实在导出中损失

`2c4d00adb9a84881836a4080483981dc`：预处理24.45m，5步smoke后验证估计24.36m/实测25.68m（−5.1%），test估计30.48m；仅验证一次+重载后的复验+test预计就约80m，再加预处理已超过90m。完整验证分数0.44211；最终在 `predict_test -> predict_positions -> probabilities.detach().float().cpu().numpy()` 收到KeyboardInterrupt，执行90.06m，无完整快照。旧的同run快照正常保留。其后debug `c3b3d05c`正常保存0.91795（19,899步）。

### 生成代码兼容性和diff稳定性仍影响候选产出

- 8次diff语法/缩进失败：A55×1，F55×5，F56×2。F55一条分支连续三个debug仍然语法错误，最终预算浪费主要是延迟获得反馈与LLM修补，不是这几个AST失败本身（每次约0.4–1.1秒）。
- 3次checkpoint二次反传：A54×1、A56×1、F55×1。
- 3次缺C编译器：全部A56；较上次运行中观察又新增1次，说明现有review/debug记忆没有防止其他候选重复选择不可用的编译路线。
- 可优先将AST/compile静态语法检查放到入队前，同时将实际容器C编译器能力与可靠checkpoint/AMP模式显式反馈给生成和review。此处仅建议，未改代码。

### A55 先前I/O等待并非永久卡死

运行中记录的 `bd1b4e2260714dbaaf1cd1b869cc5147` 后续成功完成：预处理6.24m、总执行103.33m，最优快照20,550步、公开验证0.926169，2次完整验证+导出。不能将当时单次D状态/GPU=0当成死锁。

尾部另一A55候选 `c17b04f9` 在完整验证后20分钟仍未完成导出，events没有checkpoint保存/加载阶段细分、journal遗漏尾节点，因此本地数据不能定位最后是写盘、重载复验还是test；不据此断言具体I/O根因。

## 执行开销与队列

| Run | 总候选占槽/h | 已知预训练阶段/h | 已完成验证/h | 已完成导出/h |
|---|---:|---:|---:|---:|
| A54 | 11.71 | 1.59 | 1.90 | 2.93 |
| A55 | 11.51 | 2.34 | 1.63 | 3.25 |
| A56 | 11.45 | 1.38 | 1.88 | 4.04 |
| F54 | 11.56 | 2.66 | 1.82 | 2.58 |
| F55 | 11.45 | 1.76 | 1.92 | 3.86 |
| F56 | 11.57 | 1.82 | 2.03 | 3.18 |

六个run合计占槽69.26h；已完成验证11.19h（16.15%）、已完成导出19.83h（28.63%），两者合计44.78%。导出本身含完整checkpoint重载验证+test预测；这不是额外独立训练。已知进入training_started前阶段11.55h（16.68%）。剩余部分不能直接称纯训练：包括smoke、checkpoint保存、未完成推理以及其他开销。

因此可评分保存机制已经有效，但完整评估/导出很贵。应评估可靠的更快预测实现（AMP、batch大小、统一预测callback）、减少不必要的完整重复推理，并保持checkpoint可复现和完整test门槛。单纯继续增加训练候选数量不一定更划算。

所有已完成执行区间不重叠，实际一张卡只有一个候选执行槽。相邻候选交接间隔合计仅6.08分钟（六个run合并），多数0.5–2.7秒；F55语法错误连续修补时最长136秒。未发现多候选抢同卡或执行队列死锁。

但候选从注册到实际启动的排队中位数105.3m、最大242.3m。队列长会让规划建立在数小时前的信息上，也会使尾部新候选仅获得几分钟预算。这是调度/规划反馈延迟，不能称GPU空转；前面的候选大多一直占用执行槽。

## 明细

| Run | 节点 | stage | status | scoreable | 执行/min | 预训练/min | steps(最优) | 公开分数 |
|---|---|---|---|---|---:|---:|---:|---:|
| A54 | 856506ee | draft | budget_exhausted | scoreable | 81.06 | 10.12 | 4407 | 0.915048 |
| A54 | 1e564bc6 | draft | failed | unavailable | 9.47 | 9.21 |  |  |
| A54 | da50a145 | improve | budget_exhausted | scoreable | 110.10 | 10.71 | 6138 | 0.868349 |
| A54 | 49fa616e | draft | budget_exhausted | scoreable | 55.47 | 13.17 | 813 | 0.916666 |
| A54 | bda51d56 | debug | budget_exhausted | scoreable | 82.97 | 2.93 | 613 | 0.886462 |
| A54 | 7daab15e | improve | budget_exhausted | scoreable | 110.78 | 15.00 | 6749 | 0.899321 |
| A54 | 03f42164 | improve | budget_exhausted | scoreable | 106.74 | 12.68 | 1650 | 0.929835 |
| A54 | 218911ca | improve | budget_exhausted | scoreable | 107.05 | 7.94 | 1770 | 0.916875 |
| A54 | a76b4395 | draft | timeout | unavailable | 39.06 | 13.35 |  |  |
| A54 | 2a2ab7a0 | improve | queued | unavailable | 0.00 | 0.00 |  |  |
| A54 | df85d294 | improve | queued | unavailable | 0.00 | 0.00 |  |  |
| A55 | 79a34999 | draft | budget_exhausted | scoreable | 76.80 | 5.80 | 6971 | 0.917262 |
| A55 | bb4314ad | draft | budget_exhausted | scoreable | 67.73 | 20.71 | 2263 | 0.924838 |
| A55 | bd1b4e22 | improve | budget_exhausted | scoreable | 103.33 | 6.24 | 20550 | 0.926169 |
| A55 | d4dac7ee | draft | budget_exhausted | scoreable | 65.79 | 27.21 | 1561 | 0.906367 |
| A55 | 865037d0 | improve | failed | unavailable | 0.02 | 0.00 |  |  |
| A55 | eecb92f4 | improve | budget_exhausted | scoreable | 100.25 | 3.33 | 18855 | 0.925774 |
| A55 | 20bbfe0a | debug | budget_exhausted | scoreable | 104.92 | 21.31 | 2979 | 0.927630 |
| A55 | e43131cc | improve | budget_exhausted | scoreable | 108.81 | 25.69 | 4562 | 0.913366 |
| A55 | c17b04f9 | improve | timeout | unavailable | 63.13 | 30.34 |  |  |
| A55 | 4f5f0fe0 | improve | queued | unavailable | 0.00 | 0.00 |  |  |
| A55 | 8eba8555 | improve | queued | unavailable | 0.00 | 0.00 |  |  |
| A56 | 1fb516e7 | draft | failed | unavailable | 11.32 | 6.24 |  |  |
| A56 | 1761c01b | draft | failed | unavailable | 7.31 | 6.89 |  |  |
| A56 | 5864112a | debug | budget_exhausted | scoreable | 100.39 | 3.71 | 9530 | 0.915389 |
| A56 | 35e16e80 | draft | failed | unavailable | 12.83 | 12.64 |  |  |
| A56 | 49028cb1 | debug | budget_exhausted | scoreable | 102.01 | 5.99 | 794 | 0.915217 |
| A56 | 0480acbb | improve | budget_exhausted | scoreable | 100.93 | 3.72 | 9570 | 0.917937 |
| A56 | bc4a0848 | debug | budget_exhausted | scoreable | 69.28 | 12.29 | 511 | 0.901962 |
| A56 | f7cae131 | improve | budget_exhausted | scoreable | 102.40 | 6.00 | 825 | 0.908381 |
| A56 | 5a75e359 | improve | budget_exhausted | scoreable | 101.14 | 3.72 | 9153 | 0.924555 |
| A56 | e3adb9a7 | improve | budget_exhausted | scoreable | 63.41 | 12.31 | 307 | 0.880753 |
| A56 | 83fd631c | draft | failed | unavailable | 5.95 | 5.51 |  |  |
| A56 | 4554586f | improve | timeout | unavailable | 9.93 | 3.79 |  |  |
| A56 | 091e9347 | debug | queued | unavailable | 0.00 | 0.00 |  |  |
| A56 | ff712c3f | draft | queued | unavailable | 0.00 | 0.00 |  |  |
| F54 | d24983a2 | draft | budget_exhausted | scoreable | 78.04 | 6.88 | 1933 | 0.911807 |
| F54 | 2c4d00ad | draft | timeout | unavailable | 90.06 | 24.45 |  |  |
| F54 | f7be07d5 | improve | budget_exhausted | scoreable | 91.39 | 25.74 | 1488 | 0.910052 |
| F54 | 4f9e2247 | draft | budget_exhausted | scoreable | 62.90 | 24.66 | 2148 | 0.902627 |
| F54 | c3b3d05c | debug | budget_exhausted | scoreable | 111.84 | 5.35 | 19899 | 0.917951 |
| F54 | 27273be3 | improve | budget_exhausted | scoreable | 108.16 | 24.30 | 3223 | 0.922761 |
| F54 | e66f9b92 | improve | budget_exhausted | scoreable | 108.02 | 25.91 | 16542 | 0.915616 |
| F54 | 1d927b42 | improve | budget_exhausted | scoreable | 40.29 | 22.60 | 5 | 0.475552 |
| F54 | a06dcf6a | improve | timeout | unavailable | 3.05 | 0.00 |  |  |
| F54 | 5e2ae8ff | improve | queued | unavailable | 0.00 | 0.00 |  |  |
| F55 | d5978d36 | draft | budget_exhausted | scoreable | 78.81 | 4.44 | 2752 | 0.927925 |
| F55 | 77b86b6e | draft | budget_exhausted | scoreable | 65.52 | 14.80 | 1513 | 0.915165 |
| F55 | 62fdc8e6 | improve | budget_exhausted | scoreable | 108.24 | 3.25 | 5317 | 0.928041 |
| F55 | 8e8ee68e | draft | failed | unavailable | 6.63 | 6.36 |  |  |
| F55 | b1cec675 | improve | failed | unavailable | 0.01 | 0.00 |  |  |
| F55 | d480dc30 | debug | failed | unavailable | 0.01 | 0.00 |  |  |
| F55 | 434f2a2f | debug | failed | unavailable | 0.01 | 0.00 |  |  |
| F55 | 62182c79 | debug | failed | unavailable | 0.01 | 0.00 |  |  |
| F55 | 47d29cf7 | debug | budget_exhausted | scoreable | 102.54 | 5.22 | 4476 | 0.850459 |
| F55 | 994b5cf6 | improve | budget_exhausted | scoreable | 108.40 | 21.53 | 3916 | 0.928885 |
| F55 | 3e133f62 | draft | budget_exhausted | scoreable | 60.98 | 22.86 | 1399 | 0.903241 |
| F55 | c8595686 | improve | budget_exhausted | scoreable | 102.65 | 6.31 | 13408 | 0.915415 |
| F55 | c3270863 | improve | budget_exhausted | scoreable | 44.49 | 16.54 | 5 | 0.517030 |
| F55 | 4eb1b85a | improve | failed | unavailable | 0.01 | 0.00 |  |  |
| F55 | 9199e398 | improve | timeout | unavailable | 8.64 | 4.00 |  |  |
| F55 | 60d14fdb | debug | queued | unavailable | 0.00 | 0.00 |  |  |
| F56 | 4eed868e | draft | budget_exhausted | scoreable | 62.83 | 6.29 | 1255 | 0.926935 |
| F56 | 0c6473de | draft | budget_exhausted | scoreable | 73.75 | 26.36 | 831 | 0.920188 |
| F56 | c87f0ec8 | improve | budget_exhausted | scoreable | 100.48 | 9.07 | 4714 | 0.926396 |
| F56 | 1f0059b2 | draft | budget_exhausted | scoreable | 62.19 | 24.74 | 1520 | 0.909731 |
| F56 | 5198d985 | improve | failed | unavailable | 0.01 | 0.00 |  |  |
| F56 | b1738447 | improve | budget_exhausted | scoreable | 92.19 | 5.34 | 1576 | 0.692728 |
| F56 | c339eab1 | debug | failed | unavailable | 0.01 | 0.00 |  |  |
| F56 | 580ae587 | improve | budget_exhausted | scoreable | 108.68 | 5.61 | 19002 | 0.821563 |
| F56 | 87d731b9 | draft | budget_exhausted | scoreable | 78.70 | 6.61 | 4769 | 0.909408 |
| F56 | 0f76ee62 | draft | budget_exhausted | scoreable | 57.95 | 3.43 | 1486 | 0.913926 |
| F56 | f61ccbee | improve | budget_exhausted | scoreable | 50.21 | 21.36 | 1284 | 0.832325 |
| F56 | 3d17e0b1 | fusion_draft | timeout | unavailable | 7.40 | 0.53 |  |  |
| F56 | c967bb47 | improve | queued | unavailable | 0.00 | 0.00 |  |  |

## CPU dev 补读后的完整性核对

补齐集群只读保存的 `cluster_sources/<run>/<node>/solution.py`、`execution_spec.json`、`execution.json`、`worker_finished.json` 后：75/75源码 SHA-256 与注册 `candidate.json.source_sha256` 一致；45/45可评分源码也与所选 snapshot 的 source_sha256 一致。45个 worker_finished 均存在，其 snapshot_id 和 best_validation_score 与所选快照45/45一致。逐项记录见 `source_integrity.json`。未读取模型权重，因此该核对验证源码与结果身份一致，不是离线重新加载权重验证。

A55 尾部 `c17b04f9` 没有 worker_finished；execution_spec 确认总run截止给该候选63.11分钟。源码正常使用 `torch.inference_mode()` 和 AMP，validation/test共用相同预测函数；没有发现callback中额外完整重复推理。save_checkpoint 保存可训练参数、tokenizer/config和feature_state，load_checkpoint读取保存参数；这只能列出可能开销路径，无法从源码推断具体耗时或最后中断位置。故先前“完整验证后20分钟未完成导出，具体阻塞阶段未知”的结论保持，不能归因为缺AMP或确定的I/O卡死。
