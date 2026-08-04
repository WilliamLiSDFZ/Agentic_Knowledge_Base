---
title: "Just Cluster It: An Approach for Exploration in High-Dimensions using Clustering and Pre-Trained Representations"
source: "https://proceedings.mlr.press/v235/wagner24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wagner24a/wagner24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'clustering-methods-and-multi-view-learning']
tags: ['exploration', 'reinforcement-learning', 'clustering', 'pre-trained-representations', 'density-estimation']
venue: "ICML 2024"
tldr: "Proposes using clustering of pre-trained representations as a density estimation approach for efficient exploration in high-dimensional 3D environments."
---

# Just Cluster It: An Approach for Exploration in High-Dimensions using Clustering and Pre-Trained Representations

**Source**: [https://proceedings.mlr.press/v235/wagner24a.html](https://proceedings.mlr.press/v235/wagner24a.html)

**TLDR**: Proposes using clustering of pre-trained representations as a density estimation approach for efficient exploration in high-dimensional 3D environments.

## Abstract

In this paper we adopt a representation-centric perspective on exploration in reinforcement learning, viewing exploration fundamentally as a density estimation problem. We investigate the effectiveness of clustering representations for exploration in 3-D environments, based on the observation that the importance of pixel changes between transitions is less pronounced in 3-D environments compared to 2-D environments, where pixel changes between transitions are typically distinct and significant. We propose a method that performs episodic and global clustering on random representations and on pre-trained DINO representations to count states, i.e, estimate pseudo-counts. Surprisingly, even random features can be clustered effectively to count states in 3-D environments, however when these become visually more complex, pre-trained DINO representations are more effective thanks to the pre-trained inductive biases in the representations. Overall, this presents a pathway for integrating pre-trained biases into exploration. We evaluate our approach on the VizDoom and Habitat environments, demonstrating that our method surpasses other well-known exploration methods in these settings.