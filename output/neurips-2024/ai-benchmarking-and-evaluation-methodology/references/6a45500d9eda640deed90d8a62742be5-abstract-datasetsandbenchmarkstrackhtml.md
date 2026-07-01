---
title: "CoIN: A Benchmark of Continual Instruction Tuning for Multimodel Large Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/6a45500d9eda640deed90d8a62742be5-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['continual-learning', 'instruction-tuning', 'multimodal-llm-benchmark']
venue: "NeurIPS 2024"
tldr: "Introduces CoIN, a benchmark for evaluating continual instruction tuning across diverse tasks in multimodal large language models."
---

# CoIN: A Benchmark of Continual Instruction Tuning for Multimodel Large Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/6a45500d9eda640deed90d8a62742be5-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/6a45500d9eda640deed90d8a62742be5-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces CoIN, a benchmark for evaluating continual instruction tuning across diverse tasks in multimodal large language models.

## Abstract

Instruction tuning demonstrates impressive performance in adapting Multimodal Large Language Models (MLLMs) to follow task instructions and improve generalization ability.  By extending tuning across diverse tasks, MLLMs can further enhance their understanding of world knowledge and instruction intent. However, continual instruction tuning has been largely overlooked and there are no public benchmarks available. In this paper, we present CoIN, a comprehensive benchmark tailored for assessing the behavior of existing MLLMs under continual instruction tuning. CoIN comprises 10 meticulously crafted datasets spanning 8 tasks, ensuring diversity and serving as a robust evaluation framework to assess crucial aspects of continual instruction tuning, such as task order, instruction diversity and volume. Additionally, apart from traditional evaluation, we design another LLM-based metric to assess the knowledge preserved within MLLMs for reasoning. Following an in-depth evaluation of several MLLMs, we demonstrate that they still suffer catastrophic forgetting, and the failure in instruction alignment assumes the main responsibility, instead of reasoning knowledge forgetting.  To this end, we introduce MoELoRA which is effective in retaining the previous instruction alignment.