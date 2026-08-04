---
title: "Neural operators meet conjugate gradients: The FCG-NO method for efficient PDE solving"
source: "https://proceedings.mlr.press/v235/rudikov24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/rudikov24a/rudikov24a.pdf"
categories: ['neural-operators-for-pde-solving', 'optimization-algorithms-convergence-theory']
tags: ['neural-operators', 'preconditioning', 'conjugate-gradients', 'PDE-solving', 'discretization-invariant']
venue: "ICML 2024"
tldr: "Neural operators are used as preconditioners for the flexible conjugate gradient method to improve accuracy and efficiency in solving PDEs."
---

# Neural operators meet conjugate gradients: The FCG-NO method for efficient PDE solving

**Source**: [https://proceedings.mlr.press/v235/rudikov24a.html](https://proceedings.mlr.press/v235/rudikov24a.html)

**TLDR**: Neural operators are used as preconditioners for the flexible conjugate gradient method to improve accuracy and efficiency in solving PDEs.

## Abstract

Deep learning solvers for partial differential equations typically have limited accuracy. We propose to overcome this problem by using them as preconditioners. More specifically, we apply discretization-invariant neural operators to learn preconditioners for the flexible conjugate gradient method (FCG). Architecture paired with novel loss function and training scheme allows for learning efficient preconditioners that can be used across different resolutions. On the theoretical side, FCG theory allows us to safely use nonlinear preconditioners that can be applied in $O(N)$ operations without constraining the form of the preconditioners matrix. To justify learning scheme components (the loss function and the way training data is collected) we perform several ablation studies. Numerical results indicate that our approach favorably compares with classical preconditioners and allows to reuse of preconditioners learned for lower resolution to the higher resolution data.