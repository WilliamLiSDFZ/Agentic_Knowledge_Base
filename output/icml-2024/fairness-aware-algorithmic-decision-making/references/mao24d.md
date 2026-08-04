---
title: "Regression with Multi-Expert Deferral"
source: "https://proceedings.mlr.press/v235/mao24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mao24d/mao24d.pdf"
categories: ['fairness-aware-algorithmic-decision-making']
tags: ['learning-to-defer', 'regression', 'multiple-experts']
venue: "ICML 2024"
tldr: "A framework for learning to defer predictions to multiple experts in regression settings, addressing challenges from continuous output spaces."
---

# Regression with Multi-Expert Deferral

**Source**: [https://proceedings.mlr.press/v235/mao24d.html](https://proceedings.mlr.press/v235/mao24d.html)

**TLDR**: A framework for learning to defer predictions to multiple experts in regression settings, addressing challenges from continuous output spaces.

## Abstract

Learning to defer with multiple experts is a framework where the learner can choose to defer the prediction to several experts. While this problem has received significant attention in classification contexts, it presents unique challenges in regression due to the infinite and continuous nature of the label space. In this work, we introduce a novel framework of regression with deferral, which involves deferring the prediction to multiple experts. We present a comprehensive analysis for both the single-stage scenario, where there is simultaneous learning of predictor and deferral functions, and the two-stage scenario, which involves a pre-trained predictor with a learned deferral function. We introduce new surrogate loss functions for both scenarios and prove that they are supported by $H$-consistency bounds. These bounds provide consistency guarantees that are stronger than Bayes consistency, as they are non-asymptotic and hypothesis set-specific. Our framework is versatile, applying to multiple experts, accommodating any bounded regression losses, addressing both instance-dependent and label-dependent costs, and supporting both single-stage and two-stage methods. Our single-stage formulation subsumes as a special case the recent regression with abstention (Cheng et al., 2023) framework, where only a single expert is considered, specifically for the squared loss and a label-independent cost. Minimizing our proposed loss functions directly leads to novel algorithms for regression with deferral. We report the results of extensive experiments showing the effectiveness of our proposed algorithms.