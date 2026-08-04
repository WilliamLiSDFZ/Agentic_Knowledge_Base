---
title: "Two-Stage Shadow Inclusion Estimation: An IV Approach for Causal Inference under Latent Confounding and Collider Bias"
source: "https://proceedings.mlr.press/v235/li24bu.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24bu/li24bu.pdf"
categories: ['causal-inference-and-discovery-methods', 'causal-ml-for-clinical-decision-making']
tags: ['instrumental-variables', 'latent-confounding', 'collider-bias']
venue: "ICML 2024"
tldr: "Presents a two-stage shadow inclusion estimator addressing both latent confounding and collider bias in causal inference from observational data."
---

# Two-Stage Shadow Inclusion Estimation: An IV Approach for Causal Inference under Latent Confounding and Collider Bias

**Source**: [https://proceedings.mlr.press/v235/li24bu.html](https://proceedings.mlr.press/v235/li24bu.html)

**TLDR**: Presents a two-stage shadow inclusion estimator addressing both latent confounding and collider bias in causal inference from observational data.

## Abstract

Latent confounding bias and collider bias are two key challenges of causal inference in observational studies. Latent confounding bias occurs when failing to control the unmeasured covariates that are common causes of treatments and outcomes, which can be addressed by using the Instrumental Variable (IV) approach. Collider bias comes from non-random sample selection caused by both treatments and outcomes, which can be addressed by using a different type of instruments, i.e., shadow variables. However, in most scenarios, these two biases simultaneously exist in observational data, and the previous methods focusing on either one are inadequate. To the best of our knowledge, no approach has been developed for causal inference when both biases exist. In this paper, we propose a novel IV approach, Two-Stage Shadow Inclusion (2SSI), which can simultaneously address latent confounding bias and collider bias by utilizing the residual of the treatment as a shadow variable. Extensive experimental results on benchmark synthetic datasets and a real-world dataset show that 2SSI achieves noticeable performance improvement when both biases exist compared to existing methods.