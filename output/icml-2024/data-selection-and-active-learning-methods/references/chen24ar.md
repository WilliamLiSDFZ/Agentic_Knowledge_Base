---
title: "A General Framework for Learning from Weak Supervision"
source: "https://proceedings.mlr.press/v235/chen24ar.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24ar/chen24ar.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'data-selection-and-active-learning-methods']
tags: ['weak-supervision', 'general-framework', 'label-noise', 'scalable-learning']
venue: "ICML 2024"
tldr: "Presents a unified and scalable framework for learning from diverse forms of weak supervision across various scenarios."
---

# A General Framework for Learning from Weak Supervision

**Source**: [https://proceedings.mlr.press/v235/chen24ar.html](https://proceedings.mlr.press/v235/chen24ar.html)

**TLDR**: Presents a unified and scalable framework for learning from diverse forms of weak supervision across various scenarios.

## Abstract

Weakly supervised learning generally faces challenges in applicability to various scenarios with diverse weak supervision and in scalability due to the complexity of existing algorithms, thereby hindering the practical deployment. This paper introduces a general framework for learning from weak supervision (GLWS) with a novel algorithm. Central to GLWS is an Expectation-Maximization (EM) formulation, adeptly accommodating various weak supervision sources, including instance partial labels, aggregate statistics, pairwise observations, and unlabeled data. We further present an advanced algorithm that significantly simplifies the EM computational demands using a Non-deterministic Finite Automaton (NFA) along with a forward-backward algorithm, which effectively reduces time complexity from quadratic or factorial often required in existing solutions to linear scale. The problem of learning from arbitrary weak supervision is therefore converted to the NFA modeling of them. GLWS not only enhances the scalability of machine learning models but also demonstrates superior performance and versatility across 11 weak supervision scenarios. We hope our work paves the way for further advancements and practical deployment in this field.