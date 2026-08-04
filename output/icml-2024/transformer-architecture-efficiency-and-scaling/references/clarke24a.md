---
title: "Studying K-FAC Heuristics by Viewing Adam through a Second-Order Lens"
source: "https://proceedings.mlr.press/v235/clarke24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/clarke24a/clarke24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'transformer-architecture-efficiency-and-scaling']
tags: ['k-fac', 'adam', 'second-order-optimization']
venue: "ICML 2024"
tldr: "Adam is analyzed through a second-order lens to understand and improve K-FAC heuristics for deep learning optimization."
---

# Studying K-FAC Heuristics by Viewing Adam through a Second-Order Lens

**Source**: [https://proceedings.mlr.press/v235/clarke24a.html](https://proceedings.mlr.press/v235/clarke24a.html)

**TLDR**: Adam is analyzed through a second-order lens to understand and improve K-FAC heuristics for deep learning optimization.

## Abstract

Research into optimisation for deep learning is characterised by a tension between the computational efficiency of first-order, gradient-based methods (such as SGD and Adam) and the theoretical efficiency of second-order, curvature-based methods (such as quasi-Newton methods and K-FAC). Noting that second-order methods often only function effectively with the addition of stabilising heuristics (such as Levenberg-Marquardt damping), we ask how much these (as opposed to the second-order curvature model) contribute to second-order algorithms’ performance. We thus study AdamQLR: an optimiser combining damping and learning rate selection techniques from K-FAC (Martens & Grosse, 2015) with the update directions proposed by Adam, inspired by considering Adam through a second-order lens. We evaluate AdamQLR on a range of regression and classification tasks at various scales and hyperparameter tuning methodologies, concluding K-FAC’s adaptive heuristics are of variable standalone general effectiveness, and finding an untuned AdamQLR setting can achieve comparable performance vs runtime to tuned benchmarks.