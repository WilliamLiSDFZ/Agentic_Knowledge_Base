---
title: "Scale-Free Image Keypoints Using Differentiable Persistent Homology"
source: "https://proceedings.mlr.press/v235/barbarani24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/barbarani24a/barbarani24a.pdf"
categories: ['topological-deep-learning-persistent-homology', '3d-vision-and-scene-understanding']
tags: ['keypoint-detection', 'persistent-homology', 'scale-invariance']
venue: "ICML 2024"
tldr: "A novel scale-free image keypoint detection method leveraging Morse theory and differentiable persistent homology is introduced."
---

# Scale-Free Image Keypoints Using Differentiable Persistent Homology

**Source**: [https://proceedings.mlr.press/v235/barbarani24a.html](https://proceedings.mlr.press/v235/barbarani24a.html)

**TLDR**: A novel scale-free image keypoint detection method leveraging Morse theory and differentiable persistent homology is introduced.

## Abstract

In computer vision, keypoint detection is a fundamental task, with applications spanning from robotics to image retrieval; however, existing learning-based methods suffer from scale dependency, and lack flexibility. This paper introduces a novel approach that leverages Morse theory and persistent homology, powerful tools rooted in algebraic topology. We propose a novel loss function based on the recent introduction of a notion of subgradient in persistent homology, paving the way towards topological learning. Our detector, MorseDet, is the first topology-based learning model for feature detection, which achieves competitive performance in keypoint repeatability and introduces a principled and theoretically robust approach to the problem.