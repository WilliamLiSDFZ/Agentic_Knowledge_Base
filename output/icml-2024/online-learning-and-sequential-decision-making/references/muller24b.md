---
title: "Truly No-Regret Learning in Constrained MDPs"
source: "https://proceedings.mlr.press/v235/muller24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/muller24b/muller24b.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-mdp-structure-and-dependencies']
tags: ['constrained-MDPs', 'no-regret-learning', 'primal-dual', 'safety-constraints']
venue: "ICML 2024"
tldr: "A truly no-regret algorithm for constrained MDPs is developed that avoids error cancellations in regret bounds, providing stronger safety guarantees."
---

# Truly No-Regret Learning in Constrained MDPs

**Source**: [https://proceedings.mlr.press/v235/muller24b.html](https://proceedings.mlr.press/v235/muller24b.html)

**TLDR**: A truly no-regret algorithm for constrained MDPs is developed that avoids error cancellations in regret bounds, providing stronger safety guarantees.

## Abstract

Constrained Markov decision processes (CMDPs) are a common way to model safety constraints in reinforcement learning. State-of-the-art methods for efficiently solving CMDPs are based on primal-dual algorithms. For these algorithms, all currently known regret bounds allow for error cancellations — one can compensate for a constraint violation in one round with a strict constraint satisfaction in another. This makes the online learning process unsafe since it only guarantees safety for the final (mixture) policy but not during learning. As Efroni et al. (2020) pointed out, it is an open question whether primal-dual algorithms can provably achieve sublinear regret if we do not allow error cancellations. In this paper, we give the first affirmative answer. We first generalize a result on last-iterate convergence of regularized primal-dual schemes to CMDPs with multiple constraints. Building upon this insight, we propose a model-based primal-dual algorithm to learn in an unknown CMDP. We prove that our algorithm achieves sublinear regret without error cancellations.