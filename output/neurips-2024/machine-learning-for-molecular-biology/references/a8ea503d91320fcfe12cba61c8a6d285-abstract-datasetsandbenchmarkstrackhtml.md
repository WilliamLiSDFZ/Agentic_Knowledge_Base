---
title: "BEACON: Benchmark for Comprehensive RNA Tasks and Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/a8ea503d91320fcfe12cba61c8a6d285-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['machine-learning-for-molecular-biology', 'ai-benchmarking-and-evaluation-methodology']
tags: ['RNA-language-models', 'benchmarking', 'biological-sequences', 'deep-learning', 'genomics']
venue: "NeurIPS 2024"
tldr: "BEACON is a comprehensive benchmark for evaluating RNA language models across diverse RNA biology tasks."
---

# BEACON: Benchmark for Comprehensive RNA Tasks and Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/a8ea503d91320fcfe12cba61c8a6d285-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/a8ea503d91320fcfe12cba61c8a6d285-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: BEACON is a comprehensive benchmark for evaluating RNA language models across diverse RNA biology tasks.

## Abstract

RNA plays a pivotal role in translating genetic instructions into functional outcomes, underscoring its importance in biological processes and disease mechanisms. Despite the emergence of numerous deep learning approaches for RNA, particularly universal RNA language models, there remains a significant lack of standardized benchmarks to assess the effectiveness of these methods. In this study, we introduce the first comprehensive RNA benchmark BEACON BEnchmArk for  COmprehensive RNA Task and Language Models).First, BEACON comprises 13 distinct tasks derived from extensive previous work covering structural analysis, functional studies, and engineering applications, enabling a comprehensive assessment of the performance of methods on various RNA understanding tasks. Second, we examine a range of models, including traditional approaches like CNNs, as well as advanced RNA foundation models based on language models, offering valuable insights into the task-specific performances of these models. Third, we investigate the vital RNA language model components from the tokenizer and positional encoding aspects. Notably, our findings emphasize the superiority of single nucleotide tokenization and the effectiveness of Attention with Linear Biases (ALiBi) over traditional positional encoding methods. Based on these insights, a simple yet strong baseline called BEACON-B is proposed, which can achieve outstanding performance with limited data and computational resources. The datasets and source code of our benchmark are available at https://github.com/terry-r123/RNABenchmark.