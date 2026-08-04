---
title: "Fine-grained Local Sensitivity Analysis of Standard Dot-Product Self-Attention"
source: "https://proceedings.mlr.press/v235/havens24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/havens24a/havens24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'neural-network-learning-dynamics-theory']
tags: ['self-attention', 'sensitivity-analysis', 'transformers']
venue: "ICML 2024"
tldr: "A fine-grained local sensitivity analysis of standard dot-product self-attention is presented to better understand its mathematical properties."
---

# Fine-grained Local Sensitivity Analysis of Standard Dot-Product Self-Attention

**Source**: [https://proceedings.mlr.press/v235/havens24a.html](https://proceedings.mlr.press/v235/havens24a.html)

**TLDR**: A fine-grained local sensitivity analysis of standard dot-product self-attention is presented to better understand its mathematical properties.

## Abstract

Self-attention has been widely used in various machine learning models, such as vision transformers. The standard dot-product self-attention is arguably the most popular structure, and there is a growing interest in understanding the mathematical properties of such attention mechanisms. This paper presents a fine-grained local sensitivity analysis of the standard dot-product self-attention, leading to new non-vacuous certified robustness results for vision transformers. Despite the well-known fact that dot-product self-attention is not (globally) Lipschitz, we develop new theoretical analysis of Local Fine-grained Attention Sensitivity (LoFAST) quantifying the effect of input feature perturbations on the attention output. Our analysis reveals that the local sensitivity of dot-product self-attention to $\ell_2$ perturbations can actually be controlled by several key quantities associated with the attention weight matrices and the unperturbed input. We empirically validate our theoretical findings by computing non-vacuous certified $\ell_2$-robustness for vision transformers on CIFAR-10 and SVHN datasets. The code for LoFAST is available at https://github.com/AaronHavens/LoFAST.