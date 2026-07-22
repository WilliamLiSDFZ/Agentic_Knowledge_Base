---
title: "Probing the Emergence of Cross-lingual Alignment during LLM Training"
source: "https://aclanthology.org/2024.findings-acl.724/"
categories: ['language-model-representations-and-embedding-spaces', 'language-technology-cultural-linguistic-diversity']
tags: ['multilingual-LLM', 'cross-lingual-alignment', 'representation', 'training-dynamics', 'zero-shot-transfer']
venue: "ACL 2024"
tldr: "Probes how cross-lingual alignment emerges during LLM training without explicit parallel supervision."
---

# Probing the Emergence of Cross-lingual Alignment during LLM Training

**Source**: [https://aclanthology.org/2024.findings-acl.724/](https://aclanthology.org/2024.findings-acl.724/)

**TLDR**: Probes how cross-lingual alignment emerges during LLM training without explicit parallel supervision.

## Abstract

AbstractMultilingual Large Language Models (LLMs) achieve remarkable levels of zero-shot cross-lingual transfer performance. We speculate that this is predicated on their ability to align languages without explicit supervision from parallel sentences. While representations of translationally equivalent sentences in different languages are known to be similar after convergence, however, it remains unclear how such cross-lingual alignment emerges during pre-training of LLMs. Our study leverages intrinsic probing techniques, which identify which subsets of neurons encode linguistic features, to correlate the degree of cross-lingual neuron overlap with the zero-shot cross-lingual transfer performance for a given model. In particular, we rely on checkpoints of BLOOM, a multilingual autoregressive LLM, across different training steps and model scales. We observe a high correlation between neuron overlap and downstream performance, which supports our hypothesis on the conditions leading to effective cross-lingual transfer. Interestingly, we also detect a degradation of both implicit alignment and multilingual abilities in certain phases of the pre-training process, providing new insights into the multilingual pretraining dynamics.