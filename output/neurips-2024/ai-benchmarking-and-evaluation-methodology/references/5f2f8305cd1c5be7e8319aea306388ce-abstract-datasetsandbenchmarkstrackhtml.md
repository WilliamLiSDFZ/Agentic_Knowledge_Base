---
title: "WelQrate: Defining the Gold Standard in Small Molecule Drug Discovery Benchmarking"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/5f2f8305cd1c5be7e8319aea306388ce-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['machine-learning-for-molecular-biology', 'ai-benchmarking-and-evaluation-methodology']
tags: ['drug-discovery', 'benchmarking', 'small-molecule']
venue: "NeurIPS 2024"
tldr: "WelQrate establishes gold-standard benchmarking practices for deep learning in small molecule drug discovery."
---

# WelQrate: Defining the Gold Standard in Small Molecule Drug Discovery Benchmarking

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/5f2f8305cd1c5be7e8319aea306388ce-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/5f2f8305cd1c5be7e8319aea306388ce-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: WelQrate establishes gold-standard benchmarking practices for deep learning in small molecule drug discovery.

## Abstract

While deep learning has revolutionized computer-aided drug discovery, the AI community has predominantly focused on model innovation and placed less emphasis on establishing best benchmarking practices. We posit that without a sound model evaluation framework, the AI community's efforts cannot reach their full potential, thereby slowing the progress and transfer of innovation into real-world drug discovery.Thus, in this paper, we seek to establish a new gold standard for small molecule drug discovery benchmarking, WelQrate. Specifically, our contributions are threefold: WelQrate dataset collection - we introduce a meticulously curated collection of 9 datasets spanning 5 therapeutic target classes. Our hierarchical curation pipelines, designed by drug discovery experts, go beyond the primary high-throughput screen by leveraging additional confirmatory and counter screens along with rigorous domain-driven preprocessing, such as Pan-Assay Interference Compounds (PAINS) filtering, to ensure the high-quality data in the datasets; WelQrate Evaluation Framework - we propose a standardized model evaluation framework considering high-quality datasets, featurization, 3D conformation generation, evaluation metrics, and data splits, which provides a reliable benchmarking for drug discovery experts conducting real-world virtual screening; Benchmarking - we evaluate model performance through various research questions using the WelQrate dataset collection, exploring the effects of different models, dataset quality, featurization methods, and data splitting strategies on the results.In summary, we recommend adopting our proposed WelQrate as the gold standard in small molecule drug discovery benchmarking. The WelQrate dataset collection, along with the curation codes, and experimental scripts are all publicly available at www.WelQrate.org.