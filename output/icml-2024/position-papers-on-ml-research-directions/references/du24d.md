---
title: "Position: Compositional Generative Modeling: A Single Model is Not All You Need"
source: "https://proceedings.mlr.press/v235/du24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/du24d/du24d.pdf"
categories: ['generative-models-and-variational-inference', 'position-papers-on-ml-research-directions']
tags: ['compositional-generative-models', 'position-paper', 'modular-AI', 'generative-systems']
venue: "ICML 2024"
tldr: "This position paper advocates for building large generative AI systems by composing smaller specialized generative models rather than training single monolithic models."
---

# Position: Compositional Generative Modeling: A Single Model is Not All You Need

**Source**: [https://proceedings.mlr.press/v235/du24d.html](https://proceedings.mlr.press/v235/du24d.html)

**TLDR**: This position paper advocates for building large generative AI systems by composing smaller specialized generative models rather than training single monolithic models.

## Abstract

Large monolithic generative models trained on massive amounts of data have become an increasingly dominant approach in AI research. In this paper, we argue that we should instead construct large generative systems by composing smaller generative models together. We show how such a compositional generative approach enables us to learn distributions in a more data-efficient manner, enabling generalization to parts of the data distribution unseen at training time. We further show how this enables us to program and construct new generative models for tasks completely unseen at training. Finally, we show that in many cases, we can discover separate compositional components from data.