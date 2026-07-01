---
title: "MARVEL: Multidimensional Abstraction and Reasoning through Visual Evaluation and Learning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/529d8b3a23991e83db07f21727256374-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning']
tags: ['abstract-visual-reasoning', 'multimodal-llm', 'benchmark']
venue: "NeurIPS 2024"
tldr: "Introduces MARVEL, a benchmark assessing multidimensional abstract visual reasoning capabilities of multimodal large language models."
---

# MARVEL: Multidimensional Abstraction and Reasoning through Visual Evaluation and Learning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/529d8b3a23991e83db07f21727256374-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/529d8b3a23991e83db07f21727256374-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces MARVEL, a benchmark assessing multidimensional abstract visual reasoning capabilities of multimodal large language models.

## Abstract

While multi-modal large language models (MLLMs) have shown significant progress across popular visual reasoning benchmarks, whether they possess abstract visual reasoning abilities remains an open question. Similar to the Sudoku puzzles, abstract visual reasoning (AVR) problems require finding high-level patterns (e.g., repetition constraints on numbers) that control the input shapes (e.g., digits) in a specific task configuration (e.g., matrix). However, existing AVR benchmarks only consider a limited set of patterns (addition, conjunction), input shapes (rectangle, square), and task configurations (3 × 3 matrices). And they fail to capture all abstract reasoning patterns in human cognition necessary for addressing real-world tasks, such as geometric properties and object boundary understanding in real-world navigation. To evaluate MLLMs’ AVR abilities systematically, we introduce MARVEL founded on the core knowledge system in human cognition, a multi-dimensional AVR benchmark with 770 puzzles composed of six core knowledge patterns, geometric and abstract shapes, and five different task configurations. To inspect whether the model performance is grounded in perception or reasoning, MARVEL complements the standard AVR question with perception questions in a hierarchical evaluation framework. We conduct comprehensive experiments on MARVEL with ten representative MLLMs in zero-shot and few-shot settings. Our experiments reveal that all MLLMs show near-random performance on MARVEL, with significant performance gaps (40%) compared to humans across all patterns and task configurations. Further analysis of perception questions reveals that MLLMs struggle to comprehend the visual features (near-random performance). Although closed-source MLLMs, such as GPT-4V, show a promising understanding of reasoning patterns (on par with humans) after adding textual descriptions, this advantage is hindered by their weak perception abilities. We release our entirecode and dataset at https://github.com/1171-jpg/MARVEL_AVR.