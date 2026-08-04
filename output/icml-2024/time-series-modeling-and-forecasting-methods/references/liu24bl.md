---
title: "TimeX++: Learning Time-Series Explanations with Information Bottleneck"
source: "https://proceedings.mlr.press/v235/liu24bl.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24bl/liu24bl.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'ai-explainability-uncertainty-human-decision-making']
tags: ['time-series-explanation', 'information-bottleneck', 'interpretability', 'deep-learning', 'explainability']
venue: "ICML 2024"
tldr: "An information-theoretic framework for explaining deep learning models on time-series data using the information bottleneck principle to produce better explanations."
---

# TimeX++: Learning Time-Series Explanations with Information Bottleneck

**Source**: [https://proceedings.mlr.press/v235/liu24bl.html](https://proceedings.mlr.press/v235/liu24bl.html)

**TLDR**: An information-theoretic framework for explaining deep learning models on time-series data using the information bottleneck principle to produce better explanations.

## Abstract

Explaining deep learning models operating on time series data is crucial in various applications of interest which require interpretable and transparent insights from time series signals. In this work, we investigate this problem from an information theoretic perspective and show that most existing measures of explainability may suffer from trivial solutions and distributional shift issues. To address these issues, we introduce a simple yet practical objective function for time series explainable learning. The design of the objective function builds upon the principle of information bottleneck (IB), and modifies the IB objective function to avoid trivial solutions and distributional shift issues. We further present TimeX++, a novel explanation framework that leverages a parametric network to produce explanation-embedded instances that are both in-distributed and label-preserving. We evaluate TimeX++ on both synthetic and real-world datasets comparing its performance against leading baselines, and validate its practical efficacy through case studies in a real-world environmental application. Quantitative and qualitative evaluations show that TimeX++ outperforms baselines across all datasets, demonstrating a substantial improvement in explanation quality for time series data. The source code is available at https://github.com/zichuan-liu/TimeXplusplus.