---
title: "The Reliability of OKRidge Method in Solving Sparse Ridge Regression Problems"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/8acb1688c994bee3e17df1bff8fedd62-Abstract-Conference.html"
categories: ['statistical-learning-theory-and-matrix-methods', 'statistical-computational-tradeoffs-high-dimensional-learning']
tags: ['sparse-ridge-regression', 'okridge', 'reliability-analysis']
venue: "NeurIPS 2024"
tldr: "This paper investigates the reliability of the OKRidge algorithm for solving sparse ridge regression problems, analyzing its correctness and limitations."
---

# The Reliability of OKRidge Method in Solving Sparse Ridge Regression Problems

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/8acb1688c994bee3e17df1bff8fedd62-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/8acb1688c994bee3e17df1bff8fedd62-Abstract-Conference.html)

**TLDR**: This paper investigates the reliability of the OKRidge algorithm for solving sparse ridge regression problems, analyzing its correctness and limitations.

## Abstract

Sparse ridge regression problems play a significant role across various domains. To solve sparse ridge regression, Liu et al. (2023) recently propose an advanced algorithm, Scalable Optimal $K$-Sparse Ridge Regression (OKRidge), which is both faster and more accurate than existing approaches. However, the absence of theoretical analysis on the error of OKRidge impedes its large-scale applications. In this paper, we reframe the estimation error of OKRidge as a Primary Optimization ($\textbf{PO}$) problem and employ the Convex Gaussian min-max theorem (CGMT) to simplify the $\textbf{PO}$ problem into an Auxiliary Optimization ($\textbf{AO}$) problem. Subsequently, we provide a theoretical error analysis for OKRidge based on the $\textbf{AO}$ problem. This error analysis improves the theoretical reliability of OKRidge. We also conduct experiments to verify our theorems and the results are in excellent agreement with our theoretical findings.