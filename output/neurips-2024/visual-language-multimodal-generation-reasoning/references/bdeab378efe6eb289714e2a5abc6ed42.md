---
title: "Coarse-to-Fine Concept Bottleneck Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/bdeab378efe6eb289714e2a5abc6ed42-Abstract-Conference.html"
categories: ['visual-language-multimodal-generation-reasoning', 'neural-geometric-shape-representation-learning']
tags: ['concept-bottleneck', 'interpretability', 'coarse-to-fine']
venue: "NeurIPS 2024"
tldr: "A coarse-to-fine concept bottleneck model for ante hoc interpretability in deep learning applied to safety-critical tasks."
---

# Coarse-to-Fine Concept Bottleneck Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/bdeab378efe6eb289714e2a5abc6ed42-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/bdeab378efe6eb289714e2a5abc6ed42-Abstract-Conference.html)

**TLDR**: A coarse-to-fine concept bottleneck model for ante hoc interpretability in deep learning applied to safety-critical tasks.

## Abstract

Deep learning algorithms have recently gained significant attention due to their impressive performance. However, their high complexity and un-interpretable mode of operation hinders their confident deployment in real-world safety-critical tasks. This work targets ante hoc interpretability, and specifically Concept Bottleneck Models (CBMs). Our goal is to design a framework that admits a highly interpretable decision making process with respect to human understandable concepts, on two levels of granularity. To this end, we propose a novel two-level concept discovery formulation leveraging: (i) recent advances in vision-language models, and (ii) an innovative formulation for coarse-to-fine concept selection via data-driven and sparsity inducing Bayesian arguments. Within this framework, concept information does not solely rely on the similarity between the whole image and general unstructured concepts; instead, we introduce the notion of concept hierarchy to uncover and exploit more granular concept information residing in patch-specific regions of the image scene. As we experimentally show, the proposed construction not only outperforms recent CBM approaches, but also yields a principled framework towards interpetability.