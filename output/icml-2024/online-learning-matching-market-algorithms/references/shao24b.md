---
title: "On Multi-Armed Bandit with Impatient Arms"
source: "https://proceedings.mlr.press/v235/shao24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shao24b/shao24b.pdf"
categories: ['online-learning-and-sequential-decision-making', 'online-learning-matching-market-algorithms']
tags: ['multi-armed-bandit', 'impatient-arms', 'online-advertising']
venue: "ICML 2024"
tldr: "This paper studies a multi-armed bandit setting where neglected arms exit the game, motivated by real-world online advertising and crowdsourcing scenarios."
---

# On Multi-Armed Bandit with Impatient Arms

**Source**: [https://proceedings.mlr.press/v235/shao24b.html](https://proceedings.mlr.press/v235/shao24b.html)

**TLDR**: This paper studies a multi-armed bandit setting where neglected arms exit the game, motivated by real-world online advertising and crowdsourcing scenarios.

## Abstract

In this paper, we investigate a Multi-Armed Bandit (MAB) setting where an arm exits the game if the algorithm continuously neglects it. This setup is motivated by real-world scenarios, such as online advertising and crowdsourcing, where arms only gain benefits after being pulled by the algorithm. We identify the intrinsic hardness of this problem and limitations in existing approaches. We propose FC-SE algorithm with expected regret upper bounds as our solution to this problem. As an extension, we even allow new arms to enter after the game starts and design FC-Entry algorithm with performance guarantees for this setup. Finally, we conduct experiments to validate our theoretical results.