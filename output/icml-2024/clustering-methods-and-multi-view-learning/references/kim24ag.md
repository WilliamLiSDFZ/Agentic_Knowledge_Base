---
title: "Discovering Features with Synergistic Interactions in Multiple Views"
source: "https://proceedings.mlr.press/v235/kim24ag.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24ag/kim24ag.pdf"
categories: ['clustering-methods-and-multi-view-learning', 'sufficient-dimension-reduction-correlation-methods']
tags: ['multi-view-learning', 'synergistic-interactions', 'feature-discovery']
venue: "ICML 2024"
tldr: "Proposes a method to discover features with synergistic interactions across multiple views of data."
---

# Discovering Features with Synergistic Interactions in Multiple Views

**Source**: [https://proceedings.mlr.press/v235/kim24ag.html](https://proceedings.mlr.press/v235/kim24ag.html)

**TLDR**: Proposes a method to discover features with synergistic interactions across multiple views of data.

## Abstract

Discovering features with synergistic interactions in multi-view data, that provide more information gain when considered together than when considered separately, is particularly valuable. This fosters a more comprehensive understanding of the target outcome from diverse perspectives (views). However, despite the increasing opportunities presented by multi-view data, surprisingly little attention has been paid to uncovering these crucial interactions. To address this gap, we formally define the problem of selecting synergistic and non-synergistic feature subsets in multi-view data, leveraging an information-theoretic concept known as interaction information. To this end, we introduce a novel deep learning-based feature selection method that identifies different interactions across multiple views, employing a Bernoulli relaxation technique to solve this intractable subset searching problem. Experiments on synthetic, semi-synthetic, and real-world multi-view datasets demonstrate that our model discovers relevant feature subsets with synergistic and non-synergistic interactions, achieving remarkable similarity to the ground truth. Furthermore, we corroborate the discovered features with supporting medical and scientific literature, underscoring its utility in elucidating complex dependencies and interactions in multi-view data.