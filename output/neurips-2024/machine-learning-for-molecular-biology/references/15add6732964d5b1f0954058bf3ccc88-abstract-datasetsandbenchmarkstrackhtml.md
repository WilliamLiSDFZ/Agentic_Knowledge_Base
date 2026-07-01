---
title: "AsEP: Benchmarking Deep Learning Methods for Antibody-specific Epitope Prediction"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/15add6732964d5b1f0954058bf3ccc88-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['machine-learning-for-molecular-biology', 'ai-benchmarking-and-evaluation-methodology']
tags: ['epitope-prediction', 'antibody-design', 'deep-learning-benchmark']
venue: "NeurIPS 2024"
tldr: "Presents AsEP, a benchmark for evaluating deep learning methods on antibody-specific epitope prediction tasks."
---

# AsEP: Benchmarking Deep Learning Methods for Antibody-specific Epitope Prediction

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/15add6732964d5b1f0954058bf3ccc88-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/15add6732964d5b1f0954058bf3ccc88-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents AsEP, a benchmark for evaluating deep learning methods on antibody-specific epitope prediction tasks.

## Abstract

Epitope identification is vital for antibody design yet challenging due to the inherent variability in antibodies. While many deep learning methods have been developed for general protein binding site prediction tasks, whether they work for epitope prediction remains an understudied research question. The challenge is also heightened by the lack of a consistent evaluation pipeline with sufficient dataset size and epitope diversity. We introduce a filtered antibody-antigen complex structure dataset, AsEP (Antibody-specific Epitope Prediction). AsEP is the largest of its kind and provides clustered epitope groups, allowing the community to develop and test novel epitope prediction methods and evaluate their generalisability. AsEP comes with an easy-to-use interface in Python and pre-built graph representations of each antibody-antigen complex while also supporting customizable embedding methods. Using this new dataset, we benchmark several representative general protein-binding site prediction methods and find that their performances fall short of expectations for epitope prediction. To address this, we propose a novel method, WALLE, which leverages both unstructured modeling from protein language models and structural modeling from graph neural networks. WALLE demonstrate up to 3-10X performance improvement over the baseline methods. Our empirical findings suggest that epitope prediction benefits from combining sequential features provided by language models with geometrical information from graph representations. This provides a guideline for future epitope prediction method design. In addition, we reformulate the task as bipartite link prediction, allowing convenient model performance attribution and interpretability. We open source our data and code at https://github.com/biochunan/AsEP-dataset.