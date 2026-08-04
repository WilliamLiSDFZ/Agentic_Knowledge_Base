---
title: "Understanding Inter-Concept Relationships in Concept-Based Models"
source: "https://proceedings.mlr.press/v235/raman24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/raman24a/raman24a.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'clustering-methods-and-multi-view-learning']
tags: ['concept-based-explainability', 'inter-concept-relationships', 'interpretability', 'deep-learning', 'human-reasoning']
venue: "ICML 2024"
tldr: "An investigation into whether concept-based explainability models capture inter-concept relationships as humans do."
---

# Understanding Inter-Concept Relationships in Concept-Based Models

**Source**: [https://proceedings.mlr.press/v235/raman24a.html](https://proceedings.mlr.press/v235/raman24a.html)

**TLDR**: An investigation into whether concept-based explainability models capture inter-concept relationships as humans do.

## Abstract

Concept-based explainability methods provide insight into deep learning systems by constructing explanations using human-understandable concepts. While the literature on human reasoning demonstrates that we exploit relationships between concepts when solving tasks, it is unclear whether concept-based methods incorporate the rich structure of inter-concept relationships. We analyse the concept representations learnt by concept-based models to understand whether these models correctly capture inter-concept relationships. First, we empirically demonstrate that state-of-the-art concept-based models produce representations that lack stability and robustness, and such methods fail to capture inter-concept relationships. Then, we develop a novel algorithm which leverages inter-concept relationships to improve concept intervention accuracy, demonstrating how correctly capturing inter-concept relationships can improve downstream tasks.