---
title: "Finite Smoothing Algorithm for High-Dimensional Support Vector Machines and Quantile Regression"
source: "https://proceedings.mlr.press/v235/tang24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tang24j/tang24j.pdf"
categories: ['quantile-regression-methods-and-applications', 'optimization-algorithms-convergence-theory']
tags: ['support-vector-machines', 'quantile-regression', 'high-dimensional-optimization']
venue: "ICML 2024"
tldr: "A finite smoothing algorithm is proposed to address non-smooth loss functions in high-dimensional SVMs and quantile regression, improving computational tractability."
---

# Finite Smoothing Algorithm for High-Dimensional Support Vector Machines and Quantile Regression

**Source**: [https://proceedings.mlr.press/v235/tang24j.html](https://proceedings.mlr.press/v235/tang24j.html)

**TLDR**: A finite smoothing algorithm is proposed to address non-smooth loss functions in high-dimensional SVMs and quantile regression, improving computational tractability.

## Abstract

This paper introduces a finite smoothing algorithm (FSA), a novel approach to tackle computational challenges in applying support vector machines (SVM) and quantile regression to high-dimensional data. The critical issue with these methods is the non-smooth nature of their loss functions, which traditionally limits the use of highly efficient coordinate descent techniques in high-dimensional settings. FSA innovatively addresses this issue by transforming these loss functions into their smooth counterparts, thereby facilitating more efficient computation. A distinctive feature of FSA is its theoretical foundation: FSA can yield exact solutions, not just approximations, despite the smoothing approach. Our simulation and benchmark tests demonstrate that FSA significantly outpaces its competitors in speed, often by orders of magnitude, while improving or at least maintaining precision. We have implemented FSA in two open-source R packages: hdsvm for high-dimensional SVM and hdqr for high-dimensional quantile regression.