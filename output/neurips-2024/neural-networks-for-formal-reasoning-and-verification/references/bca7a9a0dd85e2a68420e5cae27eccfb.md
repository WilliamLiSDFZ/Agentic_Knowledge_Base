---
title: "Logical characterizations of recurrent graph neural networks with reals and floats"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/bca7a9a0dd85e2a68420e5cae27eccfb-Abstract-Conference.html"
categories: ['graph-neural-networks-and-representation-learning', 'neural-networks-for-formal-reasoning-and-verification']
tags: ['recurrent-GNNs', 'logical-characterization', 'expressive-power']
venue: "NeurIPS 2024"
tldr: "Provides exact logical characterizations of recurrent graph neural networks over real and floating-point number computations."
---

# Logical characterizations of recurrent graph neural networks with reals and floats

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/bca7a9a0dd85e2a68420e5cae27eccfb-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/bca7a9a0dd85e2a68420e5cae27eccfb-Abstract-Conference.html)

**TLDR**: Provides exact logical characterizations of recurrent graph neural networks over real and floating-point number computations.

## Abstract

In pioneering work from 2019, Barceló and coauthors identified logics that precisely match the expressive power of constant iteration-depth graph neural networks (GNNs) relative to properties definable in first-order logic. In this article, we give exact logical characterizations of recurrent GNNs in two scenarios: (1) in the setting with floating-point numbers and (2) with reals. For floats, the formalism matching recurrent GNNs is a rule-based modal logic with counting, while for reals we use a suitable infinitary modal logic, also with counting. These results give exact matches between logics and GNNs in the recurrent setting without relativising to a background logic in either case, but using some natural assumptions about floating-point arithmetic. Applying our characterizations, we also prove that, relative to graph properties definable in monadic second-order logic (MSO), our infinitary and rule-based logics are equally expressive. This implies that recurrent GNNs with reals and floats have the same expressive power over MSO-definable properties and shows that, for such properties, also recurrent GNNs with reals are characterized by a (finitary!) rule-based modal logic. In the general case, in contrast, the expressive power with floats is weaker than with reals. In addition to logic-oriented results, we also characterize recurrent GNNs, with both reals and floats, via distributed automata, drawing links to distributed computing models.