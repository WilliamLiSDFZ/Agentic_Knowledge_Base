---
title: "Projection-Free Online Convex Optimization with Time-Varying Constraints"
source: "https://proceedings.mlr.press/v235/garber24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/garber24a/garber24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['online-convex-optimization', 'time-varying-constraints', 'projection-free']
venue: "ICML 2024"
tldr: "Proposes projection-free online convex optimization algorithms that handle adversarial time-varying constraints with bounded regret and constraint violation."
---

# Projection-Free Online Convex Optimization with Time-Varying Constraints

**Source**: [https://proceedings.mlr.press/v235/garber24a.html](https://proceedings.mlr.press/v235/garber24a.html)

**TLDR**: Proposes projection-free online convex optimization algorithms that handle adversarial time-varying constraints with bounded regret and constraint violation.

## Abstract

We consider the setting of online convex optimization with adversarial time-varying constraints in which actions must be feasible w.r.t. a fixed constraint set, and are also required on average to approximately satisfy additional time-varying constraints. Motivated by scenarios in which the fixed feasible set (hard constraint) is difficult to project on, we consider projection-free algorithms that access this set only through a linear optimization oracle (LOO). We present an algorithm that, on a sequence of length $T$ and using overall $T$ calls to the LOO, guarantees $\tilde{O}(T^{3/4})$ regret w.r.t. the losses and $O(T^{7/8})$ constraints violation (ignoring all quantities except for $T$). In particular, these bounds hold w.r.t. any interval of the sequence. This algorithm however also requires access to an oracle for minimizing a strongly convex nonsmooth function over a Euclidean ball. We present a more efficient algorithm that does not require the latter optimization oracle but only first-order access to the time-varying constraints, and achieves similar bounds w.r.t. the entire sequence. We extend the latter to the setting of bandit feedback and obtain similar bounds (as a function of $T$) in expectation.