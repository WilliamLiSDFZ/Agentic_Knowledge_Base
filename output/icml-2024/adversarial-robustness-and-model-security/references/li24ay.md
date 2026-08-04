---
title: "PID: Prompt-Independent Data Protection Against Latent Diffusion Models"
source: "https://proceedings.mlr.press/v235/li24ay.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24ay/li24ay.pdf"
categories: ['adversarial-robustness-and-model-security', 'generative-models-and-variational-inference']
tags: ['adversarial-defense', 'latent-diffusion-models', 'privacy-protection']
venue: "ICML 2024"
tldr: "Proposes a prompt-independent data protection method to defend personal images against unauthorized few-shot fine-tuning of latent diffusion models."
---

# PID: Prompt-Independent Data Protection Against Latent Diffusion Models

**Source**: [https://proceedings.mlr.press/v235/li24ay.html](https://proceedings.mlr.press/v235/li24ay.html)

**TLDR**: Proposes a prompt-independent data protection method to defend personal images against unauthorized few-shot fine-tuning of latent diffusion models.

## Abstract

The few-shot fine-tuning of Latent Diffusion Models (LDMs) has enabled them to grasp new concepts from a limited number of images. However, given the vast amount of personal images accessible online, this capability raises critical concerns about civil privacy. While several previous defense methods have been developed to prevent such misuse of LDMs, they typically assume that the textual prompts used by data protectors exactly match those employed by data exploiters. In this paper, we first empirically demonstrate that breaking this assumption, i.e., in cases where discrepancies exist between the textual conditions used by protectors and exploiters, could substantially reduces the effectiveness of these defenses. Furthermore, considering the visual encoder’s independence from textual prompts, we delve into the visual encoder and thoroughly investigate how manipulating the visual encoder affects the few-shot fine-tuning process of LDMs. Drawing on these insights, we propose a simple yet effective method called Prompt-Independent Defense (PID) to safeguard privacy against LDMs. We show that PID can act as a strong privacy shield on its own while requiring significantly less computational power. We believe our studies, along with the comprehensive understanding and new defense method, provide a notable advance toward reliable data protection against LDMs.