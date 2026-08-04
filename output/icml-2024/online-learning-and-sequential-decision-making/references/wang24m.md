---
title: "Imitation Learning from Purified Demonstrations"
source: "https://proceedings.mlr.press/v235/wang24m.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24m/wang24m.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'online-learning-and-sequential-decision-making']
tags: ['imitation-learning', 'imperfect-demonstrations', 'data-purification', 'sequential-decision-making', 'offline-RL']
venue: "ICML 2024"
tldr: "A purification-based imitation learning framework improves policy learning from noisy or suboptimal expert demonstrations."
---

# Imitation Learning from Purified Demonstrations

**Source**: [https://proceedings.mlr.press/v235/wang24m.html](https://proceedings.mlr.press/v235/wang24m.html)

**TLDR**: A purification-based imitation learning framework improves policy learning from noisy or suboptimal expert demonstrations.

## Abstract

Imitation learning has emerged as a promising approach for addressing sequential decision-making problems, with the assumption that expert demonstrations are optimal. However, in real-world scenarios, most demonstrations are often imperfect, leading to challenges in the effectiveness of imitation learning. While existing research has focused on optimizing with imperfect demonstrations, the training typically requires a certain proportion of optimal demonstrations to guarantee performance. To tackle these problems, we propose to purify the potential noises in imperfect demonstrations first, and subsequently conduct imitation learning from these purified demonstrations. Motivated by the success of diffusion model, we introduce a two-step purification via diffusion process. In the first step, we apply a forward diffusion process to smooth potential noises in imperfect demonstrations by introducing additional noise. Subsequently, a reverse generative process is utilized to recover the optimal demonstration from the diffused ones. We provide theoretical evidence supporting our approach, demonstrating that the distance between the purified and optimal demonstration can be bounded. Empirical results on MuJoCo and RoboSuite demonstrate the effectiveness of our method from different aspects.