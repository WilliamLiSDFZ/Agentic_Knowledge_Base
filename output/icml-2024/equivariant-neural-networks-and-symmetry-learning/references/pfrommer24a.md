---
title: "Transport of Algebraic Structure to Latent Embeddings"
source: "https://proceedings.mlr.press/v235/pfrommer24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pfrommer24a/pfrommer24a.pdf"
categories: ['algebraic-structures-in-machine-learning', 'equivariant-neural-networks-and-symmetry-learning']
tags: ['algebraic-structures', 'latent-embeddings', 'implicit-neural-representations', '3D-modeling', 'transport']
venue: "ICML 2024"
tldr: "Develops a framework for transporting algebraic structure from input spaces to latent embeddings, enabling algebraically consistent neural representations."
---

# Transport of Algebraic Structure to Latent Embeddings

**Source**: [https://proceedings.mlr.press/v235/pfrommer24a.html](https://proceedings.mlr.press/v235/pfrommer24a.html)

**TLDR**: Develops a framework for transporting algebraic structure from input spaces to latent embeddings, enabling algebraically consistent neural representations.

## Abstract

Machine learning often aims to produce latent embeddings of inputs which lie in a larger, abstract mathematical space. For example, in the field of 3D modeling, subsets of Euclidean space can be embedded as vectors using implicit neural representations. Such subsets also have a natural algebraic structure including operations (e.g., union) and corresponding laws (e.g., associativity). How can we learn to "union" two sets using only their latent embeddings while respecting associativity? We propose a general procedure for parameterizing latent space operations that are provably consistent with the laws on the input space. This is achieved by learning a bijection from the latent space to a carefully designed mirrored algebra which is constructed on Euclidean space in accordance with desired laws. We evaluate these structural transport nets for a range of mirrored algebras against baselines that operate directly on the latent space. Our experiments provide strong evidence that respecting the underlying algebraic structure of the input space is key for learning accurate and self-consistent operations.