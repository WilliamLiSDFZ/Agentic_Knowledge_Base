---
title: "OxyGenerator: Reconstructing Global Ocean Deoxygenation Over a Century with Deep Learning"
source: "https://proceedings.mlr.press/v235/lu24n.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lu24n/lu24n.pdf"
categories: ['continual-learning-memory-plasticity', 'neural-operators-for-pde-solving']
tags: ['ocean-deoxygenation', 'deep-learning', 'reconstruction', 'climate', 'scientific-modeling']
venue: "ICML 2024"
tldr: "Uses deep learning to reconstruct over a century of global ocean deoxygenation data from sparse historical observations."
---

# OxyGenerator: Reconstructing Global Ocean Deoxygenation Over a Century with Deep Learning

**Source**: [https://proceedings.mlr.press/v235/lu24n.html](https://proceedings.mlr.press/v235/lu24n.html)

**TLDR**: Uses deep learning to reconstruct over a century of global ocean deoxygenation data from sparse historical observations.

## Abstract

Accurately reconstructing the global ocean deoxygenation over a century is crucial for assessing and protecting marine ecosystem. Existing expert-dominated numerical simulations fail to catch up with the dynamic variation caused by global warming and human activities. Besides, due to the high-cost data collection, the historical observations are severely sparse, leading to big challenge for precise reconstruction. In this work, we propose OxyGenerator, the first deep learning based model, to reconstruct the global ocean deoxygenation from 1920 to 2023. Specifically, to address the heterogeneity across large temporal and spatial scales, we propose zoning-varying graph message-passing to capture the complex oceanographic correlations between missing values and sparse observations. Additionally, to further calibrate the uncertainty, we incorporate inductive bias from dissolved oxygen (DO) variations and chemical effects. Compared with in-situ DO observations, OxyGenerator significantly outperforms CMIP6 numerical simulations, reducing MAPE by 38.77%, demonstrating a promising potential to understand the “breathless ocean” in data-driven manner.