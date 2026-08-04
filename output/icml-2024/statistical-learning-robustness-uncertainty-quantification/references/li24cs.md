---
title: "Algorithmic Stability Unleashed: Generalization Bounds with Unbounded Losses"
source: "https://proceedings.mlr.press/v235/li24cs.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24cs/li24cs.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification']
tags: ['algorithmic-stability', 'generalization-bounds', 'unbounded-losses']
venue: "ICML 2024"
tldr: "New generalization bounds based on algorithmic stability are derived that extend to learning with unbounded loss functions."
---

# Algorithmic Stability Unleashed: Generalization Bounds with Unbounded Losses

**Source**: [https://proceedings.mlr.press/v235/li24cs.html](https://proceedings.mlr.press/v235/li24cs.html)

**TLDR**: New generalization bounds based on algorithmic stability are derived that extend to learning with unbounded loss functions.

## Abstract

One of the central problems of statistical learning theory is quantifying the generalization ability of learning algorithms within a probabilistic framework. Algorithmic stability is a powerful tool for deriving generalization bounds, however, it typically builds on a critical assumption that losses are bounded. In this paper, we relax this condition to unbounded loss functions with subweibull diameter. This gives new generalization bounds for algorithmic stability and also includes existing results of subgaussian and subexponential diameters as specific cases. Furthermore, we provide a refined stability analysis by developing generalization bounds which can be $\sqrt{n}$-times faster than the previous results, where $n$ is the sample size. Our main technical contribution is general concentration inequalities for subweibull random variables, which may be of independent interest.