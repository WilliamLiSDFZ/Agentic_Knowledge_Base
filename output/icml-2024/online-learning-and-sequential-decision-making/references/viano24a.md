---
title: "Imitation Learning in Discounted Linear MDPs without exploration assumptions"
source: "https://proceedings.mlr.press/v235/viano24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/viano24a/viano24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'graph-neural-networks-and-topology']
tags: ['imitation-learning', 'linear-MDPs', 'exploration-free', 'trajectory-efficiency', 'infinite-horizon']
venue: "ICML 2024"
tldr: "Presents ILARL, a new imitation learning algorithm for infinite horizon linear MDPs that removes exploration assumptions and improves sample complexity bounds."
---

# Imitation Learning in Discounted Linear MDPs without exploration assumptions

**Source**: [https://proceedings.mlr.press/v235/viano24a.html](https://proceedings.mlr.press/v235/viano24a.html)

**TLDR**: Presents ILARL, a new imitation learning algorithm for infinite horizon linear MDPs that removes exploration assumptions and improves sample complexity bounds.

## Abstract

We present a new algorithm for imitation learning in infinite horizon linear MDPs dubbed ILARL which greatly improves the bound on the number of trajectories that the learner needs to sample from the environment. In particular, we remove exploration assumptions required in previous works and we improve the dependence on the desired accuracy $\epsilon$ from $\mathcal{O}(\epsilon^{-5})$ to $\mathcal{O} (\epsilon^{-4})$. Our result relies on a connection between imitation learning and online learning in MDPs with adversarial losses. For the latter setting, we present the first result for infinite horizon linear MDP which may be of independent interest. Moreover, we are able to provide a strengthen result for the finite horizon case where we achieve $\mathcal{O}(\epsilon^{-2})$. Numerical experiments with linear function approximation shows that ILARL outperforms other commonly used algorithms.