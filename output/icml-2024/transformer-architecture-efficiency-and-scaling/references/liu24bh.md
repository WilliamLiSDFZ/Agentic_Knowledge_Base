---
title: "Unified Generation, Reconstruction, and Representation: Generalized Diffusion with Adaptive Latent Encoding-Decoding"
source: "https://proceedings.mlr.press/v235/liu24bh.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24bh/liu24bh.pdf"
categories: ['generative-models-and-variational-inference', 'transformer-architecture-efficiency-and-scaling']
tags: ['diffusion-models', 'latent-encoding', 'generative-models', 'reconstruction', 'unified-framework']
venue: "ICML 2024"
tldr: "A unified generalized diffusion framework with adaptive latent encoding-decoding that handles generation, reconstruction, and representation learning across discrete and continuous data."
---

# Unified Generation, Reconstruction, and Representation: Generalized Diffusion with Adaptive Latent Encoding-Decoding

**Source**: [https://proceedings.mlr.press/v235/liu24bh.html](https://proceedings.mlr.press/v235/liu24bh.html)

**TLDR**: A unified generalized diffusion framework with adaptive latent encoding-decoding that handles generation, reconstruction, and representation learning across discrete and continuous data.

## Abstract

The vast applications of deep generative models are anchored in three core capabilities—generating new instances, reconstructing inputs, and learning compact representations—across various data types, such as discrete text/protein sequences and continuous images. Existing model families, like variational autoencoders (VAEs), generative adversarial networks (GANs), autoregressive models, and (latent) diffusion models, generally excel in specific capabilities and data types but fall short in others. We introduce Generalized Encoding-Decoding Diffusion Probabilistic Models (EDDPMs) which integrate the core capabilities for broad applicability and enhanced performance. EDDPMs generalize the Gaussian noising-denoising in standard diffusion by introducing parameterized encoding-decoding. Crucially, EDDPMs are compatible with the well-established diffusion model objective and training recipes, allowing effective learning of the encoder-decoder parameters jointly with diffusion. By choosing appropriate encoder/decoder (e.g., large language models), EDDPMs naturally apply to different data types. Extensive experiments on text, proteins, and images demonstrate the flexibility to handle diverse data and tasks and the strong improvement over various existing models. Code is available at https://github.com/guangyliu/EDDPM .