---
title: "Disguised Copyright Infringement of Latent Diffusion Models"
source: "https://proceedings.mlr.press/v235/lu24m.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lu24m/lu24m.pdf"
categories: ['adversarial-robustness-and-model-security', 'open-ai-governance-and-data-ethics']
tags: ['copyright-infringement', 'latent-diffusion', 'generative-models', 'disguised-copying', 'IP-protection']
venue: "ICML 2024"
tldr: "Reveals disguised copyright infringement in latent diffusion models where generated samples are substantially similar to training data even without direct inclusion."
---

# Disguised Copyright Infringement of Latent Diffusion Models

**Source**: [https://proceedings.mlr.press/v235/lu24m.html](https://proceedings.mlr.press/v235/lu24m.html)

**TLDR**: Reveals disguised copyright infringement in latent diffusion models where generated samples are substantially similar to training data even without direct inclusion.

## Abstract

Copyright infringement may occur when a generative model produces samples substantially similar to some copyrighted data that it had access to during the training phase. The notion of access usually refers to including copyrighted samples directly in the training dataset, which one may inspect to identify an infringement. We argue that such visual auditing largely overlooks a concealed copyright infringement, where one constructs a disguise that looks drastically different from the copyrighted sample yet still induces the effect of training Latent Diffusion Models on it. Such disguises only require indirect access to the copyrighted material and cannot be visually distinguished, thus easily circumventing the current auditing tools. In this paper, we provide a better understanding of such disguised copyright infringement by uncovering the disguises generation algorithm, the revelation of the disguises, and importantly, how to detect them to augment the existing toolbox. Additionally, we introduce a broader notion of acknowledgment for comprehending such indirect access.