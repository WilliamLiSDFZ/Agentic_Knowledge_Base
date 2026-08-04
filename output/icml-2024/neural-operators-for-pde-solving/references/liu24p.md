---
title: "Harnessing the Power of Neural Operators with Automatically Encoded Conservation Laws"
source: "https://proceedings.mlr.press/v235/liu24p.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24p/liu24p.pdf"
categories: ['neural-operators-for-pde-solving']
tags: ['neural-operators', 'conservation-laws', 'physics-informed']
venue: "ICML 2024"
tldr: "A method is proposed to automatically encode conservation laws into neural operators for more physically consistent PDE solving."
---

# Harnessing the Power of Neural Operators with Automatically Encoded Conservation Laws

**Source**: [https://proceedings.mlr.press/v235/liu24p.html](https://proceedings.mlr.press/v235/liu24p.html)

**TLDR**: A method is proposed to automatically encode conservation laws into neural operators for more physically consistent PDE solving.

## Abstract

Neural operators (NOs) have emerged as effective tools for modeling complex physical systems in scientific machine learning. In NOs, a central characteristic is to learn the governing physical laws directly from data. In contrast to other machine learning applications, partial knowledge is often known a priori about the physical system at hand whereby quantities such as mass, energy and momentum are exactly conserved. Currently, NOs have to learn these conservation laws from data and can only approximately satisfy them due to finite training data and random noise. In this work, we introduce conservation law-encoded neural operators (clawNOs), a suite of NOs that endow inference with automatic satisfaction of such conservation laws. ClawNOs are built with a divergence-free prediction of the solution field, with which the continuity equation is automatically guaranteed. As a consequence, clawNOs are compliant with the most fundamental and ubiquitous conservation laws essential for correct physical consistency. As demonstrations, we consider a wide variety of scientific applications ranging from constitutive modeling of material deformation, incompressible fluid dynamics, to atmospheric simulation. ClawNOs significantly outperform the state-of-the-art NOs in learning efficacy, especially in small-data regimes.