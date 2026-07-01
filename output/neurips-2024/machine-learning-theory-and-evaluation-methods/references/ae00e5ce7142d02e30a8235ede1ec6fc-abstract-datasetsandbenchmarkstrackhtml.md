---
title: "A Data-Centric Perspective on Evaluating Machine Learning Models for Tabular Data"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/ae00e5ce7142d02e30a8235ede1ec6fc-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'machine-learning-theory-and-evaluation-methods']
tags: ['tabular-data', 'data-centric-evaluation', 'benchmark']
venue: "NeurIPS 2024"
tldr: "Proposes a data-centric evaluation perspective for comparing machine learning models on tabular data beyond standardized preprocessing."
---

# A Data-Centric Perspective on Evaluating Machine Learning Models for Tabular Data

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/ae00e5ce7142d02e30a8235ede1ec6fc-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/ae00e5ce7142d02e30a8235ede1ec6fc-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Proposes a data-centric evaluation perspective for comparing machine learning models on tabular data beyond standardized preprocessing.

## Abstract

Tabular data is prevalent in real-world machine learning applications, and new models for supervised learning of tabular data are frequently proposed. Comparative studies assessing performance differences typically have model-centered evaluation setups with overly standardized data preprocessing. This limits the external validity of these studies, as in real-world modeling pipelines, models are typically applied after dataset-specific preprocessing and feature engineering. We address this gap by proposing a data-centric evaluation framework. We select 10 relevant datasets from Kaggle competitions and implement expert-level preprocessing pipelines for each dataset. We conduct experiments with different preprocessing pipelines and hyperparameter optimization (HPO) regimes to quantify the impact of model selection, HPO, feature engineering, and test-time adaptation. Our main findings reveal: 1) After dataset-specific feature engineering, model rankings change considerably, performance differences decrease, and the importance of model selection reduces. 2) Recent models, despite their measurable progress, still significantly benefit from manual feature engineering. This holds true for both tree-based models and neural networks. 3) While tabular data is typically considered static, samples are often collected over time, and adapting to distribution shifts can be important even in supposedly static data. These insights suggest that research efforts should be directed toward a data-centric perspective, acknowledging that tabular data requires feature engineering and often exhibits temporal characteristics.