---
title: "Navigating Extremes: Dynamic Sparsity in Large Output Spaces"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/d4bdeed749a437de2cbe2e2c7e5a6a8a-Abstract-Conference.html"
categories: ['llm-training-and-optimization-techniques', 'deep-learning-optimization-and-generalization-theory']
tags: ['dynamic-sparse-training', 'large-output-spaces', 'model-pruning', 'efficiency']
venue: "NeurIPS 2024"
tldr: "Addresses challenges of dynamic sparse training in large output space settings, enabling memory-efficient training with maintained sparsity throughout."
---

# Navigating Extremes: Dynamic Sparsity in Large Output Spaces

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/d4bdeed749a437de2cbe2e2c7e5a6a8a-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/d4bdeed749a437de2cbe2e2c7e5a6a8a-Abstract-Conference.html)

**TLDR**: Addresses challenges of dynamic sparse training in large output space settings, enabling memory-efficient training with maintained sparsity throughout.

## Abstract

In recent years, Dynamic Sparse Training (DST) has emerged as an alternative to post-training pruning for generating efficient models. In principle, DST allows for a much more memory efficient training process,as it maintains sparsity throughout the entire training run. However, current DST implementations fail to capitalize on this. Because sparse matrix multiplication is much less efficient than dense matrix multiplication on GPUs, mostimplementations simulate sparsity by masking weights. In this paper, we leverage recent advances in semi-structured sparse training to apply DST in the domain of classificationwith large output spaces, where memory-efficiency is paramount. With a label space of possibly millions of candidates,the classification layer alone will consume several gigabytes of memory. Switching from a dense to a fixed fan-in sparse layer updated with sparse evolutionary training (SET); however, severely hampers training convergence, especiallyat the largest label spaces. We find that the gradients fed back from the classifier into the text encoder make itmuch more difficult to learn good input representations, despite using a dense encoder.By employing an intermediate layer or adding an auxiliary training objective, we recover most of the generalisation performance of the dense model. Overall, we demonstrate the applicability of DST in a challenging domain, characterized by a highly skewed label distribution, that lies outside of DST's typical benchmark datasets, and enable end-to-end training with millions of labels on commodity hardware.