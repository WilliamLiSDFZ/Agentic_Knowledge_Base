---
title: "tinyBenchmarks: evaluating LLMs with fewer examples"
source: "https://proceedings.mlr.press/v235/maia-polo24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/maia-polo24a/maia-polo24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'data-selection-and-active-learning-methods']
tags: ['llm-evaluation', 'benchmark-efficiency', 'item-response-theory']
venue: "ICML 2024"
tldr: "Strategies to evaluate large language models using far fewer benchmark examples while maintaining reliable performance estimates."
---

# tinyBenchmarks: evaluating LLMs with fewer examples

**Source**: [https://proceedings.mlr.press/v235/maia-polo24a.html](https://proceedings.mlr.press/v235/maia-polo24a.html)

**TLDR**: Strategies to evaluate large language models using far fewer benchmark examples while maintaining reliable performance estimates.

## Abstract

The versatility of large language models (LLMs) led to the creation of diverse benchmarks that thoroughly test a variety of language models’ abilities. These benchmarks consist of tens of thousands of examples making evaluation of LLMs very expensive. In this paper, we investigate strategies to reduce the number of evaluations needed to assess the performance of an LLM on several key benchmarks. For example, we show that to accurately estimate the performance of an LLM on MMLU, a popular multiple-choice QA benchmark consisting of 14K examples, it is sufficient to evaluate this LLM on 100 curated examples. We release evaluation tools and tiny versions of popular benchmarks: Open LLM Leaderboard, MMLU, HELM, and AlpacaEval 2.0. Our empirical analysis demonstrates that these tools and tiny benchmarks are sufficient to reliably and efficiently reproduce the original evaluation results.