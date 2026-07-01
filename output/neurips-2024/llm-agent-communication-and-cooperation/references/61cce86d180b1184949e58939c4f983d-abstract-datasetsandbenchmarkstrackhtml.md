---
title: "APIGen: Automated PIpeline for Generating Verifiable and Diverse Function-Calling Datasets"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/61cce86d180b1184949e58939c4f983d-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-agent-communication-and-cooperation', 'llm-training-and-optimization-techniques']
tags: ['function-calling', 'dataset-generation', 'llm-agents']
venue: "NeurIPS 2024"
tldr: "An automated pipeline for synthesizing verifiable and diverse function-calling datasets to train capable agent models."
---

# APIGen: Automated PIpeline for Generating Verifiable and Diverse Function-Calling Datasets

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/61cce86d180b1184949e58939c4f983d-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/61cce86d180b1184949e58939c4f983d-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: An automated pipeline for synthesizing verifiable and diverse function-calling datasets to train capable agent models.

## Abstract

The advancement of function-calling agent models requires diverse, reliable, and high-quality datasets. This paper presents APIGen, an automated data generation pipeline designed to synthesize high-quality datasets for function-calling applications. We leverage APIGen and collect 3,673 executable APIs across 21 different categories to generate diverse function-calling datasets in a scalable and structured manner. Each data in our dataset is verified through three hierarchical stages: format checking, actual function executions, and semantic verification, improving its reliability and correctness. We demonstrate that models trained with our curated datasets, even with only 7B parameters, can achieve state-of-the-art performance on the Berkeley Function-Calling Benchmark, outperforming multiple GPT-4 models. Moreover, our 1B model achieves exceptional performance, surpassing GPT-3.5-Turbo and Claude-3 Haiku. We release a dataset containing 60,000 high-quality entries, aiming to advance the field of function-calling agent domains. The dataset and models are available on the project homepage \url{https://apigen-pipeline.github.io/}.