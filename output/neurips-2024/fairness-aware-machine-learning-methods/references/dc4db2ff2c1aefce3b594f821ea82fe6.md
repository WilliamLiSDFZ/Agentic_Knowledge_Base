---
title: "The Group Robustness is in the Details: Revisiting Finetuning under Spurious Correlations"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/dc4db2ff2c1aefce3b594f821ea82fe6-Abstract-Conference.html"
categories: ['fairness-aware-machine-learning-methods', 'llm-training-and-optimization-techniques']
tags: ['spurious-correlations', 'worst-group-accuracy', 'finetuning']
venue: "NeurIPS 2024"
tldr: "Comprehensive experiments reveal nuanced and surprising behaviors of finetuned models regarding worst-group accuracy under spurious correlations."
---

# The Group Robustness is in the Details: Revisiting Finetuning under Spurious Correlations

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/dc4db2ff2c1aefce3b594f821ea82fe6-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/dc4db2ff2c1aefce3b594f821ea82fe6-Abstract-Conference.html)

**TLDR**: Comprehensive experiments reveal nuanced and surprising behaviors of finetuned models regarding worst-group accuracy under spurious correlations.

## Abstract

Modern machine learning models are prone to over-reliance on spurious correlations, which can often lead to poor performance on minority groups. In this paper, we identify surprising and nuanced behavior of finetuned models on worst-group accuracy via comprehensive experiments on four well-established benchmarks across vision and language tasks. We first show that the commonly used class-balancing techniques of mini-batch upsampling and loss upweighting can induce a decrease in worst-group accuracy (WGA) with training epochs, leading to performance no better than without class-balancing. While in some scenarios, removing data to create a class-balanced subset is more effective, we show this depends on group structure and propose a mixture method which can outperform both techniques. Next, we show that scaling pretrained models is generally beneficial for worst-group accuracy, but only in conjunction with appropriate class-balancing. Finally, we identify spectral imbalance in finetuning features as a potential source of group disparities --- minority group covariance matrices incur a larger spectral norm than majority groups once conditioned on the classes. Our results show more nuanced interactions of modern finetuned models with group robustness than was previously known. Our code is available at https://github.com/tmlabonte/revisiting-finetuning.