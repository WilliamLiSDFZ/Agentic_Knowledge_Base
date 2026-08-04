---
title: "Model-Based Minimum Bayes Risk Decoding for Text Generation"
source: "https://proceedings.mlr.press/v235/jinnai24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jinnai24a/jinnai24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['minimum-bayes-risk', 'text-generation', 'decoding', 'model-based']
venue: "ICML 2024"
tldr: "A model-based approach to minimum Bayes risk decoding replaces expensive sample-based probability estimation with a learned surrogate model for efficient text generation."
---

# Model-Based Minimum Bayes Risk Decoding for Text Generation

**Source**: [https://proceedings.mlr.press/v235/jinnai24a.html](https://proceedings.mlr.press/v235/jinnai24a.html)

**TLDR**: A model-based approach to minimum Bayes risk decoding replaces expensive sample-based probability estimation with a learned surrogate model for efficient text generation.

## Abstract

Minimum Bayes Risk (MBR) decoding has been shown to be a powerful alternative to beam search decoding in a variety of text generation tasks. MBR decoding selects a hypothesis from a pool of hypotheses that has the least expected risk under a probability model according to a given utility function. Since it is impractical to compute the expected risk exactly over all possible hypotheses, two approximations are commonly used in MBR. First, it integrates over a sampled set of hypotheses rather than over all possible hypotheses. Second, it estimates the probability of each hypothesis using a Monte Carlo estimator. While the first approximation is necessary to make it computationally feasible, the second is not essential since we typically have access to the model probability at inference time. We propose model-based MBR (MBMBR), a variant of MBR that uses the model probability itself as the estimate of the probability distribution instead of the Monte Carlo estimate. We show analytically and empirically that the model-based estimate is more promising than the Monte Carlo estimate in text generation tasks. Our experiments show that MBMBR outperforms MBR in several text generation tasks, both with encoder-decoder models and with language models.