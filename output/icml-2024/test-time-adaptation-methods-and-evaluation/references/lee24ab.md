---
title: "BECoTTA: Input-dependent Online Blending of Experts for Continual Test-time Adaptation"
source: "https://proceedings.mlr.press/v235/lee24ab.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lee24ab/lee24ab.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'continual-learning-memory-plasticity']
tags: ['continual-test-time-adaptation', 'mixture-of-experts', 'online-blending', 'distribution-shift']
venue: "ICML 2024"
tldr: "Proposes BECoTTA, an input-dependent online blending of experts for continual test-time adaptation under changing conditions."
---

# BECoTTA: Input-dependent Online Blending of Experts for Continual Test-time Adaptation

**Source**: [https://proceedings.mlr.press/v235/lee24ab.html](https://proceedings.mlr.press/v235/lee24ab.html)

**TLDR**: Proposes BECoTTA, an input-dependent online blending of experts for continual test-time adaptation under changing conditions.

## Abstract

Continual Test-Time Adaptation (CTTA) is designed to optimize the model during deployment under changing conditions. CTTA is an important problem as it enables models to remain effective and reliable in dynamic and evolving environments. However, tackling the CTTA problem is nontrivial. The model needs to be computationally and memory-efficient to rapidly update its parameters for ever-changing environments in real-time. Also, the model should generalize well to new unseen domains while maintaining its capability on previously encountered ones, as old domains can be revisited in future adaptation phases. To tackle these challenges, this paper proposes BECoTTA, a parameter/memory-efficient yet powerful framework for CTTA. We introduce Mixture-of-Domain Low-rank Experts (MoDE) that contains two core components: ?i) Domain-Adaptive Routing, which can aid in selectively capturing the domain-adaptive knowledge, and ii) Domain-Expert Synergy Loss to maximize the dependency between each domain and expert. We validate our proposed method over multiple CTTA benchmarks, getting 5.81% performance gain, while only requiring 0.001x trainable parameters. We also provide analyses of our BECoTTA, including expert assignment and target domain relation.