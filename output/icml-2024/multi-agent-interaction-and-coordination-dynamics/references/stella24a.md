---
title: "QORA: Zero-Shot Transfer via Interpretable Object-Relational Model Learning"
source: "https://proceedings.mlr.press/v235/stella24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/stella24a/stella24a.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['object-relational-learning', 'zero-shot-transfer', 'reinforcement-learning', 'generalization', 'interpretable-models']
venue: "ICML 2024"
tldr: "QORA learns interpretable object-relational models for reinforcement learning to enable zero-shot transfer across tasks."
---

# QORA: Zero-Shot Transfer via Interpretable Object-Relational Model Learning

**Source**: [https://proceedings.mlr.press/v235/stella24a.html](https://proceedings.mlr.press/v235/stella24a.html)

**TLDR**: QORA learns interpretable object-relational models for reinforcement learning to enable zero-shot transfer across tasks.

## Abstract

Although neural networks have demonstrated significant success in various reinforcement-learning tasks, even the highest-performing deep models often fail to generalize. As an alternative, object-oriented approaches offer a promising path towards better efficiency and generalization; however, they typically address narrow problem classes and require extensive domain knowledge. To overcome these limitations, we introduce QORA, an algorithm that constructs models expressive enough to solve a variety of domains, including those with stochastic transition functions, directly from a domain-agnostic object-based state representation. We also provide a novel benchmark suite to evaluate learners’ generalization capabilities. In our test domains, QORA achieves 100% predictive accuracy using almost four orders of magnitude fewer observations than a neural-network baseline, demonstrates zero-shot transfer to modified environments, and adapts rapidly when applied to tasks involving previously unseen object interactions. Finally, we give examples of QORA’s learned rules, showing them to be easily interpretable.