---
title: "DevBench: A multimodal developmental benchmark for language learning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/8d987b2981388c99c7eab6095d1d29fd-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'visual-language-multimodal-generation-reasoning']
tags: ['developmental-benchmark', 'vision-language-models', 'child-language-learning']
venue: "NeurIPS 2024"
tldr: "DevBench introduces a multimodal developmental benchmark to compare learning trajectories of vision-language models against children's language acquisition."
---

# DevBench: A multimodal developmental benchmark for language learning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/8d987b2981388c99c7eab6095d1d29fd-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/8d987b2981388c99c7eab6095d1d29fd-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: DevBench introduces a multimodal developmental benchmark to compare learning trajectories of vision-language models against children's language acquisition.

## Abstract

How (dis)similar are the learning trajectories of vision–language models and children? Recent modeling work has attempted to understand the gap between models’ and humans’ data efficiency by constructing models trained on less data, especially multimodal naturalistic data. However, such models are often evaluated on adult-level benchmarks, with limited breadth in language abilities tested, and without direct comparison to behavioral data. We introduce DevBench, a multimodal benchmark comprising seven language evaluation tasks spanning the domains of lexical, syntactic, and semantic ability, with behavioral data from both children and adults. We evaluate a set of vision–language models on these tasks, comparing models and humans on their response patterns, not their absolute performance. Across tasks, models exhibit variation in their closeness to human response patterns, and models that perform better on a task also more closely resemble human behavioral responses. We also examine the developmental trajectory of OpenCLIP over training, finding that greater training results in closer approximations to adult response patterns. DevBench thus provides a benchmark for comparing models to human language development. These comparisons highlight ways in which model and human language learning processes diverge, providing insight into entry points for improving language models.