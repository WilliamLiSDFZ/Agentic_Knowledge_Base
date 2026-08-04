---
title: "Towards Efficient Training and Evaluation of Robust Models against $l_0$ Bounded Adversarial Perturbations"
source: "https://proceedings.mlr.press/v235/zhong24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhong24c/zhong24c.pdf"
categories: ['adversarial-robustness-and-model-security', 'data-selection-and-active-learning-methods']
tags: ['sparse-adversarial-perturbations', 'l0-norm', 'adversarial-training']
venue: "ICML 2024"
tldr: "Proposes sparse-PGD, a white-box attack for l0-bounded perturbations, combined with black-box attacks for robust evaluation and adversarial training against sparse perturbations."
---

# Towards Efficient Training and Evaluation of Robust Models against $l_0$ Bounded Adversarial Perturbations

**Source**: [https://proceedings.mlr.press/v235/zhong24c.html](https://proceedings.mlr.press/v235/zhong24c.html)

**TLDR**: Proposes sparse-PGD, a white-box attack for l0-bounded perturbations, combined with black-box attacks for robust evaluation and adversarial training against sparse perturbations.

## Abstract

This work studies sparse adversarial perturbations bounded by $l_0$ norm. We propose a white-box PGD-like attack method named sparse-PGD to effectively and efficiently generate such perturbations. Furthermore, we combine sparse-PGD with a black-box attack to comprehensively and more reliably evaluate the models’ robustness against $l_0$ bounded adversarial perturbations. Moreover, the efficiency of sparse-PGD enables us to conduct adversarial training to build robust models against sparse perturbations. Extensive experiments demonstrate that our proposed attack algorithm exhibits strong performance in different scenarios. More importantly, compared with other robust models, our adversarially trained model demonstrates state-of-the-art robustness against various sparse attacks. Codes are available at https://github.com/CityU-MLO/sPGD.