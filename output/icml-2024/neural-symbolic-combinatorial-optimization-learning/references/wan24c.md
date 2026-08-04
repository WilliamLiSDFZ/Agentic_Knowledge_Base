---
title: "AlphaZero-Like Tree-Search can Guide Large Language Model Decoding and Training"
source: "https://proceedings.mlr.press/v235/wan24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wan24c/wan24c.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'neural-symbolic-combinatorial-optimization-learning']
tags: ['AlphaZero', 'tree-search', 'LLM-decoding', 'reasoning', 'MCTS']
venue: "ICML 2024"
tldr: "Proposes using AlphaZero-like tree-search to guide large language model decoding and fine-tuning for improved multi-step reasoning."
---

# AlphaZero-Like Tree-Search can Guide Large Language Model Decoding and Training

**Source**: [https://proceedings.mlr.press/v235/wan24c.html](https://proceedings.mlr.press/v235/wan24c.html)

**TLDR**: Proposes using AlphaZero-like tree-search to guide large language model decoding and fine-tuning for improved multi-step reasoning.

## Abstract

Recent works like Tree-of-Thought (ToT) and Reasoning via Planning (RAP) aim to augment the multi-step reasoning capabilities of LLMs by using tree-search algorithms. These methods rely on prompting a pre-trained model to serve as a value function and focus on problems with low search depth. As a result, these methods cannot benefit from in-domain training and only rely on pretraining process — they will not work in domains where the pre-trained LLM does not have enough knowledge to serve as an effective value function or in domains that require long-horizon planning. To address these limitations, we present an AlphaZero-like tree-search learning framework for LLMs (termed TS-LLM), systematically illustrating how tree-search with a learned value function can guide LLM decoding. TS-LLM distinguishes itself in two key ways. (1) Leveraging a learned value function and AlphaZero-like algorithms, our approach can be generally adaptable to a wide range of tasks, language models of any size, and tasks of varying search depths. (2) Our approach can guide LLMs during both inference and training, iteratively improving the LLMs. Empirical results across reasoning, planning, alignment, and decision-making tasks show that TS-LLM outperforms existing approaches and can handle trees with a depth of 64.