---
title: "Energy-Efficient Gaussian Processes Using Low-Precision Arithmetic"
source: "https://proceedings.mlr.press/v235/alder24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/alder24a/alder24a.pdf"
categories: ['bayesian-optimization-and-surrogate-methods', 'quantum-algorithms-for-machine-learning-optimization']
tags: ['Gaussian-processes', 'low-precision-arithmetic', 'energy-efficiency']
venue: "ICML 2024"
tldr: "This paper proposes using low-precision floating-point arithmetic in Gaussian process regression to reduce energy consumption while maintaining accuracy."
---

# Energy-Efficient Gaussian Processes Using Low-Precision Arithmetic

**Source**: [https://proceedings.mlr.press/v235/alder24a.html](https://proceedings.mlr.press/v235/alder24a.html)

**TLDR**: This paper proposes using low-precision floating-point arithmetic in Gaussian process regression to reduce energy consumption while maintaining accuracy.

## Abstract

The widespread use of artificial intelligence requires finding energy-efficient paradigms for the field. We propose to reduce the energy consumption of Gaussian process regression using low-precision floating-point representations. We explore how low-precision representations impact the results of Gaussian process regression and how data set properties, implementation approach, model performance, and energy consumption interact. Our findings show that a well-conditioned kernel matrix allows reducing the energy consumption by up to 89.01% for 98.08% of arithmetic operations with little to no impact on model performance. Our findings are relevant whenever one needs to invert a symmetric full-rank matrix.