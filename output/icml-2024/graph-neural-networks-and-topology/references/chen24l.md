---
title: "Relational Learning in Pre-Trained Models: A Theory from Hypergraph Recovery Perspective"
source: "https://proceedings.mlr.press/v235/chen24l.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24l/chen24l.pdf"
categories: ['causal-ml-for-clinical-decision-making', 'graph-neural-networks-and-topology']
tags: ['foundation-models', 'hypergraph-recovery', 'relational-learning', 'statistical-theory']
venue: "ICML 2024"
tldr: "A theoretical framework explaining how foundation models learn hybrid world relations through the lens of hypergraph recovery."
---

# Relational Learning in Pre-Trained Models: A Theory from Hypergraph Recovery Perspective

**Source**: [https://proceedings.mlr.press/v235/chen24l.html](https://proceedings.mlr.press/v235/chen24l.html)

**TLDR**: A theoretical framework explaining how foundation models learn hybrid world relations through the lens of hypergraph recovery.

## Abstract

Foundation Models (FMs) have demonstrated remarkable insights into the relational dynamics of the world, leading to the crucial question: how do these models acquire an understanding of world hybrid relations? Traditional statistical learning, particularly for prediction problems, may overlook the rich and inherently structured information from the data, especially regarding the relationships between objects. We introduce a mathematical model that formalizes relational learning as hypergraph recovery to study pre-training of FMs. In our framework, the world is represented as a hypergraph, with data abstracted as random samples from hyperedges. We theoretically examine the feasibility of a Pre-Trained Model (PTM) to recover this hypergraph and analyze the data efficiency in a minimax near-optimal style. By integrating rich graph theories into the realm of PTMs, our mathematical framework offers powerful tools for an in-depth understanding of pre-training from a unique perspective and can be used under various scenarios. As an example, we extend the framework to entity alignment in multimodal learning.