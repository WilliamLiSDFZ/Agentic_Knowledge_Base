---
title: "V-PETL Bench: A Unified Visual Parameter-Efficient Transfer Learning Benchmark"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/935de67d1a033fd517cb49d192b5c008-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['parameter-efficient-transfer-learning', 'benchmark', 'computer-vision', 'fine-tuning', 'evaluation']
venue: "NeurIPS 2024"
tldr: "V-PETL Bench provides a unified benchmark for systematically evaluating visual parameter-efficient transfer learning methods across diverse tasks."
---

# V-PETL Bench: A Unified Visual Parameter-Efficient Transfer Learning Benchmark

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/935de67d1a033fd517cb49d192b5c008-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/935de67d1a033fd517cb49d192b5c008-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: V-PETL Bench provides a unified benchmark for systematically evaluating visual parameter-efficient transfer learning methods across diverse tasks.

## Abstract

Parameter-efficient transfer learning (PETL) methods show promise in adapting a pre-trained model to various downstream tasks while training only a few parameters. In the computer vision (CV) domain, numerous PETL algorithms have been proposed, but their direct employment or comparison remains inconvenient. To address this challenge, we construct a Unified Visual PETL Benchmark (V-PETL Bench) for the CV domain by selecting 30 diverse, challenging, and comprehensive datasets from image recognition, video action recognition, and dense prediction tasks. On these datasets, we systematically evaluate 25 dominant PETL algorithms and open-source a modular and extensible codebase for fair evaluation of these algorithms. V-PETL Bench runs on NVIDIA A800 GPUs and requires approximately 310 GPU days. We release all the benchmark, making it more efficient and friendly to researchers. Additionally, V-PETL Bench will be continuously updated for new PETL algorithms and CV tasks.