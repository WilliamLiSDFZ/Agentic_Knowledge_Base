---
title: "In value-based deep reinforcement learning, a pruned network is a good network"
source: "https://proceedings.mlr.press/v235/obando-ceron24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/obando-ceron24a/obando-ceron24a.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['deep-reinforcement-learning', 'magnitude-pruning', 'sparse-networks', 'parameter-efficiency']
venue: "ICML 2024"
tldr: "Gradual magnitude pruning enables value-based RL agents to maximize parameter efficiency and outperform dense networks."
---

# In value-based deep reinforcement learning, a pruned network is a good network

**Source**: [https://proceedings.mlr.press/v235/obando-ceron24a.html](https://proceedings.mlr.press/v235/obando-ceron24a.html)

**TLDR**: Gradual magnitude pruning enables value-based RL agents to maximize parameter efficiency and outperform dense networks.

## Abstract

Recent work has shown that deep reinforcement learning agents have difficulty in effectively using their network parameters. We leverage prior insights into the advantages of sparse training techniques and demonstrate that gradual magnitude pruning enables value-based agents to maximize parameter effectiveness. This results in networks that yield dramatic performance improvements over traditional networks, using only a small fraction of the full network parameters. Our code is publicly available, see Appendix A for details.