---
title: "Online Linear Regression in Dynamic Environments via Discounting"
source: "https://proceedings.mlr.press/v235/jacobsen24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jacobsen24a/jacobsen24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['online-linear-regression', 'dynamic-regret', 'discounting', 'Vovk-Azoury-Warmuth', 'non-stationary']
venue: "ICML 2024"
tldr: "A discounted variant of the Vovk-Azoury-Warmuth forecaster achieves optimal static and dynamic regret for online linear regression without prior knowledge."
---

# Online Linear Regression in Dynamic Environments via Discounting

**Source**: [https://proceedings.mlr.press/v235/jacobsen24a.html](https://proceedings.mlr.press/v235/jacobsen24a.html)

**TLDR**: A discounted variant of the Vovk-Azoury-Warmuth forecaster achieves optimal static and dynamic regret for online linear regression without prior knowledge.

## Abstract

We develop algorithms for online linear regression which achieve optimal static and dynamic regret guarantees even in the complete absence of prior knowledge. We present a novel analysis showing that a discounted variant of the Vovk-Azoury-Warmuth forecaster achieves dynamic regret of the form $R_{T}(\vec{u})\le O\Big(d\log(T)\vee \sqrt{dP_{T}^{\gamma}(\vec{u})T}\Big)$, where $P_{T}^{\gamma}(\vec{u})$ is a measure of variability of the comparator sequence, and show that the discount factor achieving this result can be learned on-the-fly. We show that this result is optimal by providing a matching lower bound. We also extend our results to strongly-adaptive guarantees which hold over every sub-interval $[a,b]\subseteq[1,T]$ simultaneously.