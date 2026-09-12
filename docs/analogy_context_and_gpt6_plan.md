# Analogy 上下文增强、源码查询与 GPT-6 实验迁移方案

状态：**用户已审批，已实施并完成离线与真实回放验证**。日期：2026-09-11。

本文件落实四项请求：适当延长现有信息的截断长度；允许 analogy agent 查询当前实现代码；补充实现与运行事实；后续实验统一使用 GPT-6。以下保留获批方案的设计依据与范围。当前实现说明见 [MLEvolve 使用说明](../../MLEvolve/docs/analogy_context_v2.md)，验证记录见 [验证报告](../results/9.11/gpt6_context_v2_validation/REPORT.md)；UPDATELOG 已记录此次重大更新。

## 1. 拟批准的改动范围

建议在现有多轮工具循环中增加候选观察能力，让 analogy 先确认当前实现和运行事实，再检索论文、提出干预。保持现有搜索 node 类型及评分定义。

本轮包括：

1. 将截断预算配置化并提高，修复先裁剪再清理、JSON plan 重复内容、执行事实在尾部被截掉的问题。
2. 增加三个只读源码工具：索引、分段阅读、父子 diff。
3. 增加当前实现索引、快照身份、训练程度、验证轨迹、运行成本、实际预算和已有公开预测可派生的诊断。
4. 保留“源论文机制—选中干预—代码落点—验证条件”的结构化交接，传给 planner 和 coder。
5. 后续实验的 code、feedback、analogy 等生成式模型调用统一为 `gpt-6-astra`，补齐 Responses API 适配和兼容性验证。
6. 增加可复查的上下文与模型调用记录，完成针对性测试及历史节点回放。

GPU 队列调度、候选截止准入、loss 自动梯度检查框架、训练 loss/显存连续采集、任意 web search 和历史分析图修复列为后续工作。它们不作为本次方案的隐含附加改动。

## 2. 现状与需要修复的问题

当前 improve 路径为 `improve_agent._inject_analogy → retrieve_for_node → packet_from_search → run_analogy_agent`。每次调用最多 10 轮模型响应，同轮可提出多个工具调用。本批 20 次 improve 实际用了 4–7 轮，均值 5.1；这是可继续观察工具结果的多轮循环。

当前候选信息只在开头提供一次，工具只支持查论文、读摘要/全文及提交报告。缺失的候选代码和诊断无法在循环中补查。

S54–S56 的实际输入暴露了以下问题：

- 20/20 的 `code_summary` 都是“阶段；budget_exhausted；分数”，没有方法内容。runtime 的结果解析路径直接写入该状态字符串。
- 10/20 的 plan 被 1,500 字符上限截断。JSON 通常先放描述父节点问题的 `reason`，真正修改内容位于后面的 `plan`，容易被丢掉。
- `node.term_out` 已先被全局裁剪，analogy 随后才清理 warning 并再次截断，无法找回先前丢失的信息。
- runtime 附在 analysis 末尾的快照身份、所选训练步数和导出时间，20次均未作为完整说明进入 packet。
- improve 没有专门资源段；draft 的资源段又读取旧 `cfg.exec.timeout=6h`，没有使用实际阶段预算。
- planner 可见 analogy 报告，但默认 diff coder 主要收到压缩后的修改计划，论文假设和拒绝条件没有独立保留。

源码依据：[packet 构造](/Users/william/Documents/project/python/MLEvolve/engine/analogy/agent.py:116)、[runtime 结果解析](/Users/william/Documents/project/python/MLEvolve/engine/candidate_runtime/integration.py:179)、[improve 到 coder 的调用](/Users/william/Documents/project/python/MLEvolve/agents/improve_agent.py:349)。实验依据：[上一轮审计](/Users/william/Documents/project/python/Agentic_Knowledge_Base/results/9.11/s54_s56_review/REPORT.md)。

## 3. 上下文预算与裁剪规则

所有数值均是**字符数，不是 token 数**。实际输入、输出及可取得的 reasoning token 用量另行记录。建议新增 `analogy.context` 配置，不再仅依赖模块常量。

| 内容 | 当前 | 拟采用 |
|---|---:|---:|
| 任务描述 | 头4,500＋尾1,500 | 头8,000＋尾3,000；优先保留完整 Evaluation/目标定义 |
| 数据预览 | 2,000 | 6,000 |
| 当前 plan | 1,500 | 12,000；先结构化整理、去重复 |
| 当前实现概览 | 1,500，但实际上只有状态 | 6,000，提供源码索引和可确认实现信息 |
| 执行摘要 | 1,500 | 5,000；结构化状态与文本说明分开 |
| 运行输出 | 二次裁剪后的尾1,500 | 原始已捕获输出清理后，头2,000＋尾6,000 |
| 当前节点的已尝试修改 | 总计2,500 | 总计10,000；先逐条压缩，再选择展示 |
| 分支轨迹 | 最近6个，每条plan约200 | 最近10个，每条约600；附节点ID及关系 |
| 快照、成本与诊断 | 无独立段落 | 合计约12,000 |
| 初始packet总上限 | 分散控制 | 80,000 |
| 最终注入报告 | 8,000 | 12,000；最多3条机制，保留完整机制块 |
| 每次analogy模型响应上限 | 10轮 | 14轮，为代码查询和报告修正留余量 |

提高上限并不要求模型填满。增加约束如下：

- plan 是**设计意图**，不能据此声称代码已经实现。解析 `reason/module/plan`，移除嵌套 `raw_response` 的重复副本，分别呈现“当时修改理由”和“计划修改内容”。
- 执行状态、所选快照、步数、分数和预算直接由记录生成字段，永远不依赖它们在日志首尾是否碰巧出现。
- 日志从已捕获的原始 `_term_out` 清理一次，不再调用已裁剪的 `term_out` 属性再裁第二次。仍可输出清理计数及原始日志引用。
- warning 清理按已知整块模式处理，避免删掉异常堆栈或有用的后续输出；tokenizers 多行提示应单独识别。
- 分支轨迹写明是同分支近期记录，并提供 parent ID；不再让时间顺序看起来像严格父子链。
- 每段记录原始长度、返回长度、是否裁剪及遗漏内容类别。总体超限时先删重复说明和低相关历史，再裁普通日志；保留当前事实、评分契约、预算和源码索引。
- 原始数据长到单次上下文放不下时，通过工具分页读取，不能静默扩大到超过实际端点支持的上下文。

论文全文预算暂保留现值：3篇、12次read、每次8,000字符、合计40,000字符。代码读取使用独立预算，互不挤占。

另设会话累计输入预算，建议 `max_input_tokens=196608`；实际可用上限还需取端点上下文限制减去16,384输出预留及8,192余量后的较小值。每轮计入完整会话中的消息、工具定义、工具返回及需续传的response items，不能只统计新packet。优先使用可用的计数能力和实际usage，缺少精确计数时用保守估计并标注。

接近总预算时停止继续检索/读代码，预留一轮提交精简报告；保留有效的工具调用对应关系和必须续传的响应状态，不随意裁掉reasoning items。单次工具输出应在返回前受剩余预算约束。若仍不足以完成合法报告，保存trace并明确记录预算耗尽。分页解决单次响应大小，不解决会话无限累积。

## 4. 候选源码查询工具

### 4.1 工具接口

| 工具 | 输入要点 | 返回内容 |
|---|---|---|
| `candidate_code_index` | `node_id`，默认本次正在分析的父候选 | imports、类/函数qualified name、签名与行范围、顶层语句区间、可直接读取的配置常量、可识别的runtime callback绑定 |
| `read_candidate_code` | `node_id`；`symbol`或行区间二选一；可续读 | 带原始行号的源码，适合查看loss、采样、可训练参数、训练循环和预测函数 |
| `diff_candidate_code` | 基准节点与目标节点，默认“当前被分析候选相对其直接父节点”；可限定symbol | 实际源码diff、改动函数索引、两端源码哈希与行号，不自动推断因果效果 |

这里的“当前候选”是传入 analogy 的已执行父节点，不是尚未生成的下一个 improve 节点。

建议每次episode代码工具总计最多10次调用、累计120,000返回字符；单次read默认200行，上限400行或20,000字符，以先达到者为准；diff单次也不超过20,000字符。索引及元数据计入累计预算。

返回完整行和明确续读位置；长函数、长diff分段返回。单个超长行另提供字符偏移，不伪装成完整行。参数错误、无匹配symbol、预算用尽均返回可读的结构化状态，让模型能够调整下一步。

### 4.2 来源与访问范围

- 一次episode建立固定节点白名单：当前被分析候选、直接父节点、packet列出的已结束同分支候选。只有存在源码的节点可查；虚拟root返回无源码。
- 工具接收节点ID和symbol/行号，**不接收任意文件路径**。
- runtime开启时读取已注册候选目录的不可变 `solution.py`，核验 `candidate.json.source_sha256`，小文件读取一次后在episode内缓存。
- runtime关闭时，在episode开始时冻结对应 `SearchNode.code` 的字符串副本并计算hash，标记 `origin=search_node_snapshot`。
- runtime开启但不可变源码缺失或hash不符时报告问题，不悄悄改读可变 `runfile_0.py`。
- AST仅用于解析索引，不执行、import或求值候选代码。AST失败时仍可按行阅读，并标记索引不可用。
- 响应附带 run ID、node ID、stage、source SHA256、来源、行范围、是否裁剪和剩余预算。代码和注释属于分析材料，不作为agent指令执行。

工具权限无需覆盖模型权重、私有测试标签、其他run或shell。代码工具在improve/evolution等有明确候选对象的调用中才有意义；本轮先接入improve。draft尚无候选，继续使用任务与资源信息。

## 5. 提供更多实现细节与诊断

### 5.1 当前实现概览

增加独立的 `implementation_context`，不再把运行状态行作为方法摘要。内容由三类来源组成：

1. **确定的结构信息**：源码hash、类/函数/行号、可安全读取的字面量常量、实际callback绑定、与父候选发生改动的区间。
2. **设计声明**：从plan整理出的模型、loss、采样等声明，明确标注为意图、尚需源码核对。
3. **本次代码核查结论**：analogy通过源码工具确认后，记录实际backbone、loss组成与权重、采样、冻结/解冻、batch与梯度累积、预测及checkpoint方式，并引用所读代码行。

复杂表达式、动态配置、运行中才决定的状态不能由AST猜测。无法确定就写unknown。第一版不额外增加一个必经的“LLM代码总结agent”；使用确定性索引和现有analogy循环完成核查，减少重复模型调用。

旧 `code_summary` 字段保持兼容；context v2不再把runtime生成的状态行当作方法信息。若保留旧摘要作补充，标明其来源。模型对源码的解释与runtime测得的事实分开存放。

### 5.2 直接接入现有记录

| 信息 | 数据来源 | 主要作用 |
|---|---|---|
| 分数属于哪个模型 | snapshot/checkpoint ID、source hash、contract ID、metric version | 防止把不同代码或checkpoint的结果混用 |
| 训练程度 | 所选checkpoint步数、worker最终总步数 | 区分5步试运行、最佳checkpoint和训练结束位置 |
| 验证轨迹 | events中每次validation的step、metric、耗时 | 判断持续改善、回落或只有一次验证；不称其为训练loss曲线 |
| 结束与产物状态 | execution status、异常类型、artifact状态 | 区分主动收尾、硬超时、代码错误和有无可用结果 |
| 已知成本 | training_started前耗时、smoke校准、完整validation/export耗时 | 判断提议的模型或方法能否在预算内执行 |
| 同类失败 | 可取得的异常摘要、已有修复结果 | 避免重复选择已确认不可用的编译或checkpoint路径 |

通过小JSON与事件文件读取，不扫描或校验大权重文件。日志缺失、尾部中断、journal落后时按来源标记缺失，不能补造状态。

诊断以当前节点已经通过runtime校验的 `best_snapshot_id` 为准，沿用其review/失效状态，再检查小型manifest、预测文件hash与ID。不得为了生成context重新调用会遍历并hash权重的 `ResultStore.collect()/verify()`；找不到已确认有效的快照时标记诊断不可用，不自行绕过验证选一份结果。

### 5.3 从公开验证预测派生诊断

本轮纳入Jigsaw的低成本CPU诊断：使用所选snapshot的公开验证预测，与同contract验证标签按ID对应，计算overall AUC、9个identity的subgroup/BPSN/BNSP AUC、每项正负样本数，以及相对父候选的变化。

当前score实现已经计算这些分项，只未持久化。可抽出共享内部计算并保存诊断，保持现有 `score()` 的标量返回和数学定义不变。诊断缓存按预测hash、contract ID和诊断版本建立；已有预测足够，不重新推理或训练。

默认packet展示总分构成、最弱/退化最大的若干分项及样本支持。一个低分群体只是观测，不能直接等同“必须重加权”。样本过少、对照contract不一致或预测缺失时标记不可比较。

本轮不自动抽取大量文本错误样本，也不计算所有checkpoint的诊断：未保留预测的验证点只提供总分轨迹。私有测试分数只属于离线复盘，不进入运行中的检索、规划或选模反馈。

### 5.4 资源与可行性上下文

向draft和improve提供统一资源字段：

- 信息采样时间、当前run真实剩余时间、阶段配置上限、当前活跃/排队候选数。
- 父候选测得的预处理、验证、导出成本，以及估计是否经过校准。
- 当前进程可确认的GPU型号/显存、CPU额度和编译器能力；未来候选GPU尚未分配时说明可见设备与不确定性，不承诺具体卡。
- 可用离线模型索引或受限摘要；缺失就标记未知。

真实run deadline来自executor及外部时限，而非单独用 `run_start + config` 猜测。候选真正出队后才确定实际deadline，因此配置上限120分钟不等于承诺能执行120分钟。此次提供信息和不确定性；截止准入调度的行为改动另列后续方案。

### 5.5 对其他任务的支持

通用context构建负责源码、关系、预算、状态、验证轨迹及可用产物。Jigsaw通过可选诊断provider提供分项，其余任务返回“不支持该任务分项”，仍可使用源码工具与通用上下文。

当前candidate runtime本身仍只支持Jigsaw，不能因增加通用context就声称它已支持其他任务。runtime关闭的任务采用冻结的SearchNode源码与现有日志；未来再逐项增加任务诊断provider。

## 6. 多轮工作流与下游交接

建议调整为：

```mermaid
flowchart LR
    A[父候选与已保存运行事实] --> B[扩大后的初始上下文]
    B --> C[检查源码与父子差异]
    C --> D[形成事实与待验证假设]
    D --> E[检索摘要与论文全文]
    E --> F[提交机制与验证方案]
    F --> G[Planner选择或拒绝]
    G --> H[Coder收到机制约束与计划]
    H --> I[记录实际修改与运行结果]
```

源码阅读和论文检索仍可交替进行，不强制固定每轮做哪件事。system prompt允许先取证，再形成最终瓶颈；不能继续要求在任何工具调用前就下确定诊断。

涉及“当前loss、采样、冻结方式不合适”的建议，应先阅读对应源码或已有带代码证据的实现摘要。纯资源瓶颈可以由runtime事实支持，无需为满足次数机械读代码。

输出明确区分：

- `observed_facts`：有runtime字段、诊断或源码行支持的事实。
- `hypotheses`：合理但尚未验证的瓶颈假设。
- `unknowns`：缺少的证据。
- 每条机制的代码落点、适用前提、预期观测、最小验证与拒绝条件。

结构化引用可验证代码hash/行号确实被读取，不能声称该检查证明了推理正确。论文证据校验继续保留。

12,000字符为最终可见报告总上限。超限先整条移除低优先级机制或要求模型在剩余轮次内缩短重交，保留关键事实、unknowns、机制ID和验证/拒绝条件；不得直接切字符串或截断JSON。无完整可接受机制时明确返回无报告，不把半条机制交给planner。

Planner增加可选的 `selected_mechanism_id`、采用/拒绝原因及具体adaptation；最多选择一条机制。无法解析采用记录时写unknown，不从自然语言猜测“已采用”。

Coder除现有计划外，独立收到选中机制的简短原文、代码落点、假设、需保留的约束及验证条件。实际diff和执行结果记到该子节点，形成可回溯记录。此次不建立自动因果归因或通用梯度证明系统。

## 7. GPT-6迁移

### 7.1 目标与覆盖范围

后续实验使用 **GPT-6 Astra，API model ID为 `gpt-6-astra`**。覆盖code与feedback两类槽位，包括规划、代码生成、debug/review、结构化反馈，以及使用code槽位的analogy。模型ID已核对[官方模型页](https://developers.openai.com/api/docs/models/gpt-6-astra)。

这里的统一是生成式agent模型统一；embedding模型、比赛训练backbone和确定性评分器各自承担不同任务，保持其原配置。AKB的离线论文库构建与历史分析默认不因本次实验迁移整体重跑或更换模型。

拟将code、feedback和analogy的reasoning effort显式配置为 `high`，作为用户token预算充足下的实验选择。该选择不是对收益的保证；若代理不支持配置值，实施时报告确切兼容问题，不静默改成另一模型或none。

### 7.2 必须同时适配API

官方迁移说明要求GPT-6工具调用使用Responses API，`none`不受支持，并需去掉`temperature/top_p/top_logprobs`等不兼容参数。[官方迁移说明](https://developers.openai.com/api/docs/guides/latest-model)

项目当前存在三个必须覆盖的调用入口：

| 入口 | 当前行为 | 拟迁移方式 |
|---|---|---|
| `llm.query(func_spec=...)` | Chat Completions工具调用，GPT-5路径强制none | GPT-6走Responses，维持上层dict返回契约 |
| `llm.generate` | Chat流式文本或JSON schema | GPT-6走Responses流式/结构化输出，维持上层string接口 |
| analogy独立循环 | 直接调用Chat Completions，未经过query包装 | 使用同一GPT-6 transport能力，保留完整多轮工具状态 |

目前model profile只把GPT-5/o系列识别为相应推理模型；直接填GPT-6会误用通用GPT的采样参数。仅追加前缀又会进入tools设为none的旧路径。因此不能只改 `LLM_MODEL`。

拟新增一个可复用Responses适配层，GPT-6路由到该层；旧模型保留原调用路径，便于复现。多轮工具使用对应 `call_id` 返回结果，并按端点支持的官方方式保留响应状态/必要的reasoning items，不能只复制文本而丢失工具会话。[官方工具调用说明](https://developers.openai.com/api/docs/guides/function-calling)

适配还需处理：schema/工具定义转换、stream完成事件、incomplete与refusal、输出被截断、usage字段映射、错误重试，以及相同模型名下code/feedback角色的显式配置选择。确定性参数错误应快速报错，不连续重试20次。

Schema迁移采用明确策略：既有工具schema先显式保留 `strict:false` 与现有本地校验，避免API默认规范化改变原有可选字段语义；新源码工具使用规范化的strict schema，可选参数用nullable表达，互斥条件由服务端校验。现有planner JSON保留其返回结构和本地解析，单独验证Responses的格式映射，不在本次顺便重写所有schema。[严格模式规则](https://developers.openai.com/api/docs/guides/function-calling)

建议analogy单轮输出预算从6,000提高到16,384，主代码生成暂保留已有16,384默认；reasoning和可见输出共同消耗预算，若发生截断应明确记录并进行有界重试。14轮与12,000字符最终报告上限是应用设置，不等于模型上下文上限。

当前依赖固定 `openai==1.66.3`。实施时检查其实际SDK能力；如需升级，固定一个经本项目验证的明确版本及必要依赖，而非写无上限latest。文档阶段不安装或更换SDK。

### 7.3 当前代理的兼容性

本次只核对公开官方文档与本地代码，**尚未对集群代理发起GPT-6请求**。官方支持不等于现有代理已支持该模型、Responses、工具和状态续接。

实施阶段先做低成本兼容检查：

1. 现有endpoint可用的确切GPT-6模型ID，以及返回的实际model字段。
2. 简单Responses文本、JSON/结构化反馈、流式代码输出。
3. 至少两轮的函数调用及call_id回传，包含reasoning状态保留。
4. 多工具返回、拒绝后重交、输出上限和超时错误。
5. 不携带不支持的采样参数；code/feedback/analogy均使用选定模型和effort。

如果模型或Responses不通，先给出代理返回的具体兼容缺口，保持新实验未启动；不回退GPT-5后仍把实验标成GPT-6。代理自身升级或切换服务若成为必要额外工作，再基于具体情况说明。

### 7.4 后续实验配置

- 更新活动默认值、Secret示例和新实验模板为 `gpt-6-astra`。
- 新Job显式写入模型与reasoning配置，防止克隆旧yaml或环境变量覆盖后仍用GPT-5。
- 历史S51–S56等Job文件与已有run配置保留原样，继续作为历史证据。新模型实验使用新run身份；若要重跑旧seed，生成新的配置和run。
- 新实验preflight核验code/feedback/analogy最终解析值，并记录请求模型、返回模型、endpoint类型、SDK版本、effort及有效context预算；不打印凭据。
- 新版本A/F使用相同GPT-6、同候选预算及共同基础设施；F额外启用analogy上下文增强。比较时记录模型和context版本，不能与GPT-5旧批混合解释为单一功能效应。

## 8. 配置与文件落点

以下为拟新增或修改位置，审批后再实施；名称可按现有模块边界微调。

| 位置 | 拟改动 |
|---|---|
| `MLEvolve/engine/analogy/agent.py` | context v2接入、工具调度、证据/报告schema、14轮和报告预算 |
| `MLEvolve/engine/analogy/context.py`（新增） | 结构化上下文、plan整理、一次性日志清理、字段裁剪记录 |
| `MLEvolve/engine/analogy/code_tools.py`（新增） | 冻结源码、索引、分段读取、父子diff、查询ledger |
| `MLEvolve/engine/candidate_runtime/` | 导出小型运行事实、Jigsaw诊断复用；保持score和选模契约 |
| `MLEvolve/agents/improve_agent.py`及planner/diff coder | 选中机制、约束及验证条件的显式交接 |
| `MLEvolve/llm/responses.py`（新增）、LLM入口与profile | GPT-6 Responses适配和角色/能力路由 |
| `MLEvolve/config/__init__.py`、`config/config.yaml` | context/code tools预算与模型/effort配置，同时维护schema |
| `MLEvolve/k8s`活动默认、示例、preflight | 新实验GPT-6配置与兼容检查，保留历史Job |
| `MLEvolve/utils/verify_*`及必要新增检查 | 离线回归、工具状态与真实endpoint小样验证 |
| `AKB/docs`、既有UPDATELOG | 实施完成后补使用说明和一条重大更新记录 |

新增context能力由配置版本控制，例如 `analogy.context.version=2`。旧配置缺失该字段时保留v1行为，新实验模板显式启用v2，方便控制和回放。

建议保存每次episode的完整packet、逐段裁剪统计、源码查询及精确返回片段、source hash、诊断来源、最终机制与采用记录。记录模型可见内容和API状态/用量；不要求或推测模型内部隐藏推理。

## 9. 验收与实施顺序

### 9.1 离线验收

1. **信息准确性**：用S54–S56的20个历史父节点构建v2 packet，确认实际代码索引、选中快照步数及结束状态可见。F56已加入ranking、F55已更新队列的候选，不能再仅展示修改前的问题。
2. **截断行为**：长JSON plan去重、日志warning清理、关键字段优先级、超长函数与diff续读、预算统计可复现。
3. **源码工具**：current/parent/已结束白名单、不存在symbol、非法行号、hash不符、语法错误代码、runtime关闭回退都给出预期结果；工具不执行候选。
4. **诊断**：公开预测与标签ID严格对应；分项组合与既有总分一致；不同比较contract拒绝直接算delta；缺数据明确标注。
5. **交接**：选中/拒绝/未解析机制记录三种情况，验证条件确实进入diff coder；旧无analogy路径正常工作。
6. **模型适配**：mock验证请求参数、工具call_id、reasoning/output item续接、结构化dict返回、流式string返回、usage与错误分类；旧模型路径回归通过。

### 9.2 真实模型小样验证

审批实施后，通过实际实验endpoint先验证GPT-6兼容性，再回放3–5个代表节点。观察它是否主动读取loss/训练代码、能否区分旧plan与新实现、报告能否正确引用源码/论文，以及额外轮数、token和延迟。

回放无需训练或GPU分配，不使用私有分数调建议。回放成功只说明接口和信息流可用，不宣称实验收益已经提升。

### 9.3 交付与实验

推荐顺序：GPT-6 transport及preflight → context/源码工具 → 已有诊断与交接 → 离线检查 → 真实endpoint回放 → 文档与重大UPDATELOG → 新实验配置。

代码与依赖通过Git同步到新实验使用的固定checkout；若有运行中的实验，避免覆盖其共享源码或venv。新实验使用明确commit和兼容环境，用户自行apply Job。先验证接口，再分配GPU运行整批实验。

## 10. 审批摘要

本方案建议批准：**扩大并整理上下文、三个源码查询工具、现有运行事实及Jigsaw公开验证诊断、机制交接、GPT-6 Astra与必要的Responses迁移、对应验证与文档。**

主要可调参数已给出默认建议：初始packet上限80,000字符；代码查询最多10次/120,000字符；会话累计输入预算196,608 tokens且受实际端点限制；analogy最多14轮；报告12,000字符；模型统一 `gpt-6-astra`，reasoning为high。

本方案已获批准实施。未部署到共享集群代码或提交实验；集群验证使用独立临时目录，后续由用户通过 Git 同步并 apply 新实验。


## 11. 实施结果（2026-09-11）

已完成全部获批代码路径：context v2、源码三工具、运行事实及 Jigsaw 公开诊断、planner/coder 交接、GPT-6 Responses、配置与新实验模板。140 项离线检查及 20 份历史 packet 检查通过；三个修正后真实回放均生成合规报告。真实回放发现并修复了字节计数过于保守导致不能重交报告的问题，未放宽预算上限。固定 SDK 1.66.3 无需升级。

完整证据及限制见 [验证报告](../results/9.11/gpt6_context_v2_validation/REPORT.md)，使用说明见 [MLEvolve context v2](../../MLEvolve/docs/analogy_context_v2.md)。源码尚未提交／推送或部署到共享 checkout；仅在 CPU dev pod 的独立临时目录做了验证。
