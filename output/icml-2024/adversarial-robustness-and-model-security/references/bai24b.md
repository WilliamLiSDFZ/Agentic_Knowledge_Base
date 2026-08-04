---
title: "Diffusion Models Demand Contrastive Guidance for Adversarial Purification to Advance"
source: "https://proceedings.mlr.press/v235/bai24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bai24b/bai24b.pdf"
categories: ['adversarial-robustness-and-model-security', 'generative-models-and-variational-inference']
tags: ['adversarial-purification', 'diffusion-models', 'contrastive-guidance']
venue: "ICML 2024"
tldr: "This paper proposes contrastive guidance for diffusion-model-based adversarial purification to improve defense performance."
---

# Diffusion Models Demand Contrastive Guidance for Adversarial Purification to Advance

**Source**: [https://proceedings.mlr.press/v235/bai24b.html](https://proceedings.mlr.press/v235/bai24b.html)

**TLDR**: This paper proposes contrastive guidance for diffusion-model-based adversarial purification to improve defense performance.

## Abstract

In adversarial defense, adversarial purification can be viewed as a special generation task with the purpose to remove adversarial attacks and diffusion models excel in adversarial purification for their strong generative power. With different predetermined generation requirements, various types of guidance have been proposed, but few of them focuses on adversarial purification. In this work, we propose to guide diffusion models for adversarial purification using contrastive guidance. We theoretically derive the proper noise level added in the forward process diffusion models for adversarial purification from a feature learning perspective. For the reverse process, it is implied that the role of contrastive loss guidance is to facilitate the evolution towards the signal direction. From the theoretical findings and implications, we design the forward process with the proper amount of Gaussian noise added and the reverse process with the gradient of contrastive loss as the guidance of diffusion models for adversarial purification. Empirically, extensive experiments on CIFAR-10, CIFAR-100, the German Traffic Sign Recognition Benchmark and ImageNet datasets with ResNet and WideResNet classifiers show that our method outperforms most of current adversarial training and adversarial purification methods by a large improvement.