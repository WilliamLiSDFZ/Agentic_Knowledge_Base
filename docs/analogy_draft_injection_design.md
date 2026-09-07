# 方案：把类比检索 Agent 加到 draft 阶段（只注入一个 draft）

Status: **已批准，2026-09-06 实现**（branch `feature/structural_analogy_retrieval`）。上游设计：`analogy_bm25_agent_design.md`（已实现，arm D）。实现记录见文末 §9。
本文只写与它的差异；没提到的部分（语料、BM25、tokenizer、工具、id 校验、落盘格式、失败策略）原样复用。

---

## 0. 一句话

**在 run 开始时、生成第一个 draft 之前，让同一个 analogy agent 分析"这个 task 本身的问题结构"
（而不是某个节点的 bottleneck），去 paper KB 里找其他子领域处理同一结构的机制，注入到
第一个 draft 的 prompt 里；另外两个 draft 和之后所有节点不注入。**
新臂记作 **E**（draft-only）；D（improve-only）保持不动，两者不叠加。

---

## 1. 为什么现在要做这个

`plot_analogy.py` 的漏斗图（results/9.5/charts/analogy/）把问题摆得很直接：

| task | valid D run | improve 节点 | agent 调用 | 拿到建议且跑通的子节点 |
|---|---|---|---|---|
| essay | 1 | 11 | 12 | 7 |
| jubias | 4 | 3 | 3 | 1 |
| tf2qa | 0（3 个 invalid） | 0 | 0 | 0 |

D 臂的触发条件是"存在一个跑通的父节点"。在 jubias / tf2qa 这种 12 h 只跑出 7–12 个节点、大多数还 buggy 的
任务上，agent 根本没有机会工作——不是检索没用，是没轮到它。而这恰恰是知识最可能起作用的地方：
第一个方案就选错结构（jubias 用了错的 objective、tf2qa 把 20 GB 全读进内存），后面全是 debug。

上游设计 §10 问题 2 当时按"draft 完全不注入"处理，理由是备忘录 §1："任务开始时没有具体的结构问题"。
这个判断有一半对：**节点级**的 bottleneck 确实要等实验；但 **task 级**的结构性质在实验前就能看出来——
metric 与常规 loss 的失配（QWK、subgroup-AUC）、label 的结构（ordinal、多标注者聚合）、评估协议隐含的对称性、
数据规模与预算的比例、输入的层级结构（长文档 → 段落 → span）。这些是"结构"，不是"主题"，和 8/31 Slack
里"观察问题结构，发现这个结构可能在其他领域出现过"的要求一致。

## 2. 和旧 B 臂的区别（这是最容易做成的失败）

旧 B 臂也是 draft 阶段注入，结果 jigsaw adoption 3%，搜出来的是同领域的 meme / multimodal 论文。
它失败在**query 是 task 描述本身**（distill 成 50–80 词）——BM25 拿到的自然是同主题论文。

E 臂的 query 来自 agent 对 task 的**结构抽象**，和 D 臂一样禁止 competition 的领域名词，
所以它搜的是"处理 ordinal label 与 rank metric 失配的机制"，不是"essay scoring 的论文"。
这个差别是可测的，不靠信念：`plot_analogy.py` 的 retrieval 图直接给出 query 里 competition
词汇的占比和引用论文的 venue 构成。E 臂如果做成了旧 B 臂的样子，图上会是同一 venue 一统、
domain-word 占比高——那就是失败，按失败报告。

## 3. 设计

### 3.1 触发：只在第一个 draft

`run.py` Phase 1 顺序生成 `initial_drafts=3` 个 draft（只生成代码，不执行），然后并行执行。
注入点在 `draft_agent.run()`，条件：`analogy.draft` 开启 **且** `agent.virtual_root` 还没有任何 child
（即这是本 run 的第一个 draft）。第 2、3 个 draft 的 prompt 与 A 臂完全相同。

为什么是第一个而不是最后一个：draft 的 "NOVELTY & DIVERSITY" 规则要求每个 draft 与 Memory 里已有
的 draft 方案不同。注入最后一个 draft 会让它同时背两个约束——"必须和前两个不一样"和"采用这条机制"——
两者可能冲突。注入第一个 draft 时它没有 Memory，两条规则不打架；之后的 draft 会自然避开它的方案，
本 run 内就形成"1 个注入分支 vs 2 个未注入分支"的对照（只是 run 内参考，配对统计仍靠 A 臂）。

`init_solution_path` 路径（用户给定初始方案）不注入。

### 3.2 Packet：`build_task_packet()`

复用 `build_packet` 的 task 头尾截断和 data preview 规则，去掉所有节点级字段，加上 draft 阶段特有的
两项资源信息（agent 判断 feasibility 用，它们也是 impl_guideline 给 draft 看的东西）：

| 字段 | 来源 |
|---|---|
| task | `agent.task_desc` 头 4,500 + 尾 1,500（同 D） |
| data | `agent.data_preview` 前 2,000 chars |
| resource budget | `cfg.agent.time_limit`、`cfg.exec.timeout`、CPU 数、GPU 型号显存（`torch.cuda.get_device_name/mem`，拿不到就写 unknown） |
| pretrained models available locally | `agent.coldstart_description`（已有的 pretrained-model guidance，含本地权重清单） |

约 3–4k tokens。没有 "Validation behaviour"、"attempts"、"trajectory" 三段。

### 3.3 Prompt：`SYSTEM_PROMPT_DRAFT`

与 `SYSTEM_PROMPT` 同骨架（四步、同一批工具、同一 report schema），改三处：

**STEP 1 — STRUCTURE THE TASK**（替换 DIAGNOSE）。从描述和数据里找出 ≤3 条 task 的结构性质，
每条同样写 objects / relations / evidence。规则：性质必须是**输入、标签、metric、评估协议之间的关系**，
不是主题（"it is text classification" 不算）；"数据很大 / 类别不平衡"这类只有配上它和 metric 或预算的
关系才算。给两个和上线任务不重叠的例子（沿用备忘录：LMSYS 的候选顺序对称性；Vesuvius 的深度轴 nuisance）。

**STEP 2** 不变（3–6 词、其他子领域的词汇、禁领域名词）。

**STEP 4 — MAP TO A FIRST DESIGN**（替换 MAP BACK）。`intervention` 字段改为"对**第一个方案**的一条设计承诺"：
在 draft 的约束内可实现（draft prompt 要求首个方案 relatively simple、不做 ensemble），一条建议最多引入
一个非标准组件，并说明它对应哪条结构性质、预期在 validation 上看到什么。feasibility 对照 data
和 resource budget 两段。

schema 不改（`bottlenecks` 字段名沿用，语义变成 "structural properties"——改字段名会让
`inspect_analogy.py` / `measure_adoption.py` 多一套解析，不值得）。

### 3.4 注入：`draft_agent._inject_analogy_draft()`

写进 `prompt["Instructions"]`，位置在 "Solution sketch guideline" 之前（让它先于"要简单"的约束被读到，
但采用规则里重申简单性）。标题：

`Cross-domain mechanism suggestions (analogy search on this task's structure)`

采用规则（对应 improve 版的四条）：

- 最多采用 **一条**作为方案的核心设计承诺；其余忽略。
- 首个方案仍须简单：一条机制 = 一个非标准组件，不叠加。
- 如果自己对任务的判断指向别处，可以全部忽略；别的领域有效不等于这里有效。
- 采用了就在 WHY 里写明：机制名 + 它对应的结构性质（`measure_adoption` 之后靠这句判断）。

`stepwise_plan_and_code_query`（`use_stepwise_generation`）和 `plan_and_code_query` 两条路径都从
`prompt["Instructions"]` 渲染，与 improve 侧验证过的结论相同。

### 3.5 落盘

- 报告存到该 draft 节点的 `SearchNode.analogy_report`（字段已有，不需要改 dataclass）。
- `logs/analogy/draft_001.md` + `index.jsonl` 一行，`extra` 里加 `"stage": "draft"`，`parent_id` 用 virtual root 的 id。
  D 臂现有的行没有 `stage` 字段，读的时候按缺省 `"improve"` 处理。
- 主日志一行 `[analogy] draft: N mechanism(s) from M queries ...`，与 improve 一致。

### 3.6 配置与臂

```yaml
analogy:
  enabled: False
  corpus_path: ""
  improve: True        # 现有行为（arm D）
  draft: False         # 本方案（arm E：draft=True, improve=False）
  ...
```

`AnalogyConfig` 加 `improve: bool = True`、`draft: bool = False`（config 两处同时改，老规矩）。
`improve_agent._inject_analogy` 加一行 `if not cfg.analogy.improve: return ""`。

臂定义（`analyze_runs.py`）：`enabled & improve & !draft → D`，`enabled & draft & !improve → E`，
两者都开 → `F`（本方案不跑 F，但规则先定好，免得以后 config 组合无法归类）。
`EXP_NAME` 后缀 `-anad`（如 `jubias-anad-s45`），`EXP_ID_ARM_SUFFIXES` 加 `-anad`。
`plot_effects.py`：`ARMS` 加 E，`ARM_LABEL["E"] = "E  analogy @ first draft"`，`CONTRASTS` 加 `("E","A")`；
借用 baseline 的 `needy` 集合加 E。

## 4. 分析层改动（都很小）

- `plot_analogy.py`：`reported` 从"improve 且有 report"改为"有 report 的节点"（draft 或 improve）；
  漏斗图对 E 臂加一行 `draft`（值恒为 1，主要为了看它是否跑通、后代多少）；transfer 图对 E 臂改看
  **注入 draft 的分支 vs 同 run 另外两个分支**的最佳 metric（draft 没有 parent，child−parent 无定义），
  以及 E 与配对 A 的 draft 节点 valid 率；retrieval / cost / score 图不用改，按 arm 选 run。
- `inspect_analogy.py`：per-node 表把 draft 节点也列出来（`stage` 列已有）。
- `measure_adoption.py`：已经是"有 `analogy_report` 的节点才判"，draft 节点自动纳入，不改。

## 5. 离线验证（先做，不跑 12 h）

1. `utils/verify_analogy_injection.py` 加两组检查：scripted client 下 draft 1 的 prompt 含新标题、
   draft 2/3 不含；`analogy.draft=True, improve=False` 时 improve 路径不调用 agent；journal 里 draft 节点带 `analogy_report`。
2. `utils/replay_analogy.py --draft --desc <description.md> --data <preview>`：只用 task 描述跑一遍
   draft 版 agent，打印 trace 和报告。在 essay、jubias、tf2qa 三个任务上各跑一次（3 次调用，约 0.2M tokens），
   人工看：结构性质是不是"关系"而非主题；query 有没有领域词；建议在 draft 约束下可不可实现；引用全在搜索结果内。
   **这一步花 API 额度，跑之前我会再问你。**
3. 通过标准：3 份报告里 ≥2 份被判"结构对 + 可作为首个方案的设计承诺"，query 的 domain-word 占比 < 20%。

## 6. 线上实验

- 臂：A vs E，配对同 draw。先 jubias（D 臂最没机会工作、又是有 A 臂基线的任务）2–3 个 draw；tf2qa 在
  磁盘和 valid 问题解决前不排。essay 各 1 个 draw 用来和 D 对照（同一 task 上 D/E 各自的 adoption 与 valid 率）。
- 首要指标仍不是分数：（a）注入 draft 是否跑通、其分支的 valid 率和后代数，对比同 run 另两个分支和 A 臂 draft；
  （b）adoption（LLM judge，按节点）；（c）retrieval 图上的 venue 构成 / domain-word 占比——这是"没做成旧 B 臂"的证据。
- 成本：每个 run 多一次 agent 调用（≈60k input tokens、1–3 分钟，发生在第一个 draft 生成前，串行，
  相当于把 run 推迟约 2 分钟）。

## 7. 改动清单

| repo | 文件 | 改动 |
|---|---|---|
| MLEvolve | `engine/analogy/agent.py` | 新增 `build_task_packet`、`SYSTEM_PROMPT_DRAFT`、`retrieve_for_draft(agent)`（复用 `run_analogy_agent`、`_write_artifacts`，`prompt` 参数化） |
| MLEvolve | `agents/draft_agent.py` | 新增 `_inject_analogy_draft`；第一个 draft 触发；节点上存 `analogy_report` |
| MLEvolve | `agents/improve_agent.py` | `_inject_analogy` 尊重 `analogy.improve` |
| MLEvolve | `config/config.yaml` + `config/__init__.py` | `analogy.improve`、`analogy.draft` |
| MLEvolve | `utils/verify_analogy_injection.py`、`utils/replay_analogy.py` | §5 |
| MLEvolve | `k8s/job-jigsaw-unintended-ae-sNN.yaml`（新） | A + E 两臂，`EXTRA_RUN_ARGS` 加 `analogy.draft=True analogy.improve=False` |
| MLEvolve | `CLAUDE.md`、`k8s/README.md` | 臂说明 |
| AKB | `scripts/analyze_runs.py` | arm E/F 推导、`-anad` 后缀、borrow 规则 |
| AKB | `scripts/plot_effects.py`、`plot_analogy.py`、`inspect_analogy.py` | §4 |
| AKB | `docs/analogy_bm25_agent_design.md` §10 问题 2 | 加一句指向本文 |
| AKB | `CLAUDE.md`、`UPDATELOG.md` | 更新 |

不删任何东西；D 臂的行为和输出格式不变。

## 8. 需要你确认的问题

1. **注入第一个 draft**（§3.1 的理由），还是最后一个？
2. **E 臂 improve 关掉**（单因素：只测 draft 注入），而不是 D+draft 叠加？我建议先单因素；叠加（F）等 E 有结论再说。
3. draft 版建议**最多采用一条**、且受"首个方案要简单"约束——同意吗？还是允许两条？
4. resource budget 放进 packet（§3.2）——同意吗？它让 agent 能拒绝"20 GB 全读内存"这类建议，但也让它更保守。
5. 首批任务 jubias 2–3 draw + essay 1 draw，可以吗？
6. §5 第 2 步的 3 次离线 replay 调用，批准后我先跑再改线上代码，还是直接进线上？

---

## 9. 实现记录（2026-09-06）

按 §7 的清单落地，与设计的差异只有下面几处：

- **prompt 与渲染的切换用一个 `mode` 参数**（`engine/analogy/agent.py::_MODES`），而不是复制一份 loop：
  `run_analogy_agent(..., mode="draft")` 选 `SYSTEM_PROMPT_DRAFT` 和 `REPORT_HEADING_DRAFT`，报告正文里
  "Addresses bottleneck i" 变成 "Addresses property i"；schema、工具、id 校验、预算全部共用。
- **"第一个 draft"的判定**：`virtual_root.children` 为空 **且** `expected_child_count == 0`（后者挡住
  Phase 2 里并行的 root-level draft）。`init_solution_path` 路径不注入。
- **落盘**：`logs/analogy/draft_001.md`（packet、每条 query 及命中、注入原文、raw JSON）+ `index.jsonl`
  一行（`"stage": "draft"`）；improve 侧的 index 行也补了 `"stage": "improve"`。draft 节点的
  `analogy_report` 进 `journal.json`。人工复核入口：`inspect_analogy.py --run <run> --show 1`。
- **`analogy.improve=False` 生效在 `improve_agent._inject_analogy` 入口**，agent 不会被调用。
- **臂推导**（`analyze_runs.py`）：`enabled & improve & !draft → D`、`enabled & draft & !improve → E`、
  两者都开 → F；D 时代的 config 没有 `improve` 键，按 True 处理。`EXP_ID_ARM_SUFFIXES` 加 `-anad`，
  `plot_effects.py` 加 E/F 的颜色、标签和对 A 的 contrast，borrow 规则覆盖 E/F。
- **分析层**：`plot_analogy.py` 的 `reported` 改为"prompt 里带 report 的节点"（D 的 improve、E 的首个
  draft），新增 `<task>_analogy_branches.png`（注入 draft 长出的分支 vs 同 run 其它分支 vs 配对 A 的分支，
  按 branch 最佳 validation metric），score 图按臂各出一张（`_score_E.png`）；`measure_adoption.py` 对
  D/E/F 一视同仁——只判"这个节点看到了什么"；`inspect_analogy.py` 把带 report 的 draft 节点列进表并加
  stage 列。
- **离线验证**：`utils/verify_analogy_injection.py` 第 7 组（首个 draft 注入、第二个 draft 不注入、
  in-flight 不注入、`improve=False` 时 improve 不注入、draft 模式渲染、task packet），全部通过；
  `utils/replay_analogy.py --draft --run <essay D run> --packet-only` 能从旧 run 的首个 draft prompt 恢复
  描述与 data preview。§5 第 2 步（3 次真实 replay）尚未跑，需要 key。
- **k8s**：`job-jigsaw-unintended-ae-s{48,49,50}.yaml`、`job-essay-ae-s50.yaml`（SERVER_ID 77–84），
  seed 与 A/D 批次错开，免得 `analyze_runs.py` 把两批的 A 臂并成一个 draw。
