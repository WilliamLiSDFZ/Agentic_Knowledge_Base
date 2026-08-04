---
title: "MGit: A Model Versioning and Management System"
source: "https://proceedings.mlr.press/v235/hao24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hao24c/hao24c.pdf"
categories: ['llm-driven-automated-system-optimization', 'knowledge-distillation-methods-and-applications']
tags: ['model-versioning', 'model-management', 'model-derivatives']
venue: "ICML 2024"
tldr: "MGit is a version control and management system for ML model ecosystems where models are related through fine-tuning, quantization, or distillation."
---

# MGit: A Model Versioning and Management System

**Source**: [https://proceedings.mlr.press/v235/hao24c.html](https://proceedings.mlr.press/v235/hao24c.html)

**TLDR**: MGit is a version control and management system for ML model ecosystems where models are related through fine-tuning, quantization, or distillation.

## Abstract

New ML models are often derived from existing ones (e.g., through fine-tuning, quantization or distillation), forming an ecosystem where models are related to each other and can share structure or even parameter values. Managing such a large and evolving ecosystem of model derivatives is challenging. For instance, the overhead of storing all such models is high, and models may inherit bugs from related models, complicating error attribution and debugging. In this paper, we propose a model versioning and management system called MGit that makes it easier to store, test, update, and collaborate on related models. MGit introduces a lineage graph that records the relationships between models, optimizations to efficiently store model parameters, and abstractions over this lineage graph that facilitate model testing, updating and collaboration. We find that MGit works well in practice: MGit is able to reduce model storage footprint by up to 7$\times$. Additionally, in a user study with 20 ML practitioners, users complete a model updating task 3$\times$ faster on average with MGit.