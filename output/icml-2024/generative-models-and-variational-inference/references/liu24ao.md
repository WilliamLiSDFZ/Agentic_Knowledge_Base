---
title: "Energy-Guided Diffusion Sampling for Offline-to-Online Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/liu24ao.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24ao/liu24ao.pdf"
categories: ['generative-models-and-variational-inference', 'online-learning-and-sequential-decision-making']
tags: ['diffusion-models', 'offline-to-online-rl', 'energy-guidance']
venue: "ICML 2024"
tldr: "An energy-guided diffusion sampling method that bridges offline and online reinforcement learning by mitigating distribution shift during data replay."
---

# Energy-Guided Diffusion Sampling for Offline-to-Online Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/liu24ao.html](https://proceedings.mlr.press/v235/liu24ao.html)

**TLDR**: An energy-guided diffusion sampling method that bridges offline and online reinforcement learning by mitigating distribution shift during data replay.

## Abstract

Combining offline and online reinforcement learning (RL) techniques is indeed crucial for achieving efficient and safe learning where data acquisition is expensive. Existing methods replay offline data directly in the online phase, resulting in a significant challenge of data distribution shift and subsequently causing inefficiency in online fine-tuning. To address this issue, we introduce an innovative approach, Energy-guided DIffusion Sampling (EDIS), which utilizes a diffusion model to extract prior knowledge from the offline dataset and employs energy functions to distill this knowledge for enhanced data generation in the online phase. The theoretical analysis demonstrates that EDIS exhibits reduced suboptimality compared to solely utilizing online data or directly reusing offline data. EDIS is a plug-in approach and can be combined with existing methods in offline-to-online RL setting. By implementing EDIS to off-the-shelf methods Cal-QL and IQL, we observe a notable 20% average improvement in empirical performance on MuJoCo, AntMaze, and Adroit environments. Code is available at https://github.com/liuxhym/EDIS.