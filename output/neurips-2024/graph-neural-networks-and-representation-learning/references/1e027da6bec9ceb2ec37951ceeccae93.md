---
title: "Loki: Low-rank Keys for Efficient Sparse Attention"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/1e027da6bec9ceb2ec37951ceeccae93-Abstract-Conference.html"
categories: ['llm-training-and-optimization-techniques', 'graph-neural-networks-and-representation-learning']
tags: ['sparse-attention', 'low-rank', 'kv-cache', 'llm-inference', 'efficiency']
venue: "NeurIPS 2024"
tldr: "Proposes Loki, which uses low-rank structure of attention keys to enable efficient sparse attention for long-context LLM inference."
---

# Loki: Low-rank Keys for Efficient Sparse Attention

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/1e027da6bec9ceb2ec37951ceeccae93-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/1e027da6bec9ceb2ec37951ceeccae93-Abstract-Conference.html)

**TLDR**: Proposes Loki, which uses low-rank structure of attention keys to enable efficient sparse attention for long-context LLM inference.

## Abstract

Inference on large language models (LLMs) can be expensive in terms of thecompute and memory costs involved, especially when long sequence lengths areused. In particular, the self-attention mechanism used in LLM inference contributessignificantly to these costs, which has sparked an interest in approximating the self-attention computation to reduce such costs. In this work, we propose to approximateself-attention by focusing on the dimensionality of key vectors computed in theattention block. Our analysis reveals that key vectors lie in a significantly lower-dimensional space, consistently across several datasets and models. Exploiting thisobservation, we propose Loki, a novel sparse attention method that ranks and selectstokens in the KV-cache based on attention scores computed in low-dimensionalspace. Our evaluations show that Loki is able to speed up the attention computationdue to reduced data movement (load/store) and compute costs while maintainingthe efficacy of the models better than other popular approximation methods.