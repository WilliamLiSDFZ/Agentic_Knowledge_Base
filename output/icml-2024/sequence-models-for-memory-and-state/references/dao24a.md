---
title: "Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality"
source: "https://proceedings.mlr.press/v235/dao24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dao24a/dao24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'sequence-models-for-memory-and-state']
tags: ['transformers', 'state-space-models', 'Mamba', 'structured-state-space-duality', 'sequence-modeling']
venue: "ICML 2024"
tldr: "Establishes a theoretical duality between Transformers and structured state-space models (SSMs) like Mamba, unifying them under a generalized framework with efficient algorithms."
---

# Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality

**Source**: [https://proceedings.mlr.press/v235/dao24a.html](https://proceedings.mlr.press/v235/dao24a.html)

**TLDR**: Establishes a theoretical duality between Transformers and structured state-space models (SSMs) like Mamba, unifying them under a generalized framework with efficient algorithms.

## Abstract

While Transformers have been the main architecture behind deep learning’s success in language modeling, state-space models (SSMs) such as Mamba have recently been shown to match or outperform Transformers at small to medium scale. We show that these families of models are actually quite closely related, and develop a rich framework of theoretical connections between SSMs and variants of attention, connected through various decompositions of a well-studied class of structured semiseparable matrices. Our state space duality (SSD) framework allows us to design a new architecture (Mamba-2) whose core layer is an a refinement of Mamba’s selective SSM that is 2-8$\times$ faster, while continuing to be competitive with Transformers on language modeling.