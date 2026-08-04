---
title: "Residual Quantization with Implicit Neural Codebooks"
source: "https://proceedings.mlr.press/v235/huijben24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huijben24a/huijben24a.pdf"
categories: ['sampling-compression-and-dimensionality-reduction', 'graph-clustering-and-matching-algorithms']
tags: ['vector-quantization', 'residual-quantization', 'neural-codebooks', 'data-compression', 'vector-search']
venue: "ICML 2024"
tldr: "Proposes implicit neural codebooks for residual quantization to improve accuracy in data compression and vector search tasks."
---

# Residual Quantization with Implicit Neural Codebooks

**Source**: [https://proceedings.mlr.press/v235/huijben24a.html](https://proceedings.mlr.press/v235/huijben24a.html)

**TLDR**: Proposes implicit neural codebooks for residual quantization to improve accuracy in data compression and vector search tasks.

## Abstract

Vector quantization is a fundamental operation for data compression and vector search. To obtain high accuracy, multi-codebook methods represent each vector using codewords across several codebooks. Residual quantization (RQ) is one such method, which iteratively quantizes the error of the previous step. While the error distribution is dependent on previously-selected codewords, this dependency is not accounted for in conventional RQ as it uses a fixed codebook per quantization step. In this paper, we propose QINCo, a neural RQ variant that constructs specialized codebooks per step that depend on the approximation of the vector from previous steps. Experiments show that QINCo outperforms state-of-the-art methods by a large margin on several datasets and code sizes. For example, QINCo achieves better nearest-neighbor search accuracy using 12-byte codes than the state-of-the-art UNQ using 16 bytes on the BigANN1M and Deep1M datasets.