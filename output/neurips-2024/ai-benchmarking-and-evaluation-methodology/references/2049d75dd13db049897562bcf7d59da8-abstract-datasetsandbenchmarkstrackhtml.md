---
title: "Shopping MMLU: A Massive Multi-Task Online Shopping Benchmark for Large Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/2049d75dd13db049897562bcf7d59da8-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'llm-training-and-optimization-techniques']
tags: ['benchmark', 'online-shopping', 'multi-task', 'llm-evaluation', 'e-commerce']
venue: "NeurIPS 2024"
tldr: "Shopping MMLU is a massive multi-task benchmark for evaluating large language models on diverse online shopping tasks."
---

# Shopping MMLU: A Massive Multi-Task Online Shopping Benchmark for Large Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/2049d75dd13db049897562bcf7d59da8-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/2049d75dd13db049897562bcf7d59da8-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Shopping MMLU is a massive multi-task benchmark for evaluating large language models on diverse online shopping tasks.

## Abstract

Online shopping is a complex multi-task, few-shot learning problem with a wide and evolving range of entities, relations, and tasks. However, existing models and benchmarks are commonly tailored to specific tasks, falling short of capturing the full complexity of online shopping. Large Language Models (LLMs), with their multi-task and few-shot learning abilities, have the potential to profoundly transform online shopping by alleviating task-specific engineering efforts and by providing users with interactive conversations. Despite the potential, LLMs face unique challenges in online shopping, such as domain-specific concepts, implicit knowledge, and heterogeneous user behaviors. Motivated by the potential and challenges, we propose Shopping MMLU, a diverse multi-task online shopping benchmark derived from real-world Amazon data. Shopping MMLU consists of 57 tasks covering 4 major shopping skills: concept understanding, knowledge reasoning, user behavior alignment, and multi-linguality, and can thus comprehensively evaluate the abilities of LLMs as general shop assistants. With Shoppping MMLU, we benchmark over 20 existing LLMs and uncover valuable insights about practices and prospects of building versatile LLM-based shop assistants. Shopping MMLU can be publicly accessed at https://github.com/KL4805/ShoppingMMLU. In addition, with Shopping MMLU, we are hosting a competition in KDD Cup 2024 with over 500 participating teams. The winning solutions and the associated workshop can be accessed at our website https://amazon-kddcup24.github.io/.