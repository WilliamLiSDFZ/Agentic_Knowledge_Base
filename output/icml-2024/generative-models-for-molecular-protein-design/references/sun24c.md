---
title: "Representing Molecules as Random Walks Over Interpretable Grammars"
source: "https://proceedings.mlr.press/v235/sun24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sun24c/sun24c.pdf"
categories: ['generative-models-for-molecular-protein-design', 'generative-models-and-variational-inference']
tags: ['molecular-generation', 'grammar', 'random-walks', 'material-design', 'interpretable']
venue: "ICML 2024"
tldr: "Molecules are represented as random walks over interpretable grammars to enable generative modeling of complex molecular structures for material design."
---

# Representing Molecules as Random Walks Over Interpretable Grammars

**Source**: [https://proceedings.mlr.press/v235/sun24c.html](https://proceedings.mlr.press/v235/sun24c.html)

**TLDR**: Molecules are represented as random walks over interpretable grammars to enable generative modeling of complex molecular structures for material design.

## Abstract

Recent research in molecular discovery has primarily been devoted to small, drug-like molecules, leaving many similarly important applications in material design without adequate technology. These applications often rely on more complex molecular structures with fewer examples that are carefully designed using known substructures. We propose a data-efficient and interpretable model for representing and reasoning over such molecules in terms of graph grammars that explicitly describe the hierarchical design space featuring motifs to be the design basis. We present a novel representation in the form of random walks over the design space, which facilitates both molecule generation and property prediction. We demonstrate clear advantages over existing methods in terms of performance, efficiency, and synthesizability of predicted molecules, and we provide detailed insights into the method’s chemical interpretability.