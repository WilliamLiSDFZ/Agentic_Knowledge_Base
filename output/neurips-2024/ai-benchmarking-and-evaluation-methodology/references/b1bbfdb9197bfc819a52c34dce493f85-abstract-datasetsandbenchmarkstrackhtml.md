---
title: "Einsum Benchmark: Enabling the Development of Next-Generation Tensor Execution Engines"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/b1bbfdb9197bfc819a52c34dce493f85-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['tensor-computation', 'einsum', 'benchmarking']
venue: "NeurIPS 2024"
tldr: "A benchmark for einsum operations enabling development and evaluation of next-generation tensor execution engines for ML workflows."
---

# Einsum Benchmark: Enabling the Development of Next-Generation Tensor Execution Engines

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/b1bbfdb9197bfc819a52c34dce493f85-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/b1bbfdb9197bfc819a52c34dce493f85-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A benchmark for einsum operations enabling development and evaluation of next-generation tensor execution engines for ML workflows.

## Abstract

Modern artificial intelligence and machine learning workflows rely on efficient tensor libraries. However, tuning tensor libraries without considering the actual problems they are meant to execute can lead to a mismatch between expected performance and the actual performance. Einsum libraries are tuned to efficiently execute tensor expressions with only a few, relatively large, dense, floating-point tensors. But, practical applications of einsum cover a much broader range of tensor expressions than those that can currently be executed efficiently. For this reason, we have created a benchmark dataset that encompasses this broad range of tensor expressions, allowing future implementations of einsum to build upon and be evaluated against. In addition, we also provide generators for einsum expressions and converters to einsum expressions in our repository, so that additional data can be generated as needed. The benchmark dataset, the generators and converters are released openly and are publicly available at https://benchmark.einsum.org.