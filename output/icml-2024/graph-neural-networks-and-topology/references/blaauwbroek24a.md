---
title: "Graph2Tac: Online Representation Learning of Formal Math Concepts"
source: "https://proceedings.mlr.press/v235/blaauwbroek24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/blaauwbroek24a/blaauwbroek24a.pdf"
categories: ['graph-neural-networks-and-topology', 'online-learning-and-sequential-decision-making']
tags: ['graph-neural-networks', 'formal-mathematics', 'proof-assistants', 'online-learning']
venue: "ICML 2024"
tldr: "Graph2Tac exploits locality in formal math libraries through online representation learning to improve automated theorem proving in proof assistants."
---

# Graph2Tac: Online Representation Learning of Formal Math Concepts

**Source**: [https://proceedings.mlr.press/v235/blaauwbroek24a.html](https://proceedings.mlr.press/v235/blaauwbroek24a.html)

**TLDR**: Graph2Tac exploits locality in formal math libraries through online representation learning to improve automated theorem proving in proof assistants.

## Abstract

In proof assistants, the physical proximity between two formal mathematical concepts is a strong predictor of their mutual relevance. Furthermore, lemmas with close proximity regularly exhibit similar proof structures. We show that this locality property can be exploited through online learning techniques to obtain solving agents that far surpass offline learners when asked to prove theorems in an unseen mathematical setting. We extensively benchmark two such online solvers implemented in the Tactician platform for the Coq proof assistant: First, Tactician’s online $k$-nearest neighbor solver, which can learn from recent proofs, shows a $1.72\times$ improvement in theorems proved over an offline equivalent. Second, we introduce a graph neural network, Graph2Tac, with a novel approach to build hierarchical representations for new definitions. Graph2Tac’s online definition task realizes a $1.5\times$ improvement in theorems solved over an offline baseline. The $k$-NN and Graph2Tac solvers rely on orthogonal online data, making them highly complementary. Their combination improves $1.27\times$ over their individual performances. Both solvers outperform all other general purpose provers for Coq, including CoqHammer, Proverbot9001, and a transformer baseline by at least $1.48\times$ and are available for practical use by end-users.