---
title: "Vocabulary for Universal Approximation: A Linguistic Perspective of Mapping Compositions"
source: "https://proceedings.mlr.press/v235/cai24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cai24a/cai24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'anomaly-and-out-of-distribution-detection']
tags: ['universal-approximation', 'sequence-models', 'mapping-compositions', 'vocabulary']
venue: "ICML 2024"
tldr: "Establishes a linguistic perspective on universal approximation by representing deep neural networks as compositions of mappings from a vocabulary."
---

# Vocabulary for Universal Approximation: A Linguistic Perspective of Mapping Compositions

**Source**: [https://proceedings.mlr.press/v235/cai24a.html](https://proceedings.mlr.press/v235/cai24a.html)

**TLDR**: Establishes a linguistic perspective on universal approximation by representing deep neural networks as compositions of mappings from a vocabulary.

## Abstract

In recent years, deep learning-based sequence modelings, such as language models, have received much attention and success, which pushes researchers to explore the possibility of transforming non-sequential problems into a sequential form. Following this thought, deep neural networks can be represented as composite functions of a sequence of mappings, linear or nonlinear, where each composition can be viewed as a word. However, the weights of linear mappings are undetermined and hence require an infinite number of words. In this article, we investigate the finite case and constructively prove the existence of a finite vocabulary $V$=$\phi_i: \mathbb{R}^d \to \mathbb{R}^d | i=1,...,n$ with $n=O(d^2)$ for the universal approximation. That is, for any continuous mapping $f: \mathbb{R}^d \to \mathbb{R}^d$, compact domain $\Omega$ and $\varepsilon>0$, there is a sequence of mappings $\phi_{i_1}, ..., \phi_{i_m} \in V, m \in \mathbb{Z}^+$, such that the composition $\phi_{i_m} \circ ... \circ \phi_{i_1} $ approximates $f$ on $\Omega$ with an error less than $\varepsilon$. Our results demonstrate an unusual approximation power of mapping compositions and motivate a novel compositional model for regular languages.