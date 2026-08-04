---
title: "CCM: Real-Time Controllable Visual Content Creation Using Text-to-Image Consistency Models"
source: "https://proceedings.mlr.press/v235/xiao24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xiao24h/xiao24h.pdf"
categories: ['generative-models-and-variational-inference', 'image-quality-assessment-and-super-resolution']
tags: ['consistency-models', 'controllable-generation', 'text-to-image']
venue: "ICML 2024"
tldr: "CCM enables real-time controllable visual content creation by adding conditional controls to pre-trained consistency models."
---

# CCM: Real-Time Controllable Visual Content Creation Using Text-to-Image Consistency Models

**Source**: [https://proceedings.mlr.press/v235/xiao24h.html](https://proceedings.mlr.press/v235/xiao24h.html)

**TLDR**: CCM enables real-time controllable visual content creation by adding conditional controls to pre-trained consistency models.

## Abstract

Consistency Models (CMs) have showed a promise in creating high-quality images with few steps. However, the way to add new conditional controls to the pre-trained CMs has not been explored. In this paper, we explore the pivotal subject of leveraging the generative capacity and efficiency of consistency models to facilitate controllable visual content creation via ControlNet. First, it is observed that ControlNet trained for diffusion models (DMs) can be directly applied to CMs for high-level semantic controls but sacrifice image low-level details and realism. To tackle with this issue, we develop a CMs-tailored training strategy for ControlNet using the consistency training. It is substantiated that ControlNet can be successfully established through the consistency training technique. Besides, a unified adapter can be trained utilizing the consistency training, which enhances the adaptation of DM’s ControlNet. We quantitatively and qualitatively evaluate all strategies across various conditional controls, including sketch, hed, canny, depth, human pose, low-resolution image and masked image, with the pre-trained text-to-image latent consistency models.