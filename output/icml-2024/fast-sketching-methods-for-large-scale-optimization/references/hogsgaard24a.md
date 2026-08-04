---
title: "Sparse Dimensionality Reduction Revisited"
source: "https://proceedings.mlr.press/v235/hogsgaard24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hogsgaard24a/hogsgaard24a.pdf"
categories: ['sampling-compression-and-dimensionality-reduction', 'fast-sketching-methods-for-large-scale-optimization']
tags: ['Johnson-Lindenstrauss', 'sparse-embedding', 'dimensionality-reduction']
venue: "ICML 2024"
tldr: "Revisits sparse Johnson-Lindenstrauss transforms and provides improved constructions and theoretical guarantees for dimensionality reduction."
---

# Sparse Dimensionality Reduction Revisited

**Source**: [https://proceedings.mlr.press/v235/hogsgaard24a.html](https://proceedings.mlr.press/v235/hogsgaard24a.html)

**TLDR**: Revisits sparse Johnson-Lindenstrauss transforms and provides improved constructions and theoretical guarantees for dimensionality reduction.

## Abstract

The sparse Johnson-Lindenstrauss transform is one of the central techniques in dimensionality reduction. It supports embedding a set of $n$ points in $\mathbb{R}^d$ into $m=O(\varepsilon^{-2} \ln n)$ dimensions while preserving all pairwise distances to within $1 \pm \varepsilon$. Each input point $x$ is embedded to $Ax$, where $A$ is an $m \times d$ matrix having $s$ non-zeros per column, allowing for an embedding time of $O(s \|x\|_0)$. Since the sparsity of $A$ governs the embedding time, much work has gone into improving the sparsity $s$. The current state-of-the-art by Kane and Nelson (2014) shows that $s = O(\varepsilon^{-1} \ln n)$ suffices. This is almost matched by a lower bound of $s = \Omega(\varepsilon^{-1} \ln n/\ln(1/\varepsilon))$ by Nelson and Nguyen (2013) for $d=\Omega(n)$. Previous work thus suggests that we have near-optimal embeddings. In this work, we revisit sparse embeddings and present a sparser embedding for instances in which $d = n^{o(1)}$, which in many applications is realistic. Formally, our embedding achieves $s = O(\varepsilon^{-1}(\ln n/\ln(1/\varepsilon)+\ln^{2/3}n \ln^{1/3} d))$. We also complement our analysis by strengthening the lower bound of Nelson and Nguyen to hold also when $d \ll n$, thereby matching the first term in our new sparsity upper bound. Finally, we also improve the sparsity of the best oblivious subspace embeddings for optimal embedding dimensionality.