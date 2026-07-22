---
title: "UltraSparseBERT: 99% Conditionally Sparse Language Modelling"
source: "https://aclanthology.org/2024.acl-short.10/"
pdf_url: ""
categories: ['transformer-architecture-analysis-and-design', 'language-model-representations-and-embedding-spaces']
tags: ['sparse-transformers', 'conditional-computation', 'efficient-inference']
venue: "ACL 2024"
tldr: "Presents UltraSparseBERT, which activates only 0.3% of neurons during inference using fast feedforward networks while matching standard BERT performance."
---

# UltraSparseBERT: 99% Conditionally Sparse Language Modelling

**Source**: [https://aclanthology.org/2024.acl-short.10/](https://aclanthology.org/2024.acl-short.10/)

**TLDR**: Presents UltraSparseBERT, which activates only 0.3% of neurons during inference using fast feedforward networks while matching standard BERT performance.

## Abstract

AbstractWe present UltraSparseBERT, a BERT variant that uses 0.3% of its neurons during inference while performing on par with similar BERT models. UltraSparseBERT selectively engages just 12 out of 4095 neurons for each layer inference. This is achieved by reorganizing feedforward networks into fast feedforward networks (FFFs).To showcase but one benefit of high sparsity, we provide an Intel MKL implementation achieving 78x speedup over the optimized feedforward baseline on CPUs, and an OpenAI Triton implementation performing forward passes 4.1x faster than the corresponding native GPU implementation. The training and benchmarking code is enclosed.