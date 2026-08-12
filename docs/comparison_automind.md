# Ours vs AutoMind — a component-by-component comparison

Read from the AutoMind paper itself (arXiv 2506.10974**v3**, Zhejiang University + Ant Group),
not from summaries. Two numbers previously recorded in `related_work.md` from a search
summary were wrong and are corrected here:

| claim | secondary source said | the paper says |
|---|---|---|
| knowledge-base ablation | −5.0% Beats, −1.3% Valids | **−11.8% win rate, −5.6% valid rate** (Medium split, DeepSeek-V3) |
| headline result | surpasses 61.0% of humans | **38.7% (o3-mini) / 41.2% (DeepSeek-V3)** avg@3 |

---

## Side by side

| | AutoMind | Ours |
|---|---|---|
| **Corpus — craft** | 3,237 public forum posts covering 455 Kaggle competitions | **none** |
| **Corpus — papers** | KDD, ICLR, NeurIPS, ICML, EMNLP + *Bioinformatics*, last 3 years, from arXiv | AAAI, ACL, ICML, NAACL, NeurIPS, ICLR (+CVPR/ICCV in progress); no KDD, no EMNLP, no journals |
| **What is stored per paper** | meta (title, author, abstract, keywords) + main content, plus an LLM summary along data / task / technique / contribution | full-PDF extraction into a list of **techniques**, each with `effect ∈ {positive, negative, neutral}`, `delta`, a verbatim `evidence` quote and a `condition` |
| **Cross-paper layer** | none | `plugin_a2`: tool-use agent writes insights that must cite **≥2 papers** with quotes, each labelled HIGH/MEDIUM/LOW, with a self-review pass |
| **Retrieval route** | hierarchical labels. Tricks get 11 top-level categories + subcategories; the incoming task is labelled the same way; per-label similarity search | dense+sparse hybrid (BM25 + FAISS + RRF) over abstracts, then a **second stage that re-embeds each individual technique** and ranks it against the query |
| **Query construction** | the paper states task-description embeddings alone "prove ineffective", so they route around it via labels | one cached LLM call distils the description into a 50–80 word task statement; measured 3/10 → 9/10 on-topic |
| **Embedding geometry** | not discussed | mean-centring for corpus anisotropy; spread 0.017 → 0.048, on-topic 5/10 → 8/10 |
| **Build cost** | whole KB built offline up front | **lazy**: abstract index is free (local embeddings), full-text extraction happens on demand, capped at 20 papers per cold start, permanently cached |
| **Where knowledge enters** | **papers → Drafting, tricks → Improving**, debugging gets none | papers → Drafting only (improve-stage injection just added, default off) |
| **Contamination guard** | filters out solutions/tricks belonging to the target task, "to avoid plagiarism" | **none** |
| **Coding strategy** | complexity scorer → one-pass below threshold, stepwise decomposition + AST check above | MLEvolve has one-pass / stepwise / diff coders, dispatched by search state |
| **Evaluation** | MLE-Bench lite, 15 tasks in Easy/Medium/Hard, 24 h, **3 runs per task**, best@3 and avg@3; plus two post-2023 competitions (OAG KDD Cup 2024, BELKA NeurIPS 2024) | 3 tasks, 12 h, 1–3 runs; per-task raw metric |
| **KB result** | **−11.8% win rate, −5.6% valid rate** when ablated | no measurable benefit; harmful on two tasks, null on the third |

---

## What we have that they do not

1. **Signed technique extraction.** They keep a paper's summary; we decompose a paper into
   individual techniques and record whether each *helped, hurt or did nothing*, with the
   quantitative delta, the supporting quote and the condition under which it applies. Only
   `[POSITIVE]` entries are injected, so the extractor doubles as a filter on the paper's own
   ablations. This is a strictly finer unit of knowledge than a paper summary.
2. **A cross-paper synthesis layer.** `plugin_a2` produces claims that no single paper makes,
   gated on ≥2 citations with quotes and carrying an explicit confidence label. AutoMind has
   nothing between "paper" and "retrieved paper".
3. **Technique-level second-stage retrieval.** Their second stage re-ranks by label priority —
   still paper-granular. Ours re-embeds each extracted technique and scores it against the
   query, so an on-topic paper's off-topic techniques get dropped.
4. **A working answer to the query problem instead of a detour around it.** The paper reports
   that description-based retrieval "proves ineffective" and switches to labels. We diagnosed
   *why* — a diffuse query plus a strongly anisotropic corpus — and fixed both, taking on-topic
   top-10 hits from 3/10 to 9/10. That is a contribution in its own right, and it is
   orthogonal to their label system rather than competing with it.
5. **Lazy construction.** Extraction is deferred to retrieval time and capped, so adding a
   venue costs nothing until a task actually needs it. AutoMind pays the full offline build.
6. **Measurement infrastructure.** `probe_retrieval.py` validates retrieval in seconds without
   a 12 h run; `grade_local.py` grades offline against the private answers; the paired k8s
   jobs assert programmatically that the two arms differ in exactly one variable.

## What we lack

1. **The Kaggle corpus — this is the gap that matters.** 3,237 solution posts across 455
   competitions is roughly half of what makes their knowledge base work, and we have zero of
   it. Our own audit found that of ~23k indexed papers, the categories covering competition
   craft — boosting, feature engineering, CV strategy, ensembling, hyperparameter search,
   class imbalance, missing data — total **49 papers, 0.2%**. AutoMind's design implicitly
   concedes the same point: they did not expect papers alone to carry it.
2. **Two knowledge types routed to two different actions.** Papers go to *Drafting* (what
   approach to take), tricks go to *Improving* (how to squeeze more out of it). This is a
   sharper design than what I implemented last week — I wired the *same paper techniques* into
   improve. Their split says improve wants **craft**, not novelty. If we add a Kaggle corpus,
   it should go to improve, and papers should stay at draft.
3. **A contamination guard.** They exclude knowledge belonging to the target competition.
   We do not. Less acute for papers than for solution posts, but it is a rigor gap a reviewer
   will ask about — especially since spooky (2017) and jigsaw (2018) are old enough to sit in
   the backbone's pretraining data. AutoMind addresses that separately by adding two
   post-2023 competitions; we have no equivalent control.
4. **Evaluation power.** 15 tasks × 3 runs, reported as best@3 and avg@3 against a win-rate
   aggregate, versus our 3 tasks and a per-task raw metric. Aggregating over tasks is what
   makes their ablation detectable at all — our own power analysis says a per-task AUC
   difference below ~0.005 is unaffordable to detect at 12 h/run.
5. **KDD and EMNLP**, plus a domain journal. KDD in particular is the applied venue most
   likely to contain transferable engineering detail.

## Reading their ablation against ours

Their knowledge base helps: −11.8% win rate when removed. Ours does not: harmful on
OpenADMET and spooky, null on jigsaw (n=3, t = −0.34).

The two systems differ in exactly two ways that could account for this, and both are
addressable:

- **Corpus genre.** Theirs is majority competition craft; ours is entirely research papers,
  of which 0.2% is craft.
- **Injection surface.** They inject at draft *and* improve, with type-appropriate content.
  Until last week we injected at draft only — and did so through a prompt block that labelled
  the techniques as recommended pretrained models.

A third difference is not about knowledge at all and is worth keeping in view: their
self-adaptive coding ablation is *larger* than their knowledge ablation (−13.2% win rate,
−27.6% valid rate). Whatever the knowledge base contributes, code-generation robustness
contributed more in their system.
