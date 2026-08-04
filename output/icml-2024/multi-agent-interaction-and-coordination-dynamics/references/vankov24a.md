---
title: "Generalized Smooth Variational Inequalities: Methods with Adaptive Stepsizes"
source: "https://proceedings.mlr.press/v235/vankov24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/vankov24a/vankov24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['variational-inequalities', 'adaptive-stepsizes', 'non-Lipschitz']
venue: "ICML 2024"
tldr: "Proposes adaptive stepsize methods for generalized smooth variational inequality problems relaxing standard strong-monotonicity and Lipschitz assumptions."
---

# Generalized Smooth Variational Inequalities: Methods with Adaptive Stepsizes

**Source**: [https://proceedings.mlr.press/v235/vankov24a.html](https://proceedings.mlr.press/v235/vankov24a.html)

**TLDR**: Proposes adaptive stepsize methods for generalized smooth variational inequality problems relaxing standard strong-monotonicity and Lipschitz assumptions.

## Abstract

Variational Inequality (VI) problems have attracted great interest in the machine learning (ML) community due to their application in adversarial and multi-agent training. Despite its relevance in ML, the oft-used strong-monotonicity and Lipschitz continuity assumptions on VI problems are restrictive and do not hold in many machine learning problems. To address this, we relax smoothness and monotonicity assumptions and study structured non-monotone generalized smoothness. The key idea of our results is in adaptive stepsizes. We prove the first-known convergence results for solving generalized smooth VIs for the three popular methods, namely, projection, Korpelevich, and Popov methods. Our convergence rate results for generalized smooth VIs match or improve existing results on smooth VIs. We present numerical experiments that support our theoretical guarantees and highlight the efficiency of proposed adaptive stepsizes.