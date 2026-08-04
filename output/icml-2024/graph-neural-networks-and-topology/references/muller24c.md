---
title: "Aligning Transformers with Weisfeiler-Leman"
source: "https://proceedings.mlr.press/v235/muller24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/muller24c/muller24c.pdf"
categories: ['graph-neural-networks-and-topology', 'transformer-architecture-efficiency-and-scaling']
tags: ['transformers', 'Weisfeiler-Leman', 'graph-expressiveness', 'GNN-alignment']
venue: "ICML 2024"
tldr: "Transformer architectures are aligned with the k-WL hierarchy to combine theoretically grounded expressiveness with strong empirical performance on graph tasks."
---

# Aligning Transformers with Weisfeiler-Leman

**Source**: [https://proceedings.mlr.press/v235/muller24c.html](https://proceedings.mlr.press/v235/muller24c.html)

**TLDR**: Transformer architectures are aligned with the k-WL hierarchy to combine theoretically grounded expressiveness with strong empirical performance on graph tasks.

## Abstract

Graph neural network architectures aligned with the $k$-dimensional Weisfeiler–Leman ($k$-WL) hierarchy offer theoretically well-understood expressive power. However, these architectures often fail to deliver state-of-the-art predictive performance on real-world graphs, limiting their practical utility. While recent works aligning graph transformer architectures with the $k$-WL hierarchy have shown promising empirical results, employing transformers for higher orders of $k$ remains challenging due to a prohibitive runtime and memory complexity of self-attention as well as impractical architectural assumptions, such as an infeasible number of attention heads. Here, we advance the alignment of transformers with the $k$-WL hierarchy, showing stronger expressivity results for each $k$, making them more feasible in practice. In addition, we develop a theoretical framework that allows the study of established positional encodings such as Laplacian PEs and SPE. We evaluate our transformers on the large-scale PCQM4Mv2 dataset, showing competitive predictive performance with the state-of-the-art and demonstrating strong downstream performance when fine-tuning them on small-scale molecular datasets.