---
title: "ATraDiff: Accelerating Online Reinforcement Learning with Imaginary Trajectories"
source: "https://proceedings.mlr.press/v235/yang24aa.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24aa/yang24aa.pdf"
categories: ['online-learning-and-sequential-decision-making', 'generative-models-and-variational-inference']
tags: ['reinforcement-learning', 'sparse-rewards', 'imaginary-trajectories']
venue: "ICML 2024"
tldr: "ATraDiff accelerates online reinforcement learning with sparse rewards by generating imaginary trajectories via diffusion models trained on offline data."
---

# ATraDiff: Accelerating Online Reinforcement Learning with Imaginary Trajectories

**Source**: [https://proceedings.mlr.press/v235/yang24aa.html](https://proceedings.mlr.press/v235/yang24aa.html)

**TLDR**: ATraDiff accelerates online reinforcement learning with sparse rewards by generating imaginary trajectories via diffusion models trained on offline data.

## Abstract

Training autonomous agents with sparse rewards is a long-standing problem in online reinforcement learning (RL), due to low data efficiency. Prior work overcomes this challenge by extracting useful knowledge from offline data, often accomplished through the learning of action distribution from offline data and utilizing the learned distribution to facilitate online RL. However, since the offline data are given and fixed, the extracted knowledge is inherently limited, making it difficult to generalize to new tasks. We propose a novel approach that leverages offline data to learn a generative diffusion model, coined as Adaptive Trajectory Diffuser (ATraDiff). This model generates synthetic trajectories, serving as a form of data augmentation and consequently enhancing the performance of online RL methods. The key strength of our diffuser lies in its adaptability, allowing it to effectively handle varying trajectory lengths and mitigate distribution shifts between online and offline data. Because of its simplicity, ATraDiff seamlessly integrates with a wide spectrum of RL methods. Empirical evaluation shows that ATraDiff consistently achieves state-of-the-art performance across a variety of environments, with particularly pronounced improvements in complicated settings. Our code and demo video are available at https://atradiff.github.io.