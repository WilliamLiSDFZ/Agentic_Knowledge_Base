---
title: "The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/370df50ccfdf8bde18f8f9c2d9151bda-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-training-and-optimization-techniques', 'ai-benchmarking-and-evaluation-methodology']
tags: ['pretraining-data', 'web-text-curation', 'data-quality', 'large-language-models', 'dataset']
venue: "NeurIPS 2024"
tldr: "FineWeb introduces large-scale, high-quality web text datasets with a decanting pipeline to improve LLM pretraining performance."
---

# The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/370df50ccfdf8bde18f8f9c2d9151bda-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/370df50ccfdf8bde18f8f9c2d9151bda-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: FineWeb introduces large-scale, high-quality web text datasets with a decanting pipeline to improve LLM pretraining performance.

## Abstract

The performance of a large language model (LLM) depends heavily on the quality and size of its pretraining dataset. However, the pretraining datasets for state-of-the-art open LLMs like Llama 3 and Mixtral are not publicly available and very little is known about how they were created. In this work, we introduce FineWeb, a 15-trillion token dataset derived from 96 Common Crawl snapshots that produces better-performing LLMs than other open pretraining datasets. To advance the understanding of how best to curate high-quality pretraining datasets, we carefully document and ablate all of the design choices used in FineWeb, including in-depth investigations of deduplication and filtering strategies. In addition, we introduce FineWeb-Edu, a 1.3-trillion token collection of educational text filtered from FineWeb. LLMs pretrained on FineWeb-Edu exhibit dramatically better performance on knowledge- and reasoning-intensive benchmarks like MMLU and ARC. Along with our datasets, we publicly release our data curation codebase and all of the models trained during our ablation experiments.