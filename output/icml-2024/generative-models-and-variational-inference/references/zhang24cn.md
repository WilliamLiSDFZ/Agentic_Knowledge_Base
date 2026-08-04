---
title: "The Emergence of Reproducibility and Consistency in Diffusion Models"
source: "https://proceedings.mlr.press/v235/zhang24cn.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24cn/zhang24cn.pdf"
categories: ['generative-models-and-variational-inference', 'neural-network-learning-dynamics-theory']
tags: ['diffusion-models', 'reproducibility', 'noise-consistency']
venue: "ICML 2024"
tldr: "Investigates and explains the phenomenon of consistent reproducibility across different diffusion models given the same noise input."
---

# The Emergence of Reproducibility and Consistency in Diffusion Models

**Source**: [https://proceedings.mlr.press/v235/zhang24cn.html](https://proceedings.mlr.press/v235/zhang24cn.html)

**TLDR**: Investigates and explains the phenomenon of consistent reproducibility across different diffusion models given the same noise input.

## Abstract

In this work, we investigate an intriguing and prevalent phenomenon of diffusion models which we term as "consistent model reproducibility”: given the same starting noise input and a deterministic sampler, different diffusion models often yield remarkably similar outputs. We confirm this phenomenon through comprehensive experiments, implying that different diffusion models consistently reach the same data distribution and score function regardless of diffusion model frameworks, model architectures, or training procedures. More strikingly, our further investigation implies that diffusion models are learning distinct distributions influenced by the training data size. This is evident in two distinct training regimes: (I) "memorization regime,” where the diffusion model overfits to the training data distribution, and (ii) "generalization regime,” where the model learns the underlying data distribution. Our study also finds that this valuable property generalizes to many variants of diffusion models, including those for conditional generation and solving inverse problems. Lastly, we discuss how our findings connect to existing research and highlight the practical implications of our discoveries.