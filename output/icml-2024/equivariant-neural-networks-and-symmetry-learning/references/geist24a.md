---
title: "Learning with 3D rotations, a hitchhiker’s guide to SO(3)"
source: "https://proceedings.mlr.press/v235/geist24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/geist24a/geist24a.pdf"
categories: ['equivariant-neural-networks-and-symmetry-learning', 'position-papers-on-ml-research-directions']
tags: ['rotation-representations', 'SO(3)', 'machine-learning-guide']
venue: "ICML 2024"
tldr: "Provides a comprehensive survey and guide to selecting rotation representations for machine learning applications involving SO(3)."
---

# Learning with 3D rotations, a hitchhiker’s guide to SO(3)

**Source**: [https://proceedings.mlr.press/v235/geist24a.html](https://proceedings.mlr.press/v235/geist24a.html)

**TLDR**: Provides a comprehensive survey and guide to selecting rotation representations for machine learning applications involving SO(3).

## Abstract

Many settings in machine learning require the selection of a rotation representation. However, choosing a suitable representation from the many available options is challenging. This paper acts as a survey and guide through rotation representations. We walk through their properties that harm or benefit deep learning with gradient-based optimization. By consolidating insights from rotation-based learning, we provide a comprehensive overview of learning functions with rotation representations. We provide guidance on selecting representations based on whether rotations are in the model’s input or output and whether the data primarily comprises small angles.