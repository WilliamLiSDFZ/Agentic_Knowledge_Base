---
title: "Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/840abfadd04c967feaa2a49aba94a32d-Abstract-Conference.html"
categories: ['llm-training-and-optimization-techniques', 'recurrent-and-spiking-neural-network-dynamics']
tags: ['long-context-LLM', 'linear-complexity', 'efficient-pretraining']
venue: "NeurIPS 2024"
tldr: "Megalodon introduces an efficient architecture with unlimited context length that outperforms Transformers in pretraining efficiency and downstream accuracy."
---

# Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/840abfadd04c967feaa2a49aba94a32d-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/840abfadd04c967feaa2a49aba94a32d-Abstract-Conference.html)

**TLDR**: Megalodon introduces an efficient architecture with unlimited context length that outperforms Transformers in pretraining efficiency and downstream accuracy.

## Abstract

The quadratic complexity and weak length extrapolation of Transformers limits their ability to scale to long sequences, and while sub-quadratic solutions like linear attention and state space models exist, they empirically underperform Transformers in pretraining efficiency and downstream task accuracy. We introduce MEGALODON, an neural architecture for efficient sequence modeling with unlimited context length. MEGALODON inherits the architecture of MEGA (exponential moving average with gated attention), and further introduces multiple technical components to improve its capability and stability, including complex exponential moving average (CEMA), timestep normalization layer, normalized attention mechanism and pre-norm with two-hop residual configuration. In a controlled head-to-head comparison with LLAMA2, MEGALODON achieves better efficiency than Transformer in the scale of 7 billion parameters and 2 trillion training tokens. MEGALODON reaches a training loss of 1.70, landing mid-way between LLAMA2-7B (1.75) and LLAMA2-13B (1.67). This result is robust throughout a wide range of benchmarks, where MEGALODON consistently outperforms Transformers across different tasks, domains, and modalities.