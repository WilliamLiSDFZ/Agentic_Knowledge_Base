---
title: "Disentangled Representation Learning in Non-Markovian Causal Systems"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/bd7ffcbd088b5e12f3b9eecc9c498b27-Abstract-Conference.html"
categories: ['disentangled-representation-learning-cognitive-diagnosis', 'causal-discovery-and-inference-methods']
tags: ['disentangled-representation', 'non-Markovian', 'causal-reasoning']
venue: "NeurIPS 2024"
tldr: "Develops disentangled representation learning in non-Markovian causal systems to recover high-level causal variables from low-level observations."
---

# Disentangled Representation Learning in Non-Markovian Causal Systems

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/bd7ffcbd088b5e12f3b9eecc9c498b27-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/bd7ffcbd088b5e12f3b9eecc9c498b27-Abstract-Conference.html)

**TLDR**: Develops disentangled representation learning in non-Markovian causal systems to recover high-level causal variables from low-level observations.

## Abstract

Considering various data modalities, such as images, videos, and text, humans perform causal reasoning using high-level causal variables, as opposed to operating at the low, pixel level from which the data comes. In practice, most causal reasoning methods assume that the data is described as granular as the underlying causal generative factors, which is often violated in various AI tasks. This mismatch translates into a lack of guarantees in various tasks such as generative modeling, decision-making, fairness, and generalizability, to cite a few. In this paper, we acknowledge this issue and study the problem of causal disentangled representation learning from a combination of data gathered from various heterogeneous domains and assumptions in the form of a latent causal graph. To the best of our knowledge, the proposed work is the first to consider i) non-Markovian causal settings, where there may be unobserved confounding, ii) arbitrary distributions that arise from multiple domains, and iii) a relaxed version of disentanglement. Specifically, we introduce graphical criteria that allow for disentanglement under various conditions. Building on these results, we develop an algorithm that returns a causal disentanglement map, highlighting which latent variables can be disentangled given the combination of data and assumptions. The theory is corroborated by experiments.