---
title: "Smooth Tchebycheff Scalarization for Multi-Objective Optimization"
source: "https://proceedings.mlr.press/v235/lin24y.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24y/lin24y.pdf"
categories: ['optimization-algorithms-convergence-theory', 'time-series-modeling-and-forecasting-methods']
tags: ['multi-objective-optimization', 'Pareto', 'scalarization']
venue: "ICML 2024"
tldr: "A smooth Tchebycheff scalarization method for efficiently finding Pareto-optimal solutions in multi-objective optimization."
---

# Smooth Tchebycheff Scalarization for Multi-Objective Optimization

**Source**: [https://proceedings.mlr.press/v235/lin24y.html](https://proceedings.mlr.press/v235/lin24y.html)

**TLDR**: A smooth Tchebycheff scalarization method for efficiently finding Pareto-optimal solutions in multi-objective optimization.

## Abstract

Multi-objective optimization problems can be found in many real-world applications, where the objectives often conflict each other and cannot be optimized by a single solution. In the past few decades, numerous methods have been proposed to find Pareto solutions that represent optimal trade-offs among the objectives for a given problem. However, these existing methods could have high computational complexity or may not have good theoretical properties for solving a general differentiable multi-objective optimization problem. In this work, by leveraging the smooth optimization technique, we propose a lightweight and efficient smooth Tchebycheff scalarization approach for gradient-based multi-objective optimization. It has good theoretical properties for finding all Pareto solutions with valid trade-off preferences, while enjoying significantly lower computational complexity compared to other methods. Experimental results on various real-world application problems fully demonstrate the effectiveness of our proposed method.