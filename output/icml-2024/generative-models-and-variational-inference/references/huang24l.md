---
title: "Bayesian Power Steering: An Effective Approach for Domain Adaptation of Diffusion Models"
source: "https://proceedings.mlr.press/v235/huang24l.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24l/huang24l.pdf"
categories: ['generative-models-and-variational-inference', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['diffusion-models', 'domain-adaptation', 'bayesian-fine-tuning']
venue: "ICML 2024"
tldr: "Proposes Bayesian Power Steering, a Bayesian framework for fine-tuning large diffusion models for domain adaptation."
---

# Bayesian Power Steering: An Effective Approach for Domain Adaptation of Diffusion Models

**Source**: [https://proceedings.mlr.press/v235/huang24l.html](https://proceedings.mlr.press/v235/huang24l.html)

**TLDR**: Proposes Bayesian Power Steering, a Bayesian framework for fine-tuning large diffusion models for domain adaptation.

## Abstract

We propose a Bayesian framework for fine-tuning large diffusion models with a novel network structure called Bayesian Power Steering (BPS). We clarify the meaning behind adaptation from a large probability space to a small probability space and explore the task of fine-tuning pre-trained models using learnable modules from a Bayesian perspective. BPS extracts task-specific knowledge from a pre-trained model’s learned prior distribution. It efficiently leverages large diffusion models, differentially intervening different hidden features with a head-heavy and foot-light configuration. Experiments highlight the superiority of BPS over contemporary methods across a range of tasks even with limited amount of data. Notably, BPS attains an FID score of 10.49 under the sketch condition on the COCO17 dataset.