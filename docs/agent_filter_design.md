# Design: agent-based paper filtering, and the task change

Status: **Parts A, B and C implemented 2026-08-26.** Part D (task change) not started.
Written in response to Peijia's review of the two-stage retrieval.

Implemented:
- `config/config.yaml` — `agent_paper_filter`, `filter_min_keep`, `filter_max_keep`,
  `filter_batch_size`; `retr_token_budget` 6000 -> 25000; `improve_token_budget` 2000 -> 12000;
  `lazy_tech_top_n` 12 -> 0
- `engine/coldstart/ondemand.py` — `_describe_data`, `_agent_filter_papers`, `_write_filter_log`,
  wired into `build_lazy_guidance` before extraction; when the filter runs, all survivors'
  techniques are injected whole
- the previous embedding-only path stays reachable with `agent_paper_filter: False`

---

## 1. What the review said, and why it is right

> 你第一层筛出来的 40 篇论文，确实没有漏掉相关的，但里面有一些噪音：
> 1. 有些论文只是字面上相关，实际上方法并不相关
> 2. 有些方法虽然相关，但是不可用（比如它做了一些额外的假设，但在我们这个 task 里面并不存在）
>
> 所以你可以把第二阶段改一下，用一个 agent 来处理：
> 1. 先用一个 agent 筛一遍，把没用的和不可用的 paper 全部筛掉。直接看标题和摘要就可以筛。
> 2. 剩下的全部转换成一条条 technique，这里就不要再做筛选了，全部拼到 prompt 里面喂给它。

Two independent lines of evidence from our own data agree:

**Adoption measurement** (`results/8.20/adoption.csv`, 4,488 judgements). Whether the agent uses
the knowledge at all is almost entirely task-determined:

| task | nodes adopting ≥1 technique | full | proxy |
|---|---:|---:|---:|
| jigsaw | **3 / 89 (3%)** | 0 | 3 |
| essay | 92 / 105 (88%) | **1** | 114 |
| lmsys | 178 / 180 (99%) | 209 | 141 |

**What jigsaw was actually handed:**

```
Fine-tuned CLIP multimodal encoder      Image captions for targeted-harmful memes
Multimodal image-text modeling          Inline-text captions for dispirited-culture memes
Demographic-context features            Cross-task label feature
```

Half of them are multimodal meme-detection methods. jigsaw is text-only comment classification —
there are no images. Retrieval matched correctly on *toxicity* and returned methods the
competition cannot execute. This is exactly the review's category (2), and it explains the 3%
adoption: the agent is not ignoring the knowledge, it cannot use it.

**The mechanism the current design cannot fix.** Second-stage filtering is embedding similarity
(`_rerank_techniques`). "Multimodal toxicity detection" and "text toxicity classification" are
*near each other* in embedding space — that is what a good embedding does. Cosine similarity has
no way to represent "this method requires a modality the dataset does not contain". Only a reader
can. That is the whole argument for replacing this stage with an LLM.

Note also that every extracted technique already carries a `**Condition**` field stating its
preconditions ("When generating Spanish therapy transcripts…", "…input includes both the original
essay and annotated component/relation information"). It has been decorative since the pipeline
was written. The proposal finally makes something read it.

---

## 2. Current pipeline, for reference

```
task description
  → _build_query                      LLM distils to a 50-80 word ML task statement (cached)
  → retr.search(top_k=lazy_pool=40)   STAGE 1: abstract-level, mean-centred embeddings
  → filter lazy_min_score=0.05        relative threshold, recall-oriented, barely filters
  → _split_cached / _extract_one      deep-extract ≤ max_extractions_per_coldstart=20 PDFs   ← expensive
  → _split_techniques                 split extracted files into individual techniques
  → _rerank_techniques                STAGE 2: technique-level embedding similarity
        · lazy_tech_min_score=0.3     relative threshold
        · dedup by title
        · truncate to lazy_tech_top_n=12
  → _assemble_techniques              cap at retr_token_budget=6000 tokens → 24,000 chars
  → (improve stage) trim_methodology_text   cap at improve_token_budget=2000 → 8,000 chars
```

Stage 1 is endorsed by the review and is not changing. Everything from `_rerank_techniques`
onward is.

---

## 3. Part A — agent filter over papers, before extraction

### Placement

New step between the stage-1 hit list and extraction, in `build_lazy_guidance`:

```
  retr.search(top_k=40) → candidates
+ → _agent_filter_papers(candidates, task_desc, cfg)   ← NEW: LLM reads title + abstract
  → _split_cached / _extract_one    (now only over survivors)
```

Placing it **before** extraction is what makes it cheap rather than merely different: today we
pay one full-PDF extraction call per paper for up to 20 papers, then discard most of the
resulting techniques. Filtering on abstracts costs **one** call for all 40 and removes papers
before they are ever downloaded.

### What the agent is asked

One call, all 40 candidates, structured output. Draft prompt:

```
You are selecting research papers whose METHODS could actually be applied to a specific
machine-learning competition.

COMPETITION
{distilled task statement}          # the same cached 50-80 word summary stage 1 uses

AVAILABLE DATA
{data description}                  # NEW — see below

PAPERS
[1] {title}
    {abstract, truncated to ~1200 chars}
[2] ...

For each paper decide:
  "keep"       — its method could be applied to this competition with the data described above
  "irrelevant" — the topic only overlaps superficially; the method is about something else
  "infeasible" — the method is relevant but assumes something this competition does not have
                 (another modality, extra annotations, a different label structure, an external
                 corpus, human-in-the-loop, orders of magnitude more compute)

Be strict on "infeasible". A method that needs images, human annotations, or labels the
competition does not provide is infeasible no matter how well the topic matches.

Return ONLY JSON:
[{"i": 1, "decision": "keep|irrelevant|infeasible", "why": "<=15 words"}]
```

**The `AVAILABLE DATA` block is the part that makes "infeasible" decidable** and it does not exist
today. Without knowing that jigsaw is text-only with six binary labels, the model cannot rule out
a CLIP method. Source it from the competition description plus a directory listing of
`data_dir` — file names and extensions are usually enough to establish modality.

### Config

```yaml
agent_paper_filter: True        # False restores the current embedding-only path
filter_min_keep: 5              # floor — see failure modes
filter_max_keep: 15             # ceiling, enforced after the agent, by stage-1 score order
```

### Failure modes and guards

| failure | guard |
|---|---|
| agent keeps nothing → empty injection, KB arm becomes an expensive baseline | if `keep < filter_min_keep`, take the top `filter_min_keep` by stage-1 score and log loudly |
| agent keeps everything → no filtering, prompt explodes | cap at `filter_max_keep` by stage-1 score |
| API failure | fall back to the current behaviour (no filter), log it — never fail the run |
| unparseable JSON | same as API failure |

Every decision — kept, dropped, and why — must be written to `logs/paper_filter.md` next to
`injected_knowledge.md`. Without it, "the agent filtered badly" is unfalsifiable, and this project
has already been burned once by a diagnostic that recorded nothing (see the `\b429\b` and
`best_solution.py` entries in `UPDATELOG.md`).

### Cost

One extra call per cold start: 40 abstracts × ~1,200 chars ≈ 12k tokens in, ~1k out. Against a
saving of up to 20 full-PDF extraction calls, this is **net cheaper**.

---

## 4. Part B — drop the second-stage technique filter

`_rerank_techniques` and its two thresholds (`lazy_tech_min_score`, `lazy_tech_top_n`) become
unused when `agent_paper_filter` is on. Per the review, survivors' techniques are injected whole.

Keep the code and the config keys, gated on the switch, so the old path remains runnable for
comparison. Do not delete: the two-stage design is what the current results were produced with,
and the ability to re-run it is what makes the change measurable.

What is **not** discarded: mean-centring and query distillation are stage-1 properties and both
remain. They are the two retrieval fixes with measured effect (top-10 on-topic 3 → 9).

---

## 5. Part C — the truncation

> 你在做 draft 和 improve 的时候好像有时会被截断，尽量不要让它截断。你可以衡量一下平均长度，应该也就几万个字符，其实完全能接受

Three separate caps do the truncating:

| parameter | current | effective cap |
|---|---:|---|
| `retr_token_budget` | 6000 | 24,000 chars at draft |
| `improve_token_budget` | 2000 | **8,000 chars at improve** |
| `lazy_tech_top_n` | 12 | 12 techniques, regardless of budget |

**Measured from the 223 extracted papers in `methodology_kb/`:** mean **9.9** `[POSITIVE]`
techniques per paper, mean **611 chars** per technique. So "inject everything the agent kept":

| papers kept | techniques | chars | tokens |
|---:|---:|---:|---:|
| 10 | ~99 | ~61k | ~15k |
| 15 | ~149 | ~91k | ~23k |
| 20 | ~199 | ~121k | ~30k |
| 40 | ~397 | ~243k | ~61k |

The review's "几万个字符" is right for ~10 kept papers and **roughly 2× low at 20**. This is why
`filter_max_keep` exists: the prompt size is set by the agent's strictness, and that needs a
ceiling that does not depend on the agent behaving.

Proposed:

```yaml
retr_token_budget: 25000        # 6000  -> ~100k chars, covers ~15 papers
improve_token_budget: 12000     # 2000  -> ~48k chars; improve was by far the tightest
lazy_tech_top_n: 0              # 0 = no limit (only meaningful on the old path)
```

Two things to check rather than assume:

- **Context window.** 25k tokens of techniques plus the task description, the code, and the rest
  of the draft prompt. Confirm against the model's limit before running, not after.
- **Long-context degradation.** More context is not monotonically better; there is a real
  possibility that 100k chars of techniques dilutes attention relative to 24k of the *right*
  ones. This is a reason to keep the old path runnable (Part B) rather than a reason not to try.

---

## 6. Part D — the task change

> 那个 task 的规模现在比较小，你可以找一下有没有哪个 task 的 dataset 是在 10GB 左右的
> 我看你之前跑的那个最像文本分类的 task，基本上每次 retrieve 出来可能就只有一两篇文章是有用的

The second sentence is jigsaw, and it agrees with the 3% adoption number. Candidates, from the
MLE-bench appendix:

| competition | train samples | modality | split | corpus we already have? |
|---|---:|---|---|---|
| **jigsaw-unintended-bias-in-toxicity-classification** | **1.8M** | text | Medium | **yes** — ACL/NAACL |
| tensorflow2-question-answering | 307K | text | — | yes |
| histopathologic-cancer-detection | 220K | image | **Low (Lite)** | **no** — needs CVPR/ICCV |
| iwildcam-2020-fgvc7 | 218K | image | — | no |
| inaturalist-2019-fgvc6 | 265K | image | — | no |
| herbarium-2022-fgvc9 | 840K | image | — | no |
| alaska2-image-steganalysis | 75K | image | — | no |

### The tension

The tasks that are large **in gigabytes** are vision tasks. Our corpus is
aaai/acl/icml/naacl/neurips 2024 only — **CVPR and ICCV have never been built**, despite the
pipeline supporting them. Moving to a vision task without first building them means retrieving
NLP papers for an image competition, which would guarantee the failure we are trying to fix.

### Recommendation: `jigsaw-unintended-bias-in-toxicity-classification` first

- **11× the samples of jigsaw-toxic** (1.8M vs 159K) — a real answer to "the task is too small"
- **Same domain**, so the existing NLP corpus is already the right corpus and no new venue build
  is required
- **Directly comparable** to our strongest existing task, which makes the agent-filter change
  measurable rather than confounded with a domain change
- Medium complexity, so it is a step up without being a different kind of problem

Then, if a genuinely large-in-GB task is wanted, **build CVPR + ICCV first** and go to
`histopathologic-cancer-detection` (in the Lite split, 220K images, ~7 GB). Building two more
venues is a day of pipeline time and adds ~10k papers to the index; it is not free but it is not
the bottleneck either.

### What the task change costs

Every existing result is on jigsaw / essay / lmsys. A new task starts at n=0 draws and is not
poolable with them. Do the code change first on an existing task so its effect is measurable
against a known baseline, and add the new task second. Doing both at once produces a number that
cannot be attributed to either.

---

## 7. Order of work

| # | change | cost | why this order |
|---|---|---|---|
| 1 | Part C — relax truncation | minutes | independent, near-zero risk, and the current `improve` cap of 8k chars is indefensible on its own |
| 2 | Part A + B — agent filter | ~1 day | the main change; measurable on jigsaw where we know adoption is 3% |
| 3 | re-run jigsaw A/B/C | 36 GPU-h | jigsaw is the diagnostic: if adoption does not move from 3%, the filter did not work |
| 4 | re-measure adoption | 0 GPU | `measure_adoption.py` on the new runs — this is the primary metric for whether the change worked |
| 5 | Part D — add jigsaw-unintended-bias | 36 GPU-h + data | only after 3–4 show the filter helps |
| 6 | build CVPR/ICCV, consider a vision task | ~1 day + storage | last, and only if a GB-scale task is still wanted |

**The success criterion for steps 2–4 is adoption, not score.** jigsaw adoption is 3% today; if
the filter works it should rise substantially, and that is measurable at n=1 draw with no
statistics. Score would need 8+ draws to say anything, and we already know essay and lmsys need
hundreds.

---

## 8. Open questions to settle before implementing

1. **Where does `AVAILABLE DATA` come from?** Competition description alone, or description plus
   a listing of `data_dir`? The listing is more reliable for modality but adds a filesystem
   dependency to a function that currently only needs the description.
2. **Is one call for 40 papers reliable enough?** A single 12k-token call producing 40 structured
   decisions may degrade toward the end of the list. Batching in groups of 10 costs 4 calls and is
   probably safer — worth testing both on jigsaw, where we know the right answer (the multimodal
   papers must be dropped).
3. **Should `infeasible` and `irrelevant` be distinguished in the output?** They are different
   failures of the retriever and separating them tells us which stage to fix next. Cheap to keep.
4. **Does injecting ~100 techniques actually help?** Untested. The alternative reading of the
   adoption data is that the agent adopts 1–2 techniques regardless of how many it is offered, in
   which case the gain comes entirely from the filter and the volume is neutral-to-harmful.
   Keeping the old path runnable lets this be answered rather than assumed.
