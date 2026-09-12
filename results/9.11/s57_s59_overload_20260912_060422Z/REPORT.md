# 重启后 A58 的 server_is_overloaded 诊断与修复

检查时间：2026-09-11 23:03–23:07 PDT（UTC 2026-09-12 06:03–06:07）。

失败 Pod：`mlevolve-jubias-base-gpt6-s58-pxmfd`，创建于 05:36:36 UTC，
06:01:22 UTC 以 exit 1 / Error 退出，restartCount=0。
其余五个新 S57–S59 A/F Pod 检查时均为 Running；最近日志仍在初始化阶段，
没有看到同类退出。这不代表已经验证了它们后续训练的健康状态。

## 已确认原因

```text
llm.responses.ResponsesError: Responses SSE error (server_is_overloaded)
```

错误出现在第二个初始 draft 的第一步生成，模型调用 3.155 秒后失败，
telemetry 记录 category=response_error、attempts=1。共享仓库 HEAD 为
`76a1eae8a29b8725f1da97fb46167b3ab51109de`，responses.py 与 executor.py
哈希均与本地该提交一致。此次是已经同步了上次修复后出现的新过载别名，
不是未同步代码。

原暂时性错误集合包含 overloaded 和上次新增的 request_timeout，但未包含
代理本次返回的 server_is_overloaded。因此调用再次绕过重试，向 pipeline
传播终止错误；首个已排队执行的候选 `2481469999e04bc8b78699b42cf2e2c7`
也被清理，实际只运行约 4.06 秒，无结果快照。
后续 `No eligible complete runtime snapshot` 仍然是没有结果后的派生错误。

过载错误由模型调用通道返回；本次没有证据进一步定位过载是在代理内部还是上游服务。

## 本地修复与验证

- 在 llm/responses.py 的共享暂时性错误集合中加入实际观测的 server_is_overloaded。
- 保留最多三次请求、丢弃失败流部分输出、原请求完整重发，以及确定性错误的终止策略。
- 验证矩阵同时覆盖 request_timeout 和 server_is_overloaded，分别经过 JSON、
  SSE error、嵌套 SSE SDK error、response.failed、flat/nested APIError 六种表示。
- 修复前，12 个 overload 恢复/耗尽子案例都因只尝试一次而失败；修复后完整
  15 项 transport 测试通过，未知错误仍仅尝试一次。使用实际固定 SDK 1.66.3，
  所有 HTTP 均为本地 MockTransport，没有模型请求。git diff --check 通过。

本次只修改本地 MLEvolve 的 responses.py 和 verify_gpt6_transport.py，并补充
AKB 的现有重大 UPDATELOG 条目。没有提交推送、修改集群代码、apply 或重启任何 Pod。
运行中的其余五个 Pod 尚未加载此补丁，同样存在该错误别名触发终止的风险；
后续同步与重启应避免在运行中直接覆盖共享 checkout。

本目录的 A58.log、五个其他 Pod 的最近日志、runtime.json 保留诊断证据，
transport_before.log 和 transport_after.log 保留修复前后的模拟回归结果。
