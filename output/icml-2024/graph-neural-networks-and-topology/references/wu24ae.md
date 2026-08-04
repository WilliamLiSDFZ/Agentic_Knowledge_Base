---
title: "Mitigating Label Noise on Graphs via Topological Sample Selection"
source: "https://proceedings.mlr.press/v235/wu24ae.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24ae/wu24ae.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'graph-neural-networks-and-topology']
tags: ['label-noise', 'graph-neural-networks', 'sample-selection', 'topological-features', 'noisy-labels']
venue: "ICML 2024"
tldr: "Proposes topological sample selection to mitigate label noise in graph neural networks by leveraging graph topology for identifying clean samples."
---

# Mitigating Label Noise on Graphs via Topological Sample Selection

**Source**: [https://proceedings.mlr.press/v235/wu24ae.html](https://proceedings.mlr.press/v235/wu24ae.html)

**TLDR**: Proposes topological sample selection to mitigate label noise in graph neural networks by leveraging graph topology for identifying clean samples.

## Abstract

Despite the success of the carefully-annotated benchmarks, the effectiveness of existing graph neural networks (GNNs) can be considerably impaired in practice when the real-world graph data is noisily labeled. Previous explorations in sample selection have been demonstrated as an effective way for robust learning with noisy labels, however, the conventional studies focus on i.i.d data, and when moving to non-iid graph data and GNNs, two notable challenges remain: (1) nodes located near topological class boundaries are very informative for classification but cannot be successfully distinguished by the heuristic sample selection. (2) there is no available measure that considers the graph topological information to promote sample selection in a graph. To address this dilemma, we propose a $\textit{Topological Sample Selection}$ (TSS) method that boosts the informative sample selection process in a graph by utilising topological information. We theoretically prove that our procedure minimizes an upper bound of the expected risk under target clean distribution, and experimentally show the superiority of our method compared with state-of-the-art baselines.