---
title: "Rate-Optimal Policy Optimization for Linear Markov Decision Processes"
source: "https://proceedings.mlr.press/v235/sherman24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sherman24a/sherman24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['linear-MDPs', 'policy-optimization', 'regret-minimization']
venue: "ICML 2024"
tldr: "A computationally efficient policy optimization algorithm achieves rate-optimal regret for online episodic linear Markov Decision Processes."
---

# Rate-Optimal Policy Optimization for Linear Markov Decision Processes

**Source**: [https://proceedings.mlr.press/v235/sherman24a.html](https://proceedings.mlr.press/v235/sherman24a.html)

**TLDR**: A computationally efficient policy optimization algorithm achieves rate-optimal regret for online episodic linear Markov Decision Processes.

## Abstract

We study regret minimization in online episodic linear Markov Decision Processes, and propose a policy optimization algorithm that is computationally efficient, and obtains rate optimal $\widetilde O (\sqrt K)$ regret where $K$ denotes the number of episodes. Our work is the first to establish the optimal rate (in terms of $K$) of convergence in the stochastic setting with bandit feedback using a policy optimization based approach, and the first to establish the optimal rate in the adversarial setup with full information feedback, for which no algorithm with an optimal rate guarantee was previously known.