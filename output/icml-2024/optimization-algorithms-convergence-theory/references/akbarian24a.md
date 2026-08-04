---
title: "Improving Computational Complexity in Statistical Models with Local Curvature Information"
source: "https://proceedings.mlr.press/v235/akbarian24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/akbarian24a/akbarian24a.pdf"
categories: ['optimization-algorithms-convergence-theory']
tags: ['singular-models', 'fisher-information', 'gradient-descent', 'local-curvature', 'convergence']
venue: "ICML 2024"
tldr: "Exploits local curvature information to improve computational complexity of gradient descent in singular statistical models."
---

# Improving Computational Complexity in Statistical Models with Local Curvature Information

**Source**: [https://proceedings.mlr.press/v235/akbarian24a.html](https://proceedings.mlr.press/v235/akbarian24a.html)

**TLDR**: Exploits local curvature information to improve computational complexity of gradient descent in singular statistical models.

## Abstract

It is known that when the statistical models are singular, i.e., the Fisher information matrix at the true parameter is degenerate, the fixed step-size gradient descent algorithm takes polynomial number of steps in terms of the sample size $n$ to converge to a final statistical radius around the true parameter, which can be unsatisfactory for the practical application. To further improve that computational complexity, we consider utilizing the local curvature information for parameter estimation. Even though there is a rich literature in using the local curvature information for optimization, the statistical rate of these methods in statistical models, to the best of our knowledge, has not been studied rigorously. The major challenge of this problem is due to the non-convex nature of sample loss function. To shed light on these problems, we specifically study the normalized gradient descent (NormGD) algorithm, a variant of gradient descent algorithm whose step size is scaled by the maximum eigenvalue of the Hessian matrix of the empirical loss function, and deal with the aforementioned issue with a population-to-sample analysis. When the population loss function is homogeneous, the NormGD iterates reach a final statistical radius around the true parameter after a logarithmic number of iterations in terms of $n$. Therefore, for fixed dimension $d$, the NormGD algorithm achieves the optimal computational complexity $\mathcal{O}(n)$ to reach the final statistical radius, which is cheaper than the complexity $\mathcal{O}(n^{\tau})$ of the fixed step-size gradient descent algorithm for some $\tau > 1$.