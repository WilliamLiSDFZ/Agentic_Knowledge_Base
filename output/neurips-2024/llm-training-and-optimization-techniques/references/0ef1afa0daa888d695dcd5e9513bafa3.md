---
title: "DART-Math: Difficulty-Aware Rejection Tuning for Mathematical Problem-Solving"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/0ef1afa0daa888d695dcd5e9513bafa3-Abstract-Conference.html"
categories: ['llm-training-and-optimization-techniques', 'ai-benchmarking-and-evaluation-methodology']
tags: ['mathematical-reasoning', 'rejection-tuning', 'difficulty-aware']
venue: "NeurIPS 2024"
tldr: "DART-Math introduces difficulty-aware rejection tuning to synthesize better training data for mathematical problem-solving in LLMs."
---

# DART-Math: Difficulty-Aware Rejection Tuning for Mathematical Problem-Solving

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/0ef1afa0daa888d695dcd5e9513bafa3-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/0ef1afa0daa888d695dcd5e9513bafa3-Abstract-Conference.html)

**TLDR**: DART-Math introduces difficulty-aware rejection tuning to synthesize better training data for mathematical problem-solving in LLMs.

## Abstract

Solving mathematical problems requires advanced reasoning abilities and presents notable challenges for large language models. Previous works usually synthesize data from proprietary models to augment existing datasets, followed by instruction tuning to achieve top-tier results. However, our analysis of these datasets reveals severe biases towards easy queries, with frequent failures to generate any correct response for the most challenging queries.Hypothesizing that difficult queries are crucial to learning complex reasoning, we propose Difficulty-Aware Rejection Tuning (DART), a method that allocates difficult queries more trials during the synthesis phase, enabling more extensive training on difficult samples.Utilizing DART, we have created new datasets for mathematical problem-solving that focus more on difficult queries and are substantially smaller than previous ones. Remarkably, our synthesis process solely relies on a 7B-sized open-weight model, without reliance on the commonly used proprietary GPT-4.We fine-tune various base models on our datasets ranging from 7B to 70B in size, resulting in a series of strong models called DART-Math.In comprehensive in-domain and out-of-domain evaluation on 6 mathematical benchmarks, DART-Math outperforms vanilla rejection tuning significantly, being superior or comparable to previous arts, despite using much smaller datasets and no proprietary models. Furthermore, our results position our synthetic datasets as the most effective and cost-efficient publicly available resources for advancing mathematical problem-solving. Our datasets, models and code are publicly available at https://github.com/hkust-nlp/dart-math.