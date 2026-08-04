---
title: "Learning Solution-Aware Transformers for Efficiently Solving Quadratic Assignment Problem"
source: "https://proceedings.mlr.press/v235/tan24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tan24d/tan24d.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning']
tags: ['quadratic-assignment', 'transformer', 'combinatorial-optimization']
venue: "ICML 2024"
tldr: "A solution-aware Transformer is learned to efficiently solve the Quadratic Assignment Problem using machine learning."
---

# Learning Solution-Aware Transformers for Efficiently Solving Quadratic Assignment Problem

**Source**: [https://proceedings.mlr.press/v235/tan24d.html](https://proceedings.mlr.press/v235/tan24d.html)

**TLDR**: A solution-aware Transformer is learned to efficiently solve the Quadratic Assignment Problem using machine learning.

## Abstract

Recently various optimization problems, such as Mixed Integer Linear Programming Problems (MILPs), have undergone comprehensive investigation, leveraging the capabilities of machine learning. This work focuses on learning-based solutions for efficiently solving the Quadratic Assignment Problem (QAPs), which stands as a formidable challenge in combinatorial optimization. While many instances of simpler problems admit fully polynomial-time approximate solution (FPTAS), QAP is shown to be strongly NPhard. Even finding a FPTAS for QAP is difficult, in the sense that the existence of a FPTAS implies P = NP. Current research on QAPs suffer from limited scale and computational inefficiency. To attack the aforementioned issues, we here propose the first solution of its kind for QAP in the learn-to-improve category. This work encodes facility and location nodes separately, instead of forming computationally intensive association graphs prevalent in current approaches. This design choice enables scalability to larger problem sizes. Furthermore, a Solution AWare Transformer (SAWT) architecture integrates the incumbent solution matrix with the attention score to effectively capture higher-order information of the QAPs. Our model’s effectiveness is validated through extensive experiments on self-generated QAP instances of varying sizes and the QAPLIB benchmark.