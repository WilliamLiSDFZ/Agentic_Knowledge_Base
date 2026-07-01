---
title: "SynRS3D: A Synthetic Dataset for Global 3D Semantic Understanding from Monocular Remote Sensing Imagery"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/d4f3da38b491b44d40a0d5a5b37134ba-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['multi-view-clustering-and-3d-perception', 'neural-geometric-shape-representation-learning']
tags: ['synthetic-dataset', 'remote-sensing', '3D-semantic-understanding']
venue: "NeurIPS 2024"
tldr: "Presents SynRS3D, a synthetic dataset enabling global 3D semantic understanding from monocular high-resolution remote sensing imagery."
---

# SynRS3D: A Synthetic Dataset for Global 3D Semantic Understanding from Monocular Remote Sensing Imagery

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/d4f3da38b491b44d40a0d5a5b37134ba-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/d4f3da38b491b44d40a0d5a5b37134ba-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents SynRS3D, a synthetic dataset enabling global 3D semantic understanding from monocular high-resolution remote sensing imagery.

## Abstract

Global semantic 3D understanding from single-view high-resolution remote sensing (RS) imagery is crucial for Earth observation (EO). However, this task faces significant challenges due to the high costs of annotations and data collection, as well as geographically restricted data availability. To address these challenges, synthetic data offer a promising solution by being unrestricted and automatically annotatable, thus enabling the provision of large and diverse datasets. We develop a specialized synthetic data generation pipeline for EO and introduce SynRS3D, the largest synthetic RS dataset. SynRS3D comprises 69,667 high-resolution optical images that cover six different city styles worldwide and feature eight land cover types, precise height information, and building change masks. To further enhance its utility, we develop a novel multi-task unsupervised domain adaptation (UDA) method, RS3DAda, coupled with our synthetic dataset, which facilitates the RS-specific transition from synthetic to real scenarios for land cover mapping and height estimation tasks, ultimately enabling global monocular 3D semantic understanding based on synthetic data. Extensive experiments on various real-world datasets demonstrate the adaptability and effectiveness of our synthetic dataset and the proposed RS3DAda method. SynRS3D and related codes are available at https://github.com/JTRNEO/SynRS3D.