---
title: "DrivAerNet++: A Large-Scale Multimodal Car Dataset with Computational Fluid Dynamics Simulations and Deep Learning Benchmarks"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/013cf29a9e68e4411d0593040a8a1eb3-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['physics-informed-neural-operators-and-simulations', 'neural-geometric-shape-representation-learning']
tags: ['aerodynamic-car-design', 'CFD-simulation', 'multimodal-dataset']
venue: "NeurIPS 2024"
tldr: "DrivAerNet++ is a large-scale multimodal dataset of 8,000 car designs with high-fidelity CFD simulations and deep learning benchmarks."
---

# DrivAerNet++: A Large-Scale Multimodal Car Dataset with Computational Fluid Dynamics Simulations and Deep Learning Benchmarks

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/013cf29a9e68e4411d0593040a8a1eb3-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/013cf29a9e68e4411d0593040a8a1eb3-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: DrivAerNet++ is a large-scale multimodal dataset of 8,000 car designs with high-fidelity CFD simulations and deep learning benchmarks.

## Abstract

We present DrivAerNet++, the largest and most comprehensive multimodal dataset for aerodynamic car design. DrivAerNet++ comprises 8,000 diverse car designs modeled with high-fidelity computational fluid dynamics (CFD) simulations. The dataset includes diverse car configurations such as fastback, notchback, and estateback, with different underbody and wheel designs to represent both internal combustion engines and electric vehicles. Each entry in the dataset features detailed 3D meshes, parametric models, aerodynamic coefficients, and extensive flow and surface field data, along with segmented parts for car classification and point cloud data. This dataset supports a wide array of machine learning applications including data-driven design optimization, generative modeling, surrogate model training, CFD simulation acceleration, and geometric classification. With more than 39 TB of publicly available engineering data, DrivAerNet++ fills a significant gap in available resources, providing high-quality, diverse data to enhance model training, promote generalization, and accelerate automotive design processes. Along with rigorous dataset validation, we also provide ML benchmarking results on the task of aerodynamic drag prediction, showcasing the breadth of applications supported by our dataset. This dataset is set to significantly impact automotive design and broader engineering disciplines by fostering innovation and improving the fidelity of aerodynamic evaluations. Dataset and code available at: https://github.com/Mohamedelrefaie/DrivAerNet