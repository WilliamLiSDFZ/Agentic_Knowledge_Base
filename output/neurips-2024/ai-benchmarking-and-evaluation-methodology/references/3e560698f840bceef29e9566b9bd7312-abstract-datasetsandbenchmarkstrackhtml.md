---
title: "FlexMol: A Flexible Toolkit for Benchmarking Molecular Relational Learning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/3e560698f840bceef29e9566b9bd7312-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['machine-learning-for-molecular-biology', 'ai-benchmarking-and-evaluation-methodology']
tags: ['molecular-relational-learning', 'benchmarking', 'drug-discovery']
venue: "NeurIPS 2024"
tldr: "Presents FlexMol, a flexible benchmarking toolkit for systematically evaluating molecular relational learning methods in drug discovery."
---

# FlexMol: A Flexible Toolkit for Benchmarking Molecular Relational Learning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/3e560698f840bceef29e9566b9bd7312-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/3e560698f840bceef29e9566b9bd7312-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents FlexMol, a flexible benchmarking toolkit for systematically evaluating molecular relational learning methods in drug discovery.

## Abstract

Molecular relational learning (MRL) is crucial for understanding the interaction behaviors between molecular pairs, a critical aspect of drug discovery and development. However, the large feasible model space of MRL poses significant challenges to benchmarking, and existing MRL frameworks face limitations in flexibility and scope. To address these challenges, avoid repetitive coding efforts, and ensure fair comparison of models, we introduce FlexMol, a comprehensive toolkit designed to facilitate the construction and evaluation of diverse model architectures across various datasets and performance metrics. FlexMol offers a robust suite of preset model components, including 16 drug encoders, 13 protein sequence encoders, 9 protein structure encoders, and 7 interaction layers. With its easy-to-use API and flexibility, FlexMol supports the dynamic construction of over 70, 000 distinct combinations of model architectures. Additionally, we provide detailed benchmark results and code examples to demonstrate FlexMol’s effectiveness in simplifying and standardizing MRL model development and comparison. FlexMol is open-sourced and available at https://github.com/Steven51516/FlexMol.