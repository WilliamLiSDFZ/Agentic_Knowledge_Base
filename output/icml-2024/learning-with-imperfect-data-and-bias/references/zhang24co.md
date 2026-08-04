---
title: "Transferable Facial Privacy Protection against Blind Face Restoration via Domain-Consistent Adversarial Obfuscation"
source: "https://proceedings.mlr.press/v235/zhang24co.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24co/zhang24co.pdf"
categories: ['adversarial-robustness-and-model-security', 'learning-with-imperfect-data-and-bias']
tags: ['facial-privacy', 'adversarial-examples', 'face-restoration']
venue: "ICML 2024"
tldr: "Proposes domain-consistent adversarial obfuscation to protect facial privacy against blind face restoration attacks."
---

# Transferable Facial Privacy Protection against Blind Face Restoration via Domain-Consistent Adversarial Obfuscation

**Source**: [https://proceedings.mlr.press/v235/zhang24co.html](https://proceedings.mlr.press/v235/zhang24co.html)

**TLDR**: Proposes domain-consistent adversarial obfuscation to protect facial privacy against blind face restoration attacks.

## Abstract

With the rise of social media and the proliferation of facial recognition surveillance, concerns surrounding privacy have escalated significantly. While numerous studies have concentrated on safeguarding users against unauthorized face recognition, a new and often overlooked issue has emerged due to advances in facial restoration techniques: traditional methods of facial obfuscation may no longer provide a secure shield, as they can potentially expose anonymous information to human perception. Our empirical study shows that blind face restoration (BFR) models can restore obfuscated faces with high probability by simply retraining them on obfuscated (e.g., pixelated) faces. To address it, we propose a transferable adversarial obfuscation method for privacy protection against BFR models. Specifically, we observed a common characteristic among BFR models, namely, their capability to approximate an inverse mapping of a transformation from a high-quality image domain to a low-quality image domain. Leveraging this shared model attribute, we have developed a domain-consistent adversarial method for generating obfuscated images. In essence, our method is designed to minimize overfitting to surrogate models during the perturbation generation process, thereby enhancing the generalization of adversarial obfuscated facial images. Extensive experiments on various BFR models demonstrate the effectiveness and transferability of the proposed method.