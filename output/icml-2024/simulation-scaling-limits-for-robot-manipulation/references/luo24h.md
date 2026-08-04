---
title: "Potential Based Diffusion Motion Planning"
source: "https://proceedings.mlr.press/v235/luo24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/luo24h/luo24h.pdf"
categories: ['generative-models-and-variational-inference', 'simulation-scaling-limits-for-robot-manipulation']
tags: ['motion-planning', 'diffusion-models', 'potential-fields', 'robotics']
venue: "ICML 2024"
tldr: "Potential-based diffusion motion planning combines composable potential functions with diffusion models for effective high-dimensional robot motion planning."
---

# Potential Based Diffusion Motion Planning

**Source**: [https://proceedings.mlr.press/v235/luo24h.html](https://proceedings.mlr.press/v235/luo24h.html)

**TLDR**: Potential-based diffusion motion planning combines composable potential functions with diffusion models for effective high-dimensional robot motion planning.

## Abstract

Effective motion planning in high dimensional spaces is a long-standing open problem in robotics. One class of traditional motion planning algorithms corresponds to potential-based motion planning. An advantage of potential based motion planning is composability – different motion constraints can easily combined by adding corresponding potentials. However, constructing motion paths from potentials requires solving a global optimization across configuration space potential landscape, which is often prone to local minima. We propose a new approach towards learning potential based motion planning, where we train a neural network to capture and learn an easily optimizable potentials over motion planning trajectories. We illustrate the effectiveness of such approach, significantly outperforming both classical and recent learned motion planning approaches and avoiding issues with local minima. We further illustrate its inherent composability, enabling us to generalize to a multitude of different motion constraints. Project website at https://energy-based-model.github.io/potential-motion-plan.