---
title: "Hybrid Neural Representations for Spherical Data"
source: "https://proceedings.mlr.press/v235/kim24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24i/kim24i.pdf"
categories: ['neural-operators-for-pde-solving', 'equivariant-neural-networks-and-symmetry-learning']
tags: ['spherical-data', 'neural-representations', 'climate-modeling']
venue: "ICML 2024"
tldr: "Proposes hybrid neural representations for spherical data applied to weather, climate, and cosmic microwave background datasets."
---

# Hybrid Neural Representations for Spherical Data

**Source**: [https://proceedings.mlr.press/v235/kim24i.html](https://proceedings.mlr.press/v235/kim24i.html)

**TLDR**: Proposes hybrid neural representations for spherical data applied to weather, climate, and cosmic microwave background datasets.

## Abstract

In this paper, we study hybrid neural representations for spherical data, a domain of increasing relevance in scientific research. In particular, our work focuses on weather and climate data as well as cosmic microwave background (CMB) data. Although previous studies have delved into coordinate-based neural representations for spherical signals, they often fail to capture the intricate details of highly nonlinear signals. To address this limitation, we introduce a novel approach named Hybrid Neural Representations for Spherical data (HNeR-S). Our main idea is to use spherical feature-grids to obtain positional features which are combined with a multi-layer perceptron to predict the target signal. We consider feature-grids with equirectangular and hierarchical equal area isolatitude pixelization structures that align with weather data and CMB data, respectively. We extensively verify the effectiveness of our HNeR-S for regression, super-resolution, temporal interpolation, and compression tasks.