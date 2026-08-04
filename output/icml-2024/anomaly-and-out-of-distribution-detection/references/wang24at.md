---
title: "EfficientZero V2: Mastering Discrete and Continuous Control with Limited Data"
source: "https://proceedings.mlr.press/v235/wang24at.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24at/wang24at.pdf"
categories: ['online-learning-and-sequential-decision-making', 'anomaly-and-out-of-distribution-detection']
tags: ['reinforcement-learning', 'sample-efficiency', 'model-based-RL', 'continuous-control']
venue: "ICML 2024"
tldr: "EfficientZero V2 achieves consistently superior sample efficiency across both discrete and continuous control domains."
---

# EfficientZero V2: Mastering Discrete and Continuous Control with Limited Data

**Source**: [https://proceedings.mlr.press/v235/wang24at.html](https://proceedings.mlr.press/v235/wang24at.html)

**TLDR**: EfficientZero V2 achieves consistently superior sample efficiency across both discrete and continuous control domains.

## Abstract

Sample efficiency remains a crucial challenge in applying Reinforcement Learning (RL) to real-world tasks. While recent algorithms have made significant strides in improving sample efficiency, none have achieved consistently superior performance across diverse domains. In this paper, we introduce EfficientZero V2, a general framework designed for sample-efficient RL algorithms. We have expanded the performance of EfficientZero to multiple domains, encompassing both continuous and discrete actions, as well as visual and low-dimensional inputs. With a series of improvements we propose, EfficientZero V2 outperforms the current state-of-the-art (SoTA) by a significant margin in diverse tasks under the limited data setting. EfficientZero V2 exhibits a notable advancement over the prevailing general algorithm, DreamerV3, achieving superior outcomes in 50 of 66 evaluated tasks across multiple benchmarks, including Atari 100k, Proprio Control, and Vision Control.