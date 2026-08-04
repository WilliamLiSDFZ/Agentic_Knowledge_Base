---
title: "Equivariance via Minimal Frame Averaging for More Symmetries and Efficiency"
source: "https://proceedings.mlr.press/v235/lin24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24i/lin24i.pdf"
categories: ['equivariant-neural-networks-and-symmetry-learning', 'optimization-algorithms-convergence-theory']
tags: ['frame-averaging', 'equivariance', 'symmetry']
venue: "ICML 2024"
tldr: "Minimal Frame Averaging (MFA) achieves exact equivariance with minimal computational overhead across a wide range of symmetry groups."
---

# Equivariance via Minimal Frame Averaging for More Symmetries and Efficiency

**Source**: [https://proceedings.mlr.press/v235/lin24i.html](https://proceedings.mlr.press/v235/lin24i.html)

**TLDR**: Minimal Frame Averaging (MFA) achieves exact equivariance with minimal computational overhead across a wide range of symmetry groups.

## Abstract

We consider achieving equivariance in machine learning systems via frame averaging. Current frame averaging methods involve a costly sum over large frames or rely on sampling-based approaches that only yield approximate equivariance. Here, we propose Minimal Frame Averaging (MFA), a mathematical framework for constructing provably minimal frames that are exactly equivariant. The general foundations of MFA also allow us to extend frame averaging to more groups than previously considered, including the Lorentz group for describing symmetries in space-time, and the unitary group for complex-valued domains. Results demonstrate the efficiency and effectiveness of encoding symmetries via MFA across a diverse range of tasks, including $n$-body simulation, top tagging in collider physics, and relaxed energy prediction. Our code is available at https://github.com/divelab/MFA.