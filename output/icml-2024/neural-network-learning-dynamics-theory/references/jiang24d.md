---
title: "On the Origins of Linear Representations in Large Language Models"
source: "https://proceedings.mlr.press/v235/jiang24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jiang24d/jiang24d.pdf"
categories: ['llm-geometry-and-interpretability-research', 'neural-network-learning-dynamics-theory']
tags: ['linear-representations', 'llm-geometry', 'latent-variable-model', 'semantic-concepts']
venue: "ICML 2024"
tldr: "A latent variable model is introduced to formalize and explain the emergence of linear representations of semantic concepts in large language model representation spaces."
---

# On the Origins of Linear Representations in Large Language Models

**Source**: [https://proceedings.mlr.press/v235/jiang24d.html](https://proceedings.mlr.press/v235/jiang24d.html)

**TLDR**: A latent variable model is introduced to formalize and explain the emergence of linear representations of semantic concepts in large language model representation spaces.

## Abstract

An array of recent works have argued that high-level semantic concepts are encoded "linearly" in the representation space of large language models. In this work, we study the origins of such linear representations. To that end, we introduce a latent variable model to abstract and formalize the concept dynamics of the next token prediction. We use this formalism to prove that linearity arises as a consequence of the loss function and the implicit bias of gradient descent. The theory is further substantiated empirically via experiments.