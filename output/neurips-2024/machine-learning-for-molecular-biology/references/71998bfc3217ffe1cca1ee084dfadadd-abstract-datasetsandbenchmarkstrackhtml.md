---
title: "DART-Eval: A Comprehensive DNA Language Model Evaluation Benchmark on Regulatory DNA"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/71998bfc3217ffe1cca1ee084dfadadd-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['machine-learning-for-molecular-biology', 'ai-benchmarking-and-evaluation-methodology']
tags: ['dna-language-models', 'genomic-benchmarks', 'regulatory-dna']
venue: "NeurIPS 2024"
tldr: "Introduces DART-Eval, a comprehensive benchmark for evaluating DNA language models on diverse regulatory DNA prediction tasks."
---

# DART-Eval: A Comprehensive DNA Language Model Evaluation Benchmark on Regulatory DNA

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/71998bfc3217ffe1cca1ee084dfadadd-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/71998bfc3217ffe1cca1ee084dfadadd-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces DART-Eval, a comprehensive benchmark for evaluating DNA language models on diverse regulatory DNA prediction tasks.

## Abstract

Recent advances in self-supervised models for natural language, vision, and protein sequences have inspired the development of large genomic DNA language models (DNALMs). These models aim to learn generalizable representations of diverse DNA elements, potentially enabling various genomic prediction, interpretation and design tasks. Despite their potential, existing benchmarks do not adequately assess the capabilities of DNALMs on key downstream applications involving an important class of non-coding DNA elements critical for regulating gene activity. In this study, we introduce DART-Eval, a suite of representative benchmarks specifically focused on regulatory DNA to evaluate model performance across zero-shot, probed, and fine-tuned scenarios against contemporary ab initio models as baselines. Our benchmarks target biologically meaningful downstream tasks such as functional sequence feature discovery, predicting cell-type specific regulatory activity, and counterfactual prediction of the impacts of genetic variants. We find that current DNALMs exhibit inconsistent performance and do not offer compelling gains over alternative baseline models for most tasks, while requiring significantly more computational resources. We discuss potentially promising modeling, data curation, and evaluation strategies for the next generation of DNALMs. Our  code is available at https://github.com/kundajelab/DART-Eval