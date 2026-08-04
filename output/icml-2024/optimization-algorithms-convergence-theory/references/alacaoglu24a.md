---
title: "Revisiting Inexact Fixed-Point Iterations for Min-Max Problems: Stochasticity and Structured Nonconvexity"
source: "https://proceedings.mlr.press/v235/alacaoglu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/alacaoglu24a/alacaoglu24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'online-learning-and-sequential-decision-making']
tags: ['min-max-optimization', 'nonconvex-nonconcave', 'stochastic-optimization']
venue: "ICML 2024"
tldr: "This paper analyzes inexact fixed-point iterations for stochastic nonconvex-nonconcave min-max problems under cohypomonotonicity and weak Minty variational inequality conditions."
---

# Revisiting Inexact Fixed-Point Iterations for Min-Max Problems: Stochasticity and Structured Nonconvexity

**Source**: [https://proceedings.mlr.press/v235/alacaoglu24a.html](https://proceedings.mlr.press/v235/alacaoglu24a.html)

**TLDR**: This paper analyzes inexact fixed-point iterations for stochastic nonconvex-nonconcave min-max problems under cohypomonotonicity and weak Minty variational inequality conditions.

## Abstract

We focus on constrained, $L$-smooth, potentially stochastic and nonconvex-nonconcave min-max problems either satisfying $\rho$-cohypomonotonicity or admitting a solution to the $\rho$-weakly Minty Variational Inequality (MVI), where larger values of the parameter $\rho>0$ correspond to a greater degree of nonconvexity. These problem classes include examples in two player reinforcement learning, interaction dominant min-max problems, and certain synthetic test problems on which classical min-max algorithms fail. It has been conjectured that first-order methods can tolerate a value of $\rho$ no larger than $\frac{1}{L}$, but existing results in the literature have stagnated at the tighter requirement $\rho < \frac{1}{2L}$. With a simple argument, we obtain optimal or best-known complexity guarantees with cohypomonotonicity or weak MVI conditions for $\rho < \frac{1}{L}$. First main insight for the improvements in the convergence analyses is to harness the recently proposed conic nonexpansiveness property of operators. Second, we provide a refined analysis for inexact Halpern iteration that relaxes the required inexactness level to improve some state-of-the-art complexity results even for constrained stochastic convex-concave min-max problems. Third, we analyze a stochastic inexact Krasnosel’skii-Mann iteration with a multilevel Monte Carlo estimator when the assumptions only hold with respect to a solution.