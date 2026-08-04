---
title: "Breaking through the learning plateaus of in-context learning in Transformer"
source: "https://proceedings.mlr.press/v235/fu24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fu24h/fu24h.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'neural-network-learning-dynamics-theory']
tags: ['in-context-learning', 'training-dynamics', 'learning-plateaus']
venue: "ICML 2024"
tldr: "The causes and solutions for learning plateaus during transformer training for in-context learning are theoretically and empirically investigated."
---

# Breaking through the learning plateaus of in-context learning in Transformer

**Source**: [https://proceedings.mlr.press/v235/fu24h.html](https://proceedings.mlr.press/v235/fu24h.html)

**TLDR**: The causes and solutions for learning plateaus during transformer training for in-context learning are theoretically and empirically investigated.

## Abstract

In-context learning, i.e., learning from context examples, is an impressive ability of Transformer. Training Transformers to possess this in-context learning skill is computationally intensive due to the occurrence of learning plateaus, which are periods within the training process where there is minimal or no enhancement in the model’s in-context learning capability. To study the mechanism behind the learning plateaus, we conceptually separate a component within the model’s internal representation that is exclusively affected by the model’s weights. We call this the “weights component”, and the remainder is identified as the “context component”. By conducting meticulous and controlled experiments on synthetic tasks, we note that the persistence of learning plateaus correlates with compromised functionality of the weights component. Recognizing the impaired performance of the weights component as a fundamental behavior that drives learning plateaus, we have developed three strategies to expedite the learning of Transformers. The effectiveness of these strategies is further confirmed in natural language processing tasks. In conclusion, our research demonstrates the feasibility of cultivating a powerful in-context learning ability within AI systems in an eco-friendly manner.