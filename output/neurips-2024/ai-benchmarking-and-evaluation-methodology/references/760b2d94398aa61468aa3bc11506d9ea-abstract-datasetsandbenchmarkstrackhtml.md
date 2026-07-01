---
title: "Paloma: A Benchmark for Evaluating Language Model Fit"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/760b2d94398aa61468aa3bc11506d9ea-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'machine-learning-theory-and-evaluation-methods']
tags: ['language-model-evaluation', 'perplexity', 'domain-benchmark']
venue: "NeurIPS 2024"
tldr: "Introduces Paloma, a benchmark for evaluating language model fit across diverse domains using perplexity analysis."
---

# Paloma: A Benchmark for Evaluating Language Model Fit

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/760b2d94398aa61468aa3bc11506d9ea-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/760b2d94398aa61468aa3bc11506d9ea-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces Paloma, a benchmark for evaluating language model fit across diverse domains using perplexity analysis.

## Abstract

Evaluations of language models (LMs) commonly report perplexity on monolithic data held out from training. Implicitly or explicitly, this data is composed of domains—varying distributions of language. We introduce Perplexity Analysis for Language Model Assessment (Paloma), a benchmark to measure LM fit to 546 English and code domains, instead of assuming perplexity on one distribution extrapolates to others. We include two new datasets of the top 100 subreddits (e.g., r/depression on Reddit) and programming languages (e.g., Java on GitHub), both sources common in contemporary LMs. With our benchmark, we release 6 baseline 1B LMs carefully controlled to provide fair comparisons about which pretraining corpus is best and code for others to apply those controls to their own experiments. Our case studies demonstrate how the fine-grained results from Paloma surface findings such as that models pretrained without data beyond Common Crawl exhibit anomalous gaps in LM fit to many domains or that loss is dominated by the most frequently occurring strings in the vocabulary.