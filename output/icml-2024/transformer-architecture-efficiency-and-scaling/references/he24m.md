---
title: "SFC: Achieve Accurate Fast Convolution under Low-precision Arithmetic"
source: "https://proceedings.mlr.press/v235/he24m.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/he24m/he24m.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'optimization-algorithms-convergence-theory']
tags: ['fast-convolution', 'Winograd', 'quantization', 'low-precision']
venue: "ICML 2024"
tldr: "Introduces a method to achieve accurate fast convolution (Winograd/FFT) under low-precision arithmetic for deep model inference."
---

# SFC: Achieve Accurate Fast Convolution under Low-precision Arithmetic

**Source**: [https://proceedings.mlr.press/v235/he24m.html](https://proceedings.mlr.press/v235/he24m.html)

**TLDR**: Introduces a method to achieve accurate fast convolution (Winograd/FFT) under low-precision arithmetic for deep model inference.

## Abstract

Fast convolution algorithms, including Winograd and FFT, can efficiently accelerate convolution operations in deep models. However, these algorithms depend on high-precision arithmetic to maintain inference accuracy, which conflicts with the model quantization. To resolve this conflict and further improve the efficiency of quantized convolution, we proposes SFC, a new algebra transform for fast convolution by extending the Discrete Fourier Transform (DFT) with symbolic computing, in which only additions are required to perform the transformation at specific transform points, avoiding the calculation of irrational number and reducing the requirement for precision. Additionally, we enhance convolution efficiency by introducing correction terms to convert invalid circular convolution outputs of the Fourier method into effective ones. The numerical error analysis is presented for the first time in this type of work and proves that our algorithms can provide a 3.68× multiplication reduction for 3×3 convolution, while the Winograd algorithm only achieves a 2.25× reduction with similarly low numerical errors. Experiments carried out on benchmarks and FPGA show that our new algorithms can further improve the computation efficiency of quantized models while maintaining accuracy, surpassing both the quantization-alone method and existing works on fast convolution quantization.