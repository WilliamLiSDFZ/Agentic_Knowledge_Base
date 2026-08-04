---
title: "Why do Variational Autoencoders Really Promote Disentanglement?"
source: "https://proceedings.mlr.press/v235/bhowal24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bhowal24a/bhowal24a.pdf"
categories: ['generative-models-and-variational-inference', 'neural-network-learning-dynamics-theory']
tags: ['variational-autoencoders', 'disentanglement', 'representation-learning', 'loss-function']
venue: "ICML 2024"
tldr: "This paper theoretically analyzes why VAEs promote disentangled representations, attributing the effect to specific loss function properties that prevent latent space rotation."
---

# Why do Variational Autoencoders Really Promote Disentanglement?

**Source**: [https://proceedings.mlr.press/v235/bhowal24a.html](https://proceedings.mlr.press/v235/bhowal24a.html)

**TLDR**: This paper theoretically analyzes why VAEs promote disentangled representations, attributing the effect to specific loss function properties that prevent latent space rotation.

## Abstract

Despite not being designed for this purpose, the use of variational autoencoders (VAEs) has proven remarkably effective for disentangled representation learning (DRL). Recent research attributes this success to certain characteristics of the loss function that prevent latent space rotation, or hypothesize about the orthogonality properties of the decoder by drawing parallels with principal component analysis (PCA). This hypothesis, however, has only been tested experimentally for linear VAEs, and the theoretical justification still remains an open problem. Moreover, since real-world VAEs are often inherently non-linear due to the use of neural architectures, understanding DRL capabilities of real-world VAEs remains a critical task. Our work takes a step towards understanding disentanglement in real-world VAEs to theoretically establish how the orthogonality properties of the decoder promotes disentanglement in practical applications. Complementary to our theoretical contributions, our experimental results corroborate our analysis. Code is available at https://github.com/criticalml-uw/Disentanglement-in-VAE.