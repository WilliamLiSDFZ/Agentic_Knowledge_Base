---
title: "Generalization Analysis of Deep Non-linear Matrix Completion"
source: "https://proceedings.mlr.press/v235/ledent24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ledent24a/ledent24a.pdf"
categories: ['matrix-geometry-optimization-for-spectral-learning', 'neural-network-learning-dynamics-theory']
tags: ['matrix-completion', 'deep-matrix-factorization', 'generalization-bounds', 'Schatten-norm']
venue: "ICML 2024"
tldr: "Provides generalization bounds for deep non-linear matrix completion via Schatten quasi-norm constraints, showing sample complexity scales as O(rn)."
---

# Generalization Analysis of Deep Non-linear Matrix Completion

**Source**: [https://proceedings.mlr.press/v235/ledent24a.html](https://proceedings.mlr.press/v235/ledent24a.html)

**TLDR**: Provides generalization bounds for deep non-linear matrix completion via Schatten quasi-norm constraints, showing sample complexity scales as O(rn).

## Abstract

We provide generalization bounds for matrix completion with Schatten $p$ quasi-norm constraints, which is equivalent to deep matrix factorization with Frobenius constraints. In the uniform sampling regime, the sample complexity scales like $\widetilde{O}\left( rn\right)$ where $n$ is the size of the matrix and $r$ is a constraint of the same order as the ground truth rank in the isotropic case. In the distribution-free setting, the bounds scale as $\widetilde{O}\left(r^{1-\frac{p}{2}}n^{1+\frac{p}{2}}\right)$, which reduces to the familiar $\sqrt{r}n^{\frac{3}{2}}$ for $p=1$. Furthermore, we provide an analogue of the weighted trace norm for this setting which brings the sample complexity down to $\widetilde{O}(nr)$ in all cases. We then present a non-linear model, Functionally Rescaled Matrix Completion (FRMC) which applies a single trainable function from $\mathbb{R}\rightarrow \mathbb{R}$ to each entry of a latent matrix, and prove that this adds only negligible terms of the overall sample complexity, whilst experiments demonstrate that this simple model improvement already leads to significant gains on real data. We also provide extensions of our results to various neural architectures, thereby providing the first comprehensive uniform convergence PAC analysis of neural network matrix completion.