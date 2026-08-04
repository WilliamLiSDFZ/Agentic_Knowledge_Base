---
title: "Prodigy: An Expeditiously Adaptive Parameter-Free Learner"
source: "https://proceedings.mlr.press/v235/mishchenko24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mishchenko24a/mishchenko24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'online-learning-and-sequential-decision-making']
tags: ['adaptive-optimization', 'parameter-free', 'learning-rate-estimation']
venue: "ICML 2024"
tldr: "Introduces Prodigy, a parameter-free adaptive optimizer that provably estimates the distance to solution for optimal learning rate setting."
---

# Prodigy: An Expeditiously Adaptive Parameter-Free Learner

**Source**: [https://proceedings.mlr.press/v235/mishchenko24a.html](https://proceedings.mlr.press/v235/mishchenko24a.html)

**TLDR**: Introduces Prodigy, a parameter-free adaptive optimizer that provably estimates the distance to solution for optimal learning rate setting.

## Abstract

We consider the problem of estimating the learning rate in adaptive methods, such as AdaGrad and Adam. We propose Prodigy, an algorithm that provably estimates the distance to the solution $D$, which is needed to set the learning rate optimally. At its core, Prodigy is a modification of the D-Adaptation method for learning-rate-free learning. It improves upon the convergence rate of D-Adaptation by a factor of $\mathcal{O}(\sqrt{\log(D/d_0)})$, where $d_0$ is the initial estimate of $D$. We test Prodigy on 12 common logistic-regression benchmark datasets, VGG11 and ResNet-50 training on CIFAR10, ViT training on Imagenet, LSTM training on IWSLT14, DLRM training on Criteo dataset, VarNet on Knee MRI dataset, as well as RoBERTa and GPT transformer training on BookWiki. Our experimental results show that our approach consistently outperforms D-Adaptation and reaches test accuracy values close to that of hand-tuned Adam.