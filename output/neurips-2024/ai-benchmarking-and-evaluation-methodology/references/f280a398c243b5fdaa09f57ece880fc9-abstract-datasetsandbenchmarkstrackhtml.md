---
title: "IMDL-BenCo: A Comprehensive Benchmark and Codebase for Image Manipulation Detection & Localization"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/f280a398c243b5fdaa09f57ece880fc9-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'visual-language-multimodal-generation-reasoning']
tags: ['image-manipulation-detection', 'benchmark', 'localization']
venue: "NeurIPS 2024"
tldr: "Presents IMDL-BenCo, a comprehensive benchmark and codebase standardizing evaluation of image manipulation detection and localization methods."
---

# IMDL-BenCo: A Comprehensive Benchmark and Codebase for Image Manipulation Detection & Localization

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/f280a398c243b5fdaa09f57ece880fc9-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/f280a398c243b5fdaa09f57ece880fc9-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents IMDL-BenCo, a comprehensive benchmark and codebase standardizing evaluation of image manipulation detection and localization methods.

## Abstract

A comprehensive benchmark is yet to be established in the Image Manipulation Detection &amp; Localization (IMDL) field. The absence of such a benchmark leads to insufficient and misleading model evaluations, severely undermining the development of this field. However, the scarcity of open-sourced baseline models and inconsistent training and evaluation protocols make conducting rigorous experiments and faithful comparisons among IMDL models challenging. To address these challenges, we introduce IMDL-BenCo, the first comprehensive IMDL benchmark and modular codebase. IMDL-BenCo: i) decomposes the IMDL framework into standardized, reusable components and revises the model construction pipeline, improving coding efficiency and customization flexibility; ii) fully implements or incorporates training code for state-of-the-art models to establish a comprehensive IMDL benchmark; and iii) conducts deep analysis based on the established benchmark and codebase, offering new insights into IMDL model architecture, dataset characteristics, and evaluation standards.Specifically, IMDL-BenCo includes common processing algorithms, 8 state-of-the-art IMDL models (1 of which are reproduced from scratch), 2 sets of standard training and evaluation protocols, 15 GPU-accelerated evaluation metrics, and 3 kinds of robustness evaluation. This benchmark and codebase represent a significant leap forward in calibrating the current progress in the IMDL field and inspiring future breakthroughs.Code is available at: https://github.com/scu-zjz/IMDLBenCo