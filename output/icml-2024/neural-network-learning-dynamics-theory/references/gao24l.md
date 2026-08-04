---
title: "Non-convex Stochastic Composite Optimization with Polyak Momentum"
source: "https://proceedings.mlr.press/v235/gao24l.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gao24l/gao24l.pdf"
categories: ['optimization-algorithms-convergence-theory', 'neural-network-learning-dynamics-theory']
tags: ['stochastic-proximal-gradient', 'Polyak-momentum', 'non-convex-optimization', 'composite-optimization']
venue: "ICML 2024"
tldr: "This paper establishes convergence of the stochastic proximal gradient method with Polyak momentum for non-convex composite optimization beyond Lipschitz noise assumptions."
---

# Non-convex Stochastic Composite Optimization with Polyak Momentum

**Source**: [https://proceedings.mlr.press/v235/gao24l.html](https://proceedings.mlr.press/v235/gao24l.html)

**TLDR**: This paper establishes convergence of the stochastic proximal gradient method with Polyak momentum for non-convex composite optimization beyond Lipschitz noise assumptions.

## Abstract

The stochastic proximal gradient method is a powerful generalization of the widely used stochastic gradient descent (SGD) method and has found numerous applications in Machine Learning. However, it is notoriously known that this method fails to converge in non-convex settings where the stochastic noise is significant (i.e. when only small or bounded batch sizes are used). In this paper, we focus on the stochastic proximal gradient method with Polyak momentum. We prove this method attains an optimal convergence rate for non-convex composite optimization problems, regardless of batch size. Additionally, we rigorously analyze the variance reduction effect of the Polyak momentum in the composite optimization setting and we show the method also converges when the proximal step can only be solved inexactly. Finally, we provide numerical experiments to validate our theoretical results.