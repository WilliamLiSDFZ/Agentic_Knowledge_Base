---
title: "LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/9f4cc62d0632911c63163ea3d9ec19bd-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'llm-training-and-optimization-techniques']
tags: ['LLM-compression', 'benchmarking', 'efficient-deployment']
venue: "NeurIPS 2024"
tldr: "LLMCBench provides a comprehensive benchmark for systematically evaluating large language model compression techniques for efficient deployment."
---

# LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/9f4cc62d0632911c63163ea3d9ec19bd-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/9f4cc62d0632911c63163ea3d9ec19bd-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: LLMCBench provides a comprehensive benchmark for systematically evaluating large language model compression techniques for efficient deployment.

## Abstract

Although large language models (LLMs) have demonstrated their strong intelligence ability, the high demand for computation and storage hinders their practical application. To this end, many model compression techniques are proposed to increase the efficiency of LLMs. However, current researches only validate their methods on limited models, datasets, metrics, etc, and still lack a comprehensive evaluation under more general scenarios. So it is still a question of which model compression approach we should use under a specific case. To mitigate this gap, we present the Large Language Model Compression Benchmark (LLMCBench), a rigorously designed benchmark with an in-depth analysis for LLM compression algorithms. We first analyze the actual model production requirements and carefully design evaluation tracks and metrics. Then, we conduct extensive experiments and comparison using multiple mainstream LLM compression approaches. Finally, we perform an in-depth analysis based on the evaluation and provide useful insight for LLM compression design. We hope our LLMCBench can contribute insightful suggestions for LLM compression algorithm design and serve as a foundation for future research.