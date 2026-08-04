---
title: "Caduceus: Bi-Directional Equivariant Long-Range DNA Sequence Modeling"
source: "https://proceedings.mlr.press/v235/schiff24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/schiff24a/schiff24a.pdf"
categories: ['equivariant-neural-networks-and-symmetry-learning', 'sequence-models-for-memory-and-state']
tags: ['DNA-modeling', 'sequence-modeling', 'bidirectional', 'equivariance', 'long-range-dependencies']
venue: "ICML 2024"
tldr: "Caduceus introduces bidirectional equivariant sequence models for long-range DNA modeling that respect reverse complement symmetry."
---

# Caduceus: Bi-Directional Equivariant Long-Range DNA Sequence Modeling

**Source**: [https://proceedings.mlr.press/v235/schiff24a.html](https://proceedings.mlr.press/v235/schiff24a.html)

**TLDR**: Caduceus introduces bidirectional equivariant sequence models for long-range DNA modeling that respect reverse complement symmetry.

## Abstract

Large-scale sequence modeling has sparked rapid advances that now extend into biology and genomics. However, modeling genomic sequences introduces challenges such as the need to model long-range token interactions, the effects of upstream and downstream regions of the genome, and the reverse complementarity (RC) of DNA. Here, we propose an architecture motivated by these challenges that builds off the long-range Mamba block, and extends it to a BiMamba component that supports bi-directionality, and to a MambaDNA block that additionally supports RC equivariance. We use MambaDNA as the basis of Caduceus, the first family of RC equivariant bi-directional long-range DNA language models, and we introduce pre-training and fine-tuning strategies that yield Caduceus DNA foundation models. Caduceus outperforms previous long-range models on downstream benchmarks; on a challenging long-range variant effect prediction task, Caduceus exceeds the performance of 10x larger models that do not leverage bi-directionality or equivariance. Code to reproduce our experiments is available here: https://github.com/kuleshov-group/caduceus.