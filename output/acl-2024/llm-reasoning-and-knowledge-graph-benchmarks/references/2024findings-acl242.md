---
title: "A Mechanistic Analysis of a Transformer Trained on a Symbolic Multi-Step Reasoning Task"
source: "https://aclanthology.org/2024.findings-acl.242/"
categories: ['transformer-architecture-analysis-and-design', 'llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['transformer-interpretability', 'mechanistic-analysis', 'symbolic-reasoning']
venue: "ACL 2024"
tldr: "Provides a mechanistic analysis of how transformers internally implement reasoning on a symbolic multi-step reasoning task."
---

# A Mechanistic Analysis of a Transformer Trained on a Symbolic Multi-Step Reasoning Task

**Source**: [https://aclanthology.org/2024.findings-acl.242/](https://aclanthology.org/2024.findings-acl.242/)

**TLDR**: Provides a mechanistic analysis of how transformers internally implement reasoning on a symbolic multi-step reasoning task.

## Abstract

AbstractTransformers demonstrate impressive performance on a range of reasoning benchmarks. To evaluate the degree to which these abilities are a result of actual reasoning, existing work has focused on developing sophisticated benchmarks for behavioral studies. However, these studies do not provide insights into the internal mechanisms driving the observed capabilities. To improve our understanding of the internal mechanisms of transformers, we present a comprehensive mechanistic analysis of a transformer trained on a synthetic reasoning task. We identify a set of interpretable mechanisms the model uses to solve the task, and validate our findings using correlational and causal evidence. Our results suggest that it implements a depth-bounded recurrent mechanisms that operates in parallel and stores intermediate results in selected token positions. We anticipate that the motifs we identified in our synthetic setting can provide valuable insights into the broader operating principles of transformers and thus provide a basis for understanding more complex models.