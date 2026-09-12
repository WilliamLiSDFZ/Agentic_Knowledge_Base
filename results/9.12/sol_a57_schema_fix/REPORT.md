# S57 A 审查 schema 冲突修复

日期：2026-09-12。诊断见 `../sol_a57_schema_error/REPORT.md`。

## 修改

- MLEvolve `agents/code_review_agent.py`：revised_code 从 string 改为 string/null，
  与“不修改时返回 null/省略”的既有说明和消费代码一致。
- `agents/result_parse_agent.py`：metric 从 number 改为 number/null，失败候选
  可以通过结构校验，继续由解析流程标记 buggy 并设置 WorstMetricValue。
- 新增 `utils/verify_review_contracts.py`，在真实 SDK 的 HTTP 边界构造响应，
  调用真实 schema、代码审查、diff patcher 和结果解析函数。

未更改业务决策、错误处理策略或实验配置：需要修改但没有代码时保留原有最多
三次审查及最终回退，错误类型仍被结构校验拒绝，真正的传输终止异常仍会传播。
Sol/high、A/F、全文/源码工具、GPU 配置、候选预算和 runtime 协议均不变。
candidate runtime 启用时的审查分支纳入新测试；结果解析的 LLM 分支在 runtime
关闭时测试，runtime 自身解析路径不受这个 schema 修改影响。

## 验证

使用实际固定 OpenAI SDK 1.66.3，HTTP 由 httpx.MockTransport 替代。
没有真实模型调用、GPU 训练或集群写入。

修改前，第一版新测试运行 12 项，在 Sol/GPT-6 下合计出现八个 null 相关
错误；错误与现场一致。修改后最终测试（额外覆盖 runtime 开/关）全部通过。

| 检查 | 结果 |
| --- | --- |
| `verify_review_contracts.py` | 12 passed |
| `verify_gpt6_transport.py` | 30 passed |
| `verify_gpt6_configuration.py` | 6 passed |
| 修改文件语法、`git diff --check` | passed |

新套件覆盖批准时 null/省略且只发一次请求、真实 diff 应用、缺少修订代码时
重试/最多三次回退、memory 开关下失败结果的 null、成功的浮点和零分、错误
指标方向拒绝，以及数字 revised_code、字符串/布尔 metric、缺少必填字段
仍被拒绝。两种模型分别跑完整套件。格式评分器在成功结果用例中被 mock，
这里不重复验证评分器本身。日志和源文件哈希保存在同目录。

## 同步与重跑

代码仅在本地修改，尚未 commit/push。通过 Git 同步 MLEvolve 后，重建需要
重跑的 Job，再 apply 现有 S57–S59 YAML；只对同名已失败 Job 再次 apply
不会创建一次新运行。仍在运行的实验使用共享 checkout 时，应先停止相关
实验再同步，或使用独立 checkout。

本次没有修改集群共享代码、venv、Secret 或任何 Job/Pod；同步和 apply 由用户操作。
