---
title: "On Gradient-like Explanation under a Black-box Setting: When Black-box Explanations Become as Good as White-box"
source: "https://proceedings.mlr.press/v235/cai24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cai24h/cai24h.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'adversarial-robustness-and-model-security']
tags: ['attribution-methods', 'black-box-explanations', 'gradient-approximation', 'explainability']
venue: "ICML 2024"
tldr: "Proposes black-box gradient-like explanations that achieve quality comparable to white-box gradient methods without requiring internal model access."
---

# On Gradient-like Explanation under a Black-box Setting: When Black-box Explanations Become as Good as White-box

**Source**: [https://proceedings.mlr.press/v235/cai24h.html](https://proceedings.mlr.press/v235/cai24h.html)

**TLDR**: Proposes black-box gradient-like explanations that achieve quality comparable to white-box gradient methods without requiring internal model access.

## Abstract

Attribution methods shed light on the explainability of data-driven approaches such as deep learning models by uncovering the most influential features in a to-be-explained decision. While determining feature attributions via gradients delivers promising results, the internal access required for acquiring gradients can be impractical under safety concerns, thus limiting the applicability of gradient-based approaches. In response to such limited flexibility, this paper presents GEEX (gradient-estimation-based explanation), a method that produces gradient-like explanations through only query-level access. The proposed approach holds a set of fundamental properties for attribution methods, which are mathematically rigorously proved, ensuring the quality of its explanations. In addition to the theoretical analysis, with a focus on image data, the experimental results empirically demonstrate the superiority of the proposed method over state-of-the-art black-box methods and its competitive performance compared to methods with full access.