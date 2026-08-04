---
title: "Graph-Triggered Rising Bandits"
source: "https://proceedings.mlr.press/v235/genalti24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/genalti24a/genalti24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'online-learning-matching-market-algorithms']
tags: ['graph-triggered-bandits', 'restless-bandits', 'arm-evolution']
venue: "ICML 2024"
tldr: "Proposes graph-triggered rising bandits where arm reward evolution is governed by a graph structure over arms."
---

# Graph-Triggered Rising Bandits

**Source**: [https://proceedings.mlr.press/v235/genalti24a.html](https://proceedings.mlr.press/v235/genalti24a.html)

**TLDR**: Proposes graph-triggered rising bandits where arm reward evolution is governed by a graph structure over arms.

## Abstract

In this paper, we propose a novel generalization of rested and restless bandits where the evolution of the arms’ expected rewards is governed by a graph defined over the arms. An edge connecting a pair of arms $(i,j)$ represents the fact that a pull of arm $i$ triggers the evolution of arm $j$, and vice versa. Interestingly, rested and restless bandits are both special cases of our model for some suitable (degenerate) graphs. Still, the model can represent way more general and interesting scenarios. We first tackle the problem of computing the optimal policy when no specific structure is assumed on the graph, showing that it is NP-hard. Then, we focus on a specific structure forcing the graph to be composed of a set of fully connected subgraphs (i.e., cliques), and we prove that the optimal policy can be easily computed in closed form. Then, we move to the learning problem presenting regret minimization algorithms for deterministic and stochastic cases. Our regret bounds highlight the complexity of the learning problem by incorporating instance-dependent terms that encode specific properties of the underlying graph structure. Moreover, we illustrate how the knowledge of the underlying graph is not necessary for achieving the no-regret property.