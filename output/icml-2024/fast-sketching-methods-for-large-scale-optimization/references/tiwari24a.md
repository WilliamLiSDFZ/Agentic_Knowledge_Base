---
title: "Faster Maximum Inner Product Search in High Dimensions"
source: "https://proceedings.mlr.press/v235/tiwari24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tiwari24a/tiwari24a.pdf"
categories: ['graph-based-approximate-nearest-neighbor-search', 'fast-sketching-methods-for-large-scale-optimization']
tags: ['maximum-inner-product-search', 'sketching', 'high-dimensional-retrieval']
venue: "ICML 2024"
tldr: "A faster algorithm for Maximum Inner Product Search in high dimensions is proposed, improving upon the existing O(√n) query complexity bounds."
---

# Faster Maximum Inner Product Search in High Dimensions

**Source**: [https://proceedings.mlr.press/v235/tiwari24a.html](https://proceedings.mlr.press/v235/tiwari24a.html)

**TLDR**: A faster algorithm for Maximum Inner Product Search in high dimensions is proposed, improving upon the existing O(√n) query complexity bounds.

## Abstract

Maximum Inner Product Search (MIPS) is a ubiquitous task in machine learning applications. Given a query vector and $n$ other vectors in $d$ dimensions, the MIPS problem is to find the atom that has the highest inner product with the query vector. Existing MIPS algorithms scale at least as $O(\sqrt{d})$ with respect to $d$, which becomes computationally prohibitive in high-dimensional settings. In this work, we present BanditMIPS, a novel randomized algorithm that provably improves the state-of-the-art complexity from $O(\sqrt{d})$ to $O(1)$ with respect to $d$. We validate the scaling of BanditMIPS and demonstrate that BanditMIPS outperforms prior state-of-the-art MIPS algorithms in sample complexity, wall-clock time, and precision/speedup tradeoff across a variety of experimental settings. Furthermore, we propose a variant of our algorithm, named BanditMIPS-$\alpha$, which improves upon BanditMIPS by employing non-uniform sampling across coordinates. We also demonstrate the usefulness of BanditMIPS in problems for which MIPS is a subroutine, including Matching Pursuit and Fourier analysis. Finally, we demonstrate that BanditMIPS can be used in conjunction with preprocessing techniques to improve its complexity with respect to $n$. All of our experimental results are reproducible via a 1-line script at github.com/ThrunGroup/BanditMIPS.