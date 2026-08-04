---
title: "A Circuit Domain Generalization Framework for Efficient Logic Synthesis in Chip Design"
source: "https://proceedings.mlr.press/v235/wang24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24g/wang24g.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'graph-neural-networks-and-topology']
tags: ['logic-synthesis', 'circuit-design', 'domain-generalization', 'graph-neural-networks', 'chip-design']
venue: "ICML 2024"
tldr: "A circuit domain generalization framework improves logic synthesis by learning transferable GNN representations across different circuit domains."
---

# A Circuit Domain Generalization Framework for Efficient Logic Synthesis in Chip Design

**Source**: [https://proceedings.mlr.press/v235/wang24g.html](https://proceedings.mlr.press/v235/wang24g.html)

**TLDR**: A circuit domain generalization framework improves logic synthesis by learning transferable GNN representations across different circuit domains.

## Abstract

Logic Synthesis (LS) plays a vital role in chip design. A key task in LS is to simplify circuits—modeled by directed acyclic graphs (DAGs)—with functionality-equivalent transformations. To tackle this task, many LS heuristics apply transformations to subgraphs—rooted at each node on an input DAG—sequentially. However, we found that a large number of transformations are ineffective, which makes applying these heuristics highly time-consuming. In particular, we notice that the runtime of the Resub and Mfs2 heuristics often dominates the overall runtime of LS optimization processes. To address this challenge, we propose a novel data-driven LS heuristic paradigm, namely PruneX, to reduce ineffective transformations. The major challenge of developing PruneX is to learn models that well generalize to unseen circuits, i.e., the out-of-distribution (OOD) generalization problem. Thus, the major technical contribution of PruneX is the novel circuit domain generalization framework, which learns domain-invariant representations based on the transformation-invariant domain-knowledge. To the best of our knowledge, PruneX is the first approach to tackle the OOD problem in LS heuristics. We integrate PruneX with the aforementioned Resub and Mfs2 heuristics. Experiments demonstrate that PruneX significantly improves their efficiency while keeping comparable optimization performance on industrial and very large-scale circuits, achieving up to $3.1\times$ faster runtime.