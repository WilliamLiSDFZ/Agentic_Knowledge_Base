---
title: "Deep Neural Room Acoustics Primitive"
source: "https://proceedings.mlr.press/v235/he24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/he24b/he24b.pdf"
categories: ['audio-and-music-generation-diffusion-models', 'neural-operators-for-pde-solving']
tags: ['room-acoustics', 'neural-networks', 'room-impulse-response']
venue: "ICML 2024"
tldr: "A deep neural network primitive is proposed to model room acoustics and predict room impulse responses for arbitrary source-receiver positions in 3D spaces."
---

# Deep Neural Room Acoustics Primitive

**Source**: [https://proceedings.mlr.press/v235/he24b.html](https://proceedings.mlr.press/v235/he24b.html)

**TLDR**: A deep neural network primitive is proposed to model room acoustics and predict room impulse responses for arbitrary source-receiver positions in 3D spaces.

## Abstract

The primary objective of room acoustics is to model the intricate sound propagation dynamics from any source to receiver position within enclosed 3D spaces. These dynamics are encapsulated in the form of a 1D room impulse response (RIR). Precisely measuring RIR is difficult due to the complexity of sound propagation encompassing reflection, diffraction, and absorption. In this work, we propose to learn a continuous neural room acoustics field that implicitly encodes all essential sound propagation primitives for each enclosed 3D space, so that we can infer the RIR corresponding to arbitrary source-receiver positions unseen in the training dataset. Our framework, dubbed DeepNeRAP, is trained in a self-supervised manner without requiring direct access to RIR ground truth that is often needed in prior methods. The key idea is to design two cooperative acoustic agents to actively probe a 3D space, one emitting and the other receiving sound at various locations. Analyzing this sound helps to inversely characterize the acoustic primitives. Our framework is well-grounded in the fundamental physical principles of sound propagation, including reciprocity and globality, and thus is acoustically interpretable and meaningful. We present experiments on both synthetic and real-world datasets, demonstrating superior quality in RIR estimation against closely related methods.