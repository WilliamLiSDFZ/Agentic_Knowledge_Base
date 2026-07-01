---
title: "SciCode: A Research Coding Benchmark Curated by Scientists"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/36850592258c8c41cecdaa3dea5ff7de-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'neural-networks-for-formal-reasoning-and-verification']
tags: ['scientific-coding-benchmark', 'language-models', 'code-generation', 'research-problems', 'evaluation']
venue: "NeurIPS 2024"
tldr: "SciCode is a benchmark curated by scientists to evaluate language models' ability to generate code solving real scientific research problems."
---

# SciCode: A Research Coding Benchmark Curated by Scientists

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/36850592258c8c41cecdaa3dea5ff7de-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/36850592258c8c41cecdaa3dea5ff7de-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: SciCode is a benchmark curated by scientists to evaluate language models' ability to generate code solving real scientific research problems.

## Abstract

Since language models (LMs) now outperform average humans on many challenging tasks, it is becoming increasingly difficult to develop challenging, high-quality, and realistic evaluations. We address this by examining LM capabilities to generate code for solving real scientific research problems. Incorporating input from scientists and AI researchers in 16 diverse natural science sub-fields, including mathematics, physics, chemistry, biology, and materials science, we create a scientist-curated coding benchmark, SciCode. The problems naturally factorize into multiple subproblems, each involving knowledge recall, reasoning, and code synthesis. In total, SciCode contains 338 subproblems decomposed from 80 challenging main problems, and it offers optional descriptions specifying useful scientific background information and scientist-annotated gold-standard solutions and test cases for evaluation. OpenAI o1-preview, the best-performing model among those tested, can solve only 7.7\% of the problems in the most realistic setting. We believe that SciCode demonstrates both contemporary LMs' progress towards realizing helpful scientific assistants and sheds light on the building and evaluation of scientific AI in the future.