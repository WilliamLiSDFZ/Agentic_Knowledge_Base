# Context v2 与 GPT-6 实施验证

日期：2026-09-11（集群验证为 UTC 2026-09-12）。获批方案：
`docs/analogy_context_and_gpt6_plan.md`。本轮完成代码、文档和重大 UPDATELOG；
没有提交实验 Job、覆盖共享 checkout/venv 或执行训练。

## 结论

修正后的三个历史候选回放均生成了通过源码／论文证据校验、且符合 12,000 字符
预算的报告。请求与返回模型均为 `gpt-6-astra`，reasoning effort 为 `high`。
源码查询、运行事实、全文阅读和 Responses 多轮调用已连通；机制交接、旧调用
路径及执行／结果保存回归也已通过。**这证明接口和信息流可用，不证明新实验收益。**

## 离线检查

10 组共 **140 项测试通过**，另有旧 analogy injection 全部断言和 20 份历史
improve packet 检查通过。具体脚本与数量见 `offline_checks.json`。

- 固定 `openai==1.66.3`：JSON/SSE、工具 call ID、完整 opaque response items、
  结构化返回、相同模型名的角色选择、错误分类及有限重试。
- Context/source：预算、plan 去重、原始日志清理、源码 SHA256、白名单、分页、
  diff、证据范围、runtime-off 与旧配置兼容。
- Public diagnostics：分项组合与原分数一致，ID/hash 校验，同 contract 比较。
- Handoff：真实 v2 注入入口、两种 planner、选中／拒绝／unknown、完整约束进入
  coder、diff 重试和执行后来源记录。
- 原有 candidate runtime 38 项、execution pipeline 16 项、best solution 4 项
  通过；pipeline 新增终止 transport 错误时停止重排并清理执行进程的回归。

20 份历史输入均保留当前修改内容、选中快照和训练步数。验证时仅将 journal 源码
恢复到临时 fixture，并要求其 SHA256 与注册记录一致；生产源码工具不提供这种
恢复兜底。真实回放直接读取集群原有不可变 `solution.py`。详情见
`historical_packets.json`。离线环境为本地 Python 3.14 和隔离 `/tmp` 依赖；
实际集群调用使用原有 Python 3.11.13 / OpenAI SDK 1.66.3，没有升级共享依赖。

## 真实调用与三节点回放

先验证了实际 MLEvolve 包装层的 feedback function query、planner structured
stream 和 code text stream，三项均通过，见 `live/wrapper_checks.json`。
后续回放使用 CPU dev pod 下的独立临时源码目录，复制日志配置／journal 后，
只读原运行 workspace。新诊断缓存写入临时日志目录。全文只读既有已校验缓存；
cache miss 如实返回，不下载新论文，也不读取私有分数来指导建议。

| 候选 | 模型轮数 | 源码工具调用 | 报告字符 | 循环耗时 | 最大单次实际输入 |
|---|---:|---:|---:|---:|---:|
| F54 / `27273be3` | 9 | 5 | 11,038 | 184 秒 | 41,575 tokens |
| F55 / `994b5cf6` | 10 | 4 | 7,733 | 186 秒 | 49,499 tokens |
| F56 / `c87f0ec8` | 9 | 4 | 10,456 | 176 秒 | 53,806 tokens |

这些字符数为最终可见报告去首尾空白后的长度。含上下文构建和 corpus 加载的
进程总时长约 190–206 秒。各 episode 累计计费输入约 26.1万、32.5万、27.9万
tokens；这是多轮重复输入的合计，不能与单次 196,608 输入预算混为一谈。
三份报告分别有 931、779、966 reasoning tokens，多轮请求能继续处理真实返回
状态。原始明文／工具 trace、用量、源码 ledger 和全文 manifest 均保存在
`live_corrected/`；没有保存 opaque reasoning 内容。

F54、F56 的最终机制引用了实际读到的全文。F55 也读取了两篇全文，但最终选择的
GRPO 类机制仅有摘要支持，报告明确标注 `abstract_only`。开启全文工具不等于
每条最终建议都具备全文证据；这应作为后续分析的一项区分。

## 真实回放发现并修复的问题

保留首轮失败证据于 `live/`。首轮三个 episode 都完成了源码与全文工具调用，
但没有生成可注入报告：F55/F56 报告过长，F54 的一个代码引用抄错了节点 ID。
原计数器随后把仅 3.9–4.4 万实际输入 tokens 的会话按完整 UTF-8 字节重新估算，
在模型重交前误判预算耗尽，尽管完整模型上下文仍有余量。

修复后，已测量且未改变的消息前缀使用 API 实际输入加 20% 余量，仅新增 items
按字节保守估算；前缀／工具改变或无 usage 时保留原兜底。完整 opaque items
继续回传。提示明确最终渲染预算，拒绝时给出具体引用位置和报告长度反馈。
没有放宽 196,608／12,000 上限。新增回归模拟超 20 万字节历史、5 万实际输入，
验证报告超限后仍能合法重交；修正后的三次真实回放均首次提交即获接纳。

## 信息质量与仍需实验回答的问题

- F56 明确识别“当前已有 BCE＋ranking”，核对出源码只有 9 个 identity，纠正
  plan 中的 10 个；不再重复建议添加已经存在的 ranking loss。
- F55 识别队列已是 256、比较预算 64、warm-up 32 步，转而讨论组损失权重等
  后续问题。其最终机制仅有摘要支持，迁移假设仍需验证。
- 三份均指出父子选中 checkpoint 的训练步数不同，不能将分数差异直接归因于
  loss；对少数群体样本支持、缓存漂移和未来执行预算明确保留未知项。
- F56 放弃了依赖凸风险／周期性全梯度的另一条建议，说明代码与论文前提检查
  可以产生实际筛选。F54/F56 的缓存或采样修复仍可能增加计算、改变分布或带来
  score staleness；报告通过证据校验并不证明这些机制有效。

下一步用新 GPT-6 A/F 模板做独立实验，保持两臂模型、候选预算与基础设施一致。
新旧模型批次分开解释。每个 child 的 `analogy_adoption`、完整 diff 和最后 journal
可用于区分“检索到了”“planner 选中了”“代码实际改变了”和最终实验结果。

可重建摘要：`python results/9.11/gpt6_context_v2_validation/summarize.py`。
实现、配置和新 Job 的使用方法见 `MLEvolve/docs/analogy_context_v2.md`。
