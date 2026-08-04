---
title: "$\mathttVITS$ : Variational Inference Thompson Sampling for contextual bandits"
source: "https://proceedings.mlr.press/v235/clavier24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/clavier24a/clavier24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['thompson-sampling', 'contextual-bandits', 'variational-inference']
venue: "ICML 2024"
tldr: "Introduces VITS, a variant of Thompson sampling for contextual bandits that uses variational inference to approximate intractable posterior distributions."
---

# $\mathttVITS$ : Variational Inference Thompson Sampling for contextual bandits

**Source**: [https://proceedings.mlr.press/v235/clavier24a.html](https://proceedings.mlr.press/v235/clavier24a.html)

**TLDR**: Introduces VITS, a variant of Thompson sampling for contextual bandits that uses variational inference to approximate intractable posterior distributions.

## Abstract

In this paper, we introduce and analyze a variant of the Thompson sampling (TS) algorithm for contextual bandits. At each round, traditional TS requires samples from the current posterior distribution, which is usually intractable. To circumvent this issue, approximate inference techniques can be used and provide samples with distribution close to the posteriors. However, current approximate techniques yield to either poor estimation (Laplace approximation) or can be computationally expensive (MCMC methods, Ensemble sampling...). In this paper, we propose a new algorithm, Varational Inference TS $\mathtt{VITS}$, based on Gaussian Variational Inference. This scheme provides powerful posterior approximations which are easy to sample from, and is computationally efficient, making it an ideal choice for TS. In addition, we show that $\mathtt{VITS}$ achieves a sub-linear regret bound of the same order in the dimension and number of round as traditional TS for linear contextual bandit. Finally, we demonstrate experimentally the effectiveness of $\mathtt{VITS}$ on both synthetic and real world datasets