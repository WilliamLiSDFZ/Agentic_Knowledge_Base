---
title: "Convergence and Trade-Offs in Riemannian Gradient Descent and Riemannian Proximal Point"
source: "https://proceedings.mlr.press/v235/marti-nez-rubio24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/marti-nez-rubio24a/marti-nez-rubio24a.pdf"
categories: ['optimization-algorithms-convergence-theory']
tags: ['Riemannian-optimization', 'geodesic-convexity', 'convergence-rates']
venue: "ICML 2024"
tldr: "A convergence analysis of Riemannian gradient descent and proximal point methods with explicit rates and trade-offs."
---

# Convergence and Trade-Offs in Riemannian Gradient Descent and Riemannian Proximal Point

**Source**: [https://proceedings.mlr.press/v235/marti-nez-rubio24a.html](https://proceedings.mlr.press/v235/marti-nez-rubio24a.html)

**TLDR**: A convergence analysis of Riemannian gradient descent and proximal point methods with explicit rates and trade-offs.

## Abstract

In this work, we analyze two of the most fundamental algorithms in geodesically convex optimization: Riemannian gradient descent and (possibly inexact) Riemannian proximal point. We quantify their rates of convergence and produce different variants with several trade-offs. Crucially, we show the iterates naturally stay in a ball around an optimizer, of radius depending on the initial distance and, in some cases, on the curvature. Previous works simply assumed bounded iterates, resulting in rates that were not fully quantified. We also provide an implementable inexact proximal point algorithm and prove several new useful properties of Riemannian proximal methods: they work when positive curvature is present, the proximal operator does not move points away from any optimizer, and we quantify the smoothness of its induced Moreau envelope. Further, we explore beyond our theory with empirical tests.