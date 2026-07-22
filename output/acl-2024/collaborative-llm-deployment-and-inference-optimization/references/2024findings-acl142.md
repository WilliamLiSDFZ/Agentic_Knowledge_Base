---
title: "NeuroPrune: A Neuro-inspired Topological Sparse Training Algorithm for Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.142/"
pdf_url: ""
categories: ['transformer-architecture-analysis-and-design', 'collaborative-llm-deployment-and-inference-optimization']
tags: ['sparse-training', 'pruning', 'neuro-inspired']
venue: "ACL 2024"
tldr: "NeuroPrune applies neuro-inspired topological sparse training to reduce computation in large language model inference."
---

# NeuroPrune: A Neuro-inspired Topological Sparse Training Algorithm for Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.142/](https://aclanthology.org/2024.findings-acl.142/)

**TLDR**: NeuroPrune applies neuro-inspired topological sparse training to reduce computation in large language model inference.

## Abstract

AbstractTransformer-based Language Models have become ubiquitous in Natural Language Processing (NLP) due to their impressive performance on various tasks. However, expensive training as well as inference remains a significant impediment to their widespread applicability. While enforcing sparsity at various levels of the model architecture has found promise in addressing scaling and efficiency issues, there remains a disconnect between how sparsity affects network topology. Inspired by brain neuronal networks, we explore sparsity approaches through the lens of network topology. Specifically, we exploit mechanisms seen in biological networks, such as preferential attachment and redundant synapse pruning, and show that principled, model-agnostic sparsity approaches are performant and efficient across diverse NLP tasks, spanning both classification (such as natural language inference) and generation (summarization, machine translation), despite our sole objective not being optimizing performance. NeuroPrune is competitive with (or sometimes superior to) baselines on performance and can be up to 10x faster in terms of training time for a given level of sparsity, simultaneously exhibiting measurable improvements in inference time in many cases.