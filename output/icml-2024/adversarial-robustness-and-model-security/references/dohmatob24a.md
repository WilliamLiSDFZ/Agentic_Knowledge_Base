---
title: "Consistent Adversarially Robust Linear Classification: Non-Parametric Setting"
source: "https://proceedings.mlr.press/v235/dohmatob24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dohmatob24a/dohmatob24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['adversarial-robustness', 'linear-classification', 'non-parametric', 'consistent-estimation', 'minimax']
venue: "ICML 2024"
tldr: "Establishes consistent adversarially robust linear classifiers in the non-parametric setting with minimax-optimal excess adversarial risk bounds."
---

# Consistent Adversarially Robust Linear Classification: Non-Parametric Setting

**Source**: [https://proceedings.mlr.press/v235/dohmatob24a.html](https://proceedings.mlr.press/v235/dohmatob24a.html)

**TLDR**: Establishes consistent adversarially robust linear classifiers in the non-parametric setting with minimax-optimal excess adversarial risk bounds.

## Abstract

For binary classification in $d$ dimensions, it is known that with a sample size of $n$, an excess adversarial risk of $O(d/n)$ is achievable under strong parametric assumptions about the underlying data distribution (e.g., assuming a Gaussian mixture model). In the case of well-separated distributions, this rate can be further refined to $O(1/n)$. Our work studies the non-parametric setting, where very little is known. With only mild regularity conditions on the conditional distribution of the features, we examine adversarial attacks with respect to arbitrary norms and introduce a straightforward yet effective estimator with provable consistency w.r.t adversarial risk. Our estimator is given by minimizing a series of smoothed versions of the robust 0/1 loss, with a smoothing bandwidth that adapts to both $n$ and $d$. Furthermore, we demonstrate that our estimator can achieve the minimax excess adversarial risk of $\widetilde O(\sqrt{d/n})$ for linear classifiers, at the cost of solving possibly rougher optimization problems.