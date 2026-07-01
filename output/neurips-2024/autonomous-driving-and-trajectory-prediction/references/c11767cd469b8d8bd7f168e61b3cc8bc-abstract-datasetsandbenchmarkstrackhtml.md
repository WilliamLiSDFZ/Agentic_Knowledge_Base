---
title: "SS3DM: Benchmarking Street-View Surface Reconstruction with a Synthetic 3D Mesh Dataset"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/c11767cd469b8d8bd7f168e61b3cc8bc-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'autonomous-driving-and-trajectory-prediction']
tags: ['street-view', 'surface-reconstruction', '3D-mesh', 'synthetic-dataset', 'benchmark']
venue: "NeurIPS 2024"
tldr: "Introduces a synthetic 3D mesh dataset for benchmarking street-view surface reconstruction methods."
---

# SS3DM: Benchmarking Street-View Surface Reconstruction with a Synthetic 3D Mesh Dataset

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/c11767cd469b8d8bd7f168e61b3cc8bc-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/c11767cd469b8d8bd7f168e61b3cc8bc-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces a synthetic 3D mesh dataset for benchmarking street-view surface reconstruction methods.

## Abstract

Reconstructing accurate 3D surfaces for street-view scenarios is crucial for applications such as digital entertainment and autonomous driving simulation. However, existing street-view datasets, including KITTI, Waymo, and nuScenes, only offer noisy LiDAR points as ground-truth data for geometric evaluation of reconstructed surfaces. These geometric ground-truths often lack the necessary precision to evaluate surface positions and do not provide data for assessing surface normals. To overcome these challenges, we introduce the SS3DM dataset, comprising precise \textbf{S}ynthetic \textbf{S}treet-view \textbf{3D} \textbf{M}esh models exported from the CARLA simulator. These mesh models facilitate accurate position evaluation and include normal vectors for evaluating surface normal.   To simulate the input data in realistic driving scenarios for 3D reconstruction, we virtually drive a vehicle equipped with six RGB cameras and five LiDAR sensors in diverse outdoor scenes.  Leveraging this dataset, we establish a benchmark for state-of-the-art surface reconstruction methods, providing a comprehensive evaluation of the associated challenges.   For more information, visit our homepage at https://ss3dm.top.