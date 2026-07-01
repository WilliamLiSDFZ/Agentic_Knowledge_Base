---
title: "GVKF: Gaussian Voxel Kernel Functions for Highly Efficient Surface Reconstruction in Open Scenes"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/bd31bfd4caa85bffe07a35568182cdfa-Abstract-Conference.html"
categories: ['neural-geometric-shape-representation-learning', 'visual-language-multimodal-generation-reasoning']
tags: ['3D-gaussian-splatting', 'surface-reconstruction', 'neural-radiance-fields']
venue: "NeurIPS 2024"
tldr: "Introduces Gaussian voxel kernel functions for efficient and effective 3D surface reconstruction in open scenes, outperforming NeRF-based methods in speed."
---

# GVKF: Gaussian Voxel Kernel Functions for Highly Efficient Surface Reconstruction in Open Scenes

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/bd31bfd4caa85bffe07a35568182cdfa-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/bd31bfd4caa85bffe07a35568182cdfa-Abstract-Conference.html)

**TLDR**: Introduces Gaussian voxel kernel functions for efficient and effective 3D surface reconstruction in open scenes, outperforming NeRF-based methods in speed.

## Abstract

In this paper we present a novel method for efficient and effective 3D surface reconstruction in open scenes. Existing Neural Radiance Fields (NeRF) based works typically require extensive training and rendering time due to the adopted implicit representations. In contrast, 3D Gaussian splatting (3DGS) uses an explicit and discrete representation, hence the reconstructed surface is built by the huge number of Gaussian primitives, which leads to excessive memory consumption and rough surface details in sparse Gaussian areas.To address these issues, we propose Gaussian Voxel Kernel Functions (GVKF), which establish a continuous scene representation based on discrete 3DGS through kernel regression. The GVKF integrates fast 3DGS rasterization and highly effective scene implicit representations, achieving high-fidelity open scene surface reconstruction. Experiments on challenging scene datasets demonstrate the efficiency and effectiveness of our proposed GVKF, featuring with high reconstruction quality, real-time rendering speed, significant savings in storage and training memory consumption.