---
title: "DeepPolar: Inventing Nonlinear Large-Kernel Polar Codes via Deep Learning"
source: "https://proceedings.mlr.press/v235/hebbar24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hebbar24a/hebbar24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'algebraic-structures-in-machine-learning']
tags: ['polar-codes', 'deep-learning', 'error-correction', 'channel-coding']
venue: "ICML 2024"
tldr: "Uses deep learning to discover nonlinear large-kernel polar codes that outperform classical human-designed coding schemes."
---

# DeepPolar: Inventing Nonlinear Large-Kernel Polar Codes via Deep Learning

**Source**: [https://proceedings.mlr.press/v235/hebbar24a.html](https://proceedings.mlr.press/v235/hebbar24a.html)

**TLDR**: Uses deep learning to discover nonlinear large-kernel polar codes that outperform classical human-designed coding schemes.

## Abstract

Progress in designing channel codes has been driven by human ingenuity and, fittingly, has been sporadic. Polar codes, developed on the foundation of Arikan’s polarization kernel, represent the latest breakthrough in coding theory and have emerged as the state-of-the-art error-correction code for short-to-medium block length regimes. In an effort to automate the invention of good channel codes, especially in this regime, we explore a novel, non-linear generalization of Polar codes, which we call DeepPolar codes. DeepPolar codes extend the conventional Polar coding framework by utilizing a larger kernel size and parameterizing these kernels and matched decoders through neural networks. Our results demonstrate that these data-driven codes effectively leverage the benefits of a larger kernel size, resulting in enhanced reliability when compared to both existing neural codes and conventional Polar codes.