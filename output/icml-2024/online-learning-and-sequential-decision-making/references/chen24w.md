---
title: "Offline Transition Modeling via Contrastive Energy Learning"
source: "https://proceedings.mlr.press/v235/chen24w.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24w/chen24w.pdf"
categories: ['generative-models-and-variational-inference', 'online-learning-and-sequential-decision-making']
tags: ['offline-RL', 'transition-model', 'contrastive-energy', 'energy-based-models']
venue: "ICML 2024"
tldr: "Contrastive energy learning is proposed for offline transition modeling to better capture complex real-world dynamics beyond standard forward model biases."
---

# Offline Transition Modeling via Contrastive Energy Learning

**Source**: [https://proceedings.mlr.press/v235/chen24w.html](https://proceedings.mlr.press/v235/chen24w.html)

**TLDR**: Contrastive energy learning is proposed for offline transition modeling to better capture complex real-world dynamics beyond standard forward model biases.

## Abstract

Learning a high-quality transition model is of great importance for sequential decision-making tasks, especially in offline settings. Nevertheless, the complex behaviors of transition dynamics in real-world environments pose challenges for the standard forward models because of their inductive bias towards smooth regressors, conflicting with the inherent nature of transitions such as discontinuity or large curvature. In this work, we propose to model the transition probability implicitly through a scalar-value energy function, which enables not only flexible distribution prediction but also capturing complex transition behaviors. The Energy-based Transition Models (ETM) are shown to accurately fit the discontinuous transition functions and better generalize to out-of-distribution transition data. Furthermore, we demonstrate that energy-based transition models improve the evaluation accuracy and significantly outperform other off-policy evaluation methods in DOPE benchmark. Finally, we show that energy-based transition models also benefit reinforcement learning and outperform prior offline RL algorithms in D4RL Gym-Mujoco tasks.