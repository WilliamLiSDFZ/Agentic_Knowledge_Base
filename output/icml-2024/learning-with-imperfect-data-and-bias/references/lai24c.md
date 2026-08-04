---
title: "Invariant Risk Minimization Is A Total Variation Model"
source: "https://proceedings.mlr.press/v235/lai24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lai24c/lai24c.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'causal-inference-and-discovery-methods']
tags: ['invariant-risk-minimization', 'total-variation', 'domain-generalization', 'mathematical-analysis']
venue: "ICML 2024"
tldr: "A mathematical analysis showing that invariant risk minimization is equivalent to a total variation model, clarifying its inductive bias."
---

# Invariant Risk Minimization Is A Total Variation Model

**Source**: [https://proceedings.mlr.press/v235/lai24c.html](https://proceedings.mlr.press/v235/lai24c.html)

**TLDR**: A mathematical analysis showing that invariant risk minimization is equivalent to a total variation model, clarifying its inductive bias.

## Abstract

Invariant risk minimization (IRM) is an arising approach to generalize invariant features to different environments in machine learning. While most related works focus on new IRM settings or new application scenarios, the mathematical essence of IRM remains to be properly explained. We verify that IRM is essentially a total variation based on $L^2$ norm (TV-$\ell_2$) of the learning risk with respect to the classifier variable. Moreover, we propose a novel IRM framework based on the TV-$\ell_1$ model. It not only expands the classes of functions that can be used as the learning risk and the feature extractor, but also has robust performance in denoising and invariant feature preservation based on the coarea formula. We also illustrate some requirements for IRM-TV-$\ell_1$ to achieve out-of-distribution generalization. Experimental results show that the proposed framework achieves competitive performance in several benchmark machine learning scenarios.