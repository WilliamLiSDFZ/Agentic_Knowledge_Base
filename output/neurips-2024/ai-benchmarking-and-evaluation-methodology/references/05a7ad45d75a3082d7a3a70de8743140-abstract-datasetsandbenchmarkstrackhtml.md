---
title: "CARE: a Benchmark Suite for the Classification and Retrieval of Enzymes"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/05a7ad45d75a3082d7a3a70de8743140-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['machine-learning-for-molecular-biology', 'ai-benchmarking-and-evaluation-methodology']
tags: ['enzyme-function-prediction', 'benchmark', 'protein-sequence']
venue: "NeurIPS 2024"
tldr: "CARE introduces a standardized benchmark suite for evaluating machine learning methods for enzyme classification and retrieval from sequence."
---

# CARE: a Benchmark Suite for the Classification and Retrieval of Enzymes

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/05a7ad45d75a3082d7a3a70de8743140-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/05a7ad45d75a3082d7a3a70de8743140-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: CARE introduces a standardized benchmark suite for evaluating machine learning methods for enzyme classification and retrieval from sequence.

## Abstract

Enzymes are important proteins that catalyze chemical reactions. In recent years, machine learning methods have emerged to predict enzyme function from sequence; however, there are no  standardized benchmarks to evaluate these methods. We introduce CARE, a benchmark and dataset suite for the Classification And Retrieval of Enzymes (CARE). CARE centers on two tasks: (1) classification of a protein sequence by its enzyme commission (EC) number and (2) retrieval of an EC number given a chemical reaction. For each task, we design train-test splits to evaluate different kinds of out-of-distribution generalization that are relevant to real use cases. For the classification task, we provide baselines for state-of-the-art methods. Because the retrieval task has not been previously formalized, we propose a method called Contrastive Reaction-EnzymE Pretraining (CREEP) as one of the first baselines for this task and compare it to the recent method, CLIPZyme. CARE is available at https://github.com/jsunn-y/CARE/.