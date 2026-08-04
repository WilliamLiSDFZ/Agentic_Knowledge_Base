---
title: "Learning to Scale Logits for Temperature-Conditional GFlowNets"
source: "https://proceedings.mlr.press/v235/kim24s.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24s/kim24s.pdf"
categories: ['generative-models-and-variational-inference', 'online-learning-and-sequential-decision-making']
tags: ['GFlowNets', 'temperature-conditioning', 'logit-scaling']
venue: "ICML 2024"
tldr: "Proposes logit-scaling GFlowNets to enable efficient temperature-conditional exploration and exploitation in generative flow networks."
---

# Learning to Scale Logits for Temperature-Conditional GFlowNets

**Source**: [https://proceedings.mlr.press/v235/kim24s.html](https://proceedings.mlr.press/v235/kim24s.html)

**TLDR**: Proposes logit-scaling GFlowNets to enable efficient temperature-conditional exploration and exploitation in generative flow networks.

## Abstract

GFlowNets are probabilistic models that sequentially generate compositional structures through a stochastic policy. Among GFlowNets, temperature-conditional GFlowNets can introduce temperature-based controllability for exploration and exploitation. We propose Logit-scaling GFlowNets (Logit-GFN), a novel architectural design that greatly accelerates the training of temperature-conditional GFlowNets. It is based on the idea that previously proposed approaches introduced numerical challenges in the deep network training, since different temperatures may give rise to very different gradient profiles as well as magnitudes of the policy’s logits. We find that the challenge is greatly reduced if a learned function of the temperature is used to scale the policy’s logits directly. Also, using Logit-GFN, GFlowNets can be improved by having better generalization capabilities in offline learning and mode discovery capabilities in online learning, which is empirically verified in various biological and chemical tasks. Our code is available at https://github.com/dbsxodud-11/logit-gfn