---
title: "Equivariant Deep Weight Space Alignment"
source: "https://proceedings.mlr.press/v235/navon24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/navon24a/navon24a.pdf"
categories: ['equivariant-neural-networks-and-symmetry-learning']
tags: ['weight-space-alignment', 'permutation-symmetry', 'equivariant-networks']
venue: "ICML 2024"
tldr: "An equivariant deep learning approach is proposed to solve the NP-hard weight alignment problem across neural network weight spaces."
---

# Equivariant Deep Weight Space Alignment

**Source**: [https://proceedings.mlr.press/v235/navon24a.html](https://proceedings.mlr.press/v235/navon24a.html)

**TLDR**: An equivariant deep learning approach is proposed to solve the NP-hard weight alignment problem across neural network weight spaces.

## Abstract

Permutation symmetries of deep networks make basic operations like model merging and similarity estimation challenging. In many cases, aligning the weights of the networks, i.e., finding optimal permutations between their weights, is necessary. Unfortunately, weight alignment is an NP-hard problem. Prior research has mainly focused on solving relaxed versions of the alignment problem, leading to either time-consuming methods or sub-optimal solutions. To accelerate the alignment process and improve its quality, we propose a novel framework aimed at learning to solve the weight alignment problem, which we name Deep-Align. To that end, we first prove that weight alignment adheres to two fundamental symmetries and then, propose a deep architecture that respects these symmetries. Notably, our framework does not require any labeled data. We provide a theoretical analysis of our approach and evaluate Deep-Align on several types of network architectures and learning setups. Our experimental results indicate that a feed-forward pass with Deep-Align produces better or equivalent alignments compared to those produced by current optimization algorithms. Additionally, our alignments can be used as an effective initialization for other methods, leading to improved solutions with a significant speedup in convergence.