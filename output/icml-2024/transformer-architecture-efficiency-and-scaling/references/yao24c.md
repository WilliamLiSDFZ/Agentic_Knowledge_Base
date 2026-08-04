---
title: "Mobile Attention: Mobile-Friendly Linear-Attention for Vision Transformers"
source: "https://proceedings.mlr.press/v235/yao24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yao24c/yao24c.pdf"
categories: ['transformer-architecture-efficiency-and-scaling']
tags: ['vision-transformer', 'linear-attention', 'mobile-efficiency', 'low-complexity']
venue: "ICML 2024"
tldr: "A mobile-friendly linear attention mechanism is proposed to reduce the quadratic complexity of vision transformers for deployment on mobile devices."
---

# Mobile Attention: Mobile-Friendly Linear-Attention for Vision Transformers

**Source**: [https://proceedings.mlr.press/v235/yao24c.html](https://proceedings.mlr.press/v235/yao24c.html)

**TLDR**: A mobile-friendly linear attention mechanism is proposed to reduce the quadratic complexity of vision transformers for deployment on mobile devices.

## Abstract

Vision Transformers (ViTs) excel in computer vision tasks due to their ability to capture global context among tokens. However, their quadratic complexity $\mathcal{O}(N^2D)$ in terms of token number $N$ and feature dimension $D$ limits practical use on mobile devices, necessitating more mobile-friendly ViTs with reduced latency. Multi-head linear-attention is emerging as a promising alternative with linear complexity $\mathcal{O}(NDd)$, where $d$ is the per-head dimension. Still, more compute is needed as $d$ gets large for model accuracy. Reducing $d$ improves mobile friendliness at the expense of excessive small heads weak at learning valuable subspaces, ultimately impeding model capability. To overcome this efficiency-capability dilemma, we propose a novel Mobile-Attention design with a head-competition mechanism empowered by information flow, which prevents overemphasis on less important subspaces upon trivial heads while preserving essential subspaces to ensure Transformer’s capability. It enables linear-time complexity on mobile devices by supporting a small per-head dimension $d$ for mobile efficiency. By replacing the standard attention of ViTs with Mobile-Attention, our optimized ViTs achieved enhanced model capacity and competitive performance in a range of computer vision tasks. Specifically, we have achieved remarkable reductions in latency on the iPhone 12. Code is available at https://github.com/thuml/MobileAttention.