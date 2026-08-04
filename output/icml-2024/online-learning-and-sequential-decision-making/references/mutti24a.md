---
title: "Test-Time Regret Minimization in Meta Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/mutti24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mutti24a/mutti24a.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['meta-reinforcement-learning', 'regret-minimization', 'markov-decision-processes']
venue: "ICML 2024"
tldr: "A framework for minimizing test-time regret in meta-RL over finite MDP task distributions is proposed and analyzed."
---

# Test-Time Regret Minimization in Meta Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/mutti24a.html](https://proceedings.mlr.press/v235/mutti24a.html)

**TLDR**: A framework for minimizing test-time regret in meta-RL over finite MDP task distributions is proposed and analyzed.

## Abstract

Meta reinforcement learning sets a distribution over a set of tasks on which the agent can train at will, then is asked to learn an optimal policy for any test task efficiently. In this paper, we consider a finite set of tasks modeled through Markov decision processes with various dynamics. We assume to have endured a long training phase, from which the set of tasks is perfectly recovered, and we focus on regret minimization against the optimal policy in the unknown test task. Under a separation condition that states the existence of a state-action pair revealing a task against another, Chen et al. (2022) show that $O(M^2 \log(H))$ regret can be achieved, where $M, H$ are the number of tasks in the set and test episodes, respectively. In our first contribution, we demonstrate that the latter rate is nearly optimal by developing a novel lower bound for test-time regret minimization under separation, showing that a linear dependence with $M$ is unavoidable. Then, we present a family of stronger yet reasonable assumptions beyond separation, which we call strong identifiability, enabling algorithms achieving fast rates $\log (H)$ and sublinear dependence with $M$ simultaneously. Our paper provides a new understanding of the statistical barriers of test-time regret minimization and when fast rates can be achieved.