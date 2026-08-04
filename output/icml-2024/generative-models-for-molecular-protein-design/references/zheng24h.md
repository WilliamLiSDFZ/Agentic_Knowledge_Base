---
title: "ESM All-Atom: Multi-Scale Protein Language Model for Unified Molecular Modeling"
source: "https://proceedings.mlr.press/v235/zheng24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zheng24h/zheng24h.pdf"
categories: ['generative-models-for-molecular-protein-design']
tags: ['protein-language-model', 'multi-scale-modeling', 'atom-level', 'molecular-modeling']
venue: "ICML 2024"
tldr: "ESM All-Atom extends protein language models to operate at both residue and atom scales for unified molecular modeling."
---

# ESM All-Atom: Multi-Scale Protein Language Model for Unified Molecular Modeling

**Source**: [https://proceedings.mlr.press/v235/zheng24h.html](https://proceedings.mlr.press/v235/zheng24h.html)

**TLDR**: ESM All-Atom extends protein language models to operate at both residue and atom scales for unified molecular modeling.

## Abstract

Protein language models have demonstrated significant potential in the field of protein engineering. However, current protein language models primarily operate at the residue scale, which limits their ability to provide information at the atom level. This limitation prevents us from fully exploiting the capabilities of protein language models for applications involving both proteins and small molecules. In this paper, we propose ESM-AA (ESM All-Atom), a novel approach that enables atom-scale and residue-scale unified molecular modeling. ESM-AA achieves this by pre-training on multi-scale code-switch protein sequences and utilizing a multi-scale position encoding to capture relationships among residues and atoms. Experimental results indicate that ESM-AA surpasses previous methods in protein-molecule tasks, demonstrating the full utilization of protein language models. Further investigations reveal that through unified molecular modeling, ESM-AA not only gains molecular knowledge but also retains its understanding of proteins.