---
title: "Towards General Loop Invariant Generation: A Benchmark of Programs with Memory Manipulation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/e93b673c55d6768cdd39ce90de8c4d4c-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['neural-networks-for-formal-reasoning-and-verification', 'ai-benchmarking-and-evaluation-methodology']
tags: ['loop-invariants', 'program-verification', 'benchmark']
venue: "NeurIPS 2024"
tldr: "A benchmark of programs with memory manipulation to advance general loop invariant generation for formal program verification."
---

# Towards General Loop Invariant Generation: A Benchmark of Programs with Memory Manipulation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/e93b673c55d6768cdd39ce90de8c4d4c-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/e93b673c55d6768cdd39ce90de8c4d4c-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A benchmark of programs with memory manipulation to advance general loop invariant generation for formal program verification.

## Abstract

Program verification is vital for ensuring software reliability, especially in the context of increasingly complex systems. Loop invariants, remaining true before and after each iteration of loops, are crucial for this verification process. Traditional provers and machine learning based methods for generating loop invariants often require expert intervention or extensive labeled data, and typically only handle numerical property verification. These methods struggle with programs involving complex data structures and memory manipulations, limiting their applicability and automation capabilities. This paper introduces a new benchmark named LIG-MM, specifically for programs with complex data structures and memory manipulations. We collect 312 programs from various sources, including daily programs from college homework, the international competition (SV-COMP), benchmarks from previous papers (SLING), and programs from real-world software systems (Linux Kernel, GlibC, LiteOS, and Zephyr). Based on LIG-MM, our findings indicate that previous methods, including GPT-4, fail to automate verification for these programs. Consequently, we propose a novel LLM-SE framework that coordinates LLM with symbolic execution, fine-tuned using self-supervised learning, to generate loop invariants. Experimental results on LIG-MM demonstrate that our LLM-SE outperforms state-of-the-art methods, offering a new direction toward automated program verification in real-world scenarios.