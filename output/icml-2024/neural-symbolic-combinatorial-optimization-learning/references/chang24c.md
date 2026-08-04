---
title: "LaMAGIC: Language-Model-based Topology Generation for Analog Integrated Circuits"
source: "https://proceedings.mlr.press/v235/chang24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chang24c/chang24c.pdf"
categories: ['llm-driven-automated-system-optimization', 'neural-symbolic-combinatorial-optimization-learning']
tags: ['analog-circuit-design', 'topology-generation', 'language-models', 'automation']
venue: "ICML 2024"
tldr: "A language model-based method for automating analog integrated circuit topology generation, replacing search-based simulation-heavy approaches."
---

# LaMAGIC: Language-Model-based Topology Generation for Analog Integrated Circuits

**Source**: [https://proceedings.mlr.press/v235/chang24c.html](https://proceedings.mlr.press/v235/chang24c.html)

**TLDR**: A language model-based method for automating analog integrated circuit topology generation, replacing search-based simulation-heavy approaches.

## Abstract

In the realm of electronic and electrical engineering, automation of analog circuit is increasingly vital given the complexity and customized requirements of modern applications. However, existing methods only develop search-based algorithms that require many simulation iterations to design a custom circuit topology, which is usually a time-consuming process. To this end, we introduce LaMAGIC, a pioneering language model-based topology generation model that leverages supervised finetuning for automated analog circuit design. LaMAGIC can efficiently generate an optimized circuit design from the custom specification in a single pass. Our approach involves a meticulous development and analysis of various input and output formulations for circuit. These formulations can ensure canonical representations of circuits and align with the autoregressive nature of LMs to effectively addressing the challenges of representing analog circuits as graphs. The experimental results show that LaMAGIC achieves a success rate of up to 96% under a strict tolerance of 0.01. We also examine the scalability and adaptability of LaMAGIC, specifically testing its performance on more complex circuits. Our findings reveal the enhanced effectiveness of our adjacency matrix-based circuit formulation with floating-point input, suggesting its suitability for handling intricate circuit designs. This research not only demonstrates the potential of language models in graph generation, but also builds a foundational framework for future explorations in automated analog circuit design.