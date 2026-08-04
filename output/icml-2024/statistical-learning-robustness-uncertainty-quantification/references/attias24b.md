---
title: "Agnostic Sample Compression Schemes for Regression"
source: "https://proceedings.mlr.press/v235/attias24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/attias24b/attias24b.pdf"
categories: ['sampling-compression-and-dimensionality-reduction', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['sample-compression', 'agnostic-regression', 'fat-shattering-dimension', 'approximation-theory']
venue: "ICML 2024"
tldr: "Constructs the first sample compression schemes for agnostic regression with ℓp loss, with size exponential in fat-shattering dimension."
---

# Agnostic Sample Compression Schemes for Regression

**Source**: [https://proceedings.mlr.press/v235/attias24b.html](https://proceedings.mlr.press/v235/attias24b.html)

**TLDR**: Constructs the first sample compression schemes for agnostic regression with ℓp loss, with size exponential in fat-shattering dimension.

## Abstract

We obtain the first positive results for bounded sample compression in the agnostic regression setting with the $\ell_p$ loss, where $p\in [1,\infty]$. We construct a generic approximate sample compression scheme for real-valued function classes exhibiting exponential size in the fat-shattering dimension but independent of the sample size. Notably, for linear regression, an approximate compression of size linear in the dimension is constructed. Moreover, for $\ell_1$ and $\ell_\infty$ losses, we can even exhibit an efficient exact sample compression scheme of size linear in the dimension. We further show that for every other $\ell_p$ loss, $p\in (1,\infty)$, there does not exist an exact agnostic compression scheme of bounded size. This refines and generalizes a negative result of David, Moran, and Yehudayoff (2016) for the $\ell_2$ loss. We close by posing general open questions: for agnostic regression with $\ell_1$ loss, does every function class admit an exact compression scheme of polynomial size in the pseudo-dimension? For the $\ell_2$ loss, does every function class admit an approximate compression scheme of polynomial size in the fat-shattering dimension? These questions generalize Warmuth’s classic sample compression conjecture for realizable-case classification (Warmuth, 2003).