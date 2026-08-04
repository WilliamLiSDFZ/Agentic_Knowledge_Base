---
title: "An Efficient Maximal Ancestral Graph Listing Algorithm"
source: "https://proceedings.mlr.press/v235/wang24o.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24o/wang24o.pdf"
categories: ['causal-inference-and-discovery-methods', 'graph-clustering-and-matching-algorithms']
tags: ['maximal-ancestral-graphs', 'causal-discovery', 'Markov-equivalence', 'latent-variables', 'listing-algorithm']
venue: "ICML 2024"
tldr: "An efficient algorithm is proposed for listing all maximal ancestral graphs in a Markov equivalence class for causal discovery with latent variables."
---

# An Efficient Maximal Ancestral Graph Listing Algorithm

**Source**: [https://proceedings.mlr.press/v235/wang24o.html](https://proceedings.mlr.press/v235/wang24o.html)

**TLDR**: An efficient algorithm is proposed for listing all maximal ancestral graphs in a Markov equivalence class for causal discovery with latent variables.

## Abstract

Maximal ancestral graph (MAG) is a prevalent graphical model to characterize causal relations in the presence of latent variables including latent confounders and selection variables. Given observational data, only a Markov equivalence class (MEC) of MAGs is identifiable if without some additional assumptions. Due to this fact, MAG listing, listing all the MAGs in the MEC, is usually demanded in many downstream tasks. To the best of our knowledge, there are no relevant methods for MAG listing other than brute force in the literature. In this paper, we propose the first brute-force-free MAG listing method, by determining the local structures of each vertex recursively. We provide the graphical characterization for each valid local transformation of a vertex, and present sound and complete rules to incorporate the valid local transformation in the presence of latent confounders and selection variables. Based on these components, our method can efficiently output all the MAGs in the MEC with no redundance, that is, every intermediate graph in the recursive process is necessary for the MAG listing task. The empirical analysis demonstrates the superiority of our proposed method on efficiency and effectiveness.