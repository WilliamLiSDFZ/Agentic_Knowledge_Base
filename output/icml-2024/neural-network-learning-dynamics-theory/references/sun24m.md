---
title: "Learning High-Frequency Functions Made Easy with Sinusoidal Positional Encoding"
source: "https://proceedings.mlr.press/v235/sun24m.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sun24m/sun24m.pdf"
categories: ['neural-network-learning-dynamics-theory']
tags: ['positional-encoding', 'high-frequency-learning', 'neural-tangent-kernel']
venue: "ICML 2024"
tldr: "Sinusoidal positional encoding is shown to simplify and improve learning of high-frequency functions in tasks like 3D view synthesis and time series regression."
---

# Learning High-Frequency Functions Made Easy with Sinusoidal Positional Encoding

**Source**: [https://proceedings.mlr.press/v235/sun24m.html](https://proceedings.mlr.press/v235/sun24m.html)

**TLDR**: Sinusoidal positional encoding is shown to simplify and improve learning of high-frequency functions in tasks like 3D view synthesis and time series regression.

## Abstract

Fourier features based positional encoding (PE) is commonly used in machine learning tasks that involve learning high-frequency features from low-dimensional inputs, such as 3D view synthesis and time series regression with neural tangent kernels. Despite their effectiveness, existing PEs require manual, empirical adjustment of crucial hyperparameters, specifically the Fourier features, tailored to each unique task. Further, PEs face challenges in efficiently learning high-frequency functions, particularly in tasks with limited data. In this paper, we introduce sinusoidal PE (SPE), designed to efficiently learn adaptive frequency features closely aligned with the true underlying function. Our experiments demonstrate that SPE, without hyperparameter tuning, consistently achieves enhanced fidelity and faster training across various tasks, including 3D view synthesis, Text-to-Speech generation, and 1D regression. SPE is implemented as a direct replacement for existing PEs. Its plug-and-play nature lets numerous tasks easily adopt and benefit from SPE.