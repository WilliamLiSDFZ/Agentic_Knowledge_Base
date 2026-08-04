---
title: "A Universal Transfer Theorem for Convex Optimization Algorithms Using Inexact First-order Oracles"
source: "https://proceedings.mlr.press/v235/kerger24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kerger24a/kerger24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'fast-sketching-methods-for-large-scale-optimization']
tags: ['convex-optimization', 'inexact-oracles', 'black-box-transfer']
venue: "ICML 2024"
tldr: "Presents a universal black-box transfer theorem converting any exact first-order convex optimization algorithm to work with inexact first-order information."
---

# A Universal Transfer Theorem for Convex Optimization Algorithms Using Inexact First-order Oracles

**Source**: [https://proceedings.mlr.press/v235/kerger24a.html](https://proceedings.mlr.press/v235/kerger24a.html)

**TLDR**: Presents a universal black-box transfer theorem converting any exact first-order convex optimization algorithm to work with inexact first-order information.

## Abstract

Given any algorithm for convex optimization that uses exact first-order information (i.e., function values and subgradients), we show how to use such an algorithm to solve the problem with access to inexact first-order information. This is done in a “black-box” manner without knowledge of the internal workings of the algorithm. This complements previous work that considers the performance of specific algorithms like (accelerated) gradient descent with inexact information. In particular, our results apply to a wider range of algorithms beyond variants of gradient descent, e.g., projection-free methods, cutting-plane methods, or any other first-order methods formulated in the future. Further, they also apply to algorithms that handle structured nonconvexities like mixed-integer decision variables.