---
title: "HexGen: Generative Inference of Large Language Model over Heterogeneous Environment"
source: "https://proceedings.mlr.press/v235/jiang24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jiang24f/jiang24f.pdf"
categories: ['llm-serving-systems-and-infrastructure', 'privacy-preserving-federated-and-distributed-learning']
tags: ['llm-serving', 'heterogeneous-inference', 'cross-datacenter', 'generative-inference']
venue: "ICML 2024"
tldr: "HexGen enables cost-efficient generative inference of large language models across heterogeneous and cross-datacenter environments."
---

# HexGen: Generative Inference of Large Language Model over Heterogeneous Environment

**Source**: [https://proceedings.mlr.press/v235/jiang24f.html](https://proceedings.mlr.press/v235/jiang24f.html)

**TLDR**: HexGen enables cost-efficient generative inference of large language models across heterogeneous and cross-datacenter environments.

## Abstract

Serving generative inference of the large language model is a crucial component of contemporary AI applications. In this paper, our focus lies in deploying such services in a heterogeneous and cross-datacenter setting to mitigate the substantial inference costs typically associated with a single centralized datacenter. Towards this end, we propose HexGen, a flexible distributed inference engine that uniquely supports the asymmetric partition of generative inference computations over both tensor model parallelism and pipeline parallelism, which allows for effective deployment across diverse GPUs interconnected by a fully heterogeneous network. We further propose a sophisticated scheduling algorithm grounded in constrained optimization that can adaptively assign asymmetric inference computation across the GPUs to fulfill inference requests while maintaining acceptable latency levels. We conduct an extensive empirical study to evaluate the efficiency of HexGen by serving the state-of-the-art Llama-2 (70B) model. The experimental results suggest that HexGen can choose to achieve up to $2.3\times$ lower latency deadlines or tolerate up to $4\times$ more traffic request rates compared with the homogeneous baseline given the same budget.