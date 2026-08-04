---
title: "Adaptive Proximal Gradient Methods Are Universal Without Approximation"
source: "https://proceedings.mlr.press/v235/oikonomidis24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/oikonomidis24a/oikonomidis24a.pdf"
categories: ['optimization-algorithms-convergence-theory']
tags: ['adaptive-proximal-gradient', 'convex-optimization', 'Hölder-continuity', 'linesearch-free']
venue: "ICML 2024"
tldr: "Shows adaptive proximal gradient methods converge under local Hölder gradient continuity without requiring Lipschitz assumptions."
---

# Adaptive Proximal Gradient Methods Are Universal Without Approximation

**Source**: [https://proceedings.mlr.press/v235/oikonomidis24a.html](https://proceedings.mlr.press/v235/oikonomidis24a.html)

**TLDR**: Shows adaptive proximal gradient methods converge under local Hölder gradient continuity without requiring Lipschitz assumptions.

## Abstract

We show that adaptive proximal gradient methods for convex problems are not restricted to traditional Lipschitzian assumptions. Our analysis reveals that a class of linesearch-free methods is still convergent under mere local Hölder gradient continuity, covering in particular continuously differentiable semi-algebraic functions. To mitigate the lack of local Lipschitz continuity, popular approaches revolve around $\varepsilon$-oracles and/or linesearch procedures. In contrast, we exploit plain Hölder inequalities not entailing any approximation, all while retaining the linesearch-free nature of adaptive schemes. Furthermore, we prove full sequence convergence without prior knowledge of local Hölder constants nor of the order of Hölder continuity. Numerical experiments make comparisons with baseline methods on diverse tasks from machine learning covering both the locally and the globally Hölder setting.