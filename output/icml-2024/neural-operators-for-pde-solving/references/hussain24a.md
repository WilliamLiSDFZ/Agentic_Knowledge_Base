---
title: "Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph Learning with Triplet Graph Transformers"
source: "https://proceedings.mlr.press/v235/hussain24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hussain24a/hussain24a.pdf"
categories: ['graph-neural-networks-and-topology', 'neural-operators-for-pde-solving']
tags: ['graph-transformers', 'molecular-graphs', 'triplet-interaction', 'geometric-learning', 'message-passing']
venue: "ICML 2024"
tldr: "Introduces Triplet Graph Transformers with third-order node interactions for improved molecular geometry prediction accuracy."
---

# Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph Learning with Triplet Graph Transformers

**Source**: [https://proceedings.mlr.press/v235/hussain24a.html](https://proceedings.mlr.press/v235/hussain24a.html)

**TLDR**: Introduces Triplet Graph Transformers with third-order node interactions for improved molecular geometry prediction accuracy.

## Abstract

Graph transformers typically lack third-order interactions, limiting their geometric understanding which is crucial for tasks like molecular geometry prediction. We propose the Triplet Graph Transformer (TGT) that enables direct communication between pairs within a 3-tuple of nodes via novel triplet attention and aggregation mechanisms. TGT is applied to molecular property prediction by first predicting interatomic distances from 2D graphs and then using these distances for downstream tasks. A novel three-stage training procedure and stochastic inference further improve training efficiency and model performance. Our model achieves new state-of-the-art (SOTA) results on open challenge benchmarks PCQM4Mv2 and OC20 IS2RE. We also obtain SOTA results on QM9, MOLPCBA, and LIT-PCBA molecular property prediction benchmarks via transfer learning. We also demonstrate the generality of TGT with SOTA results on the traveling salesman problem (TSP).