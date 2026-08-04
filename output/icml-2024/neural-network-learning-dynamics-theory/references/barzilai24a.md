---
title: "Generalization in Kernel Regression Under Realistic Assumptions"
source: "https://proceedings.mlr.press/v235/barzilai24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/barzilai24a/barzilai24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'neural-network-learning-dynamics-theory']
tags: ['kernel-regression', 'generalization', 'bias-variance', 'overparameterization', 'benign-overfitting']
venue: "ICML 2024"
tldr: "Provides a rigorous analysis of generalization in kernel regression under realistic assumptions, revisiting the bias-variance tradeoff in overparameterized settings."
---

# Generalization in Kernel Regression Under Realistic Assumptions

**Source**: [https://proceedings.mlr.press/v235/barzilai24a.html](https://proceedings.mlr.press/v235/barzilai24a.html)

**TLDR**: Provides a rigorous analysis of generalization in kernel regression under realistic assumptions, revisiting the bias-variance tradeoff in overparameterized settings.

## Abstract

It is by now well-established that modern over-parameterized models seem to elude the bias-variance tradeoff and generalize well despite overfitting noise. Many recent works attempt to analyze this phenomenon in the relatively tractable setting of kernel regression. However, as we argue in detail, most past works on this topic either make unrealistic assumptions, or focus on a narrow problem setup. This work aims to provide a unified theory to upper bound the excess risk of kernel regression for nearly all common and realistic settings. When applied to common kernels, our results imply benign overfitting in high input dimensions, nearly tempered overfitting in fixed dimensions, and explicit convergence rates for regularized regression. As a by-product, we obtain time-dependent bounds for neural networks trained in the kernel regime. Our results rely on new relative perturbation bounds for the eigenvalues of kernel matrices, which may be of independent interest. These reveal a self-regularization phenomenon, whereby a heavy tail in the eigendecomposition of the kernel implicitly leads to good generalization.