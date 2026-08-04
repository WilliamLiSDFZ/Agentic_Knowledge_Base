---
title: "StableSSM: Alleviating the Curse of Memory in State-space Models through Stable Reparameterization"
source: "https://proceedings.mlr.press/v235/wang24ag.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24ag/wang24ag.pdf"
categories: ['sequence-models-for-memory-and-state', 'neural-network-learning-dynamics-theory']
tags: ['state-space-models', 'long-term-memory', 'reparameterization', 'sequence-modeling']
venue: "ICML 2024"
tldr: "Stable reparameterization of state-space models is proposed to alleviate the curse of memory and improve long-term dependency learning."
---

# StableSSM: Alleviating the Curse of Memory in State-space Models through Stable Reparameterization

**Source**: [https://proceedings.mlr.press/v235/wang24ag.html](https://proceedings.mlr.press/v235/wang24ag.html)

**TLDR**: Stable reparameterization of state-space models is proposed to alleviate the curse of memory and improve long-term dependency learning.

## Abstract

In this paper, we investigate the long-term memory learning capabilities of state-space models (SSMs) from the perspective of parameterization. We prove that state-space models without any reparameterization exhibit a memory limitation similar to that of traditional RNNs: the target relationships that can be stably approximated by state-space models must have an exponential decaying memory. Our analysis identifies this “curse of memory” as a result of the recurrent weights converging to a stability boundary, suggesting that a reparameterization technique can be effective. To this end, we introduce a class of reparameterization techniques for SSMs that effectively lift its memory limitations. Besides improving approximation capabilities, we further illustrate that a principled choice of reparameterization scheme can also enhance optimization stability. We validate our findings using synthetic datasets, language models and image classifications.