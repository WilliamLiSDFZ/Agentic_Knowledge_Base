---
title: "Membership Inference Attacks on Diffusion Models via Quantile Regression"
source: "https://proceedings.mlr.press/v235/tang24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tang24g/tang24g.pdf"
categories: ['adversarial-robustness-and-model-security']
tags: ['membership-inference', 'diffusion-models', 'privacy']
venue: "ICML 2024"
tldr: "A membership inference attack on diffusion models is demonstrated using quantile regression to detect training data leakage."
---

# Membership Inference Attacks on Diffusion Models via Quantile Regression

**Source**: [https://proceedings.mlr.press/v235/tang24g.html](https://proceedings.mlr.press/v235/tang24g.html)

**TLDR**: A membership inference attack on diffusion models is demonstrated using quantile regression to detect training data leakage.

## Abstract

Recently, diffusion models have become popular tools for image synthesis due to their high-quality outputs. However, like other large models, they may leak private information about their training data. Here, we demonstrate a privacy vulnerability of diffusion models through a membership inference (MI) attack, which aims to identify whether a target example belongs to the training set when given the trained diffusion model. Our proposed MI attack learns quantile regression models that predict (a quantile of) the distribution of reconstruction loss on examples not used in training. This allows us to define a granular hypothesis test for determining the membership of a point in the training set, based on thresholding the reconstruction loss of that point using a custom threshold tailored to the example. We also provide a simple bootstrap technique that takes a majority membership prediction over ”a bag of weak attackers” which improves the accuracy over individual quantile regression models. We show that our attack outperforms the prior state-of-the-art attack while being substantially less computationally expensive — prior attacks required training multiple ”shadow models” with the same architecture as the model under attack, whereas our attack requires training only much smaller models.