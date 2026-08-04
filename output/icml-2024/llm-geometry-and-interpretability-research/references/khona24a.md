---
title: "Towards an Understanding of Stepwise Inference in Transformers: A Synthetic Graph Navigation Model"
source: "https://proceedings.mlr.press/v235/khona24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/khona24a/khona24a.pdf"
categories: ['llm-geometry-and-interpretability-research', 'anomaly-and-out-of-distribution-detection']
tags: ['chain-of-thought', 'stepwise-inference', 'graph-navigation']
venue: "ICML 2024"
tldr: "Studies the mechanisms of stepwise transformer inference using a synthetic graph navigation task to understand scratchpad and chain-of-thought reasoning."
---

# Towards an Understanding of Stepwise Inference in Transformers: A Synthetic Graph Navigation Model

**Source**: [https://proceedings.mlr.press/v235/khona24a.html](https://proceedings.mlr.press/v235/khona24a.html)

**TLDR**: Studies the mechanisms of stepwise transformer inference using a synthetic graph navigation task to understand scratchpad and chain-of-thought reasoning.

## Abstract

Stepwise inference protocols, such as scratchpads and chain-of-thought, help language models solve complex problems by decomposing them into a sequence of simpler subproblems. To unravel the underlying mechanisms of stepwise inference we propose to study autoregressive Transformer models on a synthetic task that embodies the multi-step nature of problems where stepwise inference is generally most useful. Specifically, we define a graph navigation problem wherein a model is tasked with traversing a path from a start to a goal node on the graph. We find we can empirically reproduce and analyze several phenomena observed at scale: (i) the stepwise inference reasoning gap, the cause of which we find in the structure of the training data; (ii) a diversity-accuracy trade-off in model generations as sampling temperature varies; (iii) a simplicity bias in the model’s output; and (iv) compositional generalization and a primacy bias with in-context exemplars. Overall, our work introduces a grounded, synthetic framework for studying stepwise inference and offers mechanistic hypotheses that can lay the foundation for a deeper understanding of this phenomenon.