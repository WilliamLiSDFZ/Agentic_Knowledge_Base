---
title: "Language-guided Skill Learning with Temporal Variational Inference"
source: "https://proceedings.mlr.press/v235/fu24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fu24e/fu24e.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'large-language-model-alignment-and-capabilities']
tags: ['skill-discovery', 'temporal-segmentation', 'hierarchical-inference']
venue: "ICML 2024"
tldr: "LLM-proposed trajectory segmentations guide hierarchical variational inference for skill discovery from expert demonstrations."
---

# Language-guided Skill Learning with Temporal Variational Inference

**Source**: [https://proceedings.mlr.press/v235/fu24e.html](https://proceedings.mlr.press/v235/fu24e.html)

**TLDR**: LLM-proposed trajectory segmentations guide hierarchical variational inference for skill discovery from expert demonstrations.

## Abstract

We present an algorithm for skill discovery from expert demonstrations. The algorithm first utilizes Large Language Models (LLMs) to propose an initial segmentation of the trajectories. Following that, a hierarchical variational inference framework incorporates the LLM-generated segmentation information to discover reusable skills by merging trajectory segments. To further control the trade-off between compression and reusability, we introduce a novel auxiliary objective based on the Minimum Description Length principle that helps guide this skill discovery process. Our results demonstrate that agents equipped with our method are able to discover skills that help accelerate learning and outperform baseline skill learning approaches on new long-horizon tasks in BabyAI, a grid world navigation environment, as well as ALFRED, a household simulation environment.