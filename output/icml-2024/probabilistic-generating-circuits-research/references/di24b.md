---
title: "Double Variance Reduction: A Smoothing Trick for Composite Optimization Problems without First-Order Gradient"
source: "https://proceedings.mlr.press/v235/di24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/di24b/di24b.pdf"
categories: ['optimization-algorithms-convergence-theory', 'probabilistic-generating-circuits-research']
tags: ['zeroth-order-optimization', 'variance-reduction', 'composite-optimization', 'smoothing', 'convergence']
venue: "ICML 2024"
tldr: "Introduces a double variance reduction smoothing trick to reduce coordinate-wise variance in zeroth-order methods for composite optimization problems."
---

# Double Variance Reduction: A Smoothing Trick for Composite Optimization Problems without First-Order Gradient

**Source**: [https://proceedings.mlr.press/v235/di24b.html](https://proceedings.mlr.press/v235/di24b.html)

**TLDR**: Introduces a double variance reduction smoothing trick to reduce coordinate-wise variance in zeroth-order methods for composite optimization problems.

## Abstract

Variance reduction techniques are designed to decrease the sampling variance, thereby accelerating convergence rates of first-order (FO) and zeroth-order (ZO) optimization methods. However, in composite optimization problems, ZO methods encounter an additional variance called the coordinate-wise variance, which stems from the random gradient estimation. To reduce this variance, prior works require estimating all partial derivatives, essentially approximating FO information. This approach demands $\mathcal{O}(d)$ function evaluations ($d$ is the dimension size), which incurs substantial computational costs and is prohibitive in high-dimensional scenarios. This paper proposes the Zeroth-order Proximal Double Variance Reduction ($\texttt{ZPDVR}$) method, which utilizes the averaging trick to reduce both sampling and coordinate-wise variances. Compared to prior methods, $\texttt{ZPDVR}$ relies solely on random gradient estimates, calls the stochastic zeroth-order oracle (SZO) in expectation $\mathcal{O}(1)$ times per iteration, and achieves the optimal $\mathcal{O}(d(n + \kappa)\log (\frac{1}{\epsilon}))$ SZO query complexity in the strongly convex and smooth setting, where $\kappa$ represents the condition number and $\epsilon$ is the desired accuracy. Empirical results validate $\texttt{ZPDVR}$’s linear convergence and demonstrate its superior performance over other related methods.