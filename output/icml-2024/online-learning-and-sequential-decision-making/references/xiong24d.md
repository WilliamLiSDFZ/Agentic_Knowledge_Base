---
title: "A General Framework for Sequential Decision-Making under Adaptivity Constraints"
source: "https://proceedings.mlr.press/v235/xiong24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xiong24d/xiong24d.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['adaptivity-constraints', 'batch-learning', 'reinforcement-learning']
venue: "ICML 2024"
tldr: "This paper introduces a general framework for sequential decision-making under rare policy switch and batch learning adaptivity constraints via the Eluder Condition class."
---

# A General Framework for Sequential Decision-Making under Adaptivity Constraints

**Source**: [https://proceedings.mlr.press/v235/xiong24d.html](https://proceedings.mlr.press/v235/xiong24d.html)

**TLDR**: This paper introduces a general framework for sequential decision-making under rare policy switch and batch learning adaptivity constraints via the Eluder Condition class.

## Abstract

We take the first step in studying general sequential decision-making under two adaptivity constraints: rare policy switch and batch learning. First, we provide a general class called the Eluder Condition class, which includes a wide range of reinforcement learning classes. Then, for the rare policy switch constraint, we provide a generic algorithm to achieve a $\widetilde{\mathcal{O}}(\log K) $ switching cost with a $\widetilde{\mathcal{O}}(\sqrt{K})$ regret on the EC class. For the batch learning constraint, we provide an algorithm that provides a $\widetilde{\mathcal{O}}(\sqrt{K}+K/B)$ regret with the number of batches $B.$ This paper is the first work considering rare policy switch and batch learning under general function classes, which covers nearly all the models studied in the previous works such as tabular MDP (Bai et al. 2019, Zhang et al. 2020), linear MDP (Wang et al. 2021, Gao et al. 2021), low eluder dimension MDP (Kong et al., 2021; Velegkas et al., 2022), generalized linear function approximation (Qiao et al. 2023), and also some new classes such as the low $D_\Delta$-type Bellman eluder dimension problem, linear mixture MDP, kernelized nonlinear regulator and undercomplete partially observed Markov decision process (POMDP).