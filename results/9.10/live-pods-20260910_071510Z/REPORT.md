# S51–S53 A/F 六个实验 Pod：运行中日志检查

采样时间：2026-09-10 00:15–00:17 PDT（07:15–07:17 UTC）。这是运行中的快照，不是最终实验结果。
六个 Pod 均为 Running，重启次数均为 0；均分配到 NVIDIA A10。已下载六份完整 Pod stdout/stderr 日志，
以及各自的 MLEvolve.log、journal、analogy 记录、当前候选代码和进程/GPU 状态。

**核心发现：GPU 已恢复满负荷，但截至采样，已完成并写入 journal 的 15 个候选全部失败；另外每个 Pod
仍有 3 个候选主进程在执行，共 18 个。未完成的候选不能算作失败，也不能据此判断 A/F 最终效果。**

## 六个实验的状态

时间为 9 月 9 日晚洛杉矶时间；“首次执行”指启动候选 Python 子进程，不等同于首次 GPU 训练。
所有 Pod 约 19:08 启动。详细时间点、原始日志行号和异常消息见 [summary.json](/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.10/live-pods-20260910_071510Z/summary.json)。

| 实验 | 首次执行 | entrypoint 至首次执行 | 已完成失败：OOM / checkpoint | 已完成有效候选 | 00:17 GPU / 已用显存 |
|---|---|---:|---:|---:|---|
| A-S51 | 20:15:19 | 66.8 分钟 | 1 / 2 | 0 | 100% / 22,169 MiB |
| F-S51 | 20:41:12 | 92.7 分钟 | 2 / 0 | 0 | 100% / 20,171 MiB |
| A-S52 | 20:30:05 | 81.5 分钟 | 1 / 2 | 0 | 99% / 22,209 MiB |
| F-S52 | 20:15:02 | 66.6 分钟 | 1 / 1 | 0 | 100% / 20,757 MiB |
| A-S53 | 20:13:34 | 65.1 分钟 | 1 / 1 | 0 | 100% / 22,329 MiB |
| F-S53 | 20:22:02 | 73.5 分钟 | 3 / 0 | 0 | 100% / 20,125 MiB |

各卡 nvidia-smi 报告总显存 23,028 MiB。主进程之外还可见 DataLoader 子进程；不能把它们重复计为独立候选。

## 1. 前期等待由多个环节累加，全文阅读占比较小

- **依赖检查：约 12–17 分钟。** 从 entrypoint 开始到 torch 等依赖检查完成。grader 检查只占约 10 秒，
  后续 Python 依赖导入异常慢。F 的 nltk/rank_bm25 检查还花了约 5–7 分钟。
- **全局记忆初始化区间：约 13–25 分钟。** metric direction 的 API 请求数秒即完成，之后到
  `Global memory enabled and initialized` 才出现长空窗。代码表明该区间涉及 memory 模块导入及
  embedding/retriever 初始化，不能误称为“判断指标方向的 LLM 调用耗时二十分钟”。
- **串行生成 3 份 draft：约 30–42 分钟。** 第一份完成后，仍空等 19–27 分钟才统一进入执行阶段。
  这是当前 Phase 1 的行为，可以直接从日志证实。
- **编译器安装：约 13–83 秒。** 成功完成，不是十几分钟启动延迟的主要来源。

例如 A-S52 的依赖检查到 19:25:32 才完成；指标方向在 19:31:40 已确认；global memory 到 19:56:30
才完成；第一份 draft 在 20:06:52 已准备好，却直到 20:30:05 才执行。
证据：[A-S52 Pod 日志](/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.10/live-pods-20260910_071510Z/mlevolve-jubias-base-s52-4bdtd.log:544)。

依赖与模型经共享 PVC 加载，I/O、缓存或加载锁竞争是值得排查的方向，但当前日志没有逐项耗时，尚不能确诊。
候选子进程启动后仍会导入依赖、加载模型和预处理数据；现有日志也不能精确拆分这一段到首次 GPU kernel 的耗时。

## 2. 九个 OOM：共享一张卡的三个候选存在真实显存竞争

每个 Pod 的三个执行槽都指向 GPU 0。OOM 消息列出同时存在的其他进程及其显存占用。
例如 F-S51 的失败节点 df55b071 在 AdamW 更新时只想再分配 22 MiB，却仅剩 6.75 MiB；同卡另一个进程
已占 13.78 GiB，本进程占约 7.57 GiB，主 agent 进程另占约 700 MiB。
证据：[F-S51 journal](/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.10/live-pods-20260910_071510Z/20260910_023628_jubias-anaf-s51/logs/journal.json)。

这支持“并发训练缺少显存协调”的判断；不能把所有 OOM 都归为某个候选单独运行也放不下。
一些候选已经自动缩小 batch，A-S52 的一个 debug 候选已改用 DeBERTa-v3-base，但还没有完成验证结果。

## 3. 六个 checkpoint 反向传播错误在 A/F 中重复出现

异常为 `Trying to backward through the graph a second time`，调用栈经过
`torch/utils/checkpoint.py`。六次失败均涉及 DeBERTa-v3-large；其中 A 臂 5 次、F 臂 1 次。
这不支持把该错误归因于 analogy。
证据：[A-S51 journal](/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.10/live-pods-20260910_071510Z/20260910_022351_jubias-base-s51/logs/journal.json)。

已在当前 debug 候选里看到 `gradient_checkpointing_kwargs={"use_reentrant": False}`。
这说明 agent 正在尝试修复，是否足够还要等这些候选执行完成；本次没有修改生成代码或运行环境。

## 4. CPU 分配与可观测性也有问题，但不能仅由此断定训练卡死

8 CPU 被执行器按三个槽位整除，每个候选绑定 2 个逻辑 CPU。六个运行的失败输出中都出现过
DataLoader 警告：可用 CPU 建议 worker 上限为 2，但生成代码创建了 4 或 6 个 worker。
这可能拖慢分词和数据加载，值得与 GPU 执行并发一起协调。

日志最后一条停在“REPL is executing code”附近，不能证明进程卡死。
[executor.py](/Users/william/Documents/project/python/MLEvolve/engine/executor.py:239) 使用
`proc.communicate(timeout=...)`，子进程 stdout/stderr 在退出后才返回；正在执行的训练没有持续输出到 Pod 日志。
本次快照确认六卡均 99–100%，每 Pod 仍有三个候选主进程，但无法仅凭这些证明 epoch 或 validation 已推进到哪里。

## 5. F 全文阅读生效；improve 注入尚未进入实际比较

| F 实验 | analogy 调用耗时 | 读取正文字数（字符） | 打开论文数 / 读取次数 | 已记录阶段 |
|---|---:|---:|---:|---|
| S51 | 164.8 秒 | 7,065 | 1 / 1 | draft |
| S52 | 137.9 秒 | 18,370 | 3 / 3 | draft |
| S53 | 185.7 秒 | 12,548 | 2 / 2 | draft |

三次调用均成功并注入首个 draft，正文读取有 `draft_001.fulltext.json` 记录。
当前每个 F 只有一条 draft analogy invocation；已完成节点全失败，后续调度走 debug，尚未出现 improve invocation。
因此现在不能评价“F 的 draft + improve 注入”是否有益。F-S52 的首次执行甚至早于同种子的 A-S52，
也说明不能把总体启动时间差直接当作阅读论文的开销。

## 建议的下一步

1. 优先处理 checkpoint 兼容性和 GPU 显存协调，目标是先产出有效候选。下一批再统一调整 A/F，
   不要为了利用率数字继续增加训练并发。
2. 对依赖导入和 memory 初始化加分段计时，评估将依赖放进镜像、模型预缓存或使用节点本地缓存。
   先定位，避免盲目增加 CPU。
3. 让已生成 draft 尽早进入执行，并分离代码生成与 GPU 执行的容量控制；同时保持候选生成所见状态一致，
   避免顺手改变实验算法语义。
4. 增加候选 stdout/stderr 实时落盘和阶段心跳，才能把 GPU 曲线精确对齐到加载、训练、验证。

本次为只读采样，六个实验继续运行。尚未采集最终分数，也未更改资源、停止 Pod 或部署修复。
