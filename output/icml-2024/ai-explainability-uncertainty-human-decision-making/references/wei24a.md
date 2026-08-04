---
title: "Exploiting Human-AI Dependence for Learning to Defer"
source: "https://proceedings.mlr.press/v235/wei24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wei24a/wei24a.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making']
tags: ['learning-to-defer', 'human-ai-collaboration', 'surrogate-loss']
venue: "ICML 2024"
tldr: "This paper exploits human-AI dependence structure to design theoretically consistent surrogate losses for the learning-to-defer framework."
---

# Exploiting Human-AI Dependence for Learning to Defer

**Source**: [https://proceedings.mlr.press/v235/wei24a.html](https://proceedings.mlr.press/v235/wei24a.html)

**TLDR**: This paper exploits human-AI dependence structure to design theoretically consistent surrogate losses for the learning-to-defer framework.

## Abstract

The learning to defer (L2D) framework allows models to defer their decisions to human experts. For L2D, the Bayes optimality is the basic requirement of theoretical guarantees for the design of consistent surrogate loss functions, which requires the minimizer (i.e., learned classifier) by the surrogate loss to be the Bayes optimality. However, we find that the original form of Bayes optimality fails to consider the dependence between the model and the expert, and such a dependence could be further exploited to design a better consistent loss for L2D. In this paper, we provide a new formulation for the Bayes optimality called dependent Bayes optimality, which reveals the dependence pattern in determining whether to defer. Based on the dependent Bayes optimality, we further present a deferral principle for L2D. Following the guidance of the deferral principle, we propose a novel consistent surrogate loss. Comprehensive experimental results on both synthetic and real-world datasets demonstrate the superiority of our proposed method.