---
title: "Federated Neuro-Symbolic Learning"
source: "https://proceedings.mlr.press/v235/xing24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xing24a/xing24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'neural-symbolic-combinatorial-optimization-learning']
tags: ['federated-learning', 'neuro-symbolic', 'rule-learning']
venue: "ICML 2024"
tldr: "Federated neuro-symbolic learning enables distributed training of neural symbolic models while keeping client data private."
---

# Federated Neuro-Symbolic Learning

**Source**: [https://proceedings.mlr.press/v235/xing24a.html](https://proceedings.mlr.press/v235/xing24a.html)

**TLDR**: Federated neuro-symbolic learning enables distributed training of neural symbolic models while keeping client data private.

## Abstract

Neuro-symbolic learning (NSL) models complex symbolic rule patterns into latent variable distributions by neural networks, which reduces rule search space and generates unseen rules to improve downstream task performance. Centralized NSL learning involves directly acquiring data from downstream tasks, which is not feasible for federated learning (FL). To address this limitation, we shift the focus from such a one-to-one interactive neuro-symbolic paradigm to one-to-many Federated Neuro-Symbolic Learning framework (FedNSL) with latent variables as the FL communication medium. Built on the basis of our novel reformulation of the NSL theory, FedNSL is capable of identifying and addressing rule distribution heterogeneity through a simple and effective Kullback-Leibler (KL) divergence constraint on rule distribution applicable under the FL setting. It further theoretically adjusts variational expectation maximization (V-EM) to reduce the rule search space across domains. This is the first incorporation of distribution-coupled bilevel optimization into FL. Extensive experiments based on both synthetic and real-world data demonstrate significant advantages of FedNSL compared to five state-of-the-art methods. It outperforms the best baseline by 17% and 29% in terms of unbalanced average training accuracy and unseen average testing accuracy, respectively.