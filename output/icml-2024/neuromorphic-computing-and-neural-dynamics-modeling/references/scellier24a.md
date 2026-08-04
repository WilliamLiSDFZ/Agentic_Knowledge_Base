---
title: "A fast algorithm to simulate nonlinear resistive networks"
source: "https://proceedings.mlr.press/v235/scellier24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/scellier24a/scellier24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'neuromorphic-computing-and-neural-dynamics-modeling']
tags: ['resistive-networks', 'analog-computing', 'equilibrium-propagation', 'simulation', 'local-learning-rules']
venue: "ICML 2024"
tldr: "A fast algorithm for simulating nonlinear resistive networks enables energy-efficient analog computing platforms that learn via local rules."
---

# A fast algorithm to simulate nonlinear resistive networks

**Source**: [https://proceedings.mlr.press/v235/scellier24a.html](https://proceedings.mlr.press/v235/scellier24a.html)

**TLDR**: A fast algorithm for simulating nonlinear resistive networks enables energy-efficient analog computing platforms that learn via local rules.

## Abstract

Analog electrical networks have long been investigated as energy-efficient computing platforms for machine learning, leveraging analog physics during inference. More recently, resistor networks have sparked particular interest due to their ability to learn using local rules (such as equilibrium propagation), enabling potentially important energy efficiency gains for training as well. Despite their potential advantage, the simulations of these resistor networks has been a significant bottleneck to assess their scalability, with current methods either being limited to linear networks or relying on realistic, yet slow circuit simulators like SPICE. Assuming ideal circuit elements, we introduce a novel approach for the simulation of nonlinear resistive networks, which we frame as a quadratic programming problem with linear inequality constraints, and which we solve using a fast, exact coordinate descent algorithm. Our simulation methodology significantly outperforms existing SPICE-based simulations, enabling the training of networks up to 327 times larger at speeds 160 times faster, resulting in a 50,000-fold improvement in the ratio of network size to epoch duration. Our approach can foster more rapid progress in the simulations of nonlinear analog electrical networks.