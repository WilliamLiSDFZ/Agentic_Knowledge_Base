---
title: "Convergence of Some Convex Message Passing Algorithms to a Fixed Point"
source: "https://proceedings.mlr.press/v235/voracek24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/voracek24a/voracek24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'multi-agent-mdp-structure-and-dependencies']
tags: ['MAP-inference', 'graphical-models', 'message-passing', 'LP-relaxation', 'convergence']
venue: "ICML 2024"
tldr: "Proves convergence of convex message passing algorithms such as max-sum diffusion and sequential tree-reweighted message passing to fixed points for MAP inference."
---

# Convergence of Some Convex Message Passing Algorithms to a Fixed Point

**Source**: [https://proceedings.mlr.press/v235/voracek24a.html](https://proceedings.mlr.press/v235/voracek24a.html)

**TLDR**: Proves convergence of convex message passing algorithms such as max-sum diffusion and sequential tree-reweighted message passing to fixed points for MAP inference.

## Abstract

A popular approach to the MAP inference problem in graphical models is to minimize an upper bound obtained from a dual linear programming or Lagrangian relaxation by (block-)coordinate descent. This is also known as convex/convergent message passing; examples are max-sum diffusion and sequential tree-reweighted message passing (TRW-S). Convergence properties of these methods are currently not fully understood. They have been proved to converge to the set characterized by local consistency of active constraints, with unknown convergence rate; however, it was not clear if the iterates converge at all (to any point). We prove a stronger result (conjectured before but never proved): the iterates converge to a fixed point of the method. Moreover, we show that the algorithm terminates within $\mathcal{O}(1/\varepsilon)$ iterations. We first prove this for a version of coordinate descent applied to a general piecewise-affine convex objective. Then we show that several convex message passing methods are special cases of this method. Finally, we show that a slightly different version of coordinate descent can cycle.