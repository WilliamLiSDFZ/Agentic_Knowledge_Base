---
title: "When Linear Attention Meets Autoregressive Decoding: Towards More Effective and Efficient Linearized Large Language Models"
source: "https://proceedings.mlr.press/v235/you24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/you24a/you24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling']
tags: ['linear-attention', 'LLM', 'autoregressive-decoding', 'efficiency']
venue: "ICML 2024"
tldr: "Linear attention mechanisms are enhanced for more effective and efficient autoregressive decoding in large language models."
---

# When Linear Attention Meets Autoregressive Decoding: Towards More Effective and Efficient Linearized Large Language Models

**Source**: [https://proceedings.mlr.press/v235/you24a.html](https://proceedings.mlr.press/v235/you24a.html)

**TLDR**: Linear attention mechanisms are enhanced for more effective and efficient autoregressive decoding in large language models.

## Abstract

Autoregressive Large Language Models (LLMs) have achieved impressive performance in language tasks but face two significant bottlenecks: (1) quadratic complexity in the attention module as the number of tokens increases, and (2) limited efficiency due to the sequential processing nature of autoregressive LLMs during generation. While linear attention and speculative decoding offer potential solutions, their applicability and synergistic potential for enhancing autoregressive LLMs remain uncertain. We conduct the first comprehensive study on the efficacy of existing linear attention methods for autoregressive LLMs, integrating them with speculative decoding. We introduce an augmentation technique for linear attention that ensures compatibility with speculative decoding, enabling more efficient training and serving of LLMs. Extensive experiments and ablation studies involving seven existing linear attention models and five encoder/decoder-based LLMs consistently validate the effectiveness of our augmented linearized LLMs. Notably, our approach achieves up to a 6.67 reduction in perplexity on the LLaMA model and up to a 2$\times$ speedup during generation compared to prior linear attention methods. Codes and models are available at https://github.com/GATECH-EIC/Linearized-LLM.