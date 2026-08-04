---
title: "Online Cascade Learning for Efficient Inference over Streams"
source: "https://proceedings.mlr.press/v235/nie24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nie24a/nie24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'llm-serving-systems-and-infrastructure']
tags: ['LLM-inference', 'cascade-learning', 'data-streams']
venue: "ICML 2024"
tldr: "Proposes online cascade learning to efficiently route stream queries between small and large language models to reduce inference costs."
---

# Online Cascade Learning for Efficient Inference over Streams

**Source**: [https://proceedings.mlr.press/v235/nie24a.html](https://proceedings.mlr.press/v235/nie24a.html)

**TLDR**: Proposes online cascade learning to efficiently route stream queries between small and large language models to reduce inference costs.

## Abstract

Large Language Models (LLMs) have a natural role in answering complex queries about data streams, but the high computational cost of LLM inference makes them infeasible in many such tasks. We propose online cascade learning, the first approach to address this challenge. The objective here is to learn a “cascade” of models, starting with lower-capacity models (such as logistic regression) and ending with a powerful LLM, along with a deferral policy that determines the model to be used on a given input. We formulate the task of learning cascades online as an imitation-learning problem, where smaller models are updated over time imitating the collected LLM demonstrations, and give a no-regret algorithm for the problem. Experimental results across four benchmarks show that our method parallels LLMs in accuracy while cutting down inference costs by as much as 90% with strong robustness against input distribution shifts, underscoring its efficacy and adaptability in stream processing. Our source code is available at https://github.com/flitternie/online_cascade_learning.