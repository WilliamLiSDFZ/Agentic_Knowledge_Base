---
title: "Differentiable Annealed Importance Sampling Minimizes The Jensen-Shannon Divergence Between Initial and Target Distribution"
source: "https://proceedings.mlr.press/v235/zenn24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zenn24a/zenn24a.pdf"
categories: ['generative-models-and-variational-inference', 'optimization-algorithms-convergence-theory']
tags: ['annealed-importance-sampling', 'variational-inference', 'Jensen-Shannon-divergence']
venue: "ICML 2024"
tldr: "Differentiable annealed importance sampling is shown to minimize the Jensen-Shannon divergence between initial and target distributions in the limit of many transitions."
---

# Differentiable Annealed Importance Sampling Minimizes The Jensen-Shannon Divergence Between Initial and Target Distribution

**Source**: [https://proceedings.mlr.press/v235/zenn24a.html](https://proceedings.mlr.press/v235/zenn24a.html)

**TLDR**: Differentiable annealed importance sampling is shown to minimize the Jensen-Shannon divergence between initial and target distributions in the limit of many transitions.

## Abstract

Differentiable annealed importance sampling (DAIS), proposed by Geffner & Domke (2021) and Zhang et al. (2021), allows optimizing, among others, over the initial distribution of AIS. In this paper, we show that, in the limit of many transitions, DAIS minimizes the symmetrized KL divergence (Jensen-Shannon divergence) between the initial and target distribution. Thus, DAIS can be seen as a form of variational inference (VI) in that its initial distribution is a parametric fit to an intractable target distribution. We empirically evaluate the usefulness of the initial distribution as a variational distribution on synthetic and real-world data, observing that it often provides more accurate uncertainty estimates than standard VI (optimizing the reverse KL divergence), importance weighted VI, and Markovian score climbing (optimizing the forward KL divergence).