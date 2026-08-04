---
title: "Best Arm Identification for Stochastic Rising Bandits"
source: "https://proceedings.mlr.press/v235/mussi24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mussi24b/mussi24b.pdf"
categories: ['online-learning-and-sequential-decision-making', 'online-learning-matching-market-algorithms']
tags: ['best-arm-identification', 'rising-bandits', 'non-stationary', 'sequential-decision-making']
venue: "ICML 2024"
tldr: "Best arm identification is studied in stochastic rising bandits where expected rewards increase with each selection, capturing learning-entity improvement scenarios."
---

# Best Arm Identification for Stochastic Rising Bandits

**Source**: [https://proceedings.mlr.press/v235/mussi24b.html](https://proceedings.mlr.press/v235/mussi24b.html)

**TLDR**: Best arm identification is studied in stochastic rising bandits where expected rewards increase with each selection, capturing learning-entity improvement scenarios.

## Abstract

Stochastic Rising Bandits (SRBs) model sequential decision-making problems in which the expected reward of the available options increases every time they are selected. This setting captures a wide range of scenarios in which the available options are learning entities whose performance improves (in expectation) over time (e.g., online best model selection). While previous works addressed the regret minimization problem, this paper focuses on the fixed-budget Best Arm Identification (BAI) problem for SRBs. In this scenario, given a fixed budget of rounds, we are asked to provide a recommendation about the best option at the end of the identification process. We propose two algorithms to tackle the above-mentioned setting, namely R-UCBE, which resorts to a UCB-like approach, and R-SR, which employs a successive reject procedure. Then, we prove that, with a sufficiently large budget, they provide guarantees on the probability of properly identifying the optimal option at the end of the learning process and on the simple regret. Furthermore, we derive a lower bound on the error probability, matched by our R-SR (up to constants), and illustrate how the need for a sufficiently large budget is unavoidable in the SRB setting. Finally, we numerically validate the proposed algorithms in both synthetic and realistic environments.