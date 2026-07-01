---
title: "VeLoRA: Memory Efficient Training using Rank-1 Sub-Token Projections"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/4a9eaf6dff3fdac9ab1aaf4c0fe2d563-Abstract-Conference.html"
categories: ['llm-training-and-optimization-techniques', 'stochastic-optimization-convergence-and-variance-reduction']
tags: ['memory-efficient-training', 'LoRA', 'rank-1-projections', 'LLM-fine-tuning']
venue: "NeurIPS 2024"
tldr: "VeLoRA reduces memory costs in LLM training by using rank-1 sub-token projections during gradient computation."
---

# VeLoRA: Memory Efficient Training using Rank-1 Sub-Token Projections

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/4a9eaf6dff3fdac9ab1aaf4c0fe2d563-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/4a9eaf6dff3fdac9ab1aaf4c0fe2d563-Abstract-Conference.html)

**TLDR**: VeLoRA reduces memory costs in LLM training by using rank-1 sub-token projections during gradient computation.

## Abstract

Large language models (LLMs) have recently emerged as powerful tools for tackling many language-processing tasks. Despite their success, training and fine-tuning these models is still far too computationally and memory intensive. In this paper, we identify and characterise the important components needed for effective model convergence using gradient descent. In doing so we find that the intermediate activations used to implement backpropagation can be excessively compressed without incurring any degradation in performance. This result leads us to a cheap and memory-efficient algorithm for both fine-tuning and pre-training LLMs. The proposed algorithm simply divides the tokens up into smaller sub-tokens before projecting them onto a fixed 1-dimensional subspace during the forward pass. These features are then coarsely reconstructed during the backward pass to implement the update rules. We confirm the effectiveness of our algorithm as being complimentary to many state-of-the-art PEFT methods on the VTAB-1k fine-tuning benchmark. Furthermore, we outperform QLoRA for fine-tuning LLaMA and show competitive performance against other memory-efficient pre-training methods on the large-scale C4 dataset.