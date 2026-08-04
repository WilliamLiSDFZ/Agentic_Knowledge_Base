---
title: "Towards AutoAI: Optimizing a Machine Learning System with Black-box and Differentiable Components"
source: "https://proceedings.mlr.press/v235/chen24m.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24m/chen24m.pdf"
categories: ['llm-driven-automated-system-optimization', 'bayesian-optimization-and-surrogate-methods']
tags: ['AutoML', 'black-box-optimization', 'differentiable-components', 'system-optimization']
venue: "ICML 2024"
tldr: "A framework for optimizing complex ML systems with both black-box and differentiable components toward automated AI pipeline design."
---

# Towards AutoAI: Optimizing a Machine Learning System with Black-box and Differentiable Components

**Source**: [https://proceedings.mlr.press/v235/chen24m.html](https://proceedings.mlr.press/v235/chen24m.html)

**TLDR**: A framework for optimizing complex ML systems with both black-box and differentiable components toward automated AI pipeline design.

## Abstract

Machine learning (ML) models in the real world typically do not exist in isolation. They are usually part of a complex system (e.g., healthcare systems, self-driving cars) containing multiple ML and black-box components. The problem of optimizing such systems, which we refer to as automated AI (AutoAI), requires us to jointly train all ML components together and presents a significant challenge because the number of system parameters is extremely high and the system has no analytical form. To circumvent this, we introduce a novel algorithm called A-BAD-BO which uses each ML component’s local loss as an auxiliary indicator for system performance. A-BAD-BO uses Bayesian optimization (BO) to optimize the local loss configuration of a system in a smaller dimensional space and exploits the differentiable structure of ML components to recover optimal system parameters from the optimized configuration. We show A-BAD-BO converges to optimal system parameters by showing that it is asymptotically no regret. We use A-BAD-BO to optimize several synthetic and real-world complex systems, including a prompt engineering pipeline for large language models containing millions of system parameters. Our results demonstrate that A-BAD-BO yields better system optimality than gradient-driven baselines and is more sample-efficient than pure BO algorithms.