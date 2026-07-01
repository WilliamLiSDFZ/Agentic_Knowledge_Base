---
title: "HEST-1k: A Dataset For Spatial Transcriptomics and Histology Image Analysis"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/60a899cc31f763be0bde781a75e04458-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['machine-learning-for-molecular-biology', 'ai-benchmarking-and-evaluation-methodology']
tags: ['spatial-transcriptomics', 'histology-image-analysis', 'multimodal-dataset', 'computational-pathology', 'benchmarking']
venue: "NeurIPS 2024"
tldr: "HEST-1k introduces a large-scale dataset pairing spatial transcriptomics with histology images to advance computational methods for tissue molecular analysis."
---

# HEST-1k: A Dataset For Spatial Transcriptomics and Histology Image Analysis

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/60a899cc31f763be0bde781a75e04458-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/60a899cc31f763be0bde781a75e04458-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: HEST-1k introduces a large-scale dataset pairing spatial transcriptomics with histology images to advance computational methods for tissue molecular analysis.

## Abstract

Spatial transcriptomics enables interrogating the molecular composition of tissue with ever-increasing resolution and sensitivity. However, costs, rapidly evolving technology, and lack of standards have constrained computational methods in ST to narrow tasks and small cohorts. In addition, the underlying tissue morphology, as reflected by H&E-stained whole slide images (WSIs), encodes rich information often overlooked in ST studies. Here, we introduce HEST-1k, a collection of 1,229 spatial transcriptomic profiles, each linked to a WSI and extensive metadata. HEST-1k was assembled from 153 public and internal cohorts encompassing 26 organs, two species (Homo Sapiens and Mus Musculus), and 367 cancer samples from 25 cancer types. HEST-1k processing enabled the identification of 2.1 million expression-morphology pairs and over 76 million nuclei. To support its development, we additionally introduce the HEST-Library, a Python package designed to perform a range of actions with HEST samples. We test HEST-1k and Library on three use cases: (1) benchmarking foundation models for pathology (HEST-Benchmark), (2) biomarker exploration, and (3) multimodal representation learning. HEST-1k, HEST-Library, and HEST-Benchmark can be freely accessed at https://github.com/mahmoodlab/hest.