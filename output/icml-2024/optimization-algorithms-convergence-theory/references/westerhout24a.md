---
title: "On the Asymptotic Distribution of the Minimum Empirical Risk"
source: "https://proceedings.mlr.press/v235/westerhout24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/westerhout24a/westerhout24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'optimization-algorithms-convergence-theory']
tags: ['empirical-risk-minimization', 'asymptotic-distribution', 'statistical-inference', 'goodness-of-fit']
venue: "ICML 2024"
tldr: "Characterizes the asymptotic distribution of the minimum empirical risk to enable inference and goodness-of-fit testing in ERM frameworks."
---

# On the Asymptotic Distribution of the Minimum Empirical Risk

**Source**: [https://proceedings.mlr.press/v235/westerhout24a.html](https://proceedings.mlr.press/v235/westerhout24a.html)

**TLDR**: Characterizes the asymptotic distribution of the minimum empirical risk to enable inference and goodness-of-fit testing in ERM frameworks.

## Abstract

Empirical risk minimization (ERM) is a foundational framework for the estimation of solutions to statistical and machine learning problems. Characterizing the distributional properties of the minimum empirical risk (MER) provides valuable tools for conducting inference and assessing the goodness of model fit. We provide a comprehensive account of the asymptotic distribution for the order-$\sqrt{n}$ blowup of the MER under generic and abstract assumptions, and present practical conditions under which our theorems hold. Our results improve upon and relax the assumptions made in previous works. Specifically, we provide asymptotic distributions for MERs for non-independent and identically distributed data, and when the loss functions may be discontinuous or indexed by non-Euclidean spaces. We further present results that enable the application of these asymptotics for statistical inference. Specifically, the construction of consistent confidence sets using the bootstrap and consistent hypothesis tests using penalized model selection. We illustrate the utility of our approach by applying our results to neural network problems.