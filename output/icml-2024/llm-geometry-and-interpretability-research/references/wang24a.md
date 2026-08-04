---
title: "Understanding Reasoning Ability of Language Models From the Perspective of Reasoning Paths Aggregation"
source: "https://proceedings.mlr.press/v235/wang24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24a/wang24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-geometry-and-interpretability-research']
tags: ['language-model-reasoning', 'pre-training', 'reasoning-paths', 'chain-of-thought', 'next-token-prediction']
venue: "ICML 2024"
tldr: "This paper explains LLM reasoning capability as aggregation over implicit reasoning paths formed during next-token prediction pre-training."
---

# Understanding Reasoning Ability of Language Models From the Perspective of Reasoning Paths Aggregation

**Source**: [https://proceedings.mlr.press/v235/wang24a.html](https://proceedings.mlr.press/v235/wang24a.html)

**TLDR**: This paper explains LLM reasoning capability as aggregation over implicit reasoning paths formed during next-token prediction pre-training.

## Abstract

Pre-trained language models (LMs) are able to perform complex reasoning without explicit fine-tuning. To understand how pre-training with a next-token prediction objective contributes to the emergence of such reasoning capability, we propose that we can view an LM as deriving new conclusions by aggregating indirect reasoning paths seen at pre-training time. We found this perspective effective in two important cases of reasoning: logic reasoning with knowledge graphs (KGs) and chain-of-thought (CoT) reasoning. More specifically, we formalize the reasoning paths as random walk paths on the knowledge/reasoning graphs. Analyses of learned LM distributions suggest that a weighted sum of relevant random walk path probabilities is a reasonable way to explain how LMs reason. Experiments and analysis on multiple KG and CoT datasets reveal the effect of training on random walk paths and suggest that augmenting unlabeled random walk reasoning paths can improve real-world multi-step reasoning performance.