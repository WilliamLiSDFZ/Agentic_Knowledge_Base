---
title: "Towards Heterogeneous Long-tailed Learning: Benchmarking, Metrics, and Toolbox"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/85cd8edc556709341b2ef6c4d5725545-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['long-tailed-learning', 'benchmarking', 'heterogeneous-data']
venue: "NeurIPS 2024"
tldr: "Introduces a comprehensive benchmark, metrics, and toolbox for heterogeneous long-tailed learning across multiple domains."
---

# Towards Heterogeneous Long-tailed Learning: Benchmarking, Metrics, and Toolbox

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/85cd8edc556709341b2ef6c4d5725545-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/85cd8edc556709341b2ef6c4d5725545-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces a comprehensive benchmark, metrics, and toolbox for heterogeneous long-tailed learning across multiple domains.

## Abstract

Long-tailed data distributions pose challenges for a variety of domains like e-commerce, finance, biomedical science, and cyber security, where the performance of machine learning models is often dominated by head categories while tail categories are inadequately learned. This work aims to provide a systematic view of long-tailed learning with regard to three pivotal angles: (A1) the characterization of data long-tailedness, (A2) the data complexity of various domains, and (A3) the heterogeneity of emerging tasks. We develop HeroLT, a comprehensive long-tailed learning benchmark integrating 18 state-of-the-art algorithms, 10 evaluation metrics, and 17 real-world datasets across 6 tasks and 4 data modalities. HeroLT with novel angles and extensive experiments (315 in total) enables effective and fair evaluation of newly proposed methods compared with existing baselines on varying dataset types. Finally, we conclude by highlighting the significant applications of long-tailed learning and identifying several promising future directions. For accessibility and reproducibility, we open-source our benchmark HeroLT and corresponding results at https://github.com/SSSKJ/HeroLT.