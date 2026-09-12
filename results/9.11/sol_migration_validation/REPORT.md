# GPT-5.6 Sol 切换与验证

验证时间：2026-09-11 23:38 PDT（2026-09-12 06:38 UTC）。

## 改动范围

MLEvolve 的默认配置、通用 Job、S57–S59 两臂 Job 均改为
`gpt-5.6-sol/high`。code、feedback、analogy 统一走现有 Responses 接口，
保留结构化流式输出、多轮 function/tool 调用、完整 opaque state 重放、
安全 telemetry 和最多三次暂时性故障重试。没有自动回退到其他模型。

`MLEVOLVE_REQUIRED_MODEL=gpt-5.6-sol` 会在启动时核验三个模型槽位、high
推理和 context v2，防止残留配置覆盖。原 GPT-6 模板及其旧 guard、Terra
等历史模型路由继续保留。新增 `k8s/job-jigsaw-unintended-af-sol.template.yaml`
作为后续种子的模板。

A 仍是 baseline；F 保留 first-draft 和 improve 的 analogy 注入、全文阅读、
context v2 和源码工具。种子、12 小时搜索、90/120 分钟候选预算、14 轮 analogy、
输入/输出预算、candidate runtime、每张 GPU 一个候选、资源申请均未改变。
S57–S59 的 Job 和 EXP_NAME 使用 `gpt56sol`，避免与中断的 GPT-6 结果混在一起。

## 离线验证

使用本地 Python 环境和固定 OpenAI SDK 1.66.3；HTTP 全部模拟。

| 检查脚本 | 通过 | 跳过 |
| --- | ---: | ---: |
| `utils/verify_gpt6_transport.py`（GPT-6、Sol 各跑完整矩阵） | 30 | 0 |
| `utils/verify_gpt6_configuration.py` | 6 | 0 |
| `utils/verify_analogy_observation.py` | 17 | 0 |
| `utils/verify_analogy_handoff.py` | 12 | 0 |
| `utils/verify_execution_pipeline.py` | 19 | 2 |
| 合计 | 84 | 2 |

两个跳过项依赖 Linux CPU affinity，当前 macOS 不支持；此前 executor 修复的
CPU-dev Linux 验证已通过，本次没有修改 executor。传输矩阵验证实际 SDK 的
JSON/SSE、严格结构化输出、多轮 opaque/tool 状态、暂时性错误恢复/三次耗尽、
确定性错误终止；新增检查覆盖 Sol/high 工具调用、旧 Terra 路由和模型 guard。
配置检查对照原 GPT-6 模板确认实验资源、挂载和运行参数保持一致。

日志保存在本目录 `offline_*.log`；更改的代码/配置与实际打包验证版本的 SHA256
记录于 `source_manifest.json`。Python 语法与 `git diff --check` 均通过。

## 实际代理验证

CPU dev pod `mlevolve-agentic-knowledge-base-dev-cpu` 使用原有 Python 3.11.13 /
OpenAI SDK 1.66.3，通过 `http://cliproxy:8317/v1` 运行
`utils/verify_sol_proxy.py`。代码在独立临时目录中；凭据通过 stdin 传入临时进程
环境，沿用实验 Secret，没有写入验证文件或修改 Secret。

| 检查 | 结果 | 耗时 |
| --- | --- | ---: |
| `llm.generate` 文本流 | pass | 8.242 s |
| `llm.generate` 结构化 JSON 流 | pass | 2.055 s |
| `llm.query` feedback function | pass | 2.416 s |
| 两轮工具调用 + 最终答案（三次请求） | pass | 8.051 s |

共六次短请求，均显式指定 Sol/high，无 fallback。三次 wrapper 调用的返回
telemetry 均为 `model=gpt-5.6-sol`、`returned_reasoning_effort=high`、
`status=completed`。多轮测试验证第二轮消费第一轮的工具结果、call_id 匹配、
最终答案消费验证后的结果；期间重放一个 encrypted reasoning item。
探针不保存该 encrypted 内容。结果见 `live_summary.json`、`live_probe.log`
和 `live_llm_calls.jsonl`。

首次探针因 dev-cpu 环境没有 API key 在请求前退出；随后使用现有实验 Secret
完成上述验证。这是配置缺失，不是 Sol/API 拒绝。

短请求只能证明当前代理和固定 SDK 的功能兼容，未验证六个长期实验的并发额度、
完整候选生成质量或分数改善。模型切换不能保证消除代理级限流。

## 启动方式

先通过 Git 同步 MLEvolve 的本次代码和 Job。若仍有实验使用共享 checkout，
先停止它们再同步，或为新实验使用独立固定 checkout 并修改入口和 REPO_DIR。
然后手动 apply：

```bash
kubectl --context nautilus -n ecepxie apply -f k8s/job-jigsaw-unintended-af-s57.yaml
kubectl --context nautilus -n ecepxie apply -f k8s/job-jigsaw-unintended-af-s58.yaml
kubectl --context nautilus -n ecepxie apply -f k8s/job-jigsaw-unintended-af-s59.yaml
```

上述命令从 MLEvolve 仓库目录执行，每个文件包含 A/F 两个 Job。新名称形如
`mlevolve-jubias-base-gpt56sol-s57`、`mlevolve-jubias-anaf-gpt56sol-s57`。
它们不会自动停止旧 GPT-6 Job。本次没有 commit/push、更新集群共享代码/venv、
apply Job 或重启实验；临时探针目录已随进程结束清理。

官方模型能力说明：[GPT-5.6 Sol](https://developers.openai.com/api/docs/models/gpt-5.6-sol)。
