---
title: "GFlowNet Training by Policy Gradients"
source: "https://proceedings.mlr.press/v235/niu24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/niu24c/niu24c.pdf"
categories: ['generative-models-and-variational-inference', 'online-learning-and-sequential-decision-making']
tags: ['GFlowNets', 'policy-gradients', 'combinatorial-generation']
venue: "ICML 2024"
tldr: "Proposes a policy-gradient-based training framework for GFlowNets that bridges flow balance with expected reward optimization."
---

# GFlowNet Training by Policy Gradients

**Source**: [https://proceedings.mlr.press/v235/niu24c.html](https://proceedings.mlr.press/v235/niu24c.html)

**TLDR**: Proposes a policy-gradient-based training framework for GFlowNets that bridges flow balance with expected reward optimization.

## Abstract

Generative Flow Networks (GFlowNets) have been shown effective to generate combinatorial objects with desired properties. We here propose a new GFlowNet training framework, with policy-dependent rewards, that bridges keeping flow balance of GFlowNets to optimizing the expected accumulated reward in traditional Reinforcement-Learning (RL). This enables the derivation of new policy-based GFlowNet training methods, in contrast to existing ones resembling value-based RL. It is known that the design of backward policies in GFlowNet training affects efficiency. We further develop a coupled training strategy that jointly solves GFlowNet forward policy training and backward policy design. Performance analysis is provided with a theoretical guarantee of our policy-based GFlowNet training. Experiments on both simulated and real-world datasets verify that our policy-based strategies provide advanced RL perspectives for robust gradient estimation to improve GFlowNet performance. Our code is available at: github.com/niupuhua1234/GFN-PG.