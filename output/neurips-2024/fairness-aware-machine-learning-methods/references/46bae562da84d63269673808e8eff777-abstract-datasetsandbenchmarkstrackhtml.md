---
title: "ABCFair: an Adaptable Benchmark approach for Comparing Fairness Methods"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/46bae562da84d63269673808e8eff777-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['fairness-aware-machine-learning-methods', 'ai-benchmarking-and-evaluation-methodology']
tags: ['fairness', 'benchmark', 'bias-mitigation']
venue: "NeurIPS 2024"
tldr: "ABCFair proposes an adaptable benchmarking framework for systematically comparing fairness methods across diverse problem settings."
---

# ABCFair: an Adaptable Benchmark approach for Comparing Fairness Methods

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/46bae562da84d63269673808e8eff777-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/46bae562da84d63269673808e8eff777-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: ABCFair proposes an adaptable benchmarking framework for systematically comparing fairness methods across diverse problem settings.

## Abstract

Numerous methods have been implemented that pursue fairness with respect to sensitive features by mitigating biases in machine learning. Yet, the problem settings that each method tackles vary significantly, including the stage of intervention, the composition of sensitive features, the fairness notion, and the distribution of the output. Even in binary classification, the greatest common denominator of problem settings is small, significantly complicating benchmarking.Hence, we introduce ABCFair, a benchmark approach which allows adapting to the desiderata of the real-world problem setting, enabling proper comparability between methods for any use case. We apply this benchmark to a range of pre-, in-, and postprocessing methods on both large-scale, traditional datasets and on a dual label (biased and unbiased) dataset to sidestep the fairness-accuracy trade-off.