---
title: "Flexible Residual Binarization for Image Super-Resolution"
source: "https://proceedings.mlr.press/v235/zhang24bb.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24bb/zhang24bb.pdf"
categories: ['image-quality-assessment-and-super-resolution', 'sampling-compression-and-dimensionality-reduction']
tags: ['binary-neural-networks', 'image-super-resolution', 'quantization', 'high-frequency-information', 'model-compression']
venue: "ICML 2024"
tldr: "Proposes flexible residual binarization for image super-resolution to better preserve high-frequency information in binary SR networks."
---

# Flexible Residual Binarization for Image Super-Resolution

**Source**: [https://proceedings.mlr.press/v235/zhang24bb.html](https://proceedings.mlr.press/v235/zhang24bb.html)

**TLDR**: Proposes flexible residual binarization for image super-resolution to better preserve high-frequency information in binary SR networks.

## Abstract

Binarized image super-resolution (SR) has attracted much research attention due to its potential to drastically reduce parameters and operations. However, most binary SR works binarize network weights directly, which hinders high-frequency information extraction. Furthermore, as a pixel-wise reconstruction task, binarization often results in heavy representation content distortion. To address these issues, we propose a flexible residual binarization (FRB) method for image SR. We first propose a second-order residual binarization (SRB), to counter the information loss caused by binarization. In addition to the primary weight binarization, we also binarize the reconstruction error, which is added as a residual term in the prediction. Furthermore, to narrow the representation content gap between the binarized and full-precision networks, we propose Distillation-guided Binarization Training (DBT). We uniformly align the contents of different bit widths by constructing a normalized attention form. Finally, we generalize our method by applying our FRB to binarize convolution and Transformer-based SR networks, resulting in two binary baselines: FRBC and FRBT. We conduct extensive experiments and comparisons with recent leading binarization methods. Our proposed baselines, FRBC and FRBT, achieve superior performance both quantitatively and visually. The code and model will be released.