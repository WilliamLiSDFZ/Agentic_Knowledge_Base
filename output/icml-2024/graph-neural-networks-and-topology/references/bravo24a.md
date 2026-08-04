---
title: "On dimensionality of feature vectors in MPNNs"
source: "https://proceedings.mlr.press/v235/bravo24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bravo24a/bravo24a.pdf"
categories: ['graph-neural-networks-and-topology', 'neural-network-learning-dynamics-theory']
tags: ['MPNNs', 'Weisfeiler-Leman', 'graph-isomorphism', 'feature-dimensionality']
venue: "ICML 2024"
tldr: "This paper revisits the equivalence between MPNNs and the WL test, tightening bounds on the required feature vector dimensionality."
---

# On dimensionality of feature vectors in MPNNs

**Source**: [https://proceedings.mlr.press/v235/bravo24a.html](https://proceedings.mlr.press/v235/bravo24a.html)

**TLDR**: This paper revisits the equivalence between MPNNs and the WL test, tightening bounds on the required feature vector dimensionality.

## Abstract

We revisit the result of Morris et al. (AAAI’19) that message-passing graphs neural networks (MPNNs) are equal in their distinguishing power to the Weisfeiler–Leman (WL) isomorphism test. Morris et al. show their result with ReLU activation function and $O(n)$-dimensional feature vectors, where $n$ is the size of the graph. Recently, by introducing randomness into the architecture, Aamand et al. (NeurIPS’22) improved this bound to $O(\log n)$-dimensional feature vectors, although at the expense of guaranteeing perfect simulation only with high probability. In all these constructions, to guarantee equivalence to the WL test, the dimension of feature vectors in the MPNN has to increase with the size of the graphs. However, architectures used in practice have feature vectors of constant dimension. Thus, there is a gap between the guarantees provided by these results and the actual characteristics of architectures used in practice. In this paper we close this gap by showing that, for any non-polynomial analytic (like the sigmoid) activation function, to guarantee that MPNNs are equivalent to the WL test, feature vectors of dimension $d=1$ is all we need, independently of the size of the graphs. Our main technical insight is that for simulating multi-sets in the WL-test, it is enough to use linear independence of feature vectors over rationals instead of reals. Countability of the set of rationals together with nice properties of analytic functions allow us to carry out the simulation invariant over the iterations of the WL test without increasing the dimension of the feature vectors.