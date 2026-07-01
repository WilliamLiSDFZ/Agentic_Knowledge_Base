---
title: "Adaptive $Q$-Aid for Conditional Supervised Learning in Offline Reinforcement Learning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/9e72fc628edeb29f7aa64ac81b7ec6ce-Abstract-Conference.html"
categories: ['reinforcement-learning-optimization-and-decision-making', 'stochastic-sequential-learning-temporal-dynamics']
tags: ['offline-reinforcement-learning', 'Q-learning', 'conditional-supervised-learning']
venue: "NeurIPS 2024"
tldr: "QCS combines return-conditioned supervised learning stability with Q-function stitching capability for improved offline reinforcement learning."
---

# Adaptive $Q$-Aid for Conditional Supervised Learning in Offline Reinforcement Learning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/9e72fc628edeb29f7aa64ac81b7ec6ce-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/9e72fc628edeb29f7aa64ac81b7ec6ce-Abstract-Conference.html)

**TLDR**: QCS combines return-conditioned supervised learning stability with Q-function stitching capability for improved offline reinforcement learning.

## Abstract

Offline reinforcement learning (RL) has progressed with return-conditioned supervised learning (RCSL), but its lack of stitching ability remains a limitation. We introduce $Q$-Aided Conditional Supervised Learning (QCS), which effectively combines the stability of RCSL with the stitching capability of $Q$-functions. By analyzing $Q$-function over-generalization, which impairs stable stitching, QCS adaptively integrates $Q$-aid into RCSL's loss function based on trajectory return. Empirical results show that QCS significantly outperforms RCSL and value-based methods, consistently achieving or exceeding the highest trajectory returns across diverse offline RL benchmarks. QCS represents a breakthrough in offline RL, pushing the limits of what can be achieved and fostering further innovations.