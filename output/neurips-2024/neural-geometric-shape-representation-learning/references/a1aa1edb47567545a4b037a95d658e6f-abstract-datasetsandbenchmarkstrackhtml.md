---
title: "Implicit Zoo: A Large-Scale Dataset of Neural Implicit Functions for 2D Images and 3D Scenes"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/a1aa1edb47567545a4b037a95d658e6f-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['neural-geometric-shape-representation-learning', 'ai-benchmarking-and-evaluation-methodology']
tags: ['neural-implicit-functions', 'dataset', '3D-scenes', '2D-images']
venue: "NeurIPS 2024"
tldr: "A large-scale dataset of neural implicit functions for 2D images and 3D scenes to facilitate research in implicit neural representations."
---

# Implicit Zoo: A Large-Scale Dataset of Neural Implicit Functions for 2D Images and 3D Scenes

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/a1aa1edb47567545a4b037a95d658e6f-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/a1aa1edb47567545a4b037a95d658e6f-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A large-scale dataset of neural implicit functions for 2D images and 3D scenes to facilitate research in implicit neural representations.

## Abstract

Neural implicit functions have demonstrated significant importance in various areas such as computer vision, graphics. Their advantages include the ability to represent complex shapes and scenes with high fidelity, smooth interpolation capabilities, and continuous representations. Despite these benefits, the development and analysis of implicit functions have been limited by the lack of comprehensive datasets and the substantial computational resources required for their implementation and evaluation. To address these challenges, we introduce "Implicit-Zoo": a large-scale dataset requiring thousands of GPU training days designed to facilitate research and development in this field. Our dataset includes diverse 2D and 3D scenes, such as CIFAR-10, ImageNet-1K, and Cityscapes for 2D image tasks, and the OmniObject3D dataset for 3D vision tasks. We ensure high quality through strict checks, refining or filtering out low-quality data. Using Implicit-Zoo, we showcase two immediate benefits as it enables to: (1) learn token locations for transformer models; (2) Directly regress 3D cameras poses of 2D images with respect to NeRF models. This in turn leads to an \emph{improved performance} in all three task of  image classification, semantic segmentation, and 3D pose regression -- thereby unlocking new avenues for research.