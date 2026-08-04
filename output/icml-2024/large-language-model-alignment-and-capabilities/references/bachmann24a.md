---
title: "The Pitfalls of Next-Token Prediction"
source: "https://proceedings.mlr.press/v235/bachmann24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bachmann24a/bachmann24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'position-papers-on-ml-research-directions']
tags: ['next-token-prediction', 'autoregression', 'language-model-limitations']
venue: "ICML 2024"
tldr: "This paper crystallizes concerns about next-token prediction by separating inference-time autoregression from training, arguing it cannot faithfully model human thinking."
---

# The Pitfalls of Next-Token Prediction

**Source**: [https://proceedings.mlr.press/v235/bachmann24a.html](https://proceedings.mlr.press/v235/bachmann24a.html)

**TLDR**: This paper crystallizes concerns about next-token prediction by separating inference-time autoregression from training, arguing it cannot faithfully model human thinking.

## Abstract

Can a mere next-token predictor faithfully model human thinking? Our work is aimed at crystallizing this intuitive concern, which is currently fragmented in the literature. First, we emphasize isolating the two phases of next-token prediction that are often conflated: autoregression during inference vs. teacher-forcing during training. We argue that the previously-identified problem of "exponential error accumulation" is a symptom of autoregressive inference. But more concerningly, we identify that teacher-forcing can let the model fit the training data by cheating, causing total in-distribution failure. We design a minimal planning task where empirically both the Transformer and the Mamba architecture fail in this manner - remarkably, despite the task being easy to learn. Overall, our work consolidates these and other essential arguments surrounding next-token prediction. We hope this effort can ground future discussions and inspire explorations beyond the next-token prediction paradigm.