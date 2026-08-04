---
title: "OSSCAR: One-Shot Structured Pruning in Vision and Language Models with Combinatorial Optimization"
source: "https://proceedings.mlr.press/v235/meng24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/meng24a/meng24a.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning']
tags: ['structured-pruning', 'combinatorial-optimization', 'vision-language-models']
venue: "ICML 2024"
tldr: "A one-shot structured pruning method using combinatorial optimization to efficiently remove neurons and attention heads from large models."
---

# OSSCAR: One-Shot Structured Pruning in Vision and Language Models with Combinatorial Optimization

**Source**: [https://proceedings.mlr.press/v235/meng24a.html](https://proceedings.mlr.press/v235/meng24a.html)

**TLDR**: A one-shot structured pruning method using combinatorial optimization to efficiently remove neurons and attention heads from large models.

## Abstract

Structured pruning is a promising approach for reducing the inference costs of large vision and language models. By removing carefully chosen structures, e.g., neurons or attention heads, the improvements from this approach can be realized on standard deep learning hardware. In this work, we focus on structured pruning in the one-shot (post-training) setting, which does not require model retraining after pruning. We propose a novel combinatorial optimization framework for this problem, based on a layer-wise reconstruction objective and a careful reformulation that allows for scalable optimization. Moreover, we design a new local combinatorial optimization algorithm, which exploits low-rank updates for efficient local search. Our framework is time and memory-efficient and considerably improves upon state-of-the-art one-shot methods on vision models (e.g., ResNet50, MobileNet) and language models (e.g., OPT-1.3B – OPT-30B). For language models, e.g., OPT-2.7B, OSSCAR can lead to $125\times$ lower test perplexity on WikiText with $2\times$ inference time speedup in comparison to the state-of-the-art ZipLM approach. Our framework is also $6\times$ – $8\times$ faster. Notably, our work considers models with tens of billions of parameters, which is up to $100\times$ larger than what has been previously considered in the structured pruning literature. Our code is available at https://github.com/mazumder-lab/OSSCAR.