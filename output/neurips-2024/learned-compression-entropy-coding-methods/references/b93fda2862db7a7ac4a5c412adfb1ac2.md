---
title: "Random Cycle Coding: Lossless Compression of Cluster Assignments via Bits-Back Coding"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/b93fda2862db7a7ac4a5c412adfb1ac2-Abstract-Conference.html"
categories: ['learned-compression-entropy-coding-methods', 'probabilistic-circuits-and-tree-structured-models']
tags: ['lossless-compression', 'bits-back-coding', 'cluster-assignments']
venue: "NeurIPS 2024"
tldr: "Random Cycle Coding encodes cluster assignments optimally by representing them as cycles of permutations using bits-back coding without requiring training."
---

# Random Cycle Coding: Lossless Compression of Cluster Assignments via Bits-Back Coding

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/b93fda2862db7a7ac4a5c412adfb1ac2-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/b93fda2862db7a7ac4a5c412adfb1ac2-Abstract-Conference.html)

**TLDR**: Random Cycle Coding encodes cluster assignments optimally by representing them as cycles of permutations using bits-back coding without requiring training.

## Abstract

We present an optimal method for encoding cluster assignments of arbitrary data sets. Our method, Random Cycle Coding (RCC), encodes data sequentially and sends assignment information as cycles of the permutation defined by the order of encoded elements. RCC does not require any training and its worst-case complexity scales quasi-linearly with the size of the largest cluster. We characterize the achievable bit rates as a function of cluster sizes and number of elements, showing RCC consistently outperforms previous methods while requiring less compute and memory resources. Experiments show RCC can save up to $2$ bytes per element when applied to vector databases, and removes the need for assigning integer ids to identify vectors, translating to savings of up to $70\%$ in vector database systems for similarity search applications.