---
title: "Causal Effect Identification in LiNGAM Models with Latent Confounders"
source: "https://proceedings.mlr.press/v235/tramontano24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tramontano24a/tramontano24a.pdf"
categories: ['causal-inference-and-discovery-methods']
tags: ['LiNGAM', 'causal-identification', 'latent-confounders']
venue: "ICML 2024"
tldr: "Provides complete graphical characterization of generic identifiability of causal effects in linear non-Gaussian acyclic models with latent variables."
---

# Causal Effect Identification in LiNGAM Models with Latent Confounders

**Source**: [https://proceedings.mlr.press/v235/tramontano24a.html](https://proceedings.mlr.press/v235/tramontano24a.html)

**TLDR**: Provides complete graphical characterization of generic identifiability of causal effects in linear non-Gaussian acyclic models with latent variables.

## Abstract

We study the generic identifiability of causal effects in linear non-Gaussian acyclic models (LiNGAM) with latent variables. We consider the problem in two main settings: When the causal graph is known a priori, and when it is unknown. In both settings, we provide a complete graphical characterization of the identifiable direct or total causal effects among observed variables. Moreover, we propose efficient algorithms to certify the graphical conditions. Finally, we propose an adaptation of the reconstruction independent component analysis (RICA) algorithm that estimates the causal effects from the observational data given the causal graph. Experimental results show the effectiveness of the proposed method in estimating the causal effects.