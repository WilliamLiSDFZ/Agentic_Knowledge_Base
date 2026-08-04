---
title: "An Explicit Frame Construction for Normalizing 3D Point Clouds"
source: "https://proceedings.mlr.press/v235/baker24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/baker24a/baker24a.pdf"
categories: ['3d-vision-and-scene-understanding', 'equivariant-neural-networks-and-symmetry-learning']
tags: ['3D-point-clouds', 'reference-frame', 'normalization']
venue: "ICML 2024"
tldr: "An explicit frame construction method is proposed for normalizing 3D point clouds without predefined reference frames."
---

# An Explicit Frame Construction for Normalizing 3D Point Clouds

**Source**: [https://proceedings.mlr.press/v235/baker24a.html](https://proceedings.mlr.press/v235/baker24a.html)

**TLDR**: An explicit frame construction method is proposed for normalizing 3D point clouds without predefined reference frames.

## Abstract

Many real-world datasets are represented as 3D point clouds – yet they often lack a predefined reference frame, posing a challenge for machine learning or general data analysis. Traditional methods for determining reference frames and normalizing 3D point clouds often struggle with specific inputs, lack theoretical guarantees, or require massive data. We introduce a new algorithm that overcomes these limitations and guarantees both universality and compatibility with any learnable framework for 3D point cloud analysis. Our algorithm works with any input point cloud and performs consistently regardless of input complexities, unlike data-driven methods that are susceptible to biases or limited training data. Empirically, our algorithm outperforms existing methods in effectiveness and generalizability across diverse benchmark datasets. Code is available at https://github.com/Utah-Math-Data-Science/alignment.