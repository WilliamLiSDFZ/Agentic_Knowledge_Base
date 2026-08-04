---
title: "Kernel Debiased Plug-in Estimation: Simultaneous, Automated Debiasing without Influence Functions for Many Target Parameters"
source: "https://proceedings.mlr.press/v235/cho24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cho24c/cho24c.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'causal-inference-and-discovery-methods']
tags: ['plug-in-estimation', 'debiasing', 'nonparametric-estimation']
venue: "ICML 2024"
tldr: "A kernel-based debiased plug-in estimation method that simultaneously and automatically debiases many target parameters without requiring influence functions."
---

# Kernel Debiased Plug-in Estimation: Simultaneous, Automated Debiasing without Influence Functions for Many Target Parameters

**Source**: [https://proceedings.mlr.press/v235/cho24c.html](https://proceedings.mlr.press/v235/cho24c.html)

**TLDR**: A kernel-based debiased plug-in estimation method that simultaneously and automatically debiases many target parameters without requiring influence functions.

## Abstract

When estimating target parameters in nonparametric models with nuisance parameters, substituting the unknown nuisances with nonparametric estimators can introduce "plug-in bias." Traditional methods addressing this suboptimal bias-variance trade-off rely on the influence function (IF) of the target parameter. When estimating multiple target parameters, these methods require debiasing the nuisance parameter multiple times using the corresponding IFs, which poses analytical and computational challenges. In this work, we leverage the targeted maximum likelihood estimation (TMLE) framework to propose a novel method named kernel debiased plug-in estimation (KDPE). KDPE refines an initial estimate through regularized likelihood maximization steps, employing a nonparametric model based on reproducing kernel Hilbert spaces. We show that KDPE: (i) simultaneously debiases all pathwise differentiable target parameters that satisfy our regularity conditions, (ii) does not require the IF for implementation, and (iii) remains computationally tractable. We numerically illustrate the use of KDPE and validate our theoretical results.