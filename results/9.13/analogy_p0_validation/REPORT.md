# Analogy P0 实施与验证记录

日期：2026-09-13。范围：用户批准的 P0 报告交付修复，以及不再需要的一次性分析脚本清理。P1/P2 未实施。

## 实施结果

- Runtime observed facts 使用 `runtime_evidence` 数组，`report_schema_revision=2` 与 `context_version=2` 分开。保留旧提交兼容，对旧单路径、分号列表、数字数组下标做确定性规范化并记录转换；所有路径均需通过校验。
- 路径示例只来自实际展示的 runtime 数据，不把被裁剪或未知字段当作证据。源码查询明确 symbol 与行范围互斥。
- 校验问题精确到字段，区分缺字段、路径不可用、代码未读、引文未返回及渲染超限。错误反馈最多 4,096 UTF-8 字节；原始诊断完整落盘。仅尺寸错误给压缩提示。
- 保持 14 轮默认上限，第 12 轮前提交初稿；纠错期间允许一次定向证据读取，之后继续提交。输入上限不提高；默认预留初稿和两次修正历史共 24,576 token 的估算空间。
- 共享事实错误阻止交付；某个机制的论文证据错误导致整个机制移除，不能静默变成摘要支持。保留独立有效的完整机制时明确标记 partial，保存原始索引、最终 ID、校验删除和渲染裁剪对应关系。
- `.context.json` 与 replay 结果保存 `submission_attempts`；index 增加交付状态、失败类别、首次提交轮次、提交次数、纠错结果和最终机制数。旧 `ok` 含义保持不变。

主要实现：[报告校验](/Users/william/Documents/project/python/MLEvolve/engine/analogy/report_v2.py)、[多轮循环](/Users/william/Documents/project/python/MLEvolve/engine/analogy/observed_loop.py)、[落盘](/Users/william/Documents/project/python/MLEvolve/engine/analogy/agent.py)、[使用说明](/Users/william/Documents/project/python/MLEvolve/docs/analogy_context_v2.md)。

## 验证

共 **135 项 unittest 回归通过**，另有现有 analogy-injection 检查脚本通过。测试记录见 [tests.json](/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.13/analogy_p0_validation/tests.json)，各 suite 完整输出保存在同目录 `.log` 文件。

| Suite | 通过数 |
|---|---:|
| verify_analogy_report_delivery | 18 |
| verify_analogy_submission_loop | 9 |
| verify_analogy_context | 16 |
| verify_analogy_observation | 17 |
| verify_analogy_fulltext | 15 |
| verify_analogy_handoff | 12 |
| verify_gpt6_transport | 30 |
| verify_gpt6_configuration | 6 |
| verify_review_contracts | 12 |

重点覆盖：

- S57 实际提交的三条分号路径、S58 实际提交的 `[0]` 路径，以最小原始事实 fixture 复现并保留 trace SHA256；任一对应字段缺失时仍不能接受共享事实。
- 12/13/14 轮提交和修正、一次补读限制、同轮补读后提交、无效 JSON 保存、主动放弃/校验失败/调用失败区分。
- 未读代码、错 hash、隐藏字段、unknown/空值/非有限值、未返回的正文引文仍被拒绝；False 和 0 是有效值。
- 部分报告的校验/渲染裁剪不丢失机制身份；大量 Unicode 错误反馈不超过总字节预算，原始诊断不受裁剪影响。
- 旧配置、旧报告和现有手工/Responses 工具回放兼容；真实 pinned OpenAI SDK 1.66.3 使用 mocked HTTP 验证。

验证在本地 CPU 环境进行，未调用模型 API、访问集群、运行候选训练或改写历史 run。历史 fixture 验证的是具体失败输入的处理，不声称六份完整报告都已经过真实模型重试，也不把交付修复当成分数提升证据。`git diff --check` 通过。

## 清理

删除了审计确认过期或重复的 **15 个 `/tmp` 脚本**。完整路径、大小和 SHA256 见 [cleanup.json](/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.13/analogy_p0_validation/cleanup.json)。

- 历史 Pod/run 的一次性采集、GPU 查询、绘图与运行审计脚本已完成用途，输出已落盘。
- 两份临时 review harness 已由正式回归工具覆盖。
- 两份历史分析脚本与仓库中已保存的副本逐字节一致；临时 fetch 脚本与正式 fetch-run 脚本逐字节一致。
- 两个仓库内没有这些 `/tmp` 路径引用，不需要断开或重写分析报告链接。

保留仓库内的正式分析、画图、fetch、replay 和回归工具；保留报告引用的分析/恢复脚本、最新 controller 复现及候选源码、日志、JSON/CSV、图像和报告。既有 `.DS_Store` 修改未处理。

## 交付边界

改动留在本地，未 commit/push 或同步集群。没有机制状态探针、自动早停、评分改动、新 node 类型、模型切换或 Job 调整。UPDATELOG 已记录此次 P0 更新。
