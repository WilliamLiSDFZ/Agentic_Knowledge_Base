---
title: "Scalable AI Safety via Doubly-Efficient Debate"
source: "https://proceedings.mlr.press/v235/brown-cohen24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/brown-cohen24a/brown-cohen24a.pdf"
categories: ['ai-safety-governance-alignment-positions', 'large-language-model-alignment-and-capabilities']
tags: ['ai-safety', 'debate', 'scalable-oversight', 'superhuman-ai']
venue: "ICML 2024"
tldr: "Proposes a doubly-efficient debate framework for scalable AI safety where tasks are too complex for direct human judgment."
---

# Scalable AI Safety via Doubly-Efficient Debate

**Source**: [https://proceedings.mlr.press/v235/brown-cohen24a.html](https://proceedings.mlr.press/v235/brown-cohen24a.html)

**TLDR**: Proposes a doubly-efficient debate framework for scalable AI safety where tasks are too complex for direct human judgment.

## Abstract

The emergence of pre-trained AI systems with powerful capabilities across a diverse and ever-increasing set of complex domains has raised a critical challenge for AI safety as tasks can become too complicated for humans to judge directly. Irving et al (2018). proposed a debate method in this direction with the goal of pitting the power of such AI models against each other until the problem of identifying (mis)-alignment is broken down into a manageable subtask. While the promise of this approach is clear, the original framework was based on the assumption that the honest strategy is able to simulate deterministic AI systems for an exponential number of steps, limiting its applicability. In this paper, we show how to address these challenges by designing a new set of debate protocols where the honest strategy can always succeed using a simulation of a polynomial number of steps, whilst being able to verify the alignment of stochastic AI systems, even when the dishonest strategy is allowed to use exponentially many simulation steps.