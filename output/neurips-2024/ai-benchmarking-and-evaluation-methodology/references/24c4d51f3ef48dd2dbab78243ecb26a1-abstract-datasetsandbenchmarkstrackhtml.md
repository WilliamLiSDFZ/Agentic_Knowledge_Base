---
title: "A benchmark for prediction of transcriptomic responses to chemical perturbations across cell types"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/24c4d51f3ef48dd2dbab78243ecb26a1-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['machine-learning-for-molecular-biology', 'ai-benchmarking-and-evaluation-methodology']
tags: ['single-cell-transcriptomics', 'drug-perturbation', 'chemical-perturbations', 'cell-types', 'benchmark']
venue: "NeurIPS 2024"
tldr: "Presents a benchmark for predicting transcriptomic responses to chemical perturbations across diverse cell types using single-cell data."
---

# A benchmark for prediction of transcriptomic responses to chemical perturbations across cell types

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/24c4d51f3ef48dd2dbab78243ecb26a1-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/24c4d51f3ef48dd2dbab78243ecb26a1-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents a benchmark for predicting transcriptomic responses to chemical perturbations across diverse cell types using single-cell data.

## Abstract

Single-cell transcriptomics has revolutionized our understanding of cellular heterogeneity and drug perturbation effects. However, its high cost and the vast chemical space of potential drugs present barriers to experimentally characterizing the effect of chemical perturbations in all the myriad cell types of the human body. To overcome these limitations, several groups have proposed using machine learning methods to directly predict the effect of chemical perturbations either across cell contexts or chemical space. However, advances in this field have been hindered by a lack of well-designed evaluation datasets and benchmarks. To drive innovation in perturbation modeling, the Open Problems Perturbation Prediction (OP3) benchmark introduces a framework for predicting the effects of small molecule perturbations on cell type-specific gene expression. OP3 leverages the Open Problems in Single-cell Analysis benchmarking infrastructure and is enabled by a new single-cell perturbation dataset, encompassing 146 compounds tested on human blood cells. The benchmark includes diverse data representations, evaluation metrics, and winning methods from our "Single-cell perturbation prediction: generalizing experimental interventions to unseen contexts" competition at NeurIPS 2023. We envision that the OP3 benchmark and competition will drive innovation in single-cell perturbation prediction by improving the accessibility, visibility, and feasibility of this challenge, thereby promoting the impact of machine learning in drug discovery.