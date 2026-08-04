---
title: "GenCO: Generating Diverse Designs with Combinatorial Constraints"
source: "https://proceedings.mlr.press/v235/ferber24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ferber24a/ferber24a.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning']
tags: ['generative-models', 'combinatorial-constraints', 'design-generation']
venue: "ICML 2024"
tldr: "Develops a deep generative framework for producing diverse designs that satisfy hard combinatorial constraints in industrial settings."
---

# GenCO: Generating Diverse Designs with Combinatorial Constraints

**Source**: [https://proceedings.mlr.press/v235/ferber24a.html](https://proceedings.mlr.press/v235/ferber24a.html)

**TLDR**: Develops a deep generative framework for producing diverse designs that satisfy hard combinatorial constraints in industrial settings.

## Abstract

Deep generative models like GAN and VAE have shown impressive results in generating unconstrained objects like images. However, many design settings arising in industrial design, material science, computer graphics and more require that the generated objects satisfy hard combinatorial constraints or meet objectives in addition to modeling a data distribution. To address this, we propose GenCO, a generative framework that guarantees constraint satisfaction throughout training by leveraging differentiable combinatorial solvers to enforce feasibility. GenCO imposes the generative loss on provably feasible solutions rather than intermediate soft solutions, meaning that the deep generative network can focus on ensuring the generated objects match the data distribution without having to also capture feasibility. This shift enables practitioners to enforce hard constraints on the generated outputs during end-to-end training, enabling assessments of their feasibility and introducing additional combinatorial loss components to deep generative training. We demonstrate the effectiveness of our approach on a variety of generative combinatorial tasks, including game level generation, map creation for path planning, and photonic device design, consistently demonstrating its capability to yield diverse, high-quality solutions that verifiably adhere to user-specified combinatorial properties.