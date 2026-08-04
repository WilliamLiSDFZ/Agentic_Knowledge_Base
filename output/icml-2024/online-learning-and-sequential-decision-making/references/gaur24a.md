---
title: "Closing the Gap: Achieving Global Convergence (Last Iterate) of Actor-Critic under Markovian Sampling with Neural Network Parametrization"
source: "https://proceedings.mlr.press/v235/gaur24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gaur24a/gaur24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'online-learning-and-sequential-decision-making']
tags: ['actor-critic', 'Markovian-sampling', 'neural-network-parametrization']
venue: "ICML 2024"
tldr: "Establishes global last-iterate convergence of actor-critic algorithms under Markovian sampling with neural network function approximation."
---

# Closing the Gap: Achieving Global Convergence (Last Iterate) of Actor-Critic under Markovian Sampling with Neural Network Parametrization

**Source**: [https://proceedings.mlr.press/v235/gaur24a.html](https://proceedings.mlr.press/v235/gaur24a.html)

**TLDR**: Establishes global last-iterate convergence of actor-critic algorithms under Markovian sampling with neural network function approximation.

## Abstract

The current state-of-the-art theoretical analysis of Actor-Critic (AC) algorithms significantly lags in addressing the practical aspects of AC implementations. This crucial gap needs bridging to bring the analysis in line with practical implementations of AC. To address this, we advocate for considering the MMCLG criteria: Multi-layer neural network parametrization for actor/critic, Markovian sampling, Continuous state-action spaces, the performance of the Last iterate, and Global optimality. These aspects are practically significant and have been largely overlooked in existing theoretical analyses of AC algorithms. In this work, we address these gaps by providing the first comprehensive theoretical analysis of AC algorithms that encompasses all five crucial practical aspects (covers MMCLG criteria). We establish global convergence sample complexity bounds of $\tilde{\mathcal{O}}\left( \epsilon^{-3} \right)$. We achieve this result through our novel use of the weak gradient domination property of MDP’s and our unique analysis of the error in critic estimation.