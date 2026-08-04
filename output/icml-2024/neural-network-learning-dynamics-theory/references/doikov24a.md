---
title: "Spectral Preconditioning for Gradient Methods on Graded Non-convex Functions"
source: "https://proceedings.mlr.press/v235/doikov24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/doikov24a/doikov24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'neural-network-learning-dynamics-theory']
tags: ['spectral-preconditioning', 'gradient-methods', 'non-convex-optimization', 'Hessian-spectrum', 'convergence']
venue: "ICML 2024"
tldr: "Introduces spectral preconditioning for gradient methods on graded non-convex functions, enabling fine-grained convergence analysis tied to the Hessian spectrum."
---

# Spectral Preconditioning for Gradient Methods on Graded Non-convex Functions

**Source**: [https://proceedings.mlr.press/v235/doikov24a.html](https://proceedings.mlr.press/v235/doikov24a.html)

**TLDR**: Introduces spectral preconditioning for gradient methods on graded non-convex functions, enabling fine-grained convergence analysis tied to the Hessian spectrum.

## Abstract

The performance of optimization methods is often tied to the spectrum of the objective Hessian. Yet, conventional assumptions, such as smoothness, do often not enable us to make finely-grained convergence statements—particularly not for non-convex problems. Striving for a more intricate characterization of complexity, we introduce a unique concept termed graded non-convexity. This allows to partition the class of non-convex problems into a nested chain of subclasses. Interestingly, many traditional non-convex objectives, including partially convex problems, matrix factorizations, and neural networks, fall within these subclasses. As a second contribution, we propose gradient methods with spectral preconditioning, which employ inexact top eigenvectors of the Hessian to address the ill-conditioning of the problem, contingent on the grade. Our analysis reveals that these new methods provide provably superior convergence rates compared to basic gradient descent on applicable problem classes, particularly when large gaps exist between the top eigenvalues of the Hessian. Our theory is validated by numerical experiments executed on multiple practical machine learning problems.