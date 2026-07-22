---
title: "Critical Learning Periods: Leveraging Early Training Dynamics for Efficient Data Pruning"
source: "https://aclanthology.org/2024.findings-acl.560/"
categories: ['llm-training-alignment-and-evaluation', 'continual-learning-for-nlp-tasks']
tags: ['data-pruning', 'critical-learning-periods', 'neural-machine-translation']
venue: "ACL 2024"
tldr: "Leverages early training dynamics to identify and prune low-value data, improving efficiency of NMT training."
---

# Critical Learning Periods: Leveraging Early Training Dynamics for Efficient Data Pruning

**Source**: [https://aclanthology.org/2024.findings-acl.560/](https://aclanthology.org/2024.findings-acl.560/)

**TLDR**: Leverages early training dynamics to identify and prune low-value data, improving efficiency of NMT training.

## Abstract

AbstractNeural Machine Translation models are extremely data and compute-hungry. However, not all datapoints contribute equally to model training and generalization. Data pruning to remove the low-value data points has the benefit of drastically reducing the compute budget without significantdrop in model performance. In this paper, we propose a new data pruning technique: CheckpointsAcross Time (CAT ), that leverages early model training dynamics to identify the most relevantdata points for model performance. We benchmark CAT against several data pruning techniquesincluding COMET-QE, LASER and LaBSE. We find that CAT outperforms the benchmarks onIndo-European languages on multiple test sets. When applied to English-German, English-Frenchand English-Swahili translation tasks, CAT achieves comparable performance to using the fulldataset, while pruning up to 50% of training data. We inspect the data points that CAT selectsand find that it tends to favour longer sentences and sentences with unique or rare words.