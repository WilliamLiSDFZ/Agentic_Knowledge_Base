# Sol S57 A 臂退出：代码审查 schema 与 null 约定冲突

检查时间：2026-09-12 00:51–00:55 PDT。仅诊断，未修改应用代码或集群。

## 结论

失败的是 `mlevolve-jubias-base-gpt56sol-s57-dqs79`，00:34:49 PDT 以
exit 1 / Error 退出，restartCount=0。第一个 draft 的三步生成和合并均完成，
随后代码审查返回 `revised_code=null`，被本地 JSON Schema 校验拒绝：

```text
jsonschema.exceptions.ValidationError: None is not of type 'string'
Failed validating 'type' in schema['properties']['revised_code']
llm.responses.ResponsesError: Invalid structured function arguments
```

`agents/code_review_agent.py:37` 将 revised_code 定义为 string，但同一字段的
说明明确要求 `needs_revision=false` 时返回 null，审查 prompt 也允许 null/省略。
返回完整参数没有落盘，因此不能从现有日志断言这次 needs_revision 的具体值；
可以确定触发拒绝的字段值就是 null，以及代码自身存在上述约定矛盾。

Responses 路径在 `llm/openai.py:153` 对真实函数参数执行本地校验，然后将
ValidationError 包装成 `ResponsesError(category=invalid_output)`。
该异常类统一带有 `transport_retry_exhausted=True`，代码审查和初始 draft
pipeline 因此跳过各自原有处理，直接终止整个 run。此次只调用了一次审查接口，
不是真正发生了三次网络重试耗尽。

六次调用返回的模型均为 gpt-5.6-sol/high，响应状态均为 completed；前五次
outcome=success，最后一次审查在本地校验后记录 outcome=error、invalid_output。
失败请求未出现限流、过载或超时错误。Pod 事件只有正常调度、挂载和容器启动，
退出状态不是 OOMKilled 或 Evicted。

## 影响

失败 run 为 `/workspace/MLEvolve/runs/20260912_070902_jubias-base-gpt56sol-s57`。
首个候选尚未通过审查并入执行队列，candidate_results 的 candidates 和 selected
均为空。最后的 `No eligible complete runtime snapshot` 是没有训练结果后的
派生错误，不是此次根因。没有可恢复的已评分候选。

共享仓库 HEAD 为 `3c79330526f338d11e2210e7da672bd1b24e816f`；代码审查、
openai wrapper、responses transport 三个文件的 SHA256 与本地完全一致。
preflight 也确认所有槽位均为 Sol/high。此次不是漏同步代码。

另外五个 Pod 在检查时仍为 Running，没有看到同类退出。其最近日志中，A58/A59
在第一个 draft 的生成阶段，F57/F58/F59 最后可见的是 corpus 初始化；这不足以
证明后者整体进展健康，也不能据此断言卡住。所有臂共享代码审查，因此同类
null 响应都可能触发相同错误。

## 同类问题与建议修复

检查结果解析函数时发现第二处矛盾：`agents/result_parse_agent.py:135` 的
metric 类型为 number，描述和 prompt 却要求候选失败时返回 null。这是静态检查
并在本地重现的后续风险，尚不是本次 A57 实际触发的错误。

建议一并处理：

1. 将 revised_code 的 schema 调整为 string/null，保留需要修订但没有代码时的
   业务处理；metric 调整为 number/null，保留执行失败和指标方向判定。
2. 使用真实 CODE_REVIEW_SPEC 和结果解析 spec 回归验证：批准/null、修订/diff、
   执行失败/null、成功/数字，以及错误类型仍被拒绝。覆盖 Sol 和 GPT-6 路径。
3. 单独评估 invalid_output 与传输终止错误的分类，避免将业务格式问题误称为
   传输重试耗尽；不要为掩盖 schema 矛盾而关闭所有结构化校验或无限重试。

`schema_reproduction.json` 记录了两处原始 schema 均拒绝预期 null 的最小复现。
仅在内存副本中允许 null 后，相应案例通过，revised_code 数字仍被拒绝。
本次没有将该修改写回应用文件。

上一轮 Sol 兼容性探针覆盖了文本、结构化输出、合成 feedback function 和多轮
工具，但未覆盖真实 CODE_REVIEW_SPEC 的 null 分支；离线矩阵也漏了该业务契约。
因此接口兼容性通过并未发现这处现有 schema 与新校验路径之间的冲突。

建议修复上述公共契约后再启动新实验；单独原样重跑 A57 仍可能复发。此次仅保存
诊断证据，没有修改代码、UPDATELOG、共享环境，或停止/重启任何 Pod。

## 证据文件

- `a57.error_excerpt.log`：原始异常、传播链与后续融合错误。
- `a57.calls_and_results.json`：六次调用的安全元数据和空候选列表。
- `a57.runtime.json`：共享提交、文件哈希和模型 preflight。
- `a57.events.json`、`pod_status.txt`：事件和六个 Pod 状态。
- `other_pod_log_tails.json`：其他五个 Pod 最近可见进展。
- `schema_reproduction.json`：无模型调用、无代码修改的复现结果。
