---
title: "OpenMathInstruct-1: A 1.8 Million Math Instruction Tuning Dataset"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/3d5aa9a7ce28cdc710fbd044fd3610f3-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-training-and-optimization-techniques']
tags: ['math-instruction-tuning', 'synthetic-dataset', 'llm-training']
venue: "NeurIPS 2024"
tldr: "Introduces OpenMathInstruct-1, a 1.8 million example synthetically generated dataset for math instruction tuning of large language models."
---

# OpenMathInstruct-1: A 1.8 Million Math Instruction Tuning Dataset

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/3d5aa9a7ce28cdc710fbd044fd3610f3-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/3d5aa9a7ce28cdc710fbd044fd3610f3-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces OpenMathInstruct-1, a 1.8 million example synthetically generated dataset for math instruction tuning of large language models.

## Abstract

Recent work has shown the immense potential of synthetically generated datasets for training large language models (LLMs), especially for acquiring targeted skills. Current large-scale math instruction tuning datasets such as MetaMathQA (Yu et al., 2024) and MAmmoTH (Yue et al., 2024) are constructed using outputs from closed-source LLMs with commercially restrictive licenses. A key reason limiting the use of open-source LLMs in these data generation pipelines has been the wide gap between the mathematical skills of the best closed-source LLMs, such as GPT-4, and the best open-source LLMs. Building on the recent progress in open-source LLMs, our proposed prompting novelty, and some brute-force scaling, we construct OpenMathInstruct-1, a math instruction tuning dataset with 1.8M problem-solution pairs. The dataset is constructed by synthesizing code-interpreter solutions for GSM8K and MATH, two popular math reasoning benchmarks, using the recently released and permissively licensed Mixtral model. Our best model, OpenMath-CodeLlama-70B, trained on a subset of OpenMathInstruct-1, achieves a score of 84.6% on GSM8K and 50.7% on MATH, which is competitive with the best gpt-distilled models. We will release our code, models, and the OpenMathInstruct-1 dataset under a commercially permissive license.