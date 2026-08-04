---
title: "Repoformer: Selective Retrieval for Repository-Level Code Completion"
source: "https://proceedings.mlr.press/v235/wu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24a/wu24a.pdf"
categories: ['information-retrieval-and-recommendation-systems', 'transformer-architecture-efficiency-and-scaling']
tags: ['retrieval-augmented-generation', 'code-completion', 'selective-retrieval', 'repository-level']
venue: "ICML 2024"
tldr: "Repoformer selectively applies retrieval-augmented generation for repository-level code completion to improve efficiency and robustness."
---

# Repoformer: Selective Retrieval for Repository-Level Code Completion

**Source**: [https://proceedings.mlr.press/v235/wu24a.html](https://proceedings.mlr.press/v235/wu24a.html)

**TLDR**: Repoformer selectively applies retrieval-augmented generation for repository-level code completion to improve efficiency and robustness.

## Abstract

Recent advances in retrieval-augmented generation (RAG) have initiated a new era in repository-level code completion. However, the invariable use of retrieval in existing methods exposes issues in both efficiency and robustness, with a large proportion of the retrieved contexts proving unhelpful or harmful to code language models (code LMs). In this paper, we propose a selective RAG framework to avoid retrieval when unnecessary. To power this framework, we design a self-supervised learning approach to enable a code LM to accurately self-evaluate whether retrieval can improve its output quality and robustly leverage the potentially noisy retrieved contexts. Using this LM as both the selective RAG policy and the generation model, our framework achieves state-of-the-art repository-level code completion performance on diverse benchmarks including RepoEval, CrossCodeEval, and CrossCodeLongEval, a new long-form code completion benchmark. Meanwhile, our analyses show that selectively retrieving brings as much as 70% inference speedup in the online serving setting without harming the performance. We further demonstrate that our framework is able to accommodate different generation models, retrievers, and programming languages. These advancements position our framework as an important step towards more accurate and efficient repository-level code completion.