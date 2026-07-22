---
title: "Mitigate Negative Transfer with Similarity Heuristic Lifelong Prompt Tuning"
source: "https://aclanthology.org/2024.findings-acl.650/"
categories: ['continual-learning-for-nlp-tasks', 'llm-training-alignment-and-evaluation']
tags: ['lifelong-learning', 'prompt-tuning', 'negative-transfer']
venue: "ACL 2024"
tldr: "Introduces similarity heuristics into lifelong prompt tuning to mitigate negative transfer across sequentially learned tasks."
---

# Mitigate Negative Transfer with Similarity Heuristic Lifelong Prompt Tuning

**Source**: [https://aclanthology.org/2024.findings-acl.650/](https://aclanthology.org/2024.findings-acl.650/)

**TLDR**: Introduces similarity heuristics into lifelong prompt tuning to mitigate negative transfer across sequentially learned tasks.

## Abstract

AbstractLifelong prompt tuning has significantly advanced parameter-efficient lifelong learning with its efficiency and minimal storage demands on various tasks.Our empirical studies, however, highlights certain transferability constraints in the current methodologies: a universal algorithm that guarantees consistent positive transfer across all tasks is currently unattainable, especially when dealing dissimilar tasks that may engender negative transfer.Identifying the misalignment between algorithm selection and task specificity as the primary cause of negative transfer, we present the Similarity Heuristic Lifelong Prompt Tuning (SHLPT) framework. This innovative strategy partitions tasks into two distinct subsets by harnessing a learnable similarity metric, thereby facilitating fruitful transfer from tasks regardless of their similarity or dissimilarity. Additionally, SHLPT incorporates a parameter pool to combat catastrophic forgetting effectively. Our experiments shows that SHLPT outperforms state-of-the-art techniques in lifelong learning benchmarks and demonstrates robustness against negative transfer in diverse task sequences.