---
title: "Learning to Solve Quadratic Unconstrained Binary Optimization in a Classification Way"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/cfedcb3b2abdf0f519b0afd6a16c04da-Abstract-Conference.html"
categories: ['neural-combinatorial-optimization-and-learning']
tags: ['QUBO', 'combinatorial-optimization', 'binary-optimization', 'classification', 'learning-based']
venue: "NeurIPS 2024"
tldr: "This paper reformulates quadratic unconstrained binary optimization as a classification problem to enable more efficient learning-based solutions."
---

# Learning to Solve Quadratic Unconstrained Binary Optimization in a Classification Way

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/cfedcb3b2abdf0f519b0afd6a16c04da-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/cfedcb3b2abdf0f519b0afd6a16c04da-Abstract-Conference.html)

**TLDR**: This paper reformulates quadratic unconstrained binary optimization as a classification problem to enable more efficient learning-based solutions.

## Abstract

The quadratic unconstrained binary optimization (QUBO) is a well-known NP-hard problem that takes an $n\times n$ matrix $Q$ as input and decides an $n$-dimensional 0-1 vector $x$, to optimize a quadratic function. Existing learning-based models that always formulate the solution process as sequential decisions suffer from high computational overload. To overcome this issue, we propose a neural solver called the Value Classification Model (VCM) that formulates the solution process from a classification perspective. It applies a Depth Value Network (DVN) based on graph convolution that exploits the symmetry property in $Q$ to auto-grasp value features. These features are then fed into a Value Classification Network (VCN) which directly generates classification solutions. Trained by a highly efficient model-tailored Greedy-guided Self Trainer (GST) which does not require any priori optimal labels, VCM significantly outperforms competitors in both computational efficiency and solution quality with a remarkable generalization ability. It can achieve near-optimal solutions in milliseconds with an average optimality gap of just 0.362\% on benchmarks with up to 2500 variables. Notably, a VCM trained at a specific DVN depth can steadily find better solutions by simply extending the testing depth, which narrows the gap to 0.034\% on benchmarks. To our knowledge, this is the first learning-based model to reach such a performance.