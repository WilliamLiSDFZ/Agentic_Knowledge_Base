---
title: "CLLMs: Consistency Large Language Models"
source: "https://proceedings.mlr.press/v235/kou24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kou24a/kou24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'large-language-model-alignment-and-capabilities']
tags: ['LLM-inference', 'Jacobi-decoding', 'consistency-distillation', 'parallel-decoding', 'efficiency']
venue: "ICML 2024"
tldr: "Consistency Large Language Models trained to accelerate Jacobi decoding by enabling more parallelizable and efficient LLM inference."
---

# CLLMs: Consistency Large Language Models

**Source**: [https://proceedings.mlr.press/v235/kou24a.html](https://proceedings.mlr.press/v235/kou24a.html)

**TLDR**: Consistency Large Language Models trained to accelerate Jacobi decoding by enabling more parallelizable and efficient LLM inference.

## Abstract

Jacobi decoding shows promise for more efficient LLM inference as it breaks the sequential nature of the LLM decoding process and transforms it into more parallelizable computation. However, in practice, it achieves little speedup compared to traditional autoregressive (AR) decoding, primarily because Jacobi decoding seldom accurately predicts more than one token in a single fixed-point iteration step. To address this, we develop a new approach aimed at realizing fast convergence from any state to the fixed point in a Jacobi trajectory. This is accomplished by refining the target LLM to consistently predict the fixed point given any state as input. Extensive experiments demonstrate the effectiveness of our method, showing 2.4$\times$ to 3.4$\times$ improvements in generation speed while preserving generation quality across both domain-specific and open-domain benchmarks.