# S57–S59 错误修复验证

日期：2026-09-11 PDT。诊断来源：
`../s57_s59_live_errors_20260912_044127Z/REPORT.md`。

## 修改内容

1. **模型传输超时**：`llm/responses.py` 将 `request_timeout` 纳入暂时性错误，统一平铺和嵌套错误对象的解析。覆盖 JSON 返回、SSE error、response.failed 和 SDK APIError；失败流的部分输出被丢弃，重发原始请求。最多三次尝试，不增加外层重试；确定性配置/模型/凭据错误仍终止。
2. **CPU affinity 与 Python 模块语义**：`engine/executor.py` 使用独立启动器设置 CPU affinity，随后 exec 同一解释器正常执行候选脚本。候选源码不再被插入前缀，保留 docstring、future imports、__file__、argv、sys.path 和 traceback 行号。进程组、GPU 可见性、执行槽及清理逻辑保持原有行为。
3. **超时日志**：只有执行器实际触发 subprocess.TimeoutExpired 才说明超过执行上限。候选主动抛 TimeoutError 时保留原异常与实际执行秒数，不再把约两分钟的运行描述为超过两小时。
4. **生成/审查约束**：统一使用 session.remaining()/elapsed()，禁止由整个 run 或父候选时间推算当前候选截止时间；训练停止和 finalization reserve 由 runtime 管理。明确采用 finish() 返回的 submission_path，移除 runtime 模式下冲突的旧目录/输出自检指导。

第 4 项是对模型生成与审查规则的强化，不是对任意生成代码正确性的保证。既有预算实现不需要改变；新增回归证明晚启动的候选仍获得自身 7200 秒额度，同时受整个实验剩余预算封顶。未重写历史候选代码或改变已保存结果。

## 验证范围

**87 项不同测试全部通过**：CPU dev 的原有 Python 3.11.13 / OpenAI 1.66.3
环境下通过 transport 15 项、execution pipeline 21 项、candidate runtime 39 项
（共 75 项，Linux affinity 测试均实际执行）；本地 analogy handoff 12 项通过。
本地 candidate runtime 39 项亦通过。集群测试首次读取共享依赖较慢，最终均正常
完成，没有测试超时。具体输出见 `linux_checks.log`、`local_handoff.log` 和
`local_candidate_runtime.log`，汇总见 `checks.json`。
`source_manifest.json` 记录已验证的 8 个修改后 Python 文件 SHA256，确认集群临时
副本与本地最终代码一致。

- Transport：六种超时错误表示的恢复/三次耗尽；失败流部分输出丢弃；相同输入重发；确定性错误只尝试一次。采用项目固定 OpenAI SDK 和 httpx MockTransport，不请求模型服务。
- Executor：真实 CPU 子进程验证正常模块、docstring/future imports、UTF-8、路径含空格、同目录导入、错误行号、提前超时和真正执行超时；Linux 额外验证实际 CPU affinity 及绑定失败后的槽释放。
- Candidate runtime：真实小型 CPU 训练、结果发布/恢复、正常与预算停止、异常后结果保留、阶段预算及晚启动时钟；模拟任务数据全部生成在临时目录。
- 另验证 analogy handoff 和 runtime 开关下的提示兼容性。语法与 git diff 空白检查覆盖修改文件。

## 发布边界

代码修改位于本地 MLEvolve 工作区，UPDATELOG 位于 Agentic_Knowledge_Base。
集群验证仅使用 CPU dev pod 下自动清理的独立 `/tmp/mlevolve-s57-fixes-*` 副本，使用既有 Python/venv，不覆盖共享仓库或依赖。
没有提交或推送 Git、apply Job、删除/重启 Pod，也没有访问模型接口或运行 GPU 训练。
新实验应先通过 Git 同步本地修改；原有 S57–S59 Job 配置可继续使用。

上游/代理仍可能返回超时，连续三次失败仍按原策略终止；本次修复的是第一次暂时性超时即被误判为不可重试的问题。
