# S57–S59 GPT-6 在线错误诊断

检查时间：2026-09-11 21:40–21:50 PDT（2026-09-12 04:40–04:50 UTC）。
范围：六个 Jigsaw A/F Job 的 Pod 状态、日志、代理访问日志、候选执行记录和结果 manifest，以及对应源代码。集群 MLEvolve commit：`aaaef15d05240b24263d747fdd96b27611c0f4ed`，与本地 HEAD 一致。

本次仅进行只读诊断与本地证据保存，没有修改运行代码、更新集群源码、重启或删除 Pod。

## 当前状态

| 实验 | Pod | 状态 | 已保存的最好公开验证分数 |
|---|---|---|---|
| A57 | mlevolve-jubias-base-gpt6-s57-t79mc | Running | 0.9075574054 |
| F57 | mlevolve-jubias-anaf-gpt6-s57-7pnld | Failed，exit 1 | 无结果快照 |
| A58 | mlevolve-jubias-base-gpt6-s58-hn6pv | Failed，exit 1 | 无结果快照 |
| F58 | mlevolve-jubias-anaf-gpt6-s58-lhg4v | Running | 0.9018314916 |
| A59 | mlevolve-jubias-base-gpt6-s59-6tx8v | Failed，exit 1 | 无结果快照 |
| F59 | mlevolve-jubias-anaf-gpt6-s59-gbthq | Running | 0.9297157103 |

分数取自已发布快照的 `manifest.json`，对应候选的 `review.json` 均为 passed；这是公开验证分数，不是最终隐藏测试成绩。本次没有重新计算成绩或哈希校验大型模型文件。三个失败 Pod 均 restartCount=0、退出原因 Error，状态中没有 OOMKilled 或 Evicted；本次事件查询为空。

## 三个 Job 退出的共同主因：流式超时被误判为不可重试错误

三个失败日志均出现：

```text
llm.responses.ResponsesError: Responses SSE error (request_timeout)
```

| 实验 | 失败调用所在阶段 | 调用耗时 | 实际尝试次数 | Pod 退出时间 UTC |
|---|---|---:|---:|---|
| F57 | 第三个初始 draft，Step 2 / model design | 32.688 秒 | 1 | 03:49:26 |
| A58 | 第三个初始 draft，最终代码合并 | 38.388 秒 | 1 | 03:47:53 |
| A59 | 第三个初始 draft，Step 1 / data processing | 108.669 秒 | 1 | 03:42:31 |

原因链：

1. `MLEvolve/llm/responses.py:24` 的 `_TRANSIENT_CODES` 包含 `timeout`，遗漏了代理实际返回的 `request_timeout`。
2. `_read_stream()` 第 159–163 行因此抛出终止型 `ResponsesError(category="response_error")`，没有进入暂时性错误重试路径。
3. `request_response()` 第 228–230 行直接向外抛出；落盘 telemetry 明确记录 `attempts=1`。
4. `ResponsesError.transport_retry_exhausted=True` 触发 `engine/pipeline.py:68–72` 的终止逻辑，随后第 106–112 行停止正在执行的候选并取消队列。

这属于此次 GPT-6 适配代码的错误分类遗漏。离线使用实际 SDK 的模拟 SSE 复现：`request_timeout` 只发起一次请求即退出；相同情境换为已识别的 `timeout`，会进行三次有界尝试，最终报告 transient_exhausted。复现没有发送真实模型请求。

三个实验退出前，首个候选分别只执行约 840 秒（F57）、1102 秒（A58）、785 秒（A59），第二个候选还在排队。检查实际 snapshots 目录后，三个失败实验均未发布结果快照。

### 代理证据与边界

代理日志中同 Pod IP、同时间的最后一次请求耗时与模型调用记录吻合，HTTP 状态均为 200。流式连接建立后仍然可能通过 SSE 返回错误，因此访问日志的 HTTP 200 不代表整次生成成功。

代理最近三小时的有限日志中没有记录该 SSE 错误的内部原因，不能据此断定超时源于上游服务还是代理内部。三个耗时不同，也不支持“统一 30 秒客户端超时”的解释。当前证据明确证明的是应用收到 `request_timeout` 后错误地立即终止，而不是模型名称或请求格式被拒绝。

### 日志末尾的评分错误是后果

```text
ValueError: No eligible complete runtime snapshot; refusing stale legacy output
```

搜索退出后脚本仍进入融合/评分准备步骤；因没有可用快照，结果选择器拒绝使用旧的 legacy 输出。这不是导致三个 Job 退出的第一处错误，也不应通过放开旧结果回退来消除。

## 存活实验中的候选级错误

这些错误与上述整场 Job 退出不同，搜索仍在运行并尝试 debug。

### F59：执行器破坏了合法的 future import

候选 `18e399263a454872af69e66dead32791` 的不可变原始源码第一行是合法的 `from __future__ import annotations`。`engine/executor.py:244` 生成两行 CPU affinity 代码，第 257 行将它们拼到候选源码前，导致原始 future import 移到第三行：

```text
SyntaxError: from __future__ imports must occur at the beginning of the file
```

离线 compile-only 复现：原始模块可编译，加入相同前缀后出现完全相同的第三行语法错误。这是执行器代码注入问题，不能仅归因于模型生成了非法代码。Git 历史确认该前缀逻辑至少在 2026-02-14 已存在，不是此次 GPT-6 适配新引入的。修复应让 CPU 绑定发生在独立启动器中，或正确保留模块 docstring / future import 的位置。

### F59：生成代码用错预算计时起点

improve 候选 `3b53cebda8444b078a48ea92c441ea54` 被实际授予 7200 秒，但源码第 715–719 行采用整个实验的 `run.json.started_at` 计算自己的截止时间：

```text
run_started + candidate_budget_seconds - finalization_reserve_seconds
```

实验开始时间为 1789180589.0446，候选开始时间为 1789186751.3220，错误截止时间为 1789186889.0446，因此只剩 137.72 秒；实际在约 140.24 秒时报 `Admitted preparation/training budget exhausted`。执行器的真正截止时间为 1789193951.3220，确实授予了两小时。

这是生成代码的时间起点错误。应使用 runtime session 的 `remaining()`，避免从整个 run 的开始时间推算候选预算。现有提示已经将 remaining() 标为权威来源，可进一步明确禁止混用 run / candidate 的计时起点。日志把这类主动 TimeoutError 描述为“两小时执行超时”也容易误导。

### 其他候选代码错误

- F59：`optimizer.param_groups()` 把列表当函数调用；debug 后至少又出现一次相同错误。
- F58：一个 draft 在 token 特征处理阶段报 `Invalid encoded sequence length`。
- F58：另一个 draft 已发布并通过审查的结果快照，之后仍检查旧式 submission 路径，报 FileNotFoundError。其 execution_status 是 failed，但 artifact_status 为 scoreable，公开验证分数 0.9018314916 被保留。

F58 的后一例说明“执行状态”和“已保存结果是否可评分”分离已经发挥作用。A57 也在候选预算结束时保留了两份结果快照，最好分数 0.9075574054；F59 完成的 draft 保留了两份快照，最好分数 0.9297157103。

## 建议修复顺序（本次未实施）

1. 补全 `request_timeout` 暂时性错误分类，覆盖流式和其他实际可能采用的错误封装；验证“超时后成功”和“持续超时恰好三次后退出”。保留有限重试和对确定性配置错误的终止机制。
2. 修复执行器的 future import 前缀问题，验证普通模块及包含 docstring / future import 的模块。
3. 加强候选预算 API 使用约束与主动超时日志区分，避免生成代码从 run 开始时间重新计算候选截止时间。
4. 修复后重跑 F57、A58、A59。A57、F58、F59 当前仍在运行且已有保存结果，但同样使用存在超时分类遗漏的代码；不要认为一次 compatibility smoke pass 能覆盖长时间流式运行稳定性。

## 本目录证据

- 六个 Pod 的 `.log` 和 `.events.json`。
- `pod_status.json`：首次状态；`pod_status_refresh.json`：04:50 UTC 状态。
- `runtime_summary.json`：候选执行、审查、真实 manifest、事件及有限模型调用元数据。
- `mlevolve-gpt6-proxy-timeout-access.log` / `mlevolve-gpt6-proxy-timeout-summary.json`：与三个失败请求对应的有限代理访问记录。

- `mlevolve-gpt6-secondary-errors.json`：两个 F59 候选的源码关键行、时间计算、编译复现及历史核查证据。
