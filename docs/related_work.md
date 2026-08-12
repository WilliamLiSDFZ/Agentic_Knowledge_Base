# Related work: knowledge bases for ML-engineering agents

Compiled 2026-08-07 while planning a corpus expansion. Grouped by how directly each paper
bears on what this repo does. Claims marked *(abstract/summary only)* were not verified
against the full text.

---

## 1. Direct prior work — must cite and differentiate from

### AutoMind: Adaptive Knowledgeable Agent for Automated Data Science
arXiv [2506.10974](https://arxiv.org/abs/2506.10974) (v3, Oct 2025) · code:
[innovatingAI/AutoMind](https://github.com/innovatingAI/AutoMind)

**The closest existing system to ours, and the most important finding of this survey.**

Its expert knowledge base has *two* source types:

| source | volume | retrieval method |
|---|---|---|
| Kaggle competition solutions | 3,237 posts from 455 competitions | LLM pre-tags each post into 11 top-level categories with sub-categories; the LLM then picks categories at query time |
| Top conference papers | ICLR, NeurIPS, KDD, ICML, EMNLP, last 3 years | LLM writes a per-paper summary structured as Data / Task / Approach / Contribution |

**Numbers below are now read from the PDF (v3). The figures previously recorded here came
from a secondary source and were wrong — see `comparison_automind.md`.** Ablating the
knowledge base costs **11.8% win rate and 5.6% valid rate** (Medium split, DeepSeek-V3).
AutoMind surpasses **38.7% (o3-mini) / 41.2% (DeepSeek-V3)** of human participants avg@3,
i.e. +11.0% / +5.2% over AIDE — not the "61.0%" a search summary reported. It reaches
AIDE's 24 h performance in 15 h (−9.6% tokens).

**Why this matters to us.** Our corpus is papers-only. AutoMind's is majority Kaggle
solutions, and it works. This converges with our own corpus analysis (below): the craft that
wins competitions is essentially absent from conference proceedings.

Two mechanisms worth stealing regardless of corpus:
- **Source-specific retrieval.** They do not embed everything into one index. Solutions get
  categorical tagging; papers get a structured summary. We currently treat all papers
  identically.
- **Structured per-paper summaries** (Data / Task / Approach / Contribution) rather than raw
  abstract text. This is close to what `plugin_a_methodology` extracts, but applied at index
  time to *every* paper, which makes the embedding space far less anisotropic.

### AssistedDS: Benchmarking How External Domain Knowledge Assists LLMs in Automated Data Science
arXiv [2506.13992](https://arxiv.org/abs/2506.13992) · EMNLP 2025 Findings ·
[ACL Anthology](https://aclanthology.org/2025.findings-emnlp.979/)

**The explanation for our negative results.** Builds tabular tasks (synthetic + real Kaggle)
each paired with curated bundles of *helpful* and *adversarial* documents, then measures
whether LLMs can tell them apart. Three findings, all directly relevant:

1. LLMs **uncritically adopt** provided information; adversarial content significantly
   impairs predictive performance.
2. **Helpful guidance does not counteract** the damage from adversarial content — it is not
   a wash, the harm dominates.
3. On Kaggle data specifically, LLMs mishandle time series, apply feature engineering
   inconsistently across folds, and misread categorical variables.

Finding (2) is the key one for us. Our OpenADMET and spooky runs injected papers that were
*topically plausible but operationally useless*; under this framework that behaves like mild
adversarial content, and the presence of a few genuinely useful papers would not rescue it.
This reframes our negative results from "the KB didn't help" to "retrieval precision is a
safety property, not just a quality knob."

### MLE-STAR: Machine Learning Engineering Agent via Search and Targeted Refinement
[OpenReview](https://openreview.net/forum?id=vS1M06Px6u) (Google) · arXiv
[2506.15692](https://arxiv.org/pdf/2506.15692)

Retrieves effective models via a **web search engine at run time** instead of a curated
offline KB, forms an initial solution, then refines targeted pipeline components. Reports
medals in 64% of MLE-bench competitions. *(abstract only.)*

The interesting contrast: live search sidesteps corpus curation entirely and gets fresher,
more practical hits (model cards, blog posts, docs) than a conference-paper index can. If a
curated KB is to beat this, the argument has to be about *what* is curated, not that
curation per se helps.

---

## 2. Skill / experience accumulation — the `experience_kb` direction

Relevant to the still-unused `plugin_b`/`plugin_c` half of this repo.

- **Why Solve It Twice? Hierarchical Accumulation of Skills for Transfer-Efficient ML
  Engineering** — arXiv [2606.30911](https://arxiv.org/abs/2606.30911). Directly on
  cross-task skill transfer in ML engineering. *(PDF had no extractable text; needs a manual
  read.)*
- **SkillX: Automatically Constructing Skill Knowledge Bases for Agents** — arXiv
  [2604.04804](https://arxiv.org/html/2604.04804).
- **Towards Persistent Case-Based Memory for Autonomous Data Science: A CBR-Augmented
  R&D-Agent** — arXiv [2606.05250](https://arxiv.org/abs/2606.05250). Case-based reasoning
  framing of run-to-run memory; close to what `plugin_b` does with training logs.
- Also in this cluster: SkillBrew ([2605.29440](https://arxiv.org/pdf/2605.29440)),
  SkillPyramid ([2606.03692](https://arxiv.org/pdf/2606.03692)), SkillOps
  ([2605.13716](https://arxiv.org/html/2605.13716v1)), MUSE-Autoskill
  ([2605.27366](https://arxiv.org/html/2605.27366v1)). The common lineage is Voyager's
  executable skill library; the common problem they name is that each task is otherwise an
  isolated episode with no mechanism for transferable knowledge.

---

## 3. Paper → code — the `methodology_kb` extraction direction

- **PaperCoder / Paper2Code: Automating Code Generation from Scientific Papers in ML** —
  arXiv [2504.17192](https://arxiv.org/pdf/2504.17192) ·
  [OpenReview](https://openreview.net/forum?id=3DcaUTjdKc). Three stages: planning →
  analysis → generation.
- **ResearchCodeAgent: Automated Codification of Research Methodologies** — arXiv
  [2504.20117](https://arxiv.org/html/2504.20117). Two phases: context understanding, then
  iterative code generation and execution.

Both go further than we do: from paper to *runnable code*, not to a prose technique
description. Worth reading for the extraction prompt design in `plugin_a_methodology`.

---

## 4. Practitioner evidence that writeups are the useful corpus

- **NVIDIA Kaggle plugin** — [NVIDIA/nvidia-kaggle](https://github.com/NVIDIA/nvidia-kaggle).
  A single agent skill whose workflow explicitly includes *studying public writeups and
  notebooks*, reproducing kernels locally, and submitting. Used in an agent-assisted first
  place on a Kaggle Playground competition (telecom churn, March 2026): ~600k lines of code,
  850 experiments, a four-level stack of 150 models
  ([NVIDIA blog](https://developer.nvidia.com/blog/winning-a-kaggle-competition-with-generative-ai-assisted-coding/)).

Independent confirmation that the operative knowledge for competitions lives in writeups and
notebooks, not in proceedings.

---

## What this implies for the corpus expansion

Our own corpus analysis found that of ~23k indexed papers, categories covering the craft
that actually wins competitions — gradient boosting, feature engineering, cross-validation
strategy, ensembling, hyperparameter search, class imbalance, missing data — amount to
**49 papers, 0.2%**. Meanwhile theory/optimisation is 21% and LLM research 19%.

Ranked by expected value:

1. **Kaggle competition writeups and discussion posts.** This is what AutoMind has and we do
   not, and it is the only source in this survey that is the right *genre*. Obtainable via
   the Kaggle API (competitions → discussions/notebooks), which is already authenticated on
   the dev pod for `mlebench prepare`.
2. **KDD** (and possibly EMNLP). AutoMind includes KDD; we do not. Of the venues in reach it
   is the most applied, so the most likely to contain transferable engineering detail.
   Adding another 5k NeurIPS-style papers is the lowest-value option available.
3. **`experience_kb`.** Already built by `plugin_b` from our own run logs, correct genre by
   construction, and never once included in an A/B arm.
4. Restructure the index around **per-paper structured summaries** (AutoMind's Data / Task /
   Approach / Contribution) rather than raw abstracts. Independent of which corpus we add,
   this should improve the embedding geometry that forced us to mean-centre in the first
   place.
