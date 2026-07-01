---
title: "BenchX: A Unified Benchmark Framework for Medical Vision-Language Pretraining on Chest X-Rays"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/0cb35e10bf7bb73d10c12414edbd63fd-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['medical-vision-language', 'chest-X-ray', 'benchmark', 'pretraining', 'evaluation-framework']
venue: "NeurIPS 2024"
tldr: "A unified benchmark framework for systematically evaluating medical vision-language pretraining methods on chest X-rays."
---

# BenchX: A Unified Benchmark Framework for Medical Vision-Language Pretraining on Chest X-Rays

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/0cb35e10bf7bb73d10c12414edbd63fd-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/0cb35e10bf7bb73d10c12414edbd63fd-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A unified benchmark framework for systematically evaluating medical vision-language pretraining methods on chest X-rays.

## Abstract

Medical Vision-Language Pretraining (MedVLP) shows promise in learning generalizable and transferable visual representations from paired and unpaired medical images and reports. MedVLP can provide useful features to downstream tasks and facilitate adapting task-specific models to new setups using fewer examples. However, existing MedVLP methods often differ in terms of datasets, preprocessing, and finetuning implementations. This pose great challenges in evaluating how well a MedVLP method generalizes to various clinically-relevant tasks due to the lack of unified, standardized, and comprehensive benchmark. To fill this gap, we propose BenchX, a unified benchmark framework that enables head-to-head comparison and systematical analysis between MedVLP methods using public chest X-ray datasets. Specifically, BenchX is composed of three components: 1) Comprehensive datasets covering nine datasets and four medical tasks; 2) Benchmark suites to standardize data preprocessing, train-test splits, and parameter selection; 3) Unified finetuning protocols that accommodate heterogeneous MedVLP methods for consistent task adaptation in classification, segmentation, and report generation, respectively. Utilizing BenchX, we establish baselines for nine state-of-the-art MedVLP methods and found that the performance of some early MedVLP methods can be enhanced to surpass more recent ones, prompting a revisiting of the developments and conclusions from prior works in MedVLP. Our code are available at https://github.com/yangzhou12/BenchX.