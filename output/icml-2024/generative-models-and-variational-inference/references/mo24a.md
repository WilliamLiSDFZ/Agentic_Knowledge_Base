---
title: "TERD: A Unified Framework for Safeguarding Diffusion Models Against Backdoors"
source: "https://proceedings.mlr.press/v235/mo24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mo24a/mo24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'generative-models-and-variational-inference']
tags: ['diffusion-models', 'backdoor-attacks', 'defense']
venue: "ICML 2024"
tldr: "Proposes TERD, a unified framework for detecting and mitigating backdoor attacks in diffusion-based image generation models."
---

# TERD: A Unified Framework for Safeguarding Diffusion Models Against Backdoors

**Source**: [https://proceedings.mlr.press/v235/mo24a.html](https://proceedings.mlr.press/v235/mo24a.html)

**TLDR**: Proposes TERD, a unified framework for detecting and mitigating backdoor attacks in diffusion-based image generation models.

## Abstract

Diffusion models have achieved notable success in image generation, but they remain highly vulnerable to backdoor attacks, which compromise their integrity by producing specific undesirable outputs when presented with a pre-defined trigger. In this paper, we investigate how to protect diffusion models from this dangerous threat. Specifically, we propose TERD, a backdoor defense framework that builds unified modeling for current attacks, which enables us to derive an accessible reversed loss. A trigger reversion strategy is further employed: an initial approximation of the trigger through noise sampled from a prior distribution, followed by refinement through differential multi-step samplers. Additionally, with the reversed trigger, we propose backdoor detection from the noise space, introducing the first backdoor input detection approach for diffusion models and a novel model detection algorithm that calculates the KL divergence between reversed and benign distributions. Extensive evaluations demonstrate that TERD secures a 100% True Positive Rate (TPR) and True Negative Rate (TNR) across datasets of varying resolutions. TERD also demonstrates nice adaptability to other Stochastic Differential Equation (SDE)-based models. Our code is available at https://github.com/PKU-ML/TERD.