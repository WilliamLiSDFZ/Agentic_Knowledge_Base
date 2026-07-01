---
title: "Scalable Early Childhood Reading Performance Prediction"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/862170d83a17b7c2ef3c5a58e7f1992d-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['reading-performance-prediction', 'educational-data', 'early-childhood']
venue: "NeurIPS 2024"
tldr: "Develops scalable models and a public dataset for predicting early childhood reading performance to enable proactive educational interventions."
---

# Scalable Early Childhood Reading Performance Prediction

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/862170d83a17b7c2ef3c5a58e7f1992d-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/862170d83a17b7c2ef3c5a58e7f1992d-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Develops scalable models and a public dataset for predicting early childhood reading performance to enable proactive educational interventions.

## Abstract

Models for student reading performance can empower educators and institutions to proactively identify at-risk students, thereby enabling early and tailored instructional interventions. However, there are no suitable publicly available educational datasets for modeling and predicting future reading performance. In this work, we introduce the Enhanced Core Reading Instruction (ECRI) dataset, a novel large-scale longitudinal tabular dataset collected across 44 schools with 6,916 students and 172 teachers. We leverage the dataset to empirically evaluate the ability of state-of-the-art machine learning models to recognize early childhood educational patterns in multivariate and partial measurements. Specifically, we demonstrate a simple self-supervised strategy in which a Multi-Layer Perception (MLP) network is pre-trained over masked inputs to outperform several strong baselines while generalizing over diverse educational settings. To facilitate future developments in precise modeling and responsible use of models for individualized and early intervention strategies, our data and code are available at https://ecri-data.github.io/.