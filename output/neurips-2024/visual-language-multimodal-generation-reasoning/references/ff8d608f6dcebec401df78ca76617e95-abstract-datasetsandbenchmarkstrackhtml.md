---
title: "Data curation via joint example selection further accelerates multimodal learning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/ff8d608f6dcebec401df78ca76617e95-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'multi-task-learning-group-optimization']
tags: ['data-curation', 'multimodal-pretraining', 'batch-selection']
venue: "NeurIPS 2024"
tldr: "Joint batch-level data prioritization outperforms independent example selection for multimodal contrastive pretraining at scale."
---

# Data curation via joint example selection further accelerates multimodal learning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/ff8d608f6dcebec401df78ca76617e95-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/ff8d608f6dcebec401df78ca76617e95-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Joint batch-level data prioritization outperforms independent example selection for multimodal contrastive pretraining at scale.

## Abstract

Data curation is an essential component of large-scale pretraining. In this work, we demonstrate that jointly prioritizing batches of data is more effective for learning than selecting examples independently. Multimodal contrastive objectives expose the dependencies between data and thus naturally yield criteria for measuring the joint learnability of a batch. We derive a simple and tractable algorithm for selecting such batches, which significantly accelerate training beyond individually-prioritized data points. As performance improves by selecting from large super-batches, we  also leverage recent advances in model approximation to reduce the computational overhead of scoring. As a result, our approach—multimodal contrastive learning with joint example selection (JEST)—surpasses state-of-the-art pretraining methods with up to 13× fewer iterations and 10× less computation. Essential to the performance of JEST is the ability to steer the data selection process towards the distribution of smaller, well-curated datasets via pretrained reference models, exposing data curation as a new dimension for neural scaling laws.