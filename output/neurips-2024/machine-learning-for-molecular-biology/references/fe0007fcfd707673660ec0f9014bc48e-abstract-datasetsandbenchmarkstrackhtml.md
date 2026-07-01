---
title: "A survey and benchmark of high-dimensional Bayesian optimization of discrete sequences"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/fe0007fcfd707673660ec0f9014bc48e-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'machine-learning-for-molecular-biology']
tags: ['bayesian-optimization', 'discrete-sequences', 'high-dimensional', 'protein-engineering', 'drug-design']
venue: "NeurIPS 2024"
tldr: "A survey and benchmark systematically evaluating high-dimensional Bayesian optimization methods for discrete sequence optimization in biological applications."
---

# A survey and benchmark of high-dimensional Bayesian optimization of discrete sequences

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/fe0007fcfd707673660ec0f9014bc48e-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/fe0007fcfd707673660ec0f9014bc48e-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A survey and benchmark systematically evaluating high-dimensional Bayesian optimization methods for discrete sequence optimization in biological applications.

## Abstract

Optimizing discrete black-box functions is key in several domains, e.g. protein engineering and drug design. Due to the lack of gradient information and the need for sample efficiency, Bayesian optimization is an ideal candidate for these tasks. Several methods for high-dimensional continuous and categorical Bayesian optimization have been proposed recently. However, our survey of the field reveals highly heterogeneous experimental set-ups across methods and technical barriers for the replicability and application of published algorithms to real-world tasks. To address these issues, we develop a unified framework to test a vast array of high-dimensional Bayesian optimization methods and a collection of standardized black-box functions representing real-world application domains in chemistry and biology. These two components of the benchmark are each supported by flexible, scalable, and easily extendable software libraries (poli and poli-baselines), allowing practitioners to readily incorporate new optimization objectives or discrete optimizers. Project website: https://machinelearninglifescience.github.io/hdbo_benchmark.