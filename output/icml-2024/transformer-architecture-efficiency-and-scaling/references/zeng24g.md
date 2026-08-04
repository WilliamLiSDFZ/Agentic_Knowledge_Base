---
title: "IM-Unpack: Training and Inference with Arbitrarily Low Precision Integers"
source: "https://proceedings.mlr.press/v235/zeng24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zeng24g/zeng24g.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'optimization-algorithms-convergence-theory']
tags: ['quantization', 'low-precision', 'matrix-multiplication']
venue: "ICML 2024"
tldr: "A method enabling training and inference with arbitrarily low precision integers for GEMM operations in deep learning."
---

# IM-Unpack: Training and Inference with Arbitrarily Low Precision Integers

**Source**: [https://proceedings.mlr.press/v235/zeng24g.html](https://proceedings.mlr.press/v235/zeng24g.html)

**TLDR**: A method enabling training and inference with arbitrarily low precision integers for GEMM operations in deep learning.

## Abstract

GEneral Matrix Multiply (GEMM) is a central operation in deep learning and corresponds to a large chunk of the compute footprint. Therefore, improving its efficiency is an active topic of research. A popular strategy is the use of low bit-width integers to approximate the original matrix entries. This allows efficiency gains, but often requires sophisticated techniques to control the rounding error. In this work, we first verify that when the low bit-width restriction is removed, for a variety of Transformer-based models, integers are, in fact, sufficient for all GEMMs need – for both training and inference stages, and achieve parity (with floating point). No sophisticated techniques are needed. We find that while a large majority of entries in matrices (encountered in such models) can be easily represented by low bit-width integers, the existence of a few heavy hitter entries make it difficult to achieve efficiency gains via the exclusive use of low bit-width GEMMs alone. To address this issue, we develop a simple algorithm, Integer Matrix Unpacking (IM-Unpack), to unpack a matrix with large integer entries into a larger matrix whose entries all lie within the representable range of arbitrarily low bit-width integers. This allows equivalence with the original GEMM, i.e., the exact result can be obtained using purely low bit-width integer GEMMs. This comes at the cost of additional operations – we show that for many popular models, this overhead is quite small. Code is available at https://github.com/vsingh-group/im-unpack.