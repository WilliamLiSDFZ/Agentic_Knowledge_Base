---
title: "UQ-Guided Hyperparameter Optimization for Iterative Learners"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/010c5ba0cafc743fece8be02e7adb8dd-Abstract-Conference.html"
categories: ['machine-learning-theory-and-evaluation-methods', 'ai-benchmarking-and-evaluation-methodology']
tags: ['hyperparameter-optimization', 'uncertainty-quantification', 'iterative-learners']
venue: "NeurIPS 2024"
tldr: "This paper introduces uncertainty-aware hyperparameter optimization to account for training stochasticity in iterative machine learning models."
---

# UQ-Guided Hyperparameter Optimization for Iterative Learners

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/010c5ba0cafc743fece8be02e7adb8dd-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/010c5ba0cafc743fece8be02e7adb8dd-Abstract-Conference.html)

**TLDR**: This paper introduces uncertainty-aware hyperparameter optimization to account for training stochasticity in iterative machine learning models.

## Abstract

Hyperparameter Optimization (HPO) plays a pivotal role in unleashing the potential of iterative machine learning models. This paper addresses a crucial aspect that has largely been overlooked in HPO: the impact of uncertainty in ML model training. The paper introduces the concept of uncertainty-aware HPO and presents a novel approach called the UQ-guided scheme for quantifying uncertainty. This scheme offers a principled and versatile method to empower HPO techniques in handling model uncertainty during their exploration of the candidate space.By constructing a probabilistic model and implementing probability-driven candidate selection and budget allocation, this approach enhances the quality of the resulting model hyperparameters. It achieves a notable performance improvement of over 50\% in terms of accuracy regret and exploration time.