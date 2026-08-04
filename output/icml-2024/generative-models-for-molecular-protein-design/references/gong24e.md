---
title: "Evolution-Inspired Loss Functions for Protein Representation Learning"
source: "https://proceedings.mlr.press/v235/gong24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gong24e/gong24e.pdf"
categories: ['generative-models-for-molecular-protein-design', 'learning-with-imperfect-data-and-bias']
tags: ['protein-representation', 'self-supervised-learning', 'evolution-inspired']
venue: "ICML 2024"
tldr: "This paper proposes evolution-inspired loss functions for protein representation learning to improve mutation effect predictions beyond wildtype accuracy objectives."
---

# Evolution-Inspired Loss Functions for Protein Representation Learning

**Source**: [https://proceedings.mlr.press/v235/gong24e.html](https://proceedings.mlr.press/v235/gong24e.html)

**TLDR**: This paper proposes evolution-inspired loss functions for protein representation learning to improve mutation effect predictions beyond wildtype accuracy objectives.

## Abstract

AI-based frameworks for protein engineering use self-supervised learning (SSL) to obtain representations for downstream mutation effect predictions. The most common training objective for these methods is wildtype accuracy: given a sequence or structure where a wildtype residue has been masked, predict the missing amino acid. Wildtype accuracy, however, does not align with the primary goal of protein engineering, which is to suggest a mutation rather than to identify what already appears in nature. Here we present Evolutionary Ranking (EvoRank), a training objective that incorporates evolutionary information derived from multiple sequence alignments (MSAs) to learn more diverse protein representations. EvoRank corresponds to ranking amino-acid likelihoods in the probability distribution induced by an MSA. This objective forces models to learn the underlying evolutionary dynamics of a protein. Across a variety of phenotypes and datasets, we demonstrate that EvoRank leads to dramatic improvements in zero-shot performance and can compete with models fine-tuned on experimental data. This is particularly important in protein engineering, where it is expensive to obtain data for fine-tuning.