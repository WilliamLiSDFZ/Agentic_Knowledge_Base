---
title: "QBMK: Quantum-based Matching Kernels for Un-attributed Graphs"
source: "https://proceedings.mlr.press/v235/bai24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bai24a/bai24a.pdf"
categories: ['quantum-algorithms-for-machine-learning-optimization', 'graph-neural-networks-and-topology']
tags: ['quantum-walk', 'graph-kernels', 'quantum-entropy']
venue: "ICML 2024"
tldr: "A new quantum-based matching kernel for un-attributed graphs is proposed using continuous-time quantum walk and Shannon entropy alignment."
---

# QBMK: Quantum-based Matching Kernels for Un-attributed Graphs

**Source**: [https://proceedings.mlr.press/v235/bai24a.html](https://proceedings.mlr.press/v235/bai24a.html)

**TLDR**: A new quantum-based matching kernel for un-attributed graphs is proposed using continuous-time quantum walk and Shannon entropy alignment.

## Abstract

In this work, we develop a new Quantum-based Matching Kernel (QBMK) for un-attributed graphs, by computing the kernel-based similarity between the quantum Shannon entropies of aligned vertices through the Continuous-time Quantum Walk (CTQW). The theoretical analysis reveals that the proposed QBMK kernel not only addresses the shortcoming of neglecting the structural correspondence information between graphs arising in existing R-convolution graph kernels, but also overcomes the problem of neglecting the structural differences between pairs of aligned vertices arising in existing vertex-based matching kernels. Moreover, the proposed QBMK kernel can simultaneously capture both global and local structural characteristics through the quantum Shannon entropies. Experimental evaluations on standard graph datasets demonstrate that the proposed QBMK kernel is able to outperform state-of-the-art graph kernels and graph deep learning approaches.