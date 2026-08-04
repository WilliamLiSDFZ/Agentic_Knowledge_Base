---
title: "Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints"
source: "https://proceedings.mlr.press/v235/smee24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/smee24a/smee24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'sampling-compression-and-dimensionality-reduction']
tags: ['inexact-Newton', 'nonnegativity-constraints', 'nonconvex-optimization', 'nonnegative-matrix-factorization']
venue: "ICML 2024"
tldr: "Inexact Newton-type methods are developed for large-scale nonconvex optimization with nonnegativity constraints arising in machine learning."
---

# Inexact Newton-type Methods for Optimisation with Nonnegativity Constraints

**Source**: [https://proceedings.mlr.press/v235/smee24a.html](https://proceedings.mlr.press/v235/smee24a.html)

**TLDR**: Inexact Newton-type methods are developed for large-scale nonconvex optimization with nonnegativity constraints arising in machine learning.

## Abstract

We consider solving large scale nonconvex optimisation problems with nonnegativity constraints. Such problems arise frequently in machine learning, such as nonnegative least-squares, nonnegative matrix factorisation, as well as problems with sparsity-inducing regularisation. In such settings, first-order methods, despite their simplicity, can be prohibitively slow on ill-conditioned problems or become trapped near saddle regions, while most second-order alternatives involve non-trivially challenging subproblems. The two-metric projection framework, initially proposed by Bertsekas (1982), alleviates these issues and achieves the best of both worlds by combining projected gradient steps at the boundary of the feasible region with Newton steps in the interior in such a way that feasibility can be maintained by simple projection onto the nonnegative orthant. We develop extensions of the two-metric projection framework, which by inexactly solving the subproblems as well as employing non-positive curvature directions, are suitable for large scale and nonconvex settings. We obtain state-of-the-art convergence rates for various classes of non-convex problems and demonstrate competitive practical performance on a variety of problems.