# 设计:方法论冷启动的技术级语义检索

**状态:** 提案 · **范围:** 把 mlevolve 冷启动里"LLM 按名字挑 ≤5 个 category"这一步,换成对单条 insight 的向量检索。
**跨仓库:** 索引在**本仓库**(Agentic Knowledge Base)*构建*,在 `mlevolve/engine/coldstart/methodology_agent.py` 里*查询*。

> 说明:本文件是英文版 `semantic_retrieval_design.md` 的中文对照版,内容一致。代码骨架保持原样。

---

## 1. 问题

现在 mlevolve 冷启动一个任务时,选取文献知识的方式是这样的(`mlevolve/engine/coldstart/methodology_agent.py`):

1. `_scan_categories()` 列出所有含 `insight.md` 的 `paperinsight/{venue}/{category}`。
2. `_match_categories_with_llm()` 把 `task_desc[:1500]` + **category 名字列表**发给 LLM,让它返回**最多 5 个** category 名。
3. `_read_high_confidence_references()` 读这些 category 的 `insight.md`,只保留 `HIGH` 置信度的行,再读它们的 reference 文件。

失败模式:

- **召回被 category 名字卡死。** 选取发生在一个 ~80 项聚类的*名字*上,而不是内容。某个技术若落在名字不像的 category 里就完全不可见——哪怕它的 `Actionable Guidance` 完美契合任务。
- **硬上限 5 个 category**,而且没有"有多相关"的概念。
- **粒度太粗。** 选取单元是整个 category(几十篇论文),不是单个技术。
- **没有分数。** 没有可排序、可阈值、可裁剪的东西,category 层面是全有或全无。
- **每次多一次 LLM 调用**(延迟 + 成本),而这本可以用一次向量查找替代。

## 2. 目标

在 **insight/技术粒度**上、用**混合语义检索**(稠密向量 + BM25)做选取,为任务返回一组按分数排序、经阈值过滤的 insight。
保持 `build_methodology_guidance()` 的签名和输出格式不变,这样下游(`knowledge.py`、draft prompt)都不用改。

非目标(单独跟踪):迭代/逐步检索与记忆感知排除(improve #2);更细的任务分型(improve #3)。这些都留了钩子。

## 3. 检索单元

天然单元已经存在:`insight.md` 表格的每一行对应一个 `paperinsight/{venue}/{category}/references/{slug}.md`——一条**跨论文 insight**,带 title、confidence、引用论文、解释,以及一个 `Actionable Guidance` 块。这正好是"一个技术 + 适用情境"。我们**每个 reference 文件索引一条记录**。

每条记录两个文本字段,各司其职:

| 字段 | 由什么构成 | 用途 |
|------|-----------|------|
| `embed_text` | `title` + `Actionable Guidance` + `Condition` | 拿来 embedding、和任务匹配(即"何时/是什么") |
| `guidance_text` | 清洗后的 reference 正文(`_strip_ref_noise` 那套逻辑) | 命中后注入 prompt 的内容 |

embedding 的是*guidance/condition*(而不是整篇论文堆砌),让向量聚焦于"对某任务的适用性",这正是 query 关心的。

可选的更细一层(phase 2):把每篇 `*_methodology.md` 里的每个 `## [POSITIVE]` 段也索引进来。同样的记录 schema,`source: "methodology_per_paper"`。先只做 insight 级。

### 记录 schema(可移植,`index/records.jsonl` 里每行一个 JSON 对象)

```json
{
  "id": "naacl-2024/efficient-large-model-training-optimization/adaptive-rank-allocation",
  "venue": "naacl-2024",
  "category": "efficient-large-model-training-optimization",
  "title": "Adaptive Rank Allocation in Low-Rank Adaptation Outperforms Uniform Rank",
  "confidence": "HIGH",
  "papers": ["2024naacl-long.35", "2024naacl-long.13"],
  "source": "methodology_kb",
  "embed_text": "Adaptive Rank Allocation ... \nActionable Guidance: use ABLoRA importance ... \nCondition: fine-tuning LLMs with LoRA where layers differ in importance",
  "guidance_text": "# Adaptive Rank Allocation ...\n<cleaned body>"
}
```

## 4. 架构

```
构建(本仓库,离线,在 plugin_a2 之后)                 查询(mlevolve,冷启动时)
────────────────────────────────────────            ─────────────────────────────────────
scripts/build_retrieval_index.py                     methodology_agent.build_methodology_guidance()
  遍历 paperinsight/ (+ experience_kb/)                  加载索引产物(一次,缓存)
  解析每个 reference -> record                           query = task_desc (+ data_preview)
  embed embed_text  (sentence-transformers)             HybridRetriever.search(query, top_k)
  写出 index/ 产物:                                     置信度加权 + 阈值 + 裁剪
    - records.jsonl                                     拼成和现在一样的 guidance 块
    - embeddings.npy                          ── 产物 ──►    (无产物则回退到 LLM/static)
    - manifest.json (model, dim, kb_hash)
```

关键复用:**mlevolve 已经自带我们需要的 retriever**——
`mlevolve/agents/memory/retriever.py::HybridRetriever`(BM25 + FAISS `IndexFlatL2` + RRF 融合)和
`mlevolve/agents/memory/embedding_models.py::EmbeddingModel`。查询侧原样复用,只是喂进去的是 insight 记录而非 memory 记录。**mlevolve 不新增任何检索代码。**

构建侧保持轻依赖:只需 `sentence-transformers` + `numpy`(本仓库 `requirements.txt` 已有)。它写出 `embeddings.npy`;mlevolve 在加载时用这个数组在内存里建 FAISS 索引(它已经有 `faiss`),所以**本仓库不新增 `faiss` 依赖**。

## 5. 构建侧 —— `scripts/build_retrieval_index.py`(本仓库新增)

职责:

1. 遍历 `methodology_kb/paperinsight/{venue}/{category}/`。对每个 `insight.md`,解析表格
   (`# | Insight | Papers | Confidence | File`)拿到每行的 `confidence` + `papers`,再读对应的
   `references/{slug}.md`(复用 `_read_high_confidence_references` 里现成的"行→文件"解析,含 slug 前缀模糊兜底)。
2. 构造 `embed_text`(title + Actionable Guidance + Condition——从 reference 正文里把这几段解析出来)和
   `guidance_text`(去掉 frontmatter / `Papers & Evidence` / `Delta` 后的正文,即 `_strip_ref_noise` 那套)。
3. 可选:同样方式纳入 `experience_kb/*/references/*.md`(`source: experience_kb`)。
4. 用配置的模型 embedding 所有 `embed_text`;写出:
   - `index/records.jsonl` —— 记录(不含向量)
   - `index/embeddings.npy` —— `float32 [N, dim]`,与 records.jsonl 行对齐
   - `index/manifest.json` —— `{embedding_model, dim, count, built_at, kb_content_hash, schema_version}`

骨架:

```python
# scripts/build_retrieval_index.py
import json, hashlib, numpy as np
from pathlib import Path
from datetime import datetime
from sentence_transformers import SentenceTransformer

MODEL_NAME = "BAAI/bge-m3"          # 必须与查询侧一致;见 §8
KB = Path("methodology_kb")
OUT = KB / "index"

def iter_records():
    for insight_md in (KB / "paperinsight").glob("*/*/insight.md"):
        cat_dir = insight_md.parent
        venue, category = cat_dir.parts[-2], cat_dir.parts[-1]
        for row in parse_insight_table(insight_md):          # -> {title, confidence, papers, file}
            ref = resolve_reference(cat_dir, row)            # 复用 slug/模糊解析
            if not ref: continue
            body = ref.read_text(encoding="utf-8")
            yield {
                "id": f"{venue}/{category}/{ref.stem}",
                "venue": venue, "category": category,
                "title": row["title"], "confidence": row["confidence"].upper(),
                "papers": row["papers"], "source": "methodology_kb",
                "embed_text": build_embed_text(row["title"], body),   # title + guidance + condition
                "guidance_text": strip_ref_noise(body),
            }

def main():
    records = list(iter_records())
    model = SentenceTransformer(MODEL_NAME)
    vecs = model.encode([r["embed_text"] for r in records],
                        normalize_embeddings=True, show_progress_bar=True).astype("float32")
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / "records.jsonl", "w") as f:
        for r in records: f.write(json.dumps(r, ensure_ascii=False) + "\n")
    np.save(OUT / "embeddings.npy", vecs)
    json.dump({"embedding_model": MODEL_NAME, "dim": int(vecs.shape[1]),
               "count": len(records), "built_at": datetime.now().isoformat(),
               "kb_content_hash": hash_kb(KB), "schema_version": 1},
              open(OUT / "manifest.json", "w"), indent=2)
```

把它接成 plugin 层的最后一步(`plugin_a2_insighter` 之后),或在 `run_all.sh` 里加一行。KB 一变就重建;
`kb_content_hash` 让查询侧能在过期时告警。

## 6. 查询侧 —— 重写 `methodology_agent.py`(mlevolve)

用检索路径替换 `_match_categories_with_llm` + `_read_high_confidence_references`。
保持 `build_methodology_guidance(task_desc, methodology_kb_path, cfg)` 及其返回块的形状完全不变。

```python
# 一个极小的记录对象,好让 HybridRetriever 装我们的 insight
class InsightRecord:
    def __init__(self, d): self.__dict__.update(d)

_INDEX_CACHE = {}   # methodology_kb_path -> (retriever, records)

def _load_index(methodology_kb_path, cfg):
    if methodology_kb_path in _INDEX_CACHE:
        return _INDEX_CACHE[methodology_kb_path]
    idx = Path(methodology_kb_path) / "index"
    manifest = json.load(open(idx / "manifest.json"))
    records = [InsightRecord(json.loads(l)) for l in open(idx / "records.jsonl")]
    texts = [r.embed_text for r in records]
    emb_model = EmbeddingModel(model_type="local",
                               model_name=manifest["embedding_model"],   # 与构建侧相同
                               device=getattr(cfg, "embedding_device", "cpu"))
    retr = HybridRetriever(emb_model)
    vecs = np.load(idx / "embeddings.npy")
    retr.records, retr.texts = records, texts
    retr.vectors = vecs
    retr.vector_index = faiss.IndexFlatL2(retr.dimension); retr.vector_index.add(vecs)
    retr.bm25 = BM25Okapi([t.lower().split() for t in texts])          # 便宜,这里重建
    _INDEX_CACHE[methodology_kb_path] = (retr, records)
    return retr, records

def build_methodology_guidance(task_desc, methodology_kb_path, cfg):
    idx_dir = Path(methodology_kb_path) / "index"
    if not (idx_dir / "manifest.json").exists():
        return _legacy_llm_or_static(task_desc, methodology_kb_path, cfg)   # 回退,不变

    retr, _ = _load_index(methodology_kb_path, cfg)
    query = _build_query(task_desc, cfg)                 # §7
    hits = retr.search(query, top_k=cfg.retr_pool, alpha=cfg.retr_alpha)    # [(rec, score)]
    selected = _select(hits, cfg)                        # 置信度加权 + 阈值 + 裁剪
    if not selected:
        return ""
    blocks = [f"### [{r.category}] {r.title} (confidence: {r.confidence})\n\n{r.guidance_text}"
              for r, _ in selected]
    return ("\n\n---\n## Methodology Insights from Literature\n"
            "The following techniques were retrieved as most relevant to this task:\n\n"
            + "\n\n---\n\n".join(blocks))
```

`faiss`、`BM25Okapi`、`np`、`EmbeddingModel`、`HybridRetriever` 在 mlevolve 里都已可导入。
(可选:给 `HybridRetriever` 加个 `load_from_embeddings(records, texts, npy_path)` 辅助方法,把"从数组建 FAISS"的接线收在一处,而不是散在 `methodology_agent` 里。)

## 7. Query 构造

先简单,留扩展余地:

- **v1:** `query = task_desc`(完整,不截到 1500)。
- **v1.1(推荐):** 追加一段由 `agent.data_preview` 派生的紧凑数据摘要(模态、样本数、特征数/类别数、图像尺寸)。
  数据形状是"哪些技术适用"的强信号,而 mlevolve 本就算好了它。保持简短(几行),别让它主导 embedding。
- **phase 3:** 多 query(任务文本 + 数据摘要分别 embedding,取命中并集),当单一混合向量召回不足时用。

## 8. Embedding 模型

**硬规则:** 构建侧和查询侧**必须**用同一个模型(同一向量空间 + 同维度)。由 `manifest.embedding_model` 强制;
查询侧据此实例化 `EmbeddingModel`,而 `HybridRetriever` 本就会断言加载维度匹配。

推荐(2026 现状):

- **目标:`BAAI/bge-m3`** —— 2026 年开源生产默认(MIT、多语言、dense+sparse),相比 `bge-base-en-v1.5`
  是明显一档提升。~1024 维;几千条 insight 秒级 embedding,每次 query 就一次短编码。
- **零摩擦兜底:`BAAI/bge-base-en-v1.5`** —— mlevolve 的 memory 层已经加载它,复用则无需额外下载模型。
  稍弱但足够先上线。

两者都可配置,以 manifest 为准。检索单元文本很短(一个 title + 一段 guidance),对通用检索 embedding 来说
完全在分布内,不需要领域微调。

**可选 reranker(phase 2):** 对 top ~30 命中加一层 cross-encoder 精排提升精度。2026 默认是
**`BAAI/bge-reranker-v2-m3`**(质量/延迟/许可最优);对延迟敏感有更轻的(FlashRank、mxbai-rerank)。
v1 先不上——光混合检索就已经解决召回问题,reranker 是精度上的锦上添花。

## 9. 选取策略(默认值,全部可配)

- `retr_pool = 30` 个候选来自 `HybridRetriever.search`,`retr_alpha = 0.5`(BM25/向量均衡——复用 retriever 默认)。
- **置信度加权:** 分数乘 `{HIGH:1.0, MEDIUM:0.7, LOW:0.4}`;`LOW` 丢弃,除非没有别的过线的。
  (保留现在"HIGH 优先"的偏好,但不再一刀切丢掉其余。)
- **最低分阈值**(作用在归一化融合分上),让不相关的任务什么都不注入,而不是总返回 5 个 category。
- **裁到 `retr_top_n = 10`** 条 insight + **token 预算**(~4–6k token),避免 draft prompt 膨胀
  (顺带缓解现在"整块注入"的稀释问题)。
- **去重**近似相同的标题(同一技术在多个会议重复出现)——保留最高分,并记下其余来源会议。
- **给 improve #2 预留钩子:** `search(..., exclude_ids=...)`,用来丢掉 global memory 里已试过/失败的 insight。
  v1 不接线,签名先留位。

## 10. 配置与向后兼容

在现有配置项旁加(带一个模式开关,保证可回退):

```yaml
methodology_retrieval: vector      # vector | llm | static  (默认 vector;llm = 现在的行为)
retr_alpha: 0.5
retr_pool: 30
retr_top_n: 10
retr_min_score: 0.15
embedding_device: cpu              # 或 cuda
# embedding 模型来自 index/manifest.json(构建/查询必须一致)
```

`build_methodology_guidance` 按 `methodology_retrieval` 分派;`llm`/`static` 原样保留当前代码路径做兜底。
若模式是 `vector` 但没有 `index/` 产物,则记一条告警并回退到 `llm`。**调用方零改动**——
`knowledge.py:128` 和 draft prompt 不动。

## 11. 评估(切默认之前先证明召回收益)

本仓库离线 harness,`scripts/eval_retrieval.py`:

1. **探针集:** ~15–20 个代表性任务(从 `competition_tag_classified.json` / 数据集描述取名字+描述)。
   为每个任务标注 KB 里*相关*的 insight id(人工过一遍,或强 LLM 过一遍再抽检)。
2. **对比**三种选取器在同一批探针上的表现:(a) 现在的 `_match_categories_with_llm`(映射到它的 insight)、
   (b) 纯向量、(c) 混合。
3. **指标:** 每种选取器的 recall@{5,10,20} 和 nDCG@10;外加 **coverage** = 拿到 ≥1 条相关 insight 的任务比例
   (现在的方法名字不匹配时直接返回*空*——coverage 是预期涨最多的地方)。同时报检索延迟/成本
   (一次本地编码 + FAISS vs 一次 LLM 调用)。
4. **门槛:** 只有当混合在探针集上 recall 和 coverage 都 ≥ LLM 时,才把 `methodology_retrieval` 默认切成 `vector`。

## 12. 分期推进

- **Phase 1(本提案):** builder + `records.jsonl`/`embeddings.npy`/`manifest.json` 产物;
  mlevolve 查询重写并复用 `HybridRetriever`;配置开关;LLM/static 回退;评估 harness。
  评估通过后,以 `methodology_retrieval: vector` 上线。
- **Phase 2:** cross-encoder reranker;把 `experience_kb` 也索引;接线 `exclude_ids` 做记忆感知检索
  (接上 improve #2)。
- **Phase 3:** 用 `data_preview` 丰富 query;从一次性冷启动改为搜索卡住时按需检索(improve #2 正题)。

## 13. 风险与缓解

| 风险 | 缓解 |
|------|------|
| 构建/查询模型不一致 → 维度报错 | `manifest.embedding_model` 驱动查询模型;`HybridRetriever` 断言维度 |
| KB 更新后索引过期 | 作为 pipeline 最后一步重建;manifest 里 `kb_content_hash` → 不匹配则告警 |
| 冷加载延迟(模型 + 索引) | 每次 run 只加载一次,缓存在 `_INDEX_CACHE`;索引很小 |
| 没有 `index/` 产物 | 回退到现有 LLM/static 路径,不崩 |
| 过度检索撑爆 prompt | `retr_top_n` + token 预算 + 去重 |
| reference 正文解析有缺 | 复用成熟的 `insight.md` 行解析 + `_strip_ref_noise`;解析不了就跳过,不崩 |

## 14. 逐文件改动清单

**本仓库(Agentic Knowledge Base):**
- **新增** `scripts/build_retrieval_index.py` —— 构建索引产物。
- **新增** `scripts/eval_retrieval.py` —— recall/coverage harness。
- **改** `run_all.sh`(可选)—— 在 plugin 层之后跑索引构建。
- `requirements.txt` —— 已有 `sentence-transformers`、`numpy`;构建无新依赖。
- `docs/semantic_retrieval_design.md` / `docs/semantic_retrieval_design.zh.md` —— 本文档。

**mlevolve 仓库:**
- **改** `engine/coldstart/methodology_agent.py` —— 加 `InsightRecord`、`_load_index`、`_build_query`、`_select`;
  重写 `build_methodology_guidance` 按 `methodology_retrieval` 分派;把 `_match_categories_with_llm` /
  `_read_high_confidence_references` 留作 `llm` 兜底。
- **改** `config/config.yaml` + `config/__init__.py` —— §10 的那些 key。
- **可选** `agents/memory/retriever.py` —— 加 `load_from_embeddings(records, texts, npy_path)` 辅助方法,
  让"从数组建 FAISS"的接线共享,不重复。

## 15. 待定问题

- v1 就索引 `experience_kb` 还是放 v2?(它的 insight 是实战检验过的——也许值得加权——但格式/校验不同。倾向 v2。)
- 按 venue-year 分子索引,还是一个全局索引?一个全局索引更简单,且能让任务不分会议地取到最好的 insight;
  KB 变大再考虑分。
- 产物放 `methodology_kb/index/` 里(随 KB 一起走)还是作为独立发布物?放 KB 里最简单,也契合 mlevolve
  本就指向 `methodology_kb_path` 的方式。

## 16. Lazy 模式(v1.1,已实现):摘要先行索引 + 按需深加工

**动机。** 批量管线(plugin A 全量抽取 + A2 逐 category 综合)把全部抽取成本预付在前——单个
NeurIPS 年份就要 ~70M+ input token,而一次冷启动实际只消费极少数 insight。Lazy 模式把昂贵步骤
移到查询时,并加上封顶。

**流程**(`methodology_retrieval: lazy`):

1. **摘要索引**(本仓库 `scripts/6_build_abstract_index.py`):每篇论文一条记录
   (title/tldr/abstract + `pdf_url`/`source`),本地 embedding——**零 LLM 成本**。
   已作为 `run_all.sh` 的默认收尾步骤(重的批量 step 5 改为 `FULL_METHODOLOGY=1` 可选)。
2. **冷启动检索**(MLEvolve `engine/coldstart/ondemand.py`):用**低相对阈值**查摘要索引
   (`lazy_min_score` 默认 0.05;pool `lazy_pool` = 40)——重召回轻精度,因为下一步的成本
   有封顶,精度在组装时找回。
3. **按需抽取:** 没有缓存 `*_methodology.md` 的候选**现场**抽取(下 PDF → pymupdf →
   每篇一次 LLM;线程池;每任务至多 `max_extractions_per_coldstart` = 20——**成本天花板旋钮**)。
   结果写入**标准** `methodology_kb/{venue}/{category}/` 布局:缓存永久、与批量管线共享
   (它会跳过已存在文件),之后还能离线跑 A2 综合。
4. **最终选取——两种口味**(`lazy_technique_rerank` 开关):
   - **True(默认):第二级技术粒度检索。** 把抽取出的所有 `[POSITIVE]` 段拆成独立技术条目,
     用与摘要索引**同一个**模型现场编码(模型已加载——零额外 LLM 成本),按与任务的相似度排序,
     配精度导向的相对阈值(`lazy_tech_min_score` = 0.3、`lazy_tech_top_n` = 12)。
     精度在这里、以正确的粒度找回:第一级是召回导向且论文粒度的,相关论文里的不相关技术
     必须在这一层被滤掉。注入块带来源论文标注。
   - **False:论文粒度注入**——候选论文的 `[POSITIVE]` 段整包进,只按第一级摘要分排序。
   两种都做标题去重,且受 `retr_token_budget` 约束。

**成本:** 起步 ~0.3M token/任务(20 篇 × ~16k),随缓存变热趋近于零——对比批量路径的
70M+ 预付。

**取舍:** 环内没有跨论文综合和置信度校准(A2)——可定期对积累的缓存离线跑 A2 回补;
冷启动下 PDF 需要联网(失败时优雅降级为只用缓存);`pymupdf4llm` 在 MLEvolve 是软依赖
(缺失则跳过抽取);冷启动延迟 +3–8 分钟,受抽取封顶约束。

**配置(MLEvolve):** `abstract_index_path`、`lazy_pool`、`lazy_min_score`、
`max_extractions_per_coldstart`、`lazy_extract_workers`;lazy 模式下 `methodology_kb_path`
指向 **methodology_kb 根目录**(抽取缓存树)。

**预留(默认关):** `lazy_synthesize`——对抽出的技术做一次任务条件化的单发综合调用
(比 A2 的 agent 循环便宜一个量级;phase 2)。

## 参考(2026 检索现状)

- 2026 最佳开源 embedding 模型(BGE-M3 作生产默认;Qwen3-Embedding 居 MTEB 榜首):BentoML、KnowledgeSDK、CodeSOTA MTEB。
- 2026 rerankers(BGE-reranker-v2-m3 默认;更轻的替代):ZeroEntropy、BSWEN、Local AI Master。
