---
title: "Detecting and Identifying Selection Structure in Sequential Data"
source: "https://proceedings.mlr.press/v235/zheng24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zheng24k/zheng24k.pdf"
categories: ['causal-inference-and-discovery-methods']
tags: ['selection-bias', 'causal-discovery', 'sequential-data', 'latent-objectives']
venue: "ICML 2024"
tldr: "This paper argues for identifying and leveraging selection structure in sequential data rather than merely correcting for it as a bias."
---

# Detecting and Identifying Selection Structure in Sequential Data

**Source**: [https://proceedings.mlr.press/v235/zheng24k.html](https://proceedings.mlr.press/v235/zheng24k.html)

**TLDR**: This paper argues for identifying and leveraging selection structure in sequential data rather than merely correcting for it as a bias.

## Abstract

We argue that the selective inclusion of data points based on latent objectives is common in practical situations, such as music sequences. Since this selection process often distorts statistical analysis, previous work primarily views it as a bias to be corrected and proposes various methods to mitigate its effect. However, while controlling this bias is crucial, selection also offers an opportunity to provide a deeper insight into the hidden generation process, as it is a fundamental mechanism underlying what we observe. In particular, overlooking selection in sequential data can lead to an incomplete or overcomplicated inductive bias in modeling, such as assuming a universal autoregressive structure for all dependencies. Therefore, rather than merely viewing it as a bias, we explore the causal structure of selection in sequential data to delve deeper into the complete causal process. Specifically, we show that selection structure is identifiable without any parametric assumptions or interventional experiments. Moreover, even in cases where selection variables coexist with latent confounders, we still establish the nonparametric identifiability under appropriate structural conditions. Meanwhile, we also propose a provably correct algorithm to detect and identify selection structures as well as other types of dependencies. The framework has been validated empirically on both synthetic data and real-world music.