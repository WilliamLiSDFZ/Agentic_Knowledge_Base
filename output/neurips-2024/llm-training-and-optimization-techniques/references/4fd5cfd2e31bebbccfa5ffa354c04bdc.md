---
title: "Large Scale Transfer Learning for Tabular Data  via Language Modeling"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/4fd5cfd2e31bebbccfa5ffa354c04bdc-Abstract-Conference.html"
categories: ['llm-training-and-optimization-techniques', 'autonomous-driving-and-trajectory-prediction']
tags: ['tabular-data', 'language-modeling', 'transfer-learning', 'foundation-models', 'heterogeneous-data']
venue: "NeurIPS 2024"
tldr: "Proposes a large-scale language model-based transfer learning approach for tabular data that reduces the need for task-specific datasets and predictors."
---

# Large Scale Transfer Learning for Tabular Data  via Language Modeling

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/4fd5cfd2e31bebbccfa5ffa354c04bdc-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/4fd5cfd2e31bebbccfa5ffa354c04bdc-Abstract-Conference.html)

**TLDR**: Proposes a large-scale language model-based transfer learning approach for tabular data that reduces the need for task-specific datasets and predictors.

## Abstract

Tabular data – structured, heterogeneous, spreadsheet-style data with rows and columns – is widely used in practice across many domains. However, while recent foundation models have reduced the need for developing task-specific datasets and predictors in domains such as language modeling and computer vision, this transfer learning paradigm has not had similar impact in the tabular domain. In this work, we seek to narrow this gap and present TABULA-8B, a language model for tabular prediction. We define a process for extracting a large, high-quality training dataset from the TabLib corpus, proposing methods for tabular data filtering and quality control. Using the resulting dataset, which comprises over 2.1B rows from 4.2M unique tables, we fine-tune a Llama 3-8B large language model (LLM) for tabular data prediction (classification and binned regression) using a novel packing and attention scheme for tabular prediction. Through evaluation across a test suite of 329 datasets, we find that TABULA-8B has zero-shot accuracy on unseen tables that is over 15 percentage points (pp) higher than random guessing, a feat that is not possible with existing state-of-the-art tabular prediction models (e.g. XGBoost, TabPFN). In the few-shot setting (1-32 shots), without any fine-tuning on the target datasets, TABULA-8B is 5-15 pp more accurate than XGBoost and TabPFN models that are explicitly trained on equal, or even up to 16× more data. We release our model, code, and data along with the publication of this paper.