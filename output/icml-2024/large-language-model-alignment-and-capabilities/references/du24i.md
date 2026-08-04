---
title: "Exploration-Driven Policy Optimization in RLHF: Theoretical Insights on Efficient Data Utilization"
source: "https://proceedings.mlr.press/v235/du24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/du24i/du24i.pdf"
categories: ['online-learning-and-sequential-decision-making', 'large-language-model-alignment-and-capabilities']
tags: ['RLHF', 'policy-optimization', 'exploration', 'theoretical-analysis']
venue: "ICML 2024"
tldr: "Theoretical analysis of exploration-driven policy optimization in RLHF, providing insights on efficient data utilization and justifying empirical successes."
---

# Exploration-Driven Policy Optimization in RLHF: Theoretical Insights on Efficient Data Utilization

**Source**: [https://proceedings.mlr.press/v235/du24i.html](https://proceedings.mlr.press/v235/du24i.html)

**TLDR**: Theoretical analysis of exploration-driven policy optimization in RLHF, providing insights on efficient data utilization and justifying empirical successes.

## Abstract

Reinforcement Learning from Human Feedback (RLHF) has achieved impressive empirical successes while relying on a small amount of human feedback. However, there is limited theoretical justification for this phenomenon. Additionally, most recent studies focus on value-based algorithms despite the recent empirical successes of policy-based algorithms. In this work, we consider an RLHF algorithm based on policy optimization (PO-RLHF). The algorithm is based on the popular Policy Cover-Policy Gradient (PC-PG) algorithm, which assumes knowledge of the reward function. In PO-RLHF, knowledge of the reward function is not assumed and the algorithm relies on trajectory-based comparison feedback to infer the reward function. We provide performance bounds for PO-RLHF with low query complexity, which provides insight into why a small amount of human feedback may be sufficient to get good performance with RLHF. A key novelty is our trajectory-level elliptical potential analysis technique used to infer reward function parameters when comparison queries rather than reward observations are used. We provide and analyze algorithms in two settings: linear and neural function approximation, PG-RLHF and NN-PG-RLHF, respectively.