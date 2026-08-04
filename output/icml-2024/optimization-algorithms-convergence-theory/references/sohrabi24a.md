---
title: "On PI Controllers for Updating Lagrange Multipliers in Constrained Optimization"
source: "https://proceedings.mlr.press/v235/sohrabi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sohrabi24a/sohrabi24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'neuromorphic-computing-and-neural-dynamics-modeling']
tags: ['Lagrange-multipliers', 'PI-controllers', 'constrained-optimization', 'min-max-optimization']
venue: "ICML 2024"
tldr: "PI controllers are proposed for updating Lagrange multipliers in constrained neural network optimization to stabilize oscillatory gradient descent-ascent dynamics."
---

# On PI Controllers for Updating Lagrange Multipliers in Constrained Optimization

**Source**: [https://proceedings.mlr.press/v235/sohrabi24a.html](https://proceedings.mlr.press/v235/sohrabi24a.html)

**TLDR**: PI controllers are proposed for updating Lagrange multipliers in constrained neural network optimization to stabilize oscillatory gradient descent-ascent dynamics.

## Abstract

Constrained optimization offers a powerful framework to prescribe desired behaviors in neural network models. Typically, constrained problems are solved via their min-max Lagrangian formulations, which exhibit unstable oscillatory dynamics when optimized using gradient descent-ascent. The adoption of constrained optimization techniques in the machine learning community is currently limited by the lack of reliable, general-purpose update schemes for the Lagrange multipliers. This paper proposes the νPI algorithm and contributes an optimization perspective on Lagrange multiplier updates based on PI controllers, extending the work of Stooke, Achiam and Abbeel (2020). We provide theoretical and empirical insights explaining the inability of momentum methods to address the shortcomings of gradient descent-ascent, and contrast this with the empirical success of our proposed νPI controller. Moreover, we prove that νPI generalizes popular momentum methods for single-objective minimization. Our experiments demonstrate that νPI reliably stabilizes the multiplier dynamics and its hyperparameters enjoy robust and predictable behavior.