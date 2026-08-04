---
title: "Equivariant Frames and the Impossibility of Continuous Canonicalization"
source: "https://proceedings.mlr.press/v235/dym24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dym24a/dym24a.pdf"
categories: ['equivariant-neural-networks-and-symmetry-learning', 'algebraic-structures-in-machine-learning']
tags: ['equivariance', 'canonicalization', 'frame-averaging', 'symmetry', 'impossibility-theorem']
venue: "ICML 2024"
tldr: "Proves that continuous canonicalization is impossible for common symmetry groups and motivates probabilistic frame-averaging as a principled alternative."
---

# Equivariant Frames and the Impossibility of Continuous Canonicalization

**Source**: [https://proceedings.mlr.press/v235/dym24a.html](https://proceedings.mlr.press/v235/dym24a.html)

**TLDR**: Proves that continuous canonicalization is impossible for common symmetry groups and motivates probabilistic frame-averaging as a principled alternative.

## Abstract

Canonicalization provides an architecture-agnostic method for enforcing equivariance, with generalizations such as frame-averaging recently gaining prominence as a lightweight and flexible alternative to equivariant architectures. Recent works have found an empirical benefit to using probabilistic frames instead, which learn weighted distributions over group elements. In this work, we provide strong theoretical justification for this phenomenon: for commonly-used groups, there is no efficiently computable choice of frame that preserves continuity of the function being averaged. In other words, unweighted frame-averaging can turn a smooth, non-symmetric function into a discontinuous, symmetric function. To address this fundamental robustness problem, we formally define and construct weighted frames, which provably preserve continuity, and demonstrate their utility by constructing efficient and continuous weighted frames for the actions of $SO(d)$, $O(d)$, and $S_n$ on point clouds.