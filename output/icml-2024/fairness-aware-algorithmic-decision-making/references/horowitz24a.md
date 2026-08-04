---
title: "Classification Under Strategic Self-Selection"
source: "https://proceedings.mlr.press/v235/horowitz24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/horowitz24a/horowitz24a.pdf"
categories: ['strategic-information-manipulation-and-classification', 'fairness-aware-algorithmic-decision-making']
tags: ['strategic-classification', 'self-selection', 'game-theory', 'fairness', 'prediction']
venue: "ICML 2024"
tldr: "Studies a novel strategic classification setting where users strategically decide whether to participate rather than modifying their features."
---

# Classification Under Strategic Self-Selection

**Source**: [https://proceedings.mlr.press/v235/horowitz24a.html](https://proceedings.mlr.press/v235/horowitz24a.html)

**TLDR**: Studies a novel strategic classification setting where users strategically decide whether to participate rather than modifying their features.

## Abstract

When users stand to gain from certain predictive outcomes, they are prone to act strategically to obtain predictions that are favorable. Most current works consider strategic behavior that manifests as users modifying their features; instead, we study a novel setting in which users decide whether to even participate (or not), this in response to the learned classifier. Considering learning approaches of increasing strategic awareness, we investigate the effects of user self-selection on learning, and the implications of learning on the composition of the self-selected population. Building on this, we propose a differentiable framework for learning under self-selective behavior, which can be optimized effectively. We conclude with experiments on real data and simulated behavior that complement our analysis and demonstrate the utility of our approach.