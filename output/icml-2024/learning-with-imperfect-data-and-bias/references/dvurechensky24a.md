---
title: "Barrier Algorithms for Constrained Non-Convex Optimization"
source: "https://proceedings.mlr.press/v235/dvurechensky24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dvurechensky24a/dvurechensky24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'learning-with-imperfect-data-and-bias']
tags: ['interior-point-methods', 'non-convex-optimization', 'self-concordant-barriers', 'complexity-theory', 'constrained-optimization']
venue: "ICML 2024"
tldr: "Proves that interior-point methods with self-concordant barriers achieve favorable global complexity guarantees for non-convex constrained optimization problems."
---

# Barrier Algorithms for Constrained Non-Convex Optimization

**Source**: [https://proceedings.mlr.press/v235/dvurechensky24a.html](https://proceedings.mlr.press/v235/dvurechensky24a.html)

**TLDR**: Proves that interior-point methods with self-concordant barriers achieve favorable global complexity guarantees for non-convex constrained optimization problems.

## Abstract

In this paper we theoretically show that interior-point methods based on self-concordant barriers possess favorable global complexity beyond their standard application area of convex optimization. To do that we propose first- and second-order methods for non-convex optimization problems with general convex set constraints and linear constraints. Our methods attain a suitably defined class of approximate first- or second-order KKT points with the worst-case iteration complexity similar to unconstrained problems, namely $O(\varepsilon^{-2})$ (first-order) and $O(\varepsilon^{-3/2})$ (second-order), respectively.