---
title: "Semantically-correlated memories in a dense associative model"
source: "https://proceedings.mlr.press/v235/burns24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/burns24a/burns24a.pdf"
categories: ['neuromorphic-computing-and-neural-dynamics-modeling', 'multi-region-brain-connectivity-modeling']
tags: ['associative-memory', 'dense-associative-models', 'hetero-association', 'graph-structure']
venue: "ICML 2024"
tldr: "Introduces CDAM, a novel associative memory model unifying auto- and hetero-association via arbitrary graph-structured semantic links between memory patterns."
---

# Semantically-correlated memories in a dense associative model

**Source**: [https://proceedings.mlr.press/v235/burns24a.html](https://proceedings.mlr.press/v235/burns24a.html)

**TLDR**: Introduces CDAM, a novel associative memory model unifying auto- and hetero-association via arbitrary graph-structured semantic links between memory patterns.

## Abstract

I introduce a novel associative memory model named Correlated Dense Associative Memory (CDAM), which integrates both auto- and hetero-association in a unified framework for continuous-valued memory patterns. Employing an arbitrary graph structure to semantically link memory patterns, CDAM is theoretically and numerically analysed, revealing four distinct dynamical modes: auto-association, narrow hetero-association, wide hetero-association, and neutral quiescence. Drawing inspiration from inhibitory modulation studies, I employ anti-Hebbian learning rules to control the range of hetero-association, extract multi-scale representations of community structures in graphs, and stabilise the recall of temporal sequences. Experimental demonstrations showcase CDAM’s efficacy in handling real-world data, replicating a classical neuroscience experiment, performing image retrieval, and simulating arbitrary finite automata.