---
title: "How Deep Do We Need: Accelerating Training and Inference of Neural ODEs via Control Perspective"
source: "https://proceedings.mlr.press/v235/miao24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/miao24a/miao24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'transformer-architecture-efficiency-and-scaling']
tags: ['neural-ODEs', 'control-theory', 'training-efficiency']
venue: "ICML 2024"
tldr: "Accelerates Neural ODE training and inference by optimizing depth and integration steps through a control-theoretic perspective."
---

# How Deep Do We Need: Accelerating Training and Inference of Neural ODEs via Control Perspective

**Source**: [https://proceedings.mlr.press/v235/miao24a.html](https://proceedings.mlr.press/v235/miao24a.html)

**TLDR**: Accelerates Neural ODE training and inference by optimizing depth and integration steps through a control-theoretic perspective.

## Abstract

Neural Ordinary Differential Equations (ODEs) have shown promise in learning continuous dynamics. However, their slow training and inference speed hinder wider applications. In this paper, we propose to optimize Neural ODEs from a spatial and temporal perspective, drawing inspiration from control theory. We aim to find a reasonable depth of the network, accelerating both training and inference while maintaining network performance. Two approaches are proposed. One reformulates training as a minimum-time optimal control problem directly in a single stage to search for the terminal time and network weights. The second approach uses pre-training coupled with a Lyapunov method in an initial stage, and then at a secondary stage introduces a safe terminal time updating mechanism in the forward direction. Experimental results demonstrate the effectiveness of speeding up Neural ODEs.