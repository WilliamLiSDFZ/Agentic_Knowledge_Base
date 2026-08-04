---
title: "Low-Cost High-Power Membership Inference Attacks"
source: "https://proceedings.mlr.press/v235/zarifzadeh24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zarifzadeh24a/zarifzadeh24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'privacy-preserving-federated-and-distributed-learning']
tags: ['membership-inference', 'privacy', 'statistical-testing']
venue: "ICML 2024"
tldr: "A low-cost membership inference attack using fine-grained null hypothesis modeling that achieves high power with minimal computational overhead."
---

# Low-Cost High-Power Membership Inference Attacks

**Source**: [https://proceedings.mlr.press/v235/zarifzadeh24a.html](https://proceedings.mlr.press/v235/zarifzadeh24a.html)

**TLDR**: A low-cost membership inference attack using fine-grained null hypothesis modeling that achieves high power with minimal computational overhead.

## Abstract

Membership inference attacks aim to detect if a particular data point was used in training a model. We design a novel statistical test to perform robust membership inference attacks (RMIA) with low computational overhead. We achieve this by a fine-grained modeling of the null hypothesis in our likelihood ratio tests, and effectively leveraging both reference models and reference population data samples. RMIA has superior test power compared with prior methods, throughout the TPR-FPR curve (even at extremely low FPR, as low as 0). Under computational constraints, where only a limited number of pre-trained reference models (as few as 1) are available, and also when we vary other elements of the attack (e.g., data distribution), our method performs exceptionally well, unlike prior attacks that approach random guessing. RMIA lays the groundwork for practical yet accurate data privacy risk assessment in machine learning.