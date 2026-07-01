---
title: "Is Function Similarity Over-Engineered? Building a Benchmark"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/2663c994c84a79b338bca613fe1ae223-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'machine-learning-theory-and-evaluation-methods']
tags: ['binary-analysis', 'function-similarity', 'security-benchmarking']
venue: "NeurIPS 2024"
tldr: "A benchmark is constructed to evaluate whether existing function similarity approaches are over-engineered for binary analysis security tasks."
---

# Is Function Similarity Over-Engineered? Building a Benchmark

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/2663c994c84a79b338bca613fe1ae223-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/2663c994c84a79b338bca613fe1ae223-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A benchmark is constructed to evaluate whether existing function similarity approaches are over-engineered for binary analysis security tasks.

## Abstract

Binary analysis is a core component of many critical security tasks, including reverse engineering, malware analysis, and vulnerability detection. Manual analysis is often time-consuming, but identifying commonly-used or previously-seen functions can reduce the time it takes to understand a new file. However, given the complexity of assembly, and the NP-hard nature of determining function equivalence, this task is extremely difficult. Common approaches often use sophisticated disassembly and decompilation tools, graph analysis, and other expensive pre-processing steps to perform function similarity searches over some corpus. In this work, we identify a number of discrepancies between the current research environment and the underlying application need. To remedy this, we build a new benchmark, REFuSe-Bench, for binary function similarity detection consisting of high-quality datasets and tests that better reflect real-world use cases. In doing so, we address issues like data duplication and accurate labeling, experiment with real malware, and perform the first serious evaluation of ML binary function similarity models on Windows data. Our benchmark reveals that a new, simple baseline — one which looks at only the raw bytes of a function, and requires no disassembly or other pre-processing --- is able to achieve state-of-the-art performance in multiple settings. Our findings challenge conventional assumptions that complex models with highly-engineered features are being used to their full potential, and demonstrate that simpler approaches can provide significant value.