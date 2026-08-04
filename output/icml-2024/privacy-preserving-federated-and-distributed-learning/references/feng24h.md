---
title: "Privacy Backdoors: Stealing Data with Corrupted Pretrained Models"
source: "https://proceedings.mlr.press/v235/feng24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/feng24h/feng24h.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning']
tags: ['privacy-backdoor', 'pretrained-models', 'data-stealing']
venue: "ICML 2024"
tldr: "Demonstrates that tampered pretrained model weights can introduce privacy backdoors enabling attackers to steal private fine-tuning data."
---

# Privacy Backdoors: Stealing Data with Corrupted Pretrained Models

**Source**: [https://proceedings.mlr.press/v235/feng24h.html](https://proceedings.mlr.press/v235/feng24h.html)

**TLDR**: Demonstrates that tampered pretrained model weights can introduce privacy backdoors enabling attackers to steal private fine-tuning data.

## Abstract

Practitioners commonly download pretrained machine learning models from open repositories and finetune them to fit specific applications. We show that this practice introduces a new risk of privacy backdoors. By tampering with a pretrained model’s weights, an attacker can fully compromise the privacy of the finetuning data. We show how to build privacy backdoors for a variety of models, including transformers, which enable an attacker to reconstruct individual finetuning samples, with a guaranteed success! We further show that backdoored models allow for tight privacy attacks on models trained with differential privacy (DP). The common optimistic practice of training DP models with loose privacy guarantees is thus insecure if the model is not trusted. Overall, our work highlights a crucial and overlooked supply chain attack on machine learning privacy.