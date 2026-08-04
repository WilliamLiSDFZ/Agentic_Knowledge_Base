---
title: "Efficient Contextual Bandits with Uninformed Feedback Graphs"
source: "https://proceedings.mlr.press/v235/zhang24ce.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24ce/zhang24ce.pdf"
categories: ['online-learning-and-sequential-decision-making', 'sampling-compression-and-dimensionality-reduction']
tags: ['contextual-bandits', 'feedback-graphs', 'online-learning']
venue: "ICML 2024"
tldr: "Develops an efficient algorithm for contextual bandits with uninformed feedback graphs achieving optimal regret bounds."
---

# Efficient Contextual Bandits with Uninformed Feedback Graphs

**Source**: [https://proceedings.mlr.press/v235/zhang24ce.html](https://proceedings.mlr.press/v235/zhang24ce.html)

**TLDR**: Develops an efficient algorithm for contextual bandits with uninformed feedback graphs achieving optimal regret bounds.

## Abstract

Bandits with feedback graphs are powerful online learning models that interpolate between the full information and classic bandit problems, capturing many real-life applications. A recent work by [Zhang et al., 2023] studies the contextual version of this problem and proposes an efficient and optimal algorithm via a reduction to online regression. However, their algorithm crucially relies on seeing the feedback graph before making each decision, while in many applications, the feedback graph is uninformed, meaning that it is either only revealed after the learner makes her decision or even never fully revealed at all. This work develops the first contextual algorithms for such uninformed settings, via an efficient reduction to online regression over both the losses and the graphs. Importantly, we show that it is critical to learn the graphs using log loss instead of squared loss to obtain favorable regret guarantees. We also demonstrate the empirical effectiveness of our algorithm on a bidding application using both synthetic and real-world data.