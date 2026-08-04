---
title: "Robust Sparse Estimation for Gaussians with Optimal Error under Huber Contamination"
source: "https://proceedings.mlr.press/v235/diakonikolas24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/diakonikolas24a/diakonikolas24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'learning-with-imperfect-data-and-bias']
tags: ['robust-estimation', 'sparse-estimation', 'Huber-contamination', 'Gaussian', 'optimal-error']
venue: "ICML 2024"
tldr: "Provides the first sample- and computationally efficient robust estimators with optimal error for Gaussian sparse mean estimation, PCA, and regression under Huber contamination."
---

# Robust Sparse Estimation for Gaussians with Optimal Error under Huber Contamination

**Source**: [https://proceedings.mlr.press/v235/diakonikolas24a.html](https://proceedings.mlr.press/v235/diakonikolas24a.html)

**TLDR**: Provides the first sample- and computationally efficient robust estimators with optimal error for Gaussian sparse mean estimation, PCA, and regression under Huber contamination.

## Abstract

We study Gaussian sparse estimation tasks in Huber’s contamination model with a focus on mean estimation, PCA, and linear regression. For each of these tasks, we give the first sample and computationally efficient robust estimators with optimal error guarantees, within constant factors. All prior efficient algorithms for these tasks incur quantitatively suboptimal error. Concretely, for Gaussian robust $k$-sparse mean estimation on $\mathbb{R}^d$ with corruption rate $\epsilon>0$, our algorithm has sample complexity $(k^2/\epsilon ^2)\mathrm{polylog}(d/\epsilon)$, runs in sample polynomial time, and approximates the target mean within $\ell_2$-error $O(\epsilon)$. Previous efficient algorithms inherently incur error $\Omega(\epsilon \sqrt{\log(1/\epsilon)})$. At the technical level, we develop a novel multidimensional filtering method in the sparse regime that may find other applications.