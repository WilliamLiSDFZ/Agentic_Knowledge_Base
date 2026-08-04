---
title: "Symmetric Replay Training: Enhancing Sample Efficiency in Deep Reinforcement Learning for Combinatorial Optimization"
source: "https://proceedings.mlr.press/v235/kim24o.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24o/kim24o.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'online-learning-and-sequential-decision-making']
tags: ['deep-reinforcement-learning', 'combinatorial-optimization', 'sample-efficiency']
venue: "ICML 2024"
tldr: "Proposes symmetric replay training to improve sample efficiency in DRL-based combinatorial optimization solvers."
---

# Symmetric Replay Training: Enhancing Sample Efficiency in Deep Reinforcement Learning for Combinatorial Optimization

**Source**: [https://proceedings.mlr.press/v235/kim24o.html](https://proceedings.mlr.press/v235/kim24o.html)

**TLDR**: Proposes symmetric replay training to improve sample efficiency in DRL-based combinatorial optimization solvers.

## Abstract

Deep reinforcement learning (DRL) has significantly advanced the field of combinatorial optimization (CO). However, its practicality is hindered by the necessity for a large number of reward evaluations, especially in scenarios involving computationally intensive function assessments. To enhance the sample efficiency, we propose a simple but effective method, called symmetric replay training (SRT), which can be easily integrated into various DRL methods. Our method leverages high-reward samples to encourage exploration of the under-explored symmetric regions without additional online interactions - free. Through replay training, the policy is trained to maximize the likelihood of the symmetric trajectories of discovered high-rewarded samples. Experimental results demonstrate the consistent improvement of our method in sample efficiency across diverse DRL methods applied to real-world tasks, such as molecular optimization and hardware design.