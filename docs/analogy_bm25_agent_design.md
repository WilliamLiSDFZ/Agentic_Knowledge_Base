# 方案：improve 阶段的类比检索 Agent（BM25 版）

Status: **已批准，2026-09-02 实现**（branch `feature/structural_analogy_retrieval`）。实现与本文的差异见文末"实现记录"。

对应的方向来源：Peijia 8/31–9/1 的 Slack 意见、备忘录《基于局部问题结构查询的类比知识检索系统》、
以及 arXiv 2605.11258（*Unlocking LLM Creativity in Science through Analogical Reasoning*）。
本文把这三份材料翻译成一个可以在 MLEvolve + Agentic_Knowledge_Base 两个 repo 上落地的设计，
并列出要删掉的旧 retrieval 代码。方案落在新 branch 上，旧 retrieval 直接删除、不并存。

---

## 0. 一句话

**把 retrieval 从"cold start 时用 task 描述搜 paper"改成"improve 时由一个 agent 先诊断当前 pipeline
的局部 bottleneck，把它抽象成与 topic 无关的问题结构，再用 BM25 在 paper KB 里搜在其他子领域出现过的同构问题及其机制，最后写成可执行的 intervention 建议注入 improve prompt。**
KB 侧不做任何 LLM 预处理：语料就是现有的 title + tldr + abstract，索引就是 BM25。

---

## 1. 导师方向 → 系统需求

| 来源 | 原话（要点） | 落到设计上 |
|---|---|---|
| Slack 8/31 | "不是 task-to-paper 搜索……观察问题结构，发现这个结构可能在其他领域出现过……给一个结构一样的 query，可以找到其他领域中的实例" | query 的来源是 **search 中间态**（当前 methodology 暴露的局部问题），不是 competition 描述 |
| 备忘录 §1 | `Task → baseline → 实验 → 诊断局部 bottleneck → 生成结构化 query → 检索相似问题结构与历史方法 → 适配成 intervention → 执行并决定保留/放弃` | 检索挂在 **improve** 节点上（MLEvolve 里"诊断→改进"发生的地方） |
| 备忘录 §1.1 | "Retrieval 返回的核心不是整篇相似论文，而是这个局部问题在其他地方以什么形式出现过、当时用了什么机制解决" | agent 的输出是 **mechanism + 映射 + 适配方案**，不是 paper 列表 |
| 备忘录 §12.1 | `query = Diagnose(task, current methodology, validation behavior, ablation, resource profile)` | agent 的输入 packet 就按这几项组装（§4.2） |
| AR 论文 §3.3 | 两步：**Extraction**（抽 objects/relations，生成到其他 domain 的 analogy = object mappings + shared relations）→ **Search**（用 analogy 去找其他 domain 的解法） | agent prompt 的两个阶段直接沿用（§4.3）；"按功能映射，不按表面相似" 这条规则原样保留 |
| AR 论文 B.2 / G.3 | 他们的文献检索是让 LLM 写 **3–4 个词的 Semantic Scholar query**，多条 query 各取 top-15 | BM25 query 也要短、多条（今天的 probe 证实长句 query 明显更差，§6） |
| Slack 9/1 Peijia | "先做抽取然后再做 embedding 不一定合理……试一个最 naive 的方法：不做任何语料预处理，专门开一个 agent……直接在 knowledge base 里仅用字符串级别的工具去搜索" | 不做 (K,V) 抽取、不做 embedding；**一个 agent + 字符串级搜索工具**；BM25 就是这个字符串级工具 |
| Slack 9/1 Peijia | "光是 machine learning 相关，不同领域的其实也有迁移效果……先试一下 ML 相关的" | 语料只用现有 ML 会议论文；"跨领域"在这里指跨 ML 子领域（vision ↔ NLP ↔ graph ↔ theory ↔ RL …） |
| 你 9/1 | "先让 agent 去 paper knowledge base 搜看看效果" | v1 只搜 KB，不联网 |

一个关键认识，决定了 prompt 怎么写：**BM25 本身不会做类比**。它只匹配词。"结构一样但领域不同"的论文，
用的词和当前 competition 完全不同（position bias ↔ permutation equivariance）。所以类比这一步必须由
LLM 完成——把 bottleneck 翻译成 *其他子领域描述同一结构时会用的术语*，BM25 只负责把这些术语对应的论文找出来。
这正是"naive 方法"的分工：**LLM 做 analogy，BM25 做 lookup。**

---

## 2. 现状（要被替换的东西）

现在的 retrieval 全部在 cold start 发生一次，query 是 competition 描述：

```
run.py → build_guidance_description()                     engine/coldstart/knowledge.py
  → build_methodology_guidance()  mode=lazy                engine/coldstart/methodology_agent.py
    → build_lazy_guidance()                                engine/coldstart/ondemand.py
        _distill_query      LLM 把描述压成 50–80 词（disk cache）
        retr.search         bge-m3 mean-centered dense + BM25(RRF)，abstract index，top-40
        _agent_filter_papers LLM 读 title+abstract 判 keep/irrelevant/infeasible（disk cache）
        _extract_one        下载 PDF → pymupdf → LLM 抽 technique → methodology_kb/*.md
        _assemble_techniques 把 [POSITIVE] technique 拼成文本
  → cfg.coldstart.methodology_text
      → draft_agent  "Techniques from recent literature"        （arm B）
      → improve_agent._inject_methodology  (inject_into_improve)（arm C，同一段静态文本重复注入）
```

它的问题不是实现质量，而是**输入**：备忘录 §12.1 说得很直接，拿 task 描述搜出来的是同领域的模型/数据集/baseline，
真正高杠杆的类比要等实验之后才出现。jigsaw 3% adoption（`docs/agent_filter_design.md`）、essay 只在 valid count
上有信号而 score 的 CI 全部含零（`UPDATELOG.md` 8/25、`measure_adoption.py` 开头的说明），都和这个一致。

另外三件现状会影响新设计：

- **语料规模。** 本地 `output/` 有 5 个 venue-year、12,800 篇 unique paper；集群 `kb_snapshot.json`（9/1 tf2qa）
  显示 abstract index 有 **13 个 venue-year、38,273 篇**。你说的"六万多"如果是更新后的数字，新的 corpus builder
  读 `output/` 自然会带上。
- **配对实验的前提变了。** 旧设计花了很大力气保证 B、C 两臂拿到 byte-identical 的知识（`query_cache/`、`filter_cache/`、
  `prepare-task.sh` 的 WARM 阶段）。新设计的 query 依赖每个 run 自己的搜索轨迹，**天然不可预热、不可跨臂复现**。
  这不是缺陷，是备忘录定义的系统就该这样；但 analysis tier 里"两臂 digest 相同"这类检查要一并拿掉（§5.4）。
- **`agents/memory/`（GlobalMemoryLayer 的 HybridRetriever）与本次无关**，那是 per-task 的节点经验记忆，不动。

---

## 3. 新设计总览

```
improve_agent.run(parent)                                    每个健康 parent 的 improve 节点
  │
  ├─ 1. 组 packet：task 摘要 + data preview + parent 的 plan/code_summary/analysis/metric/term_out 尾部
  │        + 同 parent 下已尝试的 attempts + 本 branch 最近几个节点            （§4.2）
  │
  ├─ 2. AnalogyAgent.run(packet)  ── tool-use loop，≤ max_turns                 （§4.3）
  │        LLM: 诊断 ≤3 个 bottleneck 假设（objects / relations / evidence）
  │        LLM: 每个假设写 2–4 条 3–6 词的 query，用"别的子领域"的术语
  │        tool search_papers(query)  → BM25 top-k（id, venue, title, tldr）
  │        tool read_abstract(ids)    → 全文 abstract
  │        …迭代…
  │        tool submit_report(...)    → ≤3 条 mechanism：映射 + 机制 + 适配到本 task 的 intervention
  │
  ├─ 3. 校验（paper id 必须来自搜索结果）→ 渲染成 ≤ 8k chars 的 markdown
  │
  ├─ 4. 注入 prompt["Instructions"]["Cross-domain mechanism suggestions"]     （§4.4）
  │        （改 dict 而不是最终字符串 ⇒ full-rewrite 和 diff/planner 两条路径都能看到）
  │
  └─ 5. 落盘 logs/analogy/<parent_id>.md + journal 里的 node.analogy_report   （§4.5）
```

对应关系：备忘录的"诊断 bottleneck → 结构化 query → 检索 → 适配 intervention"就是 2→3→4；AR 论文的
Extraction = 步骤 2 前两行，Search = 步骤 2 的工具调用。

**边界（v1 明确不做）：** 不联网；不读 PDF 全文（只有 abstract）；不改 draft / debug / evolution / fusion 的 prompt；
不对语料做任何 LLM 预处理；不做 embedding。

---

## 4. 组件细节

### 4.1 语料与索引（Agentic_Knowledge_Base 侧）

**语料文件**：沿用 `scripts/6_build_abstract_index.py::iter_paper_records()` 产出的 record schema
（`id, venue, category, categories, title, source, pdf_url, tldr, abstract`），去掉 embedding 步骤。
新脚本 `scripts/6_build_paper_corpus.py` 只写两个文件：

```
output/paper_corpus/records.jsonl     一行一篇（同旧 schema，去掉 embed_text）
output/paper_corpus/manifest.json     {level:"paper", count, venues:{...}, built_at, records_sha1, schema_version:2}
```

零 LLM、零 GPU，本地 12.8k 篇 6 秒。`run_all.sh` 的 step 6 改调它。`records_sha1` 进 `kb_snapshot.json`，
替代原来的 embedding_model/dim 作为"这个 run 看到了哪份语料"的身份。

**BM25**（在 MLEvolve 加载时构建，不落盘）：

| 项 | 取值 | 理由 |
|---|---|---|
| 库 | `rank_bm25.BM25Okapi`，k1=1.5，b=0.75（默认） | 已在 `requirements_base.txt`；`agents/memory/retriever.py` 已在用 |
| 文档文本 | `title + " " + title + " " + tldr + " " + abstract` | title 重复一次 ≈ 轻微 title boost，不引入 field 权重的复杂度 |
| tokenizer | lowercase → `[a-z0-9]+` → 去停用词（~120 个英文功能词 + "paper/propose/method/results/novel" 这类论文套话）→ Porter stem | 停用词让长 query 不被功能词稀释；stem 让 equivariant/equivariance 互相命中 |
| stemmer | `nltk.stem.PorterStemmer`，import 失败则退化为不 stem，query 侧同样处理 | nltk 在 `requirements_domain.txt`；退化路径保证"不能因为它挂掉 12 小时 run" |
| 构建时间 | 本地 12.8k 篇：tokenize 25 s（stemmer 占大头）+ build 0.6 s；38k 篇估计 ~80 s | 每个 run 一次，可接受；若集群实测 > 2 min，再把 tokenized corpus pickle 到 corpus 目录旁 |
| query 延迟 | ~46 ms / 条（12.8k 篇） | agent 一次跑十几条 query 也只有秒级 |

注意 `HybridRetriever` 现有的 BM25 用的是 `text.lower().split()`，没有去标点、没有停用词、没有 stem，
不能直接复用；新的 tokenizer 放在 `engine/analogy/corpus.py` 里，只服务这个 agent。

### 4.2 Agent 的输入 packet（备忘录 §12.1 的 `Diagnose(...)`）

全部来自 improve 时已经在手的对象，不需要新的 LLM 调用：

| 字段 | 来源 | 截断 |
|---|---|---|
| task | `agent.task_desc` | 前 3,000 + 后 1,500 chars（头尾都给：`semantic_retrieval_design.md` §18 的教训是经典 Kaggle 描述的 ML 内容常在末尾的 Evaluation 段；不再做 distill 调用） |
| data | `agent.data_preview` | 前 2,000 chars（文件名/列名——判断 feasibility 用，旧 filter 的 `_describe_data` 证明这一块必须有） |
| current design | `parent_node.plan` + `parent_node.code_summary` | 各 1,500 chars |
| validation behaviour | `parent_node.analysis`（result_parse 的执行摘要）+ `parent_node.metric.value/maximize` + branch best | 1,500 chars |
| raw evidence | `parent_node.term_out` 尾部 | 1,500 chars（loss 曲线、warning、fold 分数都在尾部） |
| what was tried | `parent_node.fetch_child_memory(include_code=False)` | 2,500 chars |
| branch trajectory | `agent.branch_all_nodes[parent.branch_id]` 最近 6 个节点的 (stage, metric, plan[:200]) | — |

合计 ≈ 5–7k tokens。故意**不**给 parent 的完整代码——agent 的任务是找机制，不是读代码；代码在 improve 的主 prompt 里。

### 4.3 Agent 本体（`engine/analogy/agent.py`）

**形态**：OpenAI tools API 的多轮 tool-use loop，模式照抄 KB repo 的 `plugin_a2_insighter.py::run_agent`
（`tools=` + `tool_choice="auto"` + `MAX_TURNS` 硬上限），采样参数走 `llm/model_profiles.py` 的
`supports_sampling_params / uses_max_completion_tokens`（和 `ondemand._chat` 一样，reasoning model 不传 temperature）。
不用 `llm.query()`，因为它只支持单次强制 function call，没有多轮工具历史。

**三个工具**：

```python
search_papers(query: str, k: int = 10)
    # BM25。返回 [{id, venue, title, tldr, score}]，不含 abstract（省 context）。k ≤ 20。
read_abstract(ids: list[str])
    # 返回 [{id, title, abstract}]，一次 ≤ 8 篇。只接受出现过在搜索结果里的 id。
submit_report(bottlenecks: [...], mechanisms: [...])
    # 终止工具；结构见下。没有它就靠"没有 tool_calls 就结束"，reasoning model 上不够稳。
```

**system prompt 的骨架**（AR 论文 G.1 的 Extraction/Search prompt + 备忘录 §1.1 的 query 性质，改写到 MLE 语境）：

1. *Diagnose.* 从 packet 里找出当前 methodology 暴露的 ≤3 个局部问题。每个写成
   `objects`（当前 pipeline 里的实体及其**功能**角色）、`relations`（实体之间的关系/约束/失配）、`evidence`（packet 里的哪句话）。
   规则：bottleneck 是当前方法的性质，不是 competition 的主题；"分数低"不是 bottleneck。
2. *Abstract & query.* 对每个问题写 2–4 条 query，每条 **3–6 个术语**，用的是"别的 ML 子领域描述同一关系结构时的词"，
   **禁止出现本 competition 的领域名词**（essay、toxicity、contrail…）。按功能映射，不按表面相似
   （AR 论文原话："'Delivers payload' is a good mapping basis; 'is liquid' is not"）。
   给两个固定示例（LMSYS position bias → `permutation equivariance symmetrization pairwise antisymmetry`；
   Vesuvius depth → `nuisance variable invariance marginalization shift-invariant pooling`），示例取自备忘录，
   与线上任务不重叠。
3. *Search & read.* 调 `search_papers`；对 tldr 看起来同构的调 `read_abstract` 确认；不同构就换词重搜。
   预算：≤ `max_turns` 轮（默认 10）。
4. *Map back.* `submit_report`：每条 mechanism 必须给 `object_mappings`（本任务实体 ↔ 论文实体，附一句 rationale）、
   `shared_relations`、`mechanism`（论文做了什么，2–3 句）、`intervention`（在**当前 pipeline** 上具体改什么，
   2–4 句，要能直接变成一次 improve 的 CHANGES）、`feasibility`（对照 data 字段的一句判断）、`paper_ids`。
   只允许引用搜索结果里出现过的 id；这是防幻觉引用的硬约束。

**输出 schema**（`submit_report` 的参数）：

```json
{
  "bottlenecks": [{"statement": "...", "objects": ["..."], "relations": ["..."], "evidence": "..."}],
  "mechanisms": [{
      "bottleneck_idx": 0,
      "title": "Swap-symmetrised training + inverse-permuted TTA",
      "paper_ids": ["icml-2024/xxx"],
      "object_mappings": [{"source": "response A/B slots", "target": "group orbit elements", "rationale": "..."}],
      "shared_relations": "output must transform covariantly under a known input transformation",
      "mechanism": "...",
      "intervention": "...",
      "feasibility": "..."
  }]
}
```

**失败策略**（沿用 coldstart 的铁律：诊断/检索绝不能结束一个 run）：任何异常、超轮次、报告解析失败、id 校验后 mechanisms 为空
→ 返回空字符串，improve 走无注入路径，日志里记一行 `[analogy] node X: no report (reason)`。

**并发**：`parallel_search_num=3` 意味着多个 improve 同时跑。BM25 构建在首次使用时加锁做一次（或在 `AgentSearch.__init__`
里 `analogy.enabled` 时预热，能更早暴露语料路径错误），之后 `get_scores` 只读，线程安全。

### 4.4 注入（`agents/improve_agent.py`）

用一个 `_inject_analogy(agent, prompt, parent_node)` 替换现在的 `_inject_methodology`，同样写进
`prompt["Instructions"]`，这样 full-rewrite 和 `planner_with_memory.generate_initial_plan`（`prompt_base.copy()`
后渲染 Instructions）两条路径都拿得到——这一点旧代码的注释已经验证过，保留。

注入标题：`"Cross-domain mechanism suggestions (analogy search on this node's bottleneck)"`。前置说明沿用旧的三条纪律
（一次最多采用一条；跳过 Memory 里已试过的；如果自己的诊断指向别处就全部忽略），再加一条：
**建议里的 intervention 是针对本节点诊断出的 bottleneck 写的，采用时必须在 WHY/HOW 里说明它对应哪个 bottleneck**——
这一句是为了让 `measure_adoption` 之后能从 plan 里判断"是不是因为这条建议才做的"。

Plateau 分支（`use_magnitude_prompt`）里那句 "You can refer to the expert technique suggestions above" 保留，
措辞改成指向新标题。

预算：报告渲染后 ≤ 8,000 chars（3 条 mechanism 通常 2.5–4k）。不再需要 `improve_token_budget` 这种全局截断——
每个节点的报告是独立生成的短文本。

**触发时机（v1）**：每个 healthy parent 的 improve 节点都触发（`agent_search._run_single_step` 里走到
`improve_agent.run` 的每一次）。plateau-only 作为后续 ablation（§10 问题 1），v1 不加开关。

### 4.5 日志与可观测性

这个项目已经两次被"没记录的诊断"坑过（`\b429\b`、`best_solution.py`），所以：

- `logs/analogy/<parent_id>.md`：packet 原文、每轮 tool call 及其 top-k（id/title/score）、最终报告、轮数、token 数、耗时。
- `logs/analogy/index.jsonl`：一行一次调用 `{parent_id, child_id, turns, n_queries, paper_ids, report_digest, ok, reason}`。
- `SearchNode.analogy_report: Optional[str]`——**必须声明成 dataclass field**（`search_node.py` 用 dataclasses_json 的
  `to_dict()` 序列化，临时 attribute 不会进 `journal.json`）。`measure_adoption` 以后从这里按节点读注入内容。
- `kb_snapshot.py` 改成记录 `paper_corpus/manifest.json`（count、venues、records_sha1）；`methodology_kb` 那一段删掉。
- 每次注入 log 一行 `[analogy] node X: injected N chars, digest ...`，报告正文只在 `logs/analogy/` 里，不刷主日志
  （沿用 `preview_text` / `text_digest`，这两个函数保留）。

### 4.6 配置

`config/config.yaml` 与 `config/__init__.py` **两处同时**加（这个项目的 ConfigKeyError 教训）：

```yaml
analogy:
  enabled: False                # False = arm A 完全不变
  corpus_path: ""               # dir with records.jsonl + manifest.json (Agentic_Knowledge_Base/output/paper_corpus)
  max_turns: 10                 # tool-use loop 硬上限
  top_k: 10                     # search_papers 默认返回条数（上限 20）
  max_mechanisms: 3
  report_char_budget: 8000
```

```python
@dataclass
class AnalogyConfig:
    enabled: bool = False
    corpus_path: str = ""
    max_turns: int = 10
    top_k: int = 10
    max_mechanisms: int = 3
    report_char_budget: int = 8000
```

模型：用 `cfg.agent.code`（gpt-5.6-terra）。诊断和映射是这条链里最需要推理质量的一步，不建议用便宜槽位（§10 问题 5）。

Arm 命名：`analyze_runs.py` 里 arm 由 config 推导，新规则 `analogy.enabled → "D"`；旧的 B/C 规则保留用于读历史 run。
`EXP_NAME` 后缀用 `-ana`（如 `essay-ana-s49`）。k8s job 只需 `EXTRA_RUN_ARGS: "analogy.enabled=True analogy.corpus_path=/workspace/Agentic_Knowledge_Base/output/paper_corpus agent.seed=NN"`。

---

## 5. 删除清单（旧 retrieval）

按你的要求直接删，不留开关。历史结果所需的旧代码在 `main` 分支和 `results/*` 里。

### 5.1 MLEvolve

| 位置 | 动作 |
|---|---|
| `engine/coldstart/methodology_agent.py` | 整文件删除 |
| `engine/coldstart/ondemand.py` | 整文件删除（含 distill、agent filter、PDF 抽取、rerank） |
| `engine/coldstart/knowledge.py` | 删 `_extract_positive_sections`、`_build_methodology_text`、`trim_methodology_text`、`TECHNIQUE_SEPARATOR`、`METHODOLOGY_MAP_JSON` 及 `build_guidance_description` 里整个 methodology 分支和 `injected_knowledge.md` 写盘；**保留** `preview_text`、`text_digest`、pretrained-model guidance、`write_kb_snapshot` 调用 |
| `engine/coldstart/kb_snapshot.py` | 改写：只记录 paper corpus manifest（§4.5） |
| `agents/draft_agent.py` L155–176 | 删 "Techniques from recent literature" 块及其注释（draft 阶段不再注入） |
| `agents/improve_agent.py` | 删 `_inject_methodology`、`_LAST_IMPROVE_DIGEST`；加 `_inject_analogy` |
| `engine/agent_search.py` | 删 `self.methodology_text`；加 analogy corpus 预热（可选） |
| `config/config.yaml` + `config/__init__.py` | 删顶层 `methodology_kb_path, methodology_retrieval, abstract_index_path, lazy_pool, lazy_min_score, max_extractions_per_coldstart, lazy_extract_workers, lazy_technique_rerank, lazy_tech_top_n, lazy_tech_min_score, agent_paper_filter, filter_min_keep, filter_max_keep, filter_batch_size, retr_center_embeddings, retr_query_mode, retr_query_cache_dir, retr_alpha, retr_pool, retr_top_n, retr_min_score, retr_token_budget, retr_embedding_device`；删 `coldstart.methodology_text / inject_into_improve / improve_token_budget`；加 `analogy` 块 |
| `utils/verify_kb_injection.py`、`utils/verify_filter_cache.py`、`utils/dump_injected.py` | 删除；新增 `utils/verify_analogy_injection.py`（静态检查报告能到达 improve 的两条生成路径 + config 两处一致） |
| `k8s/prepare-task.sh` | 删 PROBE 与 WARM 两个阶段（它们服务的 cache 已不存在），只留 PREPARE |
| `k8s/job-*-abc*.yaml` | 不改历史文件；新建 `job-<task>-ad-sNN.yaml`（A + D 两臂） |
| `CLAUDE.md` / `AGENTS.md` / `k8s/README.md` | 更新 cold-start 与 A/B/C 段落 |

`agents/memory/`、`pymupdf4llm` 依赖、pretrained-model guidance（`competition_tag_classified.json` 等）不动。

### 5.2 Agentic_Knowledge_Base

| 位置 | 动作 |
|---|---|
| `scripts/6_build_abstract_index.py` | 改名/改写为 `scripts/6_build_paper_corpus.py`，保留 `iter_paper_records`，删 embedding |
| `scripts/build_retrieval_index.py` | 删除（vector 模式已无消费者） |
| `scripts/probe_retrieval.py` | 替换为 `scripts/probe_analogy.py`（§6） |
| `run_all.sh` | step 6 改调新脚本；`SKIP_INDEX` 语义不变 |
| `scripts/analyze_runs.py` | arm 推导加 `D`（`analogy.enabled`）；`EXP_ID_ARM_SUFFIXES` 加 `-ana`（否则 exp_id 剥不掉后缀、任务分组会错）；删"两臂 digest 相同"类检查 |
| `scripts/measure_adoption.py` | 输入从 `logs/injected_knowledge.md`（全 run 一份）改为按节点读 `journal.json` 的 `analogy_report` |
| `docs/semantic_retrieval_design.md`、`docs/agent_filter_design.md` | 保留作为历史记录，顶部加一行"superseded by analogy_bm25_agent_design.md" |
| `CLAUDE.md`、`UPDATELOG.md` | 更新 |

`scripts/5_build_methodology.py`、`plugin_a*/b/c`、`methodology_kb/` 是 KB 产品本身，不是 retrieval，不动
（`methodology_kb` 里的 technique 抽取以后可以做成 `read_paper` 工具的数据源，见 §9）。

### 5.3 已存在的 run 目录与 results

不动。`results/9.2` 之前的 A/B/C 分析继续用 `main` 上的 `analyze_runs.py` 读；新分支的 analyze 保留读旧 config 的兼容分支即可。

### 5.4 随之失效的实验假设

- "B 与 C 应拿到同一份注入"——不再成立，也没有对应物。
- `prepare-task.sh` 的 "cached, not new" 检查——删除。
- `kb_snapshot` 的 "arms of one draw can differ because methodology_kb is mutable"——语料改成只读的 `records.jsonl`，这条反而消失了。

---

## 6. 离线验证（不跑 12 小时）

### 6.1 今天做的 probe：BM25 在这份语料上能不能找到"机制家族"

在本地 12,800 篇（aaai/acl/icml/naacl/neurips 2024）上建 BM25（§4.1 的 tokenizer），用备忘录 10 个案例，每个案例两种 query：
**structural**——把备忘录里"Agent 会怎么 query"那句直接翻成英文长句；**mechanism**——agent 应该写出来的 3–8 个术语的短 query。看 top-8 有没有落在备忘录"可能 retrieve"那一栏的机制家族里。

| 案例 | 期望机制家族 | structural 长句 | mechanism 短 query |
|---|---|---|---|
| LMSYS position bias | symmetrization / equivariance | ✔ 全是 equivariant nets（略偏架构） | ✔ *Equivariance via Minimal Frame Averaging*、*Equivariant Frames and canonicalization* |
| Jigsaw invariance | TTA / orbit averaging / consistency | ✘ 泛 invariance/OOD | ✘ 泛 invariant learning，没有 TTA |
| Essay ordinal | ordinal regression | ✘ grading 的 LLM 论文 | △ *Exploring Ordinality in Text Classification* 在第 6 |
| Essay domain shift | domain adaptation / pseudo-label | ✔ UDA、label-shift calibration | ✔ pseudo-label UDA、targeted augmentation |
| Contrails temporal | 粗尺度时序融合 | △ 多模态融合泛匹配 | ✔ video semantic seg temporal feature fusion、multi-scale consistency |
| RSNA cascade | proposal→patch / MIL | △ 1 篇 MIL | ✔ WSI MIL ×4、weakly-supervised localization |
| Vesuvius depth | nuisance-axis invariance / pooling | ✘ 泛 3D | ✔ E(3)-invariant aggregation、shift invariance、G-invariant networks |
| NFL gating | cascade / gating / retrieve→rerank | ✘ | △ early exiting、early classification（近亲，非 cascade） |
| Lyft rotation | group averaging / rotated TTA | ✔ equivariant nets、*Improving Equivariant Model Training via Constraint Relaxation* | ✔ partial rotation equivariance、rotation-group networks |
| Breast ROI | ROI proposal → high-res classifier | ✘ | ✔ *GigaHumanDet (gigapixel)*、coarse-to-fine、high-res salient detection |

结论：

- 短的机制术语 query **7/10** 命中家族，长句 **3/10**。这直接决定了 prompt 里"每条 query 3–6 个术语、多条"的规则，
  和 AR 论文 G.3 的做法一致。
- 命中的往往是"机制家族"而非"能直接抄的 trick"（例如 equivariant 架构论文，而不是 swap-TTA 本身）。
  这符合备忘录的定位——返回的是机制，适配成 intervention 是 agent 自己的事——但也意味着 **report 里的
  intervention 质量主要靠 LLM 的世界知识 + 论文给的锚点**，abstract 只提供"确实有人这么做"的证据和术语。
- 三个失败案例（Jigsaw TTA、NFL cascade、ordinal）是词汇错位：语料里这类机制常用别的词（"test-time augmentation"
  在 abstract 里出现少；cascade 多写成 "two-stage"/"early exit"）。agent 多轮换词能部分补救，这就是为什么必须是 agent
  而不是一次 query。
- 三个失败案例里有两个（Jigsaw、NFL）其实前沿 LLM 本来就知道答案（备忘录 §5 把 spooky/NB 归为"类比存在但不稀缺"）。
  这提示评估时要单独看 **parametric novelty**（§7）。

### 6.2 要写的两个离线工具

**`scripts/probe_analogy.py`（KB repo）**——把 6.1 固化：10 个案例 × 期望关键词表，输出 family-hit@10 的表；
`--corpus` 指向任意 `paper_corpus/`。先在本地 12.8k 跑，再在集群 38k 跑一次看变化。这是改 tokenizer/停用词/字段权重时的
秒级反馈，对应旧的 `probe_retrieval.py`。

**`utils/replay_analogy.py --run <dir> --node <id>`（MLEvolve）**——从现成 run 的 `journal.json` 重建 packet，离线跑一遍
AnalogyAgent，打印 trace 和报告。不需要 GPU、不需要数据，只需要 LLM key。用它在 essay / lmsys / jigsaw-unintended 各挑 2 个
improve 节点看报告质量（bottleneck 是否真的是 packet 里的问题、query 是否去掉了领域词、intervention 是否可执行、
引用是否都在搜索结果里）。这是新设计的"probe a second, structurally different task"。

**通过标准（进入线上前）**：probe_analogy 在集群语料上 family-hit ≥ 7/10；replay 的 6 份报告里 ≥ 4 份被你/Peijia 判为
"bottleneck 对 + intervention 可执行"，且 0 份有语料外引用。

---

## 7. 线上实验

**臂**：A（无 KB，config 与现在完全一致）vs **D**（analogy agent at improve）。配对仍按 draw（同一 launch batch、同 seed）。
旧的 B/C 结果（task-semantic retrieval）就是备忘录 §12.3 要求的"Task-semantic retrieval"基线，不再重跑。

**任务**：essay、lmsys、jigsaw-unintended（都有现成 A 臂流程和 prepare 好的数据）。tf2qa 排队时间长，放后。

**看什么**（备忘录 §12.4 → 可测量的定义）：

| 指标 | 怎么算 | 来源 |
|---|---|---|
| mechanism-family hit | 每次调用的 top-k 里是否有目标机制家族（LLM judge，按案例给关键词） | `logs/analogy/*.md` |
| adoption | 每个 improve 节点是否实现了报告里 ≥1 条 intervention（full / proxy / none） | `measure_adoption.py`（按节点读 `analogy_report`） |
| parametric novelty | 同 draw 的 A 臂在整个 run 里有没有自己提出过同一机制家族（grep A 的 plan） | `journal.json` |
| time-to-first-improvement | 第一个超过 draft best 的节点的 wall time | `journal.json` |
| best score @ fixed K | 现有 `compare_arms.py` | `scores.csv` |
| negative-transfer rate | adopted 且 metric 变差的节点 / adopted 节点 | 上两项合并 |

**首要判据是 adoption 和 family-hit，不是 score**——理由与 `agent_filter_design.md` §7 相同：这两个在 n=1 draw 就能看出来，
score 要 8+ draws。

**成本估计**：每个 improve 节点约 6 轮，输入随工具结果累积，≈ 60k input / 4k output tokens；一个 run 约 10 个 improve
节点 → ≈ 0.6M input tokens / run，与旧 lazy 模式冷启动的 ~0.3M 同量级。时间：每节点 1–3 分钟落在代码生成路径上，
被三路并行的执行掩盖大半，12 小时预算内可忽略。

---

## 8. 风险与缓解

| 风险 | 缓解 |
|---|---|
| BM25 对措辞敏感（§6.1 三个失败案例） | 多 query、短 query、多轮换词；prompt 里给"同一机制的常见别名"示例；probe_analogy 持续监控 |
| agent 引用不存在的论文 | `submit_report` 的 `paper_ids` 必须来自本次搜索结果，否则整条 mechanism 丢弃 |
| agent 只是复述 parent 自己的诊断，没有跨域内容 | 报告要求 object_mappings 里 target 必须来自论文；replay 阶段人工看；线上看 parametric novelty |
| improve prompt 变长影响 CHANGES/WHY/HOW 格式遵从 | 8k chars 上限；比旧 C 臂的 48k chars 小得多 |
| 每个 improve 节点多 5–10 次 LLM 调用 | `max_turns` 硬上限；异常即放弃；成本 §7 已估 |
| 跨臂不可复现 | 接受；靠 draw 内配对 + 多 draw；所有中间产物落盘可审计 |
| nltk 不在环境里 | stemmer 退化为 identity，query 侧同样退化，仍能跑 |
| 语料只有 ML 论文，"跨领域"幅度有限 | 导师明确先这样；语料扩展是 KB 侧独立的事，不影响 agent 设计 |

---

## 9. 实施顺序（批准后）

每步都有一个不跑 12 小时就能验证的检查。

| # | 改动 | 验证 |
|---|---|---|
| 1 | KB: `6_build_paper_corpus.py` | count 与旧 `abstract_index/manifest.json` 一致；manifest 有 sha1 |
| 2 | KB: `probe_analogy.py` | 本地/集群语料的 family-hit 表；≥ 7/10 |
| 3 | MLEvolve: `engine/analogy/corpus.py`（加载、tokenizer、BM25、两个查询函数） | 构建时间、单条 query 延迟；与 probe 结果一致 |
| 4 | MLEvolve: `engine/analogy/agent.py` + `utils/replay_analogy.py` | 6 份 replay 报告人工评审；id 校验生效 |
| 5 | MLEvolve: improve 注入、config、`SearchNode.analogy_report`、`logs/analogy/` | `verify_analogy_injection.py`；`agent.steps=4` 的本地 smoke run 看 journal 里有 report |
| 6 | 删除旧 retrieval（§5），改 `kb_snapshot` | `grep` 无残留符号；A 臂 smoke run 行为与 main 一致（config 加载、无注入） |
| 7 | analysis tier：arm D、按节点 adoption | 在第 5 步的 smoke run 上跑通 |
| 8 | k8s：`job-<task>-ad-sNN.yaml`、精简 `prepare-task.sh` | `k8s/validate.py` |
| 9 | 文档：两个 CLAUDE.md、UPDATELOG、本文状态 | — |

建议拆成 3 个 PR：①（1–4，纯新增，可先合）②（5–7，接线 + 删除）③（8–9）。

**后续（不在 v1）**：`read_paper(id)` 工具（复用 `methodology_kb/` 已抽取的 technique 或按需下载 PDF）；
`analogy.trigger: plateau` ablation；random-retrieval 对照臂（备忘录 §12.3 的 "random diverse retrieval"：同一 agent、
`search_papers` 返回随机论文，用来控制"只是看到了更多样 idea"）；联网搜索工具。

---

## 10. 需要你确认的问题

1. **触发范围**：每个 improve 节点都跑（我的建议，footprint 最大、最好测），还是只在 plateau（`success_patience>=2 or total_patience>=5`）时跑以省成本？
2. **draft 阶段**：我按"完全不注入"理解（备忘录 §1：任务开始时没有具体结构问题）。是否同意 draft 只保留 pretrained-model guidance？
3. **v1 只读 abstract**，不下载 PDF。可以吗？`read_paper` 放 v1.1。
4. **删除范围**：§5 的清单是"两个 repo 都删干净"，包括 KB 侧的 `build_retrieval_index.py`、`probe_retrieval.py` 和 MLEvolve 的三个 `verify_*/dump_*` 工具、`prepare-task.sh` 的两个阶段。是否照单全删，还是只删 MLEvolve 侧、KB 侧脚本先留？
5. **模型槽位**：agent 用 `agent.code`（gpt-5.6-terra）。同意吗？
6. **首批任务**：essay + lmsys + jigsaw-unintended，各 2 个 draw 起步？
7. **命名**：arm `D`、`EXP_NAME` 后缀 `-ana`，可以吗？
8. **语料**：集群上现在到底是 38k（9/1 snapshot）还是你说的六万多？如果 `output/` 已经加了新 venue，第 1 步会自动带上；如果是别的来源，我需要知道格式。

---

## 11. 实现记录（2026-09-02）

按 §9 的顺序落地，与设计的差异只有下面几处：

- **tokenizer**：Porter stem 加了按词记忆化，12.8k 篇的加载从 25 s 降到 ~4 s，38k 篇预计 15 s 以内，所以没有做 pickle 缓存；语料在 `AgentSearch.__init__` 里预加载，错误在第一分钟就能看见。
- **probe 指标**：`probe_analogy.py` 用关键词判 family-hit@10，比 §6.1 的人工判读宽松（关键词 9/10 vs 7/10；结构长句 7/10 vs 3/10），方向一致；脚本 docstring 里两组数字都记了。它直接 import MLEvolve 的 `engine/analogy/corpus.py`，不复制 tokenizer。
- **reasoning**：gpt-5.6 走 `/v1/chat/completions` 带 tools 时必须 `reasoning_effort=none`（`llm/openai.py` 的既有约束），所以 agent 的诊断是以可见文本写出来的，不是私下推理；换 Claude 时走 adaptive thinking。
- **prepare-task.sh** 只剩数据集与语料存在性检查；旧的 PROBE/WARM/VERIFY 三段随 cache 一起删除。
- **`5_build_methodology.py --build-index` 与 `build_methodology_all.sh` 末尾的 index 构建**：因 `build_retrieval_index.py` 删除而一并移除；`methodology_kb` 本身不动。
- **未做**（留待 v1.1，见 §9 后续）：`read_paper` 工具、plateau-only 触发、random-retrieval 对照臂。

离线验证：`MLEvolve/utils/verify_analogy_injection.py`（六组检查，~2 s，不需要 key）；线上第一份 draw 用 `k8s/job-essay-ad-s49.yaml`。
