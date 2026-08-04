---
title: "A Fixed-Point Approach for Causal Generative Modeling"
source: "https://proceedings.mlr.press/v235/scetbon24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/scetbon24a/scetbon24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'generative-models-and-variational-inference']
tags: ['structural-causal-models', 'fixed-point', 'causal-generative-modeling', 'DAG-free', 'topological-ordering']
venue: "ICML 2024"
tldr: "A novel DAG-free formalism for structural causal models as fixed-point problems with weakest known conditions for unique recovery given topological ordering."
---

# A Fixed-Point Approach for Causal Generative Modeling

**Source**: [https://proceedings.mlr.press/v235/scetbon24a.html](https://proceedings.mlr.press/v235/scetbon24a.html)

**TLDR**: A novel DAG-free formalism for structural causal models as fixed-point problems with weakest known conditions for unique recovery given topological ordering.

## Abstract

We propose a novel formalism for describing Structural Causal Models (SCMs) as fixed-point problems on causally ordered variables, eliminating the need for Directed Acyclic Graphs (DAGs), and establish the weakest known conditions for their unique recovery given the topological ordering (TO). Based on this, we design a two-stage causal generative model that first infers in a zero-shot manner a valid TO from observations, and then learns the generative SCM on the ordered variables. To infer TOs, we propose to amortize the learning of TOs on synthetically generated datasets by sequentially predicting the leaves of graphs seen during training. To learn SCMs, we design a transformer-based architecture that exploits a new attention mechanism enabling the modeling of causal structures, and show that this parameterization is consistent with our formalism. Finally, we conduct an extensive evaluation of each method individually, and show that when combined, our model outperforms various baselines on generated out-of-distribution problems.