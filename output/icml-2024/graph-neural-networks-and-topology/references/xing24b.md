---
title: "Less is More: on the Over-Globalizing Problem in Graph Transformers"
source: "https://proceedings.mlr.press/v235/xing24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xing24b/xing24b.pdf"
categories: ['graph-neural-networks-and-topology', 'transformer-architecture-efficiency-and-scaling']
tags: ['graph-transformers', 'over-globalization', 'attention']
venue: "ICML 2024"
tldr: "Identifies an over-globalizing problem in graph transformers where excessive global attention hurts performance and proposes targeted fixes."
---

# Less is More: on the Over-Globalizing Problem in Graph Transformers

**Source**: [https://proceedings.mlr.press/v235/xing24b.html](https://proceedings.mlr.press/v235/xing24b.html)

**TLDR**: Identifies an over-globalizing problem in graph transformers where excessive global attention hurts performance and proposes targeted fixes.

## Abstract

Graph Transformer, due to its global attention mechanism, has emerged as a new tool in dealing with graph-structured data. It is well recognized that the global attention mechanism considers a wider receptive field in a fully connected graph, leading many to believe that useful information can be extracted from all the nodes. In this paper, we challenge this belief: does the globalizing property always benefit Graph Transformers? We reveal the over-globalizing problem in Graph Transformer by presenting both empirical evidence and theoretical analysis, i.e., the current attention mechanism overly focuses on those distant nodes, while the near nodes, which actually contain most of the useful information, are relatively weakened. Then we propose a novel Bi-Level Global Graph Transformer with Collaborative Training (CoBFormer), including the inter-cluster and intra-cluster Transformers, to prevent the over-globalizing problem while keeping the ability to extract valuable information from distant nodes. Moreover, the collaborative training is proposed to improve the model’s generalization ability with a theoretical guarantee. Extensive experiments on various graphs well validate the effectiveness of our proposed CoBFormer.