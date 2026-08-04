---
title: "FlowMM: Generating Materials with Riemannian Flow Matching"
source: "https://proceedings.mlr.press/v235/miller24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/miller24a/miller24a.pdf"
categories: ['generative-models-for-molecular-protein-design', 'generative-models-and-variational-inference']
tags: ['crystal-materials', 'riemannian-flow-matching', 'generative-models']
venue: "ICML 2024"
tldr: "Proposes FlowMM, a Riemannian flow matching approach for generating thermodynamically stable crystalline materials."
---

# FlowMM: Generating Materials with Riemannian Flow Matching

**Source**: [https://proceedings.mlr.press/v235/miller24a.html](https://proceedings.mlr.press/v235/miller24a.html)

**TLDR**: Proposes FlowMM, a Riemannian flow matching approach for generating thermodynamically stable crystalline materials.

## Abstract

Crystalline materials are a fundamental component in next-generation technologies, yet modeling their distribution presents unique computational challenges. Of the plausible arrangements of atoms in a periodic lattice only a vanishingly small percentage are thermodynamically stable, which is a key indicator of the materials that can be experimentally realized. Two fundamental tasks in this area are to (a) predict the stable crystal structure of a known composition of elements and (b) propose novel compositions along with their stable structures. We present FlowMM, a pair of generative models that achieve state-of-the-art performance on both tasks while being more efficient and more flexible than competing methods. We extend Riemannian Flow Matching to suit the symmetries inherent to crystals: translation, rotation, permutation, and periodic boundary conditions. Our framework enables the freedom to choose the flow base distributions, drastically simplifying the problem of learning crystal structures compared with diffusion models. In addition to standard benchmarks, we validate FlowMM’s generated structures with quantum chemistry calculations, demonstrating that it is $\sim$3x more efficient, in terms of integration steps, at finding stable materials compared to previous open methods.