---
title: "Parameter Efficient Quasi-Orthogonal Fine-Tuning via Givens Rotation"
source: "https://proceedings.mlr.press/v235/ma24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ma24a/ma24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'algebraic-structures-in-machine-learning']
tags: ['parameter-efficient-fine-tuning', 'orthogonal-fine-tuning', 'Givens-rotation', 'pretrained-models']
venue: "ICML 2024"
tldr: "Quasi-orthogonal fine-tuning via Givens rotations achieves parameter-efficient adaptation of large pretrained models with orthogonality constraints."
---

# Parameter Efficient Quasi-Orthogonal Fine-Tuning via Givens Rotation

**Source**: [https://proceedings.mlr.press/v235/ma24a.html](https://proceedings.mlr.press/v235/ma24a.html)

**TLDR**: Quasi-orthogonal fine-tuning via Givens rotations achieves parameter-efficient adaptation of large pretrained models with orthogonality constraints.

## Abstract

With the increasingly powerful performances and enormous scales of pretrained models, promoting parameter efficiency in fine-tuning has become a crucial need for effective and efficient adaptation to various downstream tasks. One representative line of fine-tuning methods is Orthogonal Fine-tuning (OFT), which rigorously preserves the angular distances within the parameter space to preserve the pretrained knowledge. Despite the empirical effectiveness, OFT still suffers low parameter efficiency at $\mathcal{O}(d^2)$ and limited capability of downstream adaptation. Inspired by Givens rotation, in this paper, we proposed quasi-Givens Orthogonal Fine-Tuning (qGOFT) to address the problems. We first use $\mathcal{O}(d)$ Givens rotations to accomplish arbitrary orthogonal transformation in $SO(d)$ with provable equivalence, reducing parameter complexity from $\mathcal{O}(d^2)$ to $\mathcal{O}(d)$. Then we introduce flexible norm and relative angular adjustments under soft orthogonality regularization to enhance the adaptation capability of downstream semantic deviations. Extensive experiments on various tasks and pretrained models validate the effectiveness of our methods.