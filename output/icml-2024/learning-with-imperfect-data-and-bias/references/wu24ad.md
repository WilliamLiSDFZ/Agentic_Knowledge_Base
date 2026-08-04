---
title: "Unraveling the Impact of Heterophilic Structures on Graph Positive-Unlabeled Learning"
source: "https://proceedings.mlr.press/v235/wu24ad.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24ad/wu24ad.pdf"
categories: ['graph-neural-networks-and-topology', 'learning-with-imperfect-data-and-bias']
tags: ['positive-unlabeled-learning', 'graph-heterophily', 'semi-supervised', 'graph-neural-networks', 'label-bias']
venue: "ICML 2024"
tldr: "Reveals that edge heterophily critically challenges PU learning on graphs by violating the irreducibility assumption, and proposes methods to address this."
---

# Unraveling the Impact of Heterophilic Structures on Graph Positive-Unlabeled Learning

**Source**: [https://proceedings.mlr.press/v235/wu24ad.html](https://proceedings.mlr.press/v235/wu24ad.html)

**TLDR**: Reveals that edge heterophily critically challenges PU learning on graphs by violating the irreducibility assumption, and proposes methods to address this.

## Abstract

While Positive-Unlabeled (PU) learning is vital in many real-world scenarios, its application to graph data still remains under-explored. We unveil that a critical challenge for PU learning on graph lies on the edge heterophily, which directly violates the $\textit{irreducibility assumption}$ for $\textit{Class-Prior Estimation}$ (class prior is essential for building PU learning algorithms) and degenerates the latent label inference on unlabeled nodes during classifier training. In response to this challenge, we introduce a new method, named $\textit{$\underline{G}$raph $\underline{P}$U Learning with $\underline{L}$abel Propagation Loss}$ (GPL). Specifically, GPL considers learning from PU nodes along with an intermediate heterophily reduction, which helps mitigate the negative impact of the heterophilic structure. We formulate this procedure as a bilevel optimization that reduces heterophily in the inner loop and efficiently learns a classifier in the outer loop. Extensive experiments across a variety of datasets have shown that GPL significantly outperforms baseline methods, confirming its effectiveness and superiority.