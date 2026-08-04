---
title: "Knowledge Graphs Can be Learned with Just Intersection Features"
source: "https://proceedings.mlr.press/v235/le24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/le24c/le24c.pdf"
categories: ['graph-neural-networks-and-topology', 'information-retrieval-and-recommendation-systems']
tags: ['knowledge-graphs', 'KG-completion', 'intersection-features', 'link-prediction']
venue: "ICML 2024"
tldr: "Demonstrates that knowledge graph completion can be achieved effectively using only intersection features, reducing the need for complex embeddings."
---

# Knowledge Graphs Can be Learned with Just Intersection Features

**Source**: [https://proceedings.mlr.press/v235/le24c.html](https://proceedings.mlr.press/v235/le24c.html)

**TLDR**: Demonstrates that knowledge graph completion can be achieved effectively using only intersection features, reducing the need for complex embeddings.

## Abstract

Knowledge Graphs (KGs) are potent frameworks for knowledge representation and reasoning. Nevertheless, KGs are inherently incomplete, leaving numerous uncharted relationships and facts awaiting discovery. Deep learning methodologies have proven effective in enhancing KG completion by framing it as a link prediction task, where the goal is to discern the validity of a triple comprising a head, relation, and tail. The significance of structural information in assessing the validity of a triple within a KG is well-established. However, quantifying this structural information poses a challenge. We need to pinpoint the metric that encapsulates the structural information of a triple and smoothly incorporate this metric into the link prediction learning process. In this study, we recognize the critical importance of the intersection among the $k$-hop neighborhoods of the head, relation, and tail when determining the validity of a triple. To address this, we introduce a novel randomized algorithm designed to efficiently generate intersection features for candidate triples. Our experimental results demonstrate that a straightforward fully-connected network leveraging these intersection features can surpass the performance of established KG embedding models and even outperform graph neural network baselines. Additionally, we highlight the substantial training time efficiency gains achieved by our network trained on intersection features.