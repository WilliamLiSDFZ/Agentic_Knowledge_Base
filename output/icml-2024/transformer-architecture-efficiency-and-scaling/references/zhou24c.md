---
title: "MVMoE: Multi-Task Vehicle Routing Solver with Mixture-of-Experts"
source: "https://proceedings.mlr.press/v235/zhou24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhou24c/zhou24c.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'transformer-architecture-efficiency-and-scaling']
tags: ['vehicle-routing', 'mixture-of-experts', 'multi-task-learning']
venue: "ICML 2024"
tldr: "Develops MVMoE, a unified mixture-of-experts neural solver capable of handling multiple vehicle routing problem variants simultaneously."
---

# MVMoE: Multi-Task Vehicle Routing Solver with Mixture-of-Experts

**Source**: [https://proceedings.mlr.press/v235/zhou24c.html](https://proceedings.mlr.press/v235/zhou24c.html)

**TLDR**: Develops MVMoE, a unified mixture-of-experts neural solver capable of handling multiple vehicle routing problem variants simultaneously.

## Abstract

Learning to solve vehicle routing problems (VRPs) has garnered much attention. However, most neural solvers are only structured and trained independently on a specific problem, making them less generic and practical. In this paper, we aim to develop a unified neural solver that can cope with a range of VRP variants simultaneously. Specifically, we propose a multi-task vehicle routing solver with mixture-of-experts (MVMoE), which greatly enhances the model capacity without a proportional increase in computation. We further develop a hierarchical gating mechanism for the MVMoE, delivering a good trade-off between empirical performance and computational complexity. Experimentally, our method significantly promotes zero-shot generalization performance on 10 unseen VRP variants, and showcases decent results on the few-shot setting and real-world benchmark instances. We further conduct extensive studies on the effect of MoE configurations in solving VRPs, and observe the superiority of hierarchical gating when facing out-of-distribution data. The source code is available at: https://github.com/RoyalSkye/Routing-MVMoE.