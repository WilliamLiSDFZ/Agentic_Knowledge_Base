---
title: "Unlock the Cognitive Generalization of Deep Reinforcement Learning via Granular Ball Representation"
source: "https://proceedings.mlr.press/v235/liu24u.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24u/liu24u.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['deep-RL', 'cognitive-generalization', 'granular-ball']
venue: "ICML 2024"
tldr: "Granular ball representation is used to unlock cognitive generalization in deep reinforcement learning across varying scenario complexities."
---

# Unlock the Cognitive Generalization of Deep Reinforcement Learning via Granular Ball Representation

**Source**: [https://proceedings.mlr.press/v235/liu24u.html](https://proceedings.mlr.press/v235/liu24u.html)

**TLDR**: Granular ball representation is used to unlock cognitive generalization in deep reinforcement learning across varying scenario complexities.

## Abstract

The policies learned by humans in simple scenarios can be deployed in complex scenarios with the same task logic through limited feature alignment training, a process referred to as cognitive generalization or systematic generalization. Thus, a plausible conjecture is that unlocking cognitive generalization in DRL could enable effective generalization of policies from simple to complex scenarios through reward-agnostic fine-tuning. This would eliminate the need for designing reward functions in complex scenarios, thus reducing environment-building costs. In this paper, we propose a general framework to enhance the cognitive generalization ability of standard DRL methods. Our framework builds a cognitive latent space in a simple scenario, then segments the latent space to cluster samples with similar environmental influences into same subregion. During the fine-tuning in the complex scenario, the policy uses cognitive latent space to align the new sample with the same subregion sample collected from the simple scenario and approximates the rewards and Q values of the new samples for policy update. Based on this framework, we propose Granular Ball Reinforcement Leaning (GBRL), a practical algorithm via Variational Autoencoder (VAE) and Granular Ball Representation. GBRL achieves effective policy generalization on various difficult scenarios with the same task logic.