---
title: "How to Make the Gradients Small Privately: Improved Rates for Differentially Private Non-Convex Optimization"
source: "https://proceedings.mlr.press/v235/lowy24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lowy24b/lowy24b.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'optimization-algorithms-convergence-theory']
tags: ['differential-privacy', 'non-convex-optimization', 'stationary-points', 'private-algorithms']
venue: "ICML 2024"
tldr: "Presents an improved framework for differentially private non-convex optimization achieving better rates for finding approximate stationary points."
---

# How to Make the Gradients Small Privately: Improved Rates for Differentially Private Non-Convex Optimization

**Source**: [https://proceedings.mlr.press/v235/lowy24b.html](https://proceedings.mlr.press/v235/lowy24b.html)

**TLDR**: Presents an improved framework for differentially private non-convex optimization achieving better rates for finding approximate stationary points.

## Abstract

We provide a simple and flexible framework for designing differentially private algorithms to find approximate stationary points of non-convex loss functions. Our framework is based on using a private approximate risk minimizer to "warm start" another private algorithm for finding stationary points. We use this framework to obtain improved, and sometimes optimal, rates for several classes of non-convex loss functions. First, we obtain improved rates for finding stationary points of smooth non-convex empirical loss functions. Second, we specialize to quasar-convex functions, which generalize star-convex functions and arise in learning dynamical systems and training some neural nets. We achieve the optimal rate for this class. Third, we give an optimal algorithm for finding stationary points of functions satisfying the Kurdyka-Lojasiewicz (KL) condition. For example, over-parameterized neural networks often satisfy this condition. Fourth, we provide new state-of-the-art rates for stationary points of non-convex population loss functions. Fifth, we obtain improved rates for non-convex generalized linear models. A modification of our algorithm achieves nearly the same rates for second-order stationary points of functions with Lipschitz Hessian, improving over the previous state-of-the-art for each of the above problems.