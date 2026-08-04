---
title: "Lyapunov-stable Neural Control for State and Output Feedback: A Novel Formulation"
source: "https://proceedings.mlr.press/v235/yang24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24f/yang24f.pdf"
categories: ['neural-network-learning-dynamics-theory', 'set-membership-uncertainty-learning-control']
tags: ['lyapunov-stability', 'neural-control', 'region-of-attraction']
venue: "ICML 2024"
tldr: "A novel formulation for learning neural network control policies with formal Lyapunov stability guarantees for both state and output feedback in nonlinear dynamical systems."
---

# Lyapunov-stable Neural Control for State and Output Feedback: A Novel Formulation

**Source**: [https://proceedings.mlr.press/v235/yang24f.html](https://proceedings.mlr.press/v235/yang24f.html)

**TLDR**: A novel formulation for learning neural network control policies with formal Lyapunov stability guarantees for both state and output feedback in nonlinear dynamical systems.

## Abstract

Learning-based neural-network (NN) control policies have shown impressive empirical performance in a wide range of tasks in robotics and control. However, formal (Lyapunov) stability guarantees over the region-of-attraction (ROA) for NN controllers with nonlinear dynamical systems are challenging to obtain, and most existing approaches rely on expensive solvers for sums-of-squares (SOS), mixed-integer programming (MIP), or satisfiability modulo theories (SMT). In this paper, we demonstrate a new framework for learning NN controllers together with Lyapunov certificates using fast empirical falsification and strategic regularizations. We propose a novel formulation that defines a larger verifiable region-of-attraction (ROA) than shown in the literature, and refines the conventional restrictive constraints on Lyapunov derivatives to focus only on certifiable ROAs. The Lyapunov condition is rigorously verified post-hoc using branch-and-bound with scalable linear bound propagation-based NN verification techniques. The approach is efficient and flexible, and the full training and verification procedure is accelerated on GPUs without relying on expensive solvers for SOS, MIP, nor SMT. The flexibility and efficiency of our framework allow us to demonstrate Lyapunov-stable output feedback control with synthesized NN-based controllers and NN-based observers with formal stability guarantees, for the first time in literature.