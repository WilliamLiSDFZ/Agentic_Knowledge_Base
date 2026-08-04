---
title: "Probabilistic Modeling of Interpersonal Coordination Processes"
source: "https://proceedings.mlr.press/v235/soares24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/soares24a/soares24a.pdf"
categories: ['bayesian-filtering-and-dynamical-systems-learning', 'time-series-modeling-and-forecasting-methods']
tags: ['probabilistic-modeling', 'interpersonal-coordination', 'temporal-influence', 'latent-variables']
venue: "ICML 2024"
tldr: "A probabilistic latent-variable model is developed to capture interpersonal coordination as temporal statistical influence between observed behavioral signals."
---

# Probabilistic Modeling of Interpersonal Coordination Processes

**Source**: [https://proceedings.mlr.press/v235/soares24a.html](https://proceedings.mlr.press/v235/soares24a.html)

**TLDR**: A probabilistic latent-variable model is developed to capture interpersonal coordination as temporal statistical influence between observed behavioral signals.

## Abstract

We develop a novel probabilistic model for interpersonal coordination as a latent phenomenon explaining statistical temporal influence between multiple components in a system. For example, the state of one person can influence that of another at a later time, as indicated by their observed behaviors. We characterize coordination as the degree to which the distributions for such states at one time point are merged for the next salient time point. We evaluate our model in the context of three-person teams executing a virtual search and rescue (SAR) mission. We first use synthetic data to confirm that our technical definition of coordination is consistent with expectations and that we can recover generated coordination despite noise. We then show that captured coordination can be predictive of team performance on real data. Here we use speech vocalics and semantics to infer coordination for 36 teams carrying out two successive SAR missions. In two different datasets, we find that coordination is generally predictive of team score for the second mission, but not for the first, where teams are largely learning to play the game. In addition, we found that including a semantic modality improves prediction in some scenarios. This shows that our intuitive technical definition can capture useful explanatory aspects of team behavior.