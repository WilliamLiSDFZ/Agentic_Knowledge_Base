---
title: "Re-Dock: Towards Flexible and Realistic Molecular Docking with Diffusion Bridge"
source: "https://proceedings.mlr.press/v235/huang24ag.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24ag/huang24ag.pdf"
categories: ['generative-models-for-molecular-protein-design', 'generative-models-and-variational-inference']
tags: ['molecular-docking', 'diffusion-bridge', 'protein-ligand', 'flexible-docking', 'drug-design']
venue: "ICML 2024"
tldr: "Introduces Re-Dock, a diffusion bridge model for flexible and realistic molecular docking without requiring holo-protein structures."
---

# Re-Dock: Towards Flexible and Realistic Molecular Docking with Diffusion Bridge

**Source**: [https://proceedings.mlr.press/v235/huang24ag.html](https://proceedings.mlr.press/v235/huang24ag.html)

**TLDR**: Introduces Re-Dock, a diffusion bridge model for flexible and realistic molecular docking without requiring holo-protein structures.

## Abstract

Accurate prediction of protein-ligand binding structures, a task known as molecular docking is crucial for drug design but remains challenging. While deep learning has shown promise, existing methods often depend on holo-protein structures (docked, and not accessible in realistic tasks) or neglect pocket sidechain conformations, leading to limited practical utility and unrealistic conformation predictions. To fill these gaps, we introduce an under-explored task, named flexible docking to predict poses of ligand and pocket sidechains simultaneously and introduce Re-Dock, a novel diffusion bridge generative model extended to geometric manifolds. Specifically, we propose energy-to-geometry mapping inspired by the Newton-Euler equation to co-model the binding energy and conformations for reflecting the energy-constrained docking generative process. Comprehensive experiments on designed benchmark datasets including apo-dock and cross-dock demonstrate our model’s superior effectiveness and efficiency over current methods.