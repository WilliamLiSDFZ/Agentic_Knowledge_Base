---
title: "Careful with that Scalpel: Improving Gradient Surgery with an EMA"
source: "https://proceedings.mlr.press/v235/hsieh24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hsieh24a/hsieh24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'neural-network-learning-dynamics-theory']
tags: ['gradient-surgery', 'multi-objective', 'ema', 'auxiliary-loss', 'optimization']
venue: "ICML 2024"
tldr: "Improves gradient surgery for multi-objective deep learning by incorporating an exponential moving average to better balance primary and auxiliary objectives."
---

# Careful with that Scalpel: Improving Gradient Surgery with an EMA

**Source**: [https://proceedings.mlr.press/v235/hsieh24a.html](https://proceedings.mlr.press/v235/hsieh24a.html)

**TLDR**: Improves gradient surgery for multi-objective deep learning by incorporating an exponential moving average to better balance primary and auxiliary objectives.

## Abstract

Beyond minimizing a single training loss, many deep learning estimation pipelines rely on an auxiliary objective to quantify and encourage desirable properties of the model (e.g. performance on another dataset, robustness, agreement with a prior). Although the simplest approach to incorporating an auxiliary loss is to sum it with the training loss as a regularizer, recent works have shown that one can improve performance by blending the gradients beyond a simple sum; this is known as gradient surgery. We cast the problem as a constrained minimization problem where the auxiliary objective is minimized among the set of minimizers of the training loss. To solve this bilevel problem, we follow a parameter update direction that combines the training loss gradient and the orthogonal projection of the auxiliary gradient to the training gradient. In a setting where gradients come from mini-batches, we explain how, using a moving average of the training loss gradients, we can carefully maintain this critical orthogonality property. We demonstrate that our method, Bloop, can lead to much better performances on NLP and vision experiments than other gradient surgery methods without EMA.