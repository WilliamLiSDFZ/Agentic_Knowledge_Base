---
title: "Theory of Consistency Diffusion Models: Distribution Estimation Meets Fast Sampling"
source: "https://proceedings.mlr.press/v235/dou24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dou24a/dou24a.pdf"
categories: ['generative-models-and-variational-inference', 'neural-network-learning-dynamics-theory']
tags: ['diffusion-models', 'consistency-models', 'fast-sampling', 'distribution-estimation']
venue: "ICML 2024"
tldr: "A theoretical analysis of consistency diffusion models establishing distribution estimation guarantees while enabling fast sampling."
---

# Theory of Consistency Diffusion Models: Distribution Estimation Meets Fast Sampling

**Source**: [https://proceedings.mlr.press/v235/dou24a.html](https://proceedings.mlr.press/v235/dou24a.html)

**TLDR**: A theoretical analysis of consistency diffusion models establishing distribution estimation guarantees while enabling fast sampling.

## Abstract

Diffusion models have revolutionized various application domains, including computer vision and audio generation. Despite the state-of-the-art performance, diffusion models are known for their slow sample generation due to the extensive number of steps involved. In response, consistency models have been developed to merge multiple steps in the sampling process, thereby significantly boosting the speed of sample generation without compromising quality. This paper contributes towards the first statistical theory for consistency models, formulating their training as a distribution discrepancy minimization problem. Our analysis yields statistical estimation rates based on the Wasserstein distance for consistency models, matching those of vanilla diffusion models. Additionally, our results encompass the training of consistency models through both distillation and isolation methods, demystifying their underlying advantage.