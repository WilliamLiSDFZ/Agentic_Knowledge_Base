---
title: "Stability-Informed Initialization of Neural Ordinary Differential Equations"
source: "https://proceedings.mlr.press/v235/westny24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/westny24a/westny24a.pdf"
categories: ['bayesian-filtering-and-dynamical-systems-learning', 'optimization-algorithms-convergence-theory']
tags: ['neural-ODEs', 'stability', 'numerical-integration', 'initialization']
venue: "ICML 2024"
tldr: "Analyzes how numerical integration choices affect stability regions of neural ODEs and proposes stability-informed initialization strategies to improve training."
---

# Stability-Informed Initialization of Neural Ordinary Differential Equations

**Source**: [https://proceedings.mlr.press/v235/westny24a.html](https://proceedings.mlr.press/v235/westny24a.html)

**TLDR**: Analyzes how numerical integration choices affect stability regions of neural ODEs and proposes stability-informed initialization strategies to improve training.

## Abstract

This paper addresses the training of Neural Ordinary Differential Equations (neural ODEs), and in particular explores the interplay between numerical integration techniques, stability regions, step size, and initialization techniques. It is shown how the choice of integration technique implicitly regularizes the learned model, and how the solver’s corresponding stability region affects training and prediction performance. From this analysis, a stability-informed parameter initialization technique is introduced. The effectiveness of the initialization method is displayed across several learning benchmarks and industrial applications.