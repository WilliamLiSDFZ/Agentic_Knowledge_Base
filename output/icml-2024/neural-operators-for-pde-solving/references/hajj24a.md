---
title: "Incorporating probabilistic domain knowledge into deep multiple instance learning"
source: "https://proceedings.mlr.press/v235/hajj24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hajj24a/hajj24a.pdf"
categories: ['neural-operators-for-pde-solving', 'probabilistic-generating-circuits-research']
tags: ['multiple-instance-learning', 'domain-knowledge', 'probabilistic-circuits', 'deep-learning', 'knowledge-incorporation']
venue: "ICML 2024"
tldr: "A framework for incorporating probabilistic domain knowledge into deep multiple instance learning models."
---

# Incorporating probabilistic domain knowledge into deep multiple instance learning

**Source**: [https://proceedings.mlr.press/v235/hajj24a.html](https://proceedings.mlr.press/v235/hajj24a.html)

**TLDR**: A framework for incorporating probabilistic domain knowledge into deep multiple instance learning models.

## Abstract

Deep learning methods, including deep multiple instance learning methods, have been criticized for their limited ability to incorporate domain knowledge. A reason that knowledge incorporation is challenging in deep learning is that the models usually lack a mapping between their model components and the entities of the domain, making it a non-trivial task to incorporate probabilistic prior information. In this work, we show that such a mapping between domain entities and model components can be defined for a multiple instance learning setting and propose a framework DeeMILIP that encompasses multiple strategies to exploit this mapping for prior knowledge incorporation. We motivate and formalize these strategies from a probabilistic perspective. Experiments on an immune-based diagnostics case show that our proposed strategies allow to learn generalizable models even in settings with weak signals, limited dataset size, and limited compute.