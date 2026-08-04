---
title: "Weakly Convex Regularisers for Inverse Problems: Convergence of Critical Points and Primal-Dual Optimisation"
source: "https://proceedings.mlr.press/v235/shumaylov24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shumaylov24a/shumaylov24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'generative-models-and-variational-inference']
tags: ['variational-regularisation', 'inverse-problems', 'weakly-convex']
venue: "ICML 2024"
tldr: "Establishes convergence of critical points and primal-dual optimization for weakly convex deep-learned regularizers in inverse problems."
---

# Weakly Convex Regularisers for Inverse Problems: Convergence of Critical Points and Primal-Dual Optimisation

**Source**: [https://proceedings.mlr.press/v235/shumaylov24a.html](https://proceedings.mlr.press/v235/shumaylov24a.html)

**TLDR**: Establishes convergence of critical points and primal-dual optimization for weakly convex deep-learned regularizers in inverse problems.

## Abstract

Variational regularisation is the primary method for solving inverse problems, and recently there has been considerable work leveraging deeply learned regularisation for enhanced performance. However, few results exist addressing the convergence of such regularisation, particularly within the context of critical points as opposed to global minimisers. In this paper, we present a generalised formulation of convergent regularisation in terms of critical points, and show that this is achieved by a class of weakly convex regularisers. We prove convergence of the primal-dual hybrid gradient method for the associated variational problem, and, given a Kurdyka-Łojasiewicz condition, an $\mathcal{O}(\log{k}/k)$ ergodic convergence rate. Finally, applying this theory to learned regularisation, we prove universal approximation for input weakly convex neural networks (IWCNN), and show empirically that IWCNNs can lead to improved performance of learned adversarial regularisers for computed tomography (CT) reconstruction.