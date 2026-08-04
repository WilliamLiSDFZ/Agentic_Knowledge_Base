---
title: "Challenges in Training PINNs: A Loss Landscape Perspective"
source: "https://proceedings.mlr.press/v235/rathore24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/rathore24a/rathore24a.pdf"
categories: ['neural-operators-for-pde-solving', 'optimization-algorithms-convergence-theory']
tags: ['PINNs', 'loss-landscape', 'ill-conditioning', 'physics-informed', 'training-challenges']
venue: "ICML 2024"
tldr: "This paper analyzes training difficulties in Physics-Informed Neural Networks through the lens of the loss landscape and ill-conditioning from differential operators."
---

# Challenges in Training PINNs: A Loss Landscape Perspective

**Source**: [https://proceedings.mlr.press/v235/rathore24a.html](https://proceedings.mlr.press/v235/rathore24a.html)

**TLDR**: This paper analyzes training difficulties in Physics-Informed Neural Networks through the lens of the loss landscape and ill-conditioning from differential operators.

## Abstract

This paper explores challenges in training Physics-Informed Neural Networks (PINNs), emphasizing the role of the loss landscape in the training process. We examine difficulties in minimizing the PINN loss function, particularly due to ill-conditioning caused by differential operators in the residual term. We compare gradient-based optimizers Adam, L-BFGS, and their combination Adam+L-BFGS, showing the superiority of Adam+L-BFGS, and introduce a novel second-order optimizer, NysNewton-CG (NNCG), which significantly improves PINN performance. Theoretically, our work elucidates the connection between ill-conditioned differential operators and ill-conditioning in the PINN loss and shows the benefits of combining first- and second-order optimization methods. Our work presents valuable insights and more powerful optimization strategies for training PINNs, which could improve the utility of PINNs for solving difficult partial differential equations.