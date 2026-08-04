---
title: "Reflected Flow Matching"
source: "https://proceedings.mlr.press/v235/xie24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xie24k/xie24k.pdf"
categories: ['generative-models-and-variational-inference', 'sampling-and-optimization-on-manifolds']
tags: ['flow-matching', 'constrained-domains', 'normalizing-flows']
venue: "ICML 2024"
tldr: "Reflected flow matching extends flow matching to constrained domains by incorporating reflection to keep trajectories within boundaries."
---

# Reflected Flow Matching

**Source**: [https://proceedings.mlr.press/v235/xie24k.html](https://proceedings.mlr.press/v235/xie24k.html)

**TLDR**: Reflected flow matching extends flow matching to constrained domains by incorporating reflection to keep trajectories within boundaries.

## Abstract

Continuous normalizing flows (CNFs) learn an ordinary differential equation to transform prior samples into data. Flow matching (FM) has recently emerged as a simulation-free approach for training CNFs by regressing a velocity model towards the conditional velocity field. However, on constrained domains, the learned velocity model may lead to undesirable flows that result in highly unnatural samples, e.g., oversaturated images, due to both flow matching error and simulation error. To address this, we add a boundary constraint term to CNFs, which leads to reflected CNFs that keep trajectories within the constrained domains. We propose reflected flow matching (RFM) to train the velocity model in reflected CNFs by matching the conditional velocity fields in a simulation-free manner, similar to the vanilla FM. Moreover, the analytical form of conditional velocity fields in RFM avoids potentially biased approximations, making it superior to existing score-based generative models on constrained domains. We demonstrate that RFM achieves comparable or better results on standard image benchmarks and produces high-quality class-conditioned samples under high guidance weight.