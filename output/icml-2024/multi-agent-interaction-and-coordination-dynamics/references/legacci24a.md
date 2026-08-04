---
title: "A Geometric Decomposition of Finite Games: Convergence vs. Recurrence under Exponential Weights"
source: "https://proceedings.mlr.press/v235/legacci24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/legacci24a/legacci24a.pdf"
categories: ['multi-agent-interaction-and-coordination-dynamics', 'optimization-algorithms-convergence-theory']
tags: ['game-decomposition', 'Helmholtz-theorem', 'exponential-weights', 'convergence', 'recurrence']
venue: "ICML 2024"
tldr: "Decomposes finite games into potential and incompressible components to characterize convergence versus recurrent behavior of exponential weight learning dynamics."
---

# A Geometric Decomposition of Finite Games: Convergence vs. Recurrence under Exponential Weights

**Source**: [https://proceedings.mlr.press/v235/legacci24a.html](https://proceedings.mlr.press/v235/legacci24a.html)

**TLDR**: Decomposes finite games into potential and incompressible components to characterize convergence versus recurrent behavior of exponential weight learning dynamics.

## Abstract

In view of the complexity of the dynamics of learning in games, we seek to decompose a game into simpler components where the dynamics’ long-run behavior is well understood. A natural starting point for this is Helmholtz’s theorem, which decomposes a vector field into a potential and an incompressible component. However, the geometry of game dynamics - and, in particular, the dynamics of exponential / multiplicative weights (EW) schemes - is not compatible with the Euclidean underpinnings of Helmholtz’s theorem. This leads us to consider a specific Riemannian framework based on the so-called Shahshahani metric, and introduce the class of incompressible games, for which we establish the following results: First, in addition to being volume-preserving, the continuous-time EW dynamics in incompressible games admit a constant of motion and are Poincaré recurrent - i.e., almost every trajectory of play comes arbitrarily close to its starting point infinitely often. Second, we establish a deep connection with a well-known decomposition of games into a potential and harmonic component (where the players’ objectives are aligned and anti-aligned respectively): a game is incompressible if and only if it is harmonic, implying in turn that the EW dynamics lead to Poincaré recurrence in harmonic games.