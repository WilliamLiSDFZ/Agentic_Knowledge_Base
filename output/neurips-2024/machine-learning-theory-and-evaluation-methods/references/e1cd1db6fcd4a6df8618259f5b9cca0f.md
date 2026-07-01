---
title: "Almost Surely Asymptotically Constant Graph Neural Networks"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/e1cd1db6fcd4a6df8618259f5b9cca0f-Abstract-Conference.html"
categories: ['graph-neural-networks-and-representation-learning', 'machine-learning-theory-and-evaluation-methods']
tags: ['graph-neural-networks', 'expressive-power', 'random-graph-models']
venue: "NeurIPS 2024"
tldr: "Proves that real-valued GNN classifier outputs converge to constants almost surely as graphs grow larger under random graph models, revealing fundamental expressiveness limitations."
---

# Almost Surely Asymptotically Constant Graph Neural Networks

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/e1cd1db6fcd4a6df8618259f5b9cca0f-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/e1cd1db6fcd4a6df8618259f5b9cca0f-Abstract-Conference.html)

**TLDR**: Proves that real-valued GNN classifier outputs converge to constants almost surely as graphs grow larger under random graph models, revealing fundamental expressiveness limitations.

## Abstract

We present a new angle on the expressive power of graph neural networks (GNNs) by studying how the predictions of real-valued GNN classifiers, such as those classifying graphs probabilistically, evolve as we apply them on larger graphs drawn from some random graph model. We show that the output converges to a constant function, which upper-bounds what these classifiers can uniformly express. This strong convergence phenomenon applies to a very wide class of GNNs, including state of the art models, with aggregates including mean and the attention-based mechanism of graph transformers. Our results apply to a broad class of random graph models, including sparse and dense variants of the Erdős-Rényi model, the stochastic block model, and the Barabási-Albert model. We empirically validate these findings, observing that the convergence phenomenon appears not only on random graphs but also on some real-world graphs.