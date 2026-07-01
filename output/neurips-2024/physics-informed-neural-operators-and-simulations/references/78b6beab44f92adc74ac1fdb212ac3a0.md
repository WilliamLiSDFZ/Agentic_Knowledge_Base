---
title: "NeuMA: Neural Material Adaptor for Visual Grounding of Intrinsic Dynamics"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/78b6beab44f92adc74ac1fdb212ac3a0-Abstract-Conference.html"
categories: ['physics-informed-neural-operators-and-simulations', 'visual-language-multimodal-generation-reasoning']
tags: ['physical-simulation', 'neural-material', 'visual-grounding']
venue: "NeurIPS 2024"
tldr: "NeuMA is a neural material adaptor that bridges neural and physics-based simulators for visually grounded intrinsic dynamics estimation."
---

# NeuMA: Neural Material Adaptor for Visual Grounding of Intrinsic Dynamics

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/78b6beab44f92adc74ac1fdb212ac3a0-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/78b6beab44f92adc74ac1fdb212ac3a0-Abstract-Conference.html)

**TLDR**: NeuMA is a neural material adaptor that bridges neural and physics-based simulators for visually grounded intrinsic dynamics estimation.

## Abstract

While humans effortlessly discern intrinsic dynamics and adapt to new scenarios, modern AI systems often struggle. Current methods for visual grounding of dynamics either use pure neural-network-based simulators (black box), which may violate physical laws, or traditional physical simulators (white box), which rely on expert-defined equations that may not fully capture actual dynamics. We propose the Neural Material Adaptor (NeuMA), which integrates existing physical laws with learned corrections, facilitating accurate learning of actual dynamics while maintaining the generalizability and interpretability of physical priors. Additionally, we propose Particle-GS, a particle-driven 3D Gaussian Splatting variant that bridges simulation and observed images, allowing back-propagate image gradients to optimize the simulator. Comprehensive experiments on various dynamics in terms of grounded particle accuracy, dynamic rendering quality, and generalization ability demonstrate that NeuMA can accurately capture intrinsic dynamics. Project Page: https://xjay18.github.io/projects/neuma.html.