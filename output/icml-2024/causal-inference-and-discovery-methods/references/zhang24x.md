---
title: "Towards Causal Foundation Model: on Duality between Optimal Balancing and Attention"
source: "https://proceedings.mlr.press/v235/zhang24x.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24x/zhang24x.pdf"
categories: ['causal-inference-and-discovery-methods', 'large-language-model-alignment-and-capabilities']
tags: ['causal-inference', 'foundation-models', 'attention-mechanism']
venue: "ICML 2024"
tldr: "Reveals a duality between optimal covariate balancing for causal inference and the attention mechanism, motivating causal foundation models."
---

# Towards Causal Foundation Model: on Duality between Optimal Balancing and Attention

**Source**: [https://proceedings.mlr.press/v235/zhang24x.html](https://proceedings.mlr.press/v235/zhang24x.html)

**TLDR**: Reveals a duality between optimal covariate balancing for causal inference and the attention mechanism, motivating causal foundation models.

## Abstract

Foundation models have brought changes to the landscape of machine learning, demonstrating sparks of human-level intelligence across a diverse array of tasks. However, a gap persists in complex tasks such as causal inference, primarily due to challenges associated with intricate reasoning steps and high numerical precision requirements. In this work, we take a first step towards building causally-aware foundation models for treatment effect estimations. We propose a novel, theoretically justified method called Causal Inference with Attention (CInA), which utilizes multiple unlabeled datasets to perform self-supervised causal learning, and subsequently enables zero-shot causal inference on unseen tasks with new data. This is based on our theoretical results that demonstrate the primal-dual connection between optimal covariate balancing and self-attention, facilitating zero-shot causal inference through the final layer of a trained transformer-type architecture. We demonstrate empirically that CInA effectively generalizes to out-of-distribution datasets and various real-world datasets, matching or even surpassing traditional per-dataset methodologies. These results provide compelling evidence that our method has the potential to serve as a stepping stone for the development of causal foundation models.