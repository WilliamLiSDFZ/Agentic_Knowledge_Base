---
title: "EMC$^2$: Efficient MCMC Negative Sampling for Contrastive Learning with Global Convergence"
source: "https://proceedings.mlr.press/v235/yau24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yau24a/yau24a.pdf"
categories: ['optimization-algorithms-convergence-theory']
tags: ['contrastive-learning', 'MCMC', 'negative-sampling', 'convergence']
venue: "ICML 2024"
tldr: "An efficient MCMC-based negative sampling method with global convergence guarantees is proposed for contrastive learning."
---

# EMC$^2$: Efficient MCMC Negative Sampling for Contrastive Learning with Global Convergence

**Source**: [https://proceedings.mlr.press/v235/yau24a.html](https://proceedings.mlr.press/v235/yau24a.html)

**TLDR**: An efficient MCMC-based negative sampling method with global convergence guarantees is proposed for contrastive learning.

## Abstract

A key challenge in contrastive learning is to generate negative samples from a large sample set to contrast with positive samples, for learning better encoding of the data. These negative samples often follow a softmax distribution which are dynamically updated during the training process. However, sampling from this distribution is non-trivial due to the high computational costs in computing the partition function. In this paper, we propose an $\underline{\text{E}}$fficient $\underline{\text{M}}$arkov $\underline{\text{C}}$hain Monte Carlo negative sampling method for $\underline{\text{C}}$ontrastive learning (EMC$^2$). We follow the global contrastive learning loss as introduced in SogCLR, and propose EMC$^2$ which utilizes an adaptive Metropolis-Hastings subroutine to generate hardness-aware negative samples in an online fashion during the optimization. We prove that EMC$^2$ finds an $\mathcal{O}(1/\sqrt{T})$-stationary point of the global contrastive loss in $T$ iterations. Compared to prior works, EMC$^2$ is the first algorithm that exhibits global convergence (to stationarity) regardless of the choice of batch size while exhibiting low computation and memory cost. Numerical experiments validate that EMC$^2$ is effective with small batch training and achieves comparable or better performance than baseline algorithms. We report the results for pre-training image encoders on STL-10 and Imagenet-100.