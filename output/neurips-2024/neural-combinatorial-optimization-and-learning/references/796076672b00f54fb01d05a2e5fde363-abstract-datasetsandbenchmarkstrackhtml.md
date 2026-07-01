---
title: "Benchmarking PtO and PnO Methods in the Predictive Combinatorial Optimization Regime"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/796076672b00f54fb01d05a2e5fde363-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['neural-combinatorial-optimization-and-learning', 'ai-benchmarking-and-evaluation-methodology']
tags: ['predict-then-optimize', 'combinatorial-optimization', 'benchmarking', 'decision-making', 'regret']
venue: "NeurIPS 2024"
tldr: "Benchmarks predict-then-optimize and predict-now-optimize methods for predictive combinatorial optimization across real-world applications."
---

# Benchmarking PtO and PnO Methods in the Predictive Combinatorial Optimization Regime

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/796076672b00f54fb01d05a2e5fde363-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/796076672b00f54fb01d05a2e5fde363-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Benchmarks predict-then-optimize and predict-now-optimize methods for predictive combinatorial optimization across real-world applications.

## Abstract

Predictive combinatorial optimization, where the parameters of combinatorial optimization (CO) are unknown at the decision-making time, is the precise modeling of many real-world applications, including energy cost-aware scheduling and budget allocation on advertising. Tackling such a problem usually involves a prediction model and a CO solver. These two modules are integrated into the predictive CO pipeline following two design principles: ''Predict-then-Optimize (PtO)'', which learns predictions by supervised training and subsequently solves CO using predicted coefficients, while the other, named ''Predict-and-Optimize (PnO)'', directly optimizes towards the ultimate decision quality and claims to yield better decisions than traditional PtO approaches. However, there lacks a systematic benchmark of both approaches, including the specific design choices at the module level, as well as an evaluation dataset that covers representative real-world scenarios. To this end, we develop a modular framework to benchmark 11 existing PtO/PnO methods on 8 problems, including a new industrial dataset for combinatorial advertising that will be released. Our study shows that PnO approaches are better than PtO on 7 out of 8 benchmarks, but there is no silver bullet found for the specific design choices of PnO. A comprehensive categorization of current approaches and integration of typical scenarios are provided under a unified benchmark. Therefore, this paper could serve as a comprehensive benchmark for future PnO approach development and also offer fast prototyping for application-focused development. The code is available at \url{https://github.com/Thinklab-SJTU/PredictiveCO-Benchmark}.