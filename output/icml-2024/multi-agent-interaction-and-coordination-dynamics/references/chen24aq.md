---
title: "Subequivariant Reinforcement Learning in 3D Multi-Entity Physical Environments"
source: "https://proceedings.mlr.press/v235/chen24aq.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24aq/chen24aq.pdf"
categories: ['equivariant-neural-networks-and-symmetry-learning', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['multi-agent-reinforcement-learning', '3D-environments', 'equivariance', 'subequivariance']
venue: "ICML 2024"
tldr: "Proposes subequivariant reinforcement learning to exploit geometric symmetries in 3D multi-entity environments, reducing state space complexity."
---

# Subequivariant Reinforcement Learning in 3D Multi-Entity Physical Environments

**Source**: [https://proceedings.mlr.press/v235/chen24aq.html](https://proceedings.mlr.press/v235/chen24aq.html)

**TLDR**: Proposes subequivariant reinforcement learning to exploit geometric symmetries in 3D multi-entity environments, reducing state space complexity.

## Abstract

Learning policies for multi-entity systems in 3D environments is far more complicated against single-entity scenarios, due to the exponential expansion of the global state space as the number of entities increases. One potential solution of alleviating the exponential complexity is dividing the global space into independent local views that are invariant to transformations including translations and rotations. To this end, this paper proposes Subequivariant Hierarchical Neural Networks (SHNN) to facilitate multi-entity policy learning. In particular, SHNN first dynamically decouples the global space into local entity-level graphs via task assignment. Second, it leverages subequivariant message passing over the local entity-level graphs to devise local reference frames, remarkably compressing the representation redundancy, particularly in gravity-affected environments. Furthermore, to overcome the limitations of existing benchmarks in capturing the subtleties of multi-entity systems under the Euclidean symmetry, we propose the Multi-entity Benchmark (MEBEN), a new suite of environments tailored for exploring a wide range of multi-entity reinforcement learning. Extensive experiments demonstrate significant advancements of SHNN on the proposed benchmarks compared to existing methods. Comprehensive ablations are conducted to verify the indispensability of task assignment and subequivariance.