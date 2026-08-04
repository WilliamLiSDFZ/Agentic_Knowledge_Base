---
title: "Vague Prototype-Oriented Diffusion Model for Multi-Class Anomaly Detection"
source: "https://proceedings.mlr.press/v235/li24u.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24u/li24u.pdf"
categories: ['anomaly-and-out-of-distribution-detection', 'generative-models-and-variational-inference']
tags: ['anomaly-detection', 'diffusion-model', 'multi-class', 'prototype', 'reconstruction']
venue: "ICML 2024"
tldr: "A vague prototype-oriented diffusion model addresses the identical shortcut problem in multi-class unsupervised anomaly detection."
---

# Vague Prototype-Oriented Diffusion Model for Multi-Class Anomaly Detection

**Source**: [https://proceedings.mlr.press/v235/li24u.html](https://proceedings.mlr.press/v235/li24u.html)

**TLDR**: A vague prototype-oriented diffusion model addresses the identical shortcut problem in multi-class unsupervised anomaly detection.

## Abstract

Multi-class unsupervised anomaly detection aims to create a unified model for identifying anomalies in objects from multiple classes when only normal data is available. In such a challenging setting, widely used reconstruction-based networks persistently grapple with the "identical shortcut" problem, wherein the infiltration of abnormal information from the condition biases the output towards an anomalous distribution. In response to this critical challenge, we introduce a Vague Prototype-Oriented Diffusion Model (VPDM) that extracts only fundamental information from the condition to prevent the occurrence of the "identical shortcut" problem from the input layer. This model leverages prototypes that contain only vague information about the target as the initial condition. Subsequently, a novel conditional diffusion model is introduced to incrementally enhance details based on vague conditions. Finally, a Vague Prototype-Oriented Optimal Transport (VPOT) method is proposed to provide more accurate information about conditions. All these components are seamlessly integrated into a unified optimization objective. The effectiveness of our approach is demonstrated across diverse datasets, including the MVTec, VisA, and MPDD benchmarks, achieving state-of-the-art results.