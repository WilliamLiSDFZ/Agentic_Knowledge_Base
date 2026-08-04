---
title: "Scene Graph Generation Strategy with Co-occurrence Knowledge and Learnable Term Frequency"
source: "https://proceedings.mlr.press/v235/kim24n.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24n/kim24n.pdf"
categories: ['graph-neural-networks-and-topology', '3d-vision-and-scene-understanding']
tags: ['scene-graph-generation', 'co-occurrence-knowledge', 'term-frequency']
venue: "ICML 2024"
tldr: "Improves scene graph generation by incorporating co-occurrence knowledge and learnable term frequency into a message-passing framework."
---

# Scene Graph Generation Strategy with Co-occurrence Knowledge and Learnable Term Frequency

**Source**: [https://proceedings.mlr.press/v235/kim24n.html](https://proceedings.mlr.press/v235/kim24n.html)

**TLDR**: Improves scene graph generation by incorporating co-occurrence knowledge and learnable term frequency into a message-passing framework.

## Abstract

Scene graph generation (SGG) is an important task in image understanding because it represents the relationships between objects in an image as a graph structure, making it possible to understand the semantic relationships between objects intuitively. Previous SGG studies used a message-passing neural networks (MPNN) to update features, which can effectively reflect information about surrounding objects. However, these studies have failed to reflect the co-occurrence of objects during SGG generation. In addition, they only addressed the long-tail problem of the training dataset from the perspectives of sampling and learning methods. To address these two problems, we propose CooK, which reflects the Co-occurrence Knowledge between objects, and the learnable term frequency-inverse document frequency (TF-$l$-IDF) to solve the long-tail problem. We applied the proposed model to the SGG benchmark dataset, and the results showed a performance improvement of up to 3.8% compared with existing state-of-the-art models in SGGen subtask. The proposed method exhibits generalization ability from the results obtained, showing uniform performance improvement for all MPNN models.