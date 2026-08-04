---
title: "Neural Operators with Localized Integral and Differential Kernels"
source: "https://proceedings.mlr.press/v235/liu-schiaffini24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu-schiaffini24a/liu-schiaffini24a.pdf"
categories: ['neural-operators-for-pde-solving']
tags: ['neural-operators', 'PDE-solving', 'local-kernels', 'Fourier-neural-operator']
venue: "ICML 2024"
tldr: "Proposes neural operators with localized integral and differential kernels as alternatives to global Fourier-based convolutions for improved PDE solution learning."
---

# Neural Operators with Localized Integral and Differential Kernels

**Source**: [https://proceedings.mlr.press/v235/liu-schiaffini24a.html](https://proceedings.mlr.press/v235/liu-schiaffini24a.html)

**TLDR**: Proposes neural operators with localized integral and differential kernels as alternatives to global Fourier-based convolutions for improved PDE solution learning.

## Abstract

Neural operators learn mappings between function spaces, which is practical for learning solution operators of PDEs and other scientific modeling applications. Among them, the Fourier neural operator (FNO) is a popular architecture that performs global convolutions in the Fourier space. However, such global operations are often prone to over-smoothing and may fail to capture local details. In contrast, convolutional neural networks (CNN) can capture local features but are limited to training and inference at a single resolution. In this work, we present a principled approach to operator learning that can capture local features under two frameworks by learning differential operators and integral operators with locally supported kernels. Specifically, inspired by stencil methods, we prove that we obtain differential operators under an appropriate scaling of the kernel values of CNNs. To obtain local integral operators, we utilize suitable basis representations for the kernels based on discrete-continuous convolutions. Both these approaches preserve the properties of operator learning and, hence, the ability to predict at any resolution. Adding our layers to FNOs significantly improves their performance, reducing the relative L2-error by 34-72% in our experiments, which include a turbulent 2D Navier-Stokes and the spherical shallow water equations.