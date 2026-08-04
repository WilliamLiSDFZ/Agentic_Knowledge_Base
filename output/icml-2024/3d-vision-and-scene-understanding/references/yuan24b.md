---
title: "A Linear Time and Space Local Point Cloud Geometry Encoder via Vectorized Kernel Mixture (VecKM)"
source: "https://proceedings.mlr.press/v235/yuan24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yuan24b/yuan24b.pdf"
categories: ['3d-vision-and-scene-understanding', 'sampling-compression-and-dimensionality-reduction']
tags: ['point-cloud', 'local-geometry-encoder', 'kernel-mixture', 'linear-complexity']
venue: "ICML 2024"
tldr: "VecKM is a linear-time local point cloud geometry encoder using vectorized kernel mixtures with theoretical descriptiveness guarantees."
---

# A Linear Time and Space Local Point Cloud Geometry Encoder via Vectorized Kernel Mixture (VecKM)

**Source**: [https://proceedings.mlr.press/v235/yuan24b.html](https://proceedings.mlr.press/v235/yuan24b.html)

**TLDR**: VecKM is a linear-time local point cloud geometry encoder using vectorized kernel mixtures with theoretical descriptiveness guarantees.

## Abstract

We propose VecKM, a local point cloud geometry encoder that is descriptive and efficient to compute. VecKM leverages a unique approach by vectorizing a kernel mixture to represent the local point cloud. Such representation’s descriptiveness is supported by two theorems that validate its ability to reconstruct and preserve the similarity of the local shape. Unlike existing encoders downsampling the local point cloud, VecKM constructs the local geometry encoding using all neighboring points, producing a more descriptive encoding. Moreover, VecKM is efficient to compute and scalable to large point cloud inputs: VecKM reduces the memory cost from $(n^2+nKd)$ to $(nd+np)$; and reduces the major runtime cost from computing $nK$ MLPs to $n$ MLPs, where $n$ is the size of the point cloud, $K$ is the neighborhood size, $d$ is the encoding dimension, and $p$ is a marginal factor. The efficiency is due to VecKM’s unique factorizable property that eliminates the need of explicitly grouping points into neighbors. In the normal estimation task, VecKM demonstrates not only 100x faster inference speed but also highest accuracy and strongest robustness. In classification and segmentation tasks, integrating VecKM as a preprocessing module achieves consistently better performance than the PointNet, PointNet++, and point transformer baselines, and runs consistently faster by up to 10 times.