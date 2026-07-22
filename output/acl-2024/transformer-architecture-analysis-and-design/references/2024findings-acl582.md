---
title: "Pruning Large Language Models to Intra-module Low-rank Architecture with Transitional Activations"
source: "https://aclanthology.org/2024.findings-acl.582/"
pdf_url: ""
categories: ['transformer-architecture-analysis-and-design', 'collaborative-llm-deployment-and-inference-optimization']
tags: ['structured-pruning', 'low-rank', 'llm-compression']
venue: "ACL 2024"
tldr: "Proposes pruning LLMs into intra-module low-rank architectures using transitional activations for efficient end-side deployment."
---

# Pruning Large Language Models to Intra-module Low-rank Architecture with Transitional Activations

**Source**: [https://aclanthology.org/2024.findings-acl.582/](https://aclanthology.org/2024.findings-acl.582/)

**TLDR**: Proposes pruning LLMs into intra-module low-rank architectures using transitional activations for efficient end-side deployment.

## Abstract

AbstractStructured pruning fundamentally reduces computational and memory overheads of large language models (LLMs) and offers a feasible solution for end-side LLM deployment. Structurally pruned models remain dense and high-precision, highly compatible with further tuning and compression. However, as the coarse-grained structured pruning poses large damage to the highly interconnected model, achieving a high compression ratio for scaled-up LLMs remains a challenge. In this paper, we introduce a task-agnostic structured pruning approach coupled with a compact Transformer architecture design. The proposed approach, named TransAct, reduces transitional activations inside multi-head attention (MHA) and multi-layer perceptron (MLP) modules, while preserving the inter-module activations that are sensitive to perturbations. Hence, the LLM is pruned into an intra-module low-rank architecture, significantly reducing weights, KV Cache and attention computation. TransAct is implemented on the LLaMA model and evaluated on downstream benchmarks. Results verify the optimality of our approach at high compression with respect to both efficiency and performance. Further, ablation studies reveal the strength of activation-guided iterative pruning and provide experimental analysis on the redundancy of MHA and MLP modules.