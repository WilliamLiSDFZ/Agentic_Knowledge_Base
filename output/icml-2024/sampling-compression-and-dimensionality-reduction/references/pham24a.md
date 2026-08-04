---
title: "Neural NeRF Compression"
source: "https://proceedings.mlr.press/v235/pham24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pham24a/pham24a.pdf"
categories: ['3d-vision-and-scene-understanding', 'sampling-compression-and-dimensionality-reduction']
tags: ['NeRF', 'neural-compression', 'feature-grids', '3D-scene', 'storage-efficiency']
venue: "ICML 2024"
tldr: "Proposes a neural compression method for NeRF feature grids to significantly reduce storage overhead while maintaining rendering quality."
---

# Neural NeRF Compression

**Source**: [https://proceedings.mlr.press/v235/pham24a.html](https://proceedings.mlr.press/v235/pham24a.html)

**TLDR**: Proposes a neural compression method for NeRF feature grids to significantly reduce storage overhead while maintaining rendering quality.

## Abstract

Neural Radiance Fields (NeRFs) have emerged as powerful tools for capturing detailed 3D scenes through continuous volumetric representations. Recent NeRFs utilize feature grids to improve rendering quality and speed; however, these representations introduce significant storage overhead. This paper presents a novel method for efficiently compressing a grid-based NeRF model, addressing the storage overhead concern. Our approach is based on the non-linear transform coding paradigm, employing neural compression for compressing the model’s feature grids. Due to the lack of training data involving many i.i.d scenes, we design an encoder-free, end-to-end optimized approach for individual scenes, using lightweight decoders. To leverage the spatial inhomogeneity of the latent feature grids, we introduce an importance-weighted rate-distortion objective and a sparse entropy model employing a masking mechanism. Our experimental results validate that our proposed method surpasses existing works in terms of grid-based NeRF compression efficacy and reconstruction quality.