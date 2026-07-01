---
title: "CoMix: A Comprehensive Benchmark for Multi-Task Comic Understanding"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/fe79898dcf078ec54b6feeea10ebb751-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'visual-language-multimodal-generation-reasoning']
tags: ['comic-understanding', 'multi-task-benchmark', 'visual-reasoning']
venue: "NeurIPS 2024"
tldr: "Presents CoMix, a comprehensive benchmark for evaluating multi-task understanding capabilities of models on comic content."
---

# CoMix: A Comprehensive Benchmark for Multi-Task Comic Understanding

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/fe79898dcf078ec54b6feeea10ebb751-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/fe79898dcf078ec54b6feeea10ebb751-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents CoMix, a comprehensive benchmark for evaluating multi-task understanding capabilities of models on comic content.

## Abstract

The comic domain is rapidly advancing with the development of single-page analysis and synthesis models. However, evaluation metrics and datasets lag behind, often limited to small-scale or single-style test sets. We introduce a novel benchmark, CoMix, designed to evaluate the multi-task capabilities of models in comic analysis. Unlike existing benchmarks that focus on isolated tasks such as object detection or text recognition, CoMix addresses a broader range of tasks including object detection, speaker identification, character re-identification, reading order, and multi-modal reasoning tasks like character naming and dialogue generation. Our benchmark comprises three existing datasets with expanded annotations to support multi-task evaluation. To mitigate the over-representation of manga-style data, we have incorporated a new dataset of carefully selected American comic-style books, thereby enriching the diversity of comic styles. CoMix is designed to assess pre-trained models in zero-shot and limited fine-tuning settings, probing their transfer capabilities across different comic styles and tasks. The validation split of the benchmark is publicly available for research purposes, and an evaluation server for the held-out test split is also provided. Comparative results between human performance and state-of-the-art models reveal a significant performance gap, highlighting substantial opportunities for advancements in comic understanding. The dataset, baseline models, and code are accessible at https://github.com/emanuelevivoli/CoMix-dataset. This initiative sets a new standard for comprehensive comic analysis, providing the community with a common benchmark for evaluation on a large and varied set.