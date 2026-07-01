---
title: "Mercury: A Code Efficiency Benchmark for Code Large Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/1df1df43b58845650b8dada00fca9772-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'llm-training-and-optimization-techniques']
tags: ['code-efficiency', 'benchmark', 'code-llm', 'computational-efficiency', 'evaluation']
venue: "NeurIPS 2024"
tldr: "Introduces Mercury, the first benchmark evaluating Code LLMs on computational efficiency of generated code beyond mere functional correctness."
---

# Mercury: A Code Efficiency Benchmark for Code Large Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/1df1df43b58845650b8dada00fca9772-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/1df1df43b58845650b8dada00fca9772-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces Mercury, the first benchmark evaluating Code LLMs on computational efficiency of generated code beyond mere functional correctness.

## Abstract

Amidst the recent strides in evaluating Large Language Models for Code (Code LLMs), existing benchmarks have mainly focused on the functional correctness of generated code, neglecting the importance of their computational efficiency. To fill the gap, we present Mercury, the first code efficiency benchmark for Code LLMs. It comprises 1,889 Python tasks, each accompanied by adequate solutions that serve as real-world efficiency baselines, enabling a comprehensive analysis of the runtime distribution. Based on the distribution, we introduce a new metric Beyond, which computes a runtime-percentile-weighted Pass score to reflect functional correctness and code efficiency simultaneously. On Mercury, leading Code LLMs can achieve 65% on Pass, while less than 50% on Beyond. Given that an ideal Beyond score would be aligned with the Pass score, it indicates that while Code LLMs exhibit impressive capabilities in generating functionally correct code, there remains a notable gap in their efficiency. Finally, our empirical experiments reveal that Direct Preference Optimization (DPO) serves as a robust baseline for enhancing code efficiency compared with Supervised Fine Tuning (SFT), which paves a promising avenue for future exploration of efficient code generation. Our code and data are available on GitHub: https://github.com/Elfsong/Mercury.