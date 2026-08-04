---
title: "Monotone Individual Fairness"
source: "https://proceedings.mlr.press/v235/bechavod24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bechavod24a/bechavod24a.pdf"
categories: ['fairness-aware-algorithmic-decision-making', 'online-learning-and-sequential-decision-making']
tags: ['individual-fairness', 'online-learning', 'fairness-feedback', 'similar-treatment', 'regret']
venue: "ICML 2024"
tldr: "Extends online learning frameworks for individual fairness by incorporating monotone feedback to ensure similar individuals are treated similarly."
---

# Monotone Individual Fairness

**Source**: [https://proceedings.mlr.press/v235/bechavod24a.html](https://proceedings.mlr.press/v235/bechavod24a.html)

**TLDR**: Extends online learning frameworks for individual fairness by incorporating monotone feedback to ensure similar individuals are treated similarly.

## Abstract

We revisit the problem of online learning with individual fairness, where an online learner strives to maximize predictive accuracy while ensuring that similar individuals are treated similarly. We first extend the frameworks of Gillen et al. (2018); Bechavod et al. (2020), which rely on feedback from human auditors regarding fairness violations, to allow for auditing schemes that can aggregate feedback from any number of auditors, using a rich class we term monotone aggregation functions, for which we also prove a useful characterization. Using our generalized framework, we present an oracle-efficient algorithm guaranteeing a bound of $\mathcal{O}(T^\frac{3}{4})$ simultaneously for regret and number of fairness violations. We then study an online classification setting where label feedback is available for positively-predicted individuals only, and present an algorithm guaranteeing a bound of $\mathcal{O}(T^\frac{5}{6})$ simultaneously for regret and number of fairness violations. In both settings, our algorithms improve on the best known bounds for oracle-efficient algorithms. Furthermore, our algorithms offer significant improvements in computational efficiency, greatly reducing the number of required calls to an (offline) optimization oracle, as opposed to previous algorithms which required $T$ such calls every round.