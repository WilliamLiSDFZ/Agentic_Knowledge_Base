---
title: "Feel-Good Thompson Sampling for Contextual Dueling Bandits"
source: "https://proceedings.mlr.press/v235/li24co.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24co/li24co.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['contextual-bandits', 'dueling-bandits', 'Thompson-sampling']
venue: "ICML 2024"
tldr: "Feel-Good Thompson Sampling is proposed for contextual dueling bandits with theoretical guarantees for preference learning."
---

# Feel-Good Thompson Sampling for Contextual Dueling Bandits

**Source**: [https://proceedings.mlr.press/v235/li24co.html](https://proceedings.mlr.press/v235/li24co.html)

**TLDR**: Feel-Good Thompson Sampling is proposed for contextual dueling bandits with theoretical guarantees for preference learning.

## Abstract

Contextual dueling bandits, where a learner compares two options based on context and receives feedback indicating which was preferred, extends classic dueling bandits by incorporating contextual information for decision-making and preference learning. Several algorithms based on the upper confidence bound (UCB) have been proposed for linear contextual dueling bandits. However, no algorithm based on posterior sampling has been developed in this setting, despite the empirical success observed in traditional contextual bandits. In this paper, we propose a Thompson sampling algorithm, named FGTS.CDB, for linear contextual dueling bandits. At the core of our algorithm is a new Feel-Good exploration term specifically tailored for dueling bandits. This term leverages the independence of the two selected arms, thereby avoiding a cross term in the analysis. We show that our algorithm achieves nearly minimax-optimal regret, i.e., $\tilde{\mathcal{O}}(d\sqrt T)$, where $d$ is the model dimension and $T$ is the time horizon. Finally, we evaluate our algorithm on synthetic data and observe that FGTS.CDB outperforms existing algorithms by a large margin.