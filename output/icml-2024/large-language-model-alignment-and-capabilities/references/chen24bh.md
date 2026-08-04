---
title: "LLaGA: Large Language and Graph Assistant"
source: "https://proceedings.mlr.press/v235/chen24bh.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24bh/chen24bh.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'graph-neural-networks-and-topology']
tags: ['graph-LLM', 'node-classification', 'LLM-graph-integration']
venue: "ICML 2024"
tldr: "LLaGA integrates large language models with graph neural networks to enable versatile graph-structured data analysis."
---

# LLaGA: Large Language and Graph Assistant

**Source**: [https://proceedings.mlr.press/v235/chen24bh.html](https://proceedings.mlr.press/v235/chen24bh.html)

**TLDR**: LLaGA integrates large language models with graph neural networks to enable versatile graph-structured data analysis.

## Abstract

Graph Neural Networks (GNNs) have empowered the advance in graph-structured data analysis. Recently, the rise of Large Language Models (LLMs) like GPT-4 has heralded a new era in deep learning. However, their application to graph data poses distinct challenges due to the inherent difficulty of translating graph structures to language. To this end, we introduce the the Large Language and Graph Assistant (LLaGA), an innovative model that effectively integrates LLM capabilities to handle the complexities of graph-structured data. LLaGA retains the general-purpose nature of LLMs while adapting graph data into a format compatible with LLM input. LLaGA achieves this by reorganizing graph nodes to structure-aware sequences and then mapping these into the token embedding space through a versatile projector. LLaGA excels in versatility, generalizability and interpretability, allowing it to perform consistently well across different datasets and tasks, extend its ability to unseen datasets or tasks, and provide explanations for graphs. Our extensive experiments across popular graph benchmarks show that LLaGA delivers outstanding performance across four datasets and three tasks using one single model, surpassing state-of-the-art graph models in both supervised and zero-shot scenarios.