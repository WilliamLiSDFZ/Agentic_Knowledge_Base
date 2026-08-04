---
title: "On the Role of Edge Dependency in Graph Generative Models"
source: "https://proceedings.mlr.press/v235/chanpuriya24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chanpuriya24a/chanpuriya24a.pdf"
categories: ['generative-models-and-variational-inference', 'probabilistic-generating-circuits-research']
tags: ['graph-generative-models', 'edge-dependency', 'model-overlap', 'representation-power']
venue: "ICML 2024"
tldr: "A theoretical study of how edge dependency in graph generative models affects the trade-off between representational power and training data memorization."
---

# On the Role of Edge Dependency in Graph Generative Models

**Source**: [https://proceedings.mlr.press/v235/chanpuriya24a.html](https://proceedings.mlr.press/v235/chanpuriya24a.html)

**TLDR**: A theoretical study of how edge dependency in graph generative models affects the trade-off between representational power and training data memorization.

## Abstract

We investigate the trade-off between the representation power of graph generative models and model overlap, i.e., the degree to which the model generates diverse outputs versus regurgitating its training data. In particular, we delineate a nested hierarchy of graph generative models categorized into three levels of complexity: edge independent, node independent, and arbitrarily dependent models. This hierarchy encapsulates a wide range of prevalent methods. We derive theoretical bounds on the number of triangles and other short-length cycles producible by each level of the hierarchy, finding that more complex dependency structure allows an improved trade-off between representation power and overlap. We provide instances demonstrating the asymptotic optimality of our bounds. Furthermore, we introduce new generative models for each of the three hierarchical levels, leveraging dense subgraph discovery. Our evaluation, conducted on real-world datasets, focuses on assessing the output quality and overlap of our proposed models in comparison to other popular models. Our results indicate that our simple, interpretable models provide competitive baselines to popular generative models. Through this investigation, we offer a structured and robust evaluation scheme, thereby facilitating the development of models capable of generating accurate and edge-diverse graphs.