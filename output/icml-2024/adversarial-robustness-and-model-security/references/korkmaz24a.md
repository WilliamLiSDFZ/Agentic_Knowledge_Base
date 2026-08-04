---
title: "Understanding and Diagnosing Deep Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/korkmaz24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/korkmaz24a/korkmaz24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'ai-explainability-uncertainty-human-decision-making']
tags: ['deep-reinforcement-learning', 'adversarial-robustness', 'decision-boundary', 'value-function', 'diagnostics']
venue: "ICML 2024"
tldr: "A framework for understanding and diagnosing decision boundary stability and robustness in deep reinforcement learning policies."
---

# Understanding and Diagnosing Deep Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/korkmaz24a.html](https://proceedings.mlr.press/v235/korkmaz24a.html)

**TLDR**: A framework for understanding and diagnosing decision boundary stability and robustness in deep reinforcement learning policies.

## Abstract

Deep neural policies have recently been installed in a diverse range of settings, from biotechnology to automated financial systems. However, the utilization of deep neural networks to approximate the value function leads to concerns on the decision boundary stability, in particular, with regard to the sensitivity of policy decision making to indiscernible, non-robust features due to highly non-convex and complex deep neural manifolds. These concerns constitute an obstruction to understanding the reasoning made by deep neural policies, and their foundational limitations. Hence, it is crucial to develop techniques that aim to understand the sensitivities in the learnt representations of neural network policies. To achieve this we introduce a theoretically founded method that provides a systematic analysis of the unstable directions in the deep neural policy decision boundary across both time and space. Through experiments in the Arcade Learning Environment (ALE), we demonstrate the effectiveness of our technique for identifying correlated directions of instability, and for measuring how sample shifts remold the set of sensitive directions in the neural policy landscape. Most importantly, we demonstrate that state-of-the-art robust training techniques yield learning of disjoint unstable directions, with dramatically larger oscillations over time, when compared to standard training. We believe our results reveal the fundamental properties of the decision process made by reinforcement learning policies, and can help in constructing reliable and robust deep neural policies.