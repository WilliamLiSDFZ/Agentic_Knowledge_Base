---
title: "Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/b631da756d1573c24c9ba9c702fde5a9-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'reinforcement-learning-optimization-and-decision-making']
tags: ['embodied-AI', 'LLM-benchmarking', 'decision-making', 'evaluation', 'agent-interface']
venue: "NeurIPS 2024"
tldr: "Introduces a systematic benchmark interface for evaluating LLMs on embodied decision-making tasks across diverse domains."
---

# Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/b631da756d1573c24c9ba9c702fde5a9-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/b631da756d1573c24c9ba9c702fde5a9-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces a systematic benchmark interface for evaluating LLMs on embodied decision-making tasks across diverse domains.

## Abstract

We aim to evaluate Large Language Models (LLMs) for embodied decision making. While a significant body of work has been leveraging LLMs for decision making in embodied environments, we still lack a systematic understanding of their performance because they are usually applied in different domains, for different purposes, and built based on different inputs and outputs. Furthermore, existing evaluations tend to rely solely on a final success rate, making it difficult to pinpoint what ability is missing in LLMs and where the problem lies, which in turn blocks embodied agents from leveraging LLMs effectively and selectively. To address these limitations, we propose a generalized interface (Embodied Agent Interface) that supports the formalization of various types of tasks and input-output specifications of LLM-based modules. Specifically, it allows us to unify 1) a broad set of embodied decision-making tasks involving both state and temporally extended goals, 2) four commonly-used LLM-based modules for decision making: goal interpretation, subgoal decomposition, action sequencing, and transition modeling, and 3) a collection of fine-grained metrics that break down evaluation into error types, such as hallucination errors, affordance errors, and various types of planning errors. Overall, our benchmark offers a comprehensive assessment of LLMs’ performance for different subtasks, pinpointing the strengths and weaknesses in LLM-powered embodied AI systems and providing insights into the effective and selective use of LLMs in embodied decision making.