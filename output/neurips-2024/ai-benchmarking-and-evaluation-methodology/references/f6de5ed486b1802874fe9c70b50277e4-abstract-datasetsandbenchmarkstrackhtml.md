---
title: "SELECT: A Large-Scale Benchmark of Data Curation Strategies for Image Classification"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/f6de5ed486b1802874fe9c70b50277e4-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['data-curation', 'benchmark', 'image-classification']
venue: "NeurIPS 2024"
tldr: "SELECT is a large-scale benchmark systematically comparing diverse data curation strategies for image classification tasks."
---

# SELECT: A Large-Scale Benchmark of Data Curation Strategies for Image Classification

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/f6de5ed486b1802874fe9c70b50277e4-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/f6de5ed486b1802874fe9c70b50277e4-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: SELECT is a large-scale benchmark systematically comparing diverse data curation strategies for image classification tasks.

## Abstract

Data curation is the problem of how to collect and organize samples into a dataset that supports efficient learning. Despite the centrality of the task, little work has been devoted towards a large-scale, systematic comparison of various curation methods. In this work, we take steps towards a formal evaluation of data curation strategies and introduce SELECT, the first large-scale benchmark of curation strategies for image classification.In order to generate baseline methods for the SELECT benchmark, we create a new dataset, ImageNet++, which constitutes the largest superset of ImageNet-1K to date. Our dataset extends ImageNet with 5 new training-data shifts, each approximately the size of  ImageNet-1K, and each assembled using a distinct curation strategy. We evaluate our data curation baselines in two ways: (i) using each training-data shift to train identical image classification models from scratch (ii) using it to inspect a fixed pretrained self-supervised representation.Our findings show interesting trends, particularly pertaining to recent methods for data curation such as synthetic data generation and lookup based on CLIP embeddings. We show that although these strategies are highly competitive for certain tasks, the curation strategy used to assemble the original ImageNet-1K dataset remains the gold standard. We anticipate that our benchmark can illuminate the path for new methods to further reduce the gap. We release our checkpoints, code, documentation, and a link to our dataset at https://github.com/jimmyxu123/SELECT.