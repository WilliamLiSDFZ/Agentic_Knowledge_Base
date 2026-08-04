---
title: "Learning Latent Structures in Network Games via Data-Dependent Gated-Prior Graph Variational Autoencoders"
source: "https://proceedings.mlr.press/v235/yu24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yu24f/yu24f.pdf"
categories: ['generative-models-and-variational-inference', 'graph-neural-networks-and-topology']
tags: ['graph-variational-autoencoder', 'network-games', 'latent-structure-learning']
venue: "ICML 2024"
tldr: "A data-dependent gated-prior graph VAE that infers latent network structures from strategic interaction data in network games."
---

# Learning Latent Structures in Network Games via Data-Dependent Gated-Prior Graph Variational Autoencoders

**Source**: [https://proceedings.mlr.press/v235/yu24f.html](https://proceedings.mlr.press/v235/yu24f.html)

**TLDR**: A data-dependent gated-prior graph VAE that infers latent network structures from strategic interaction data in network games.

## Abstract

In network games, individuals interact strategically within network environments to maximize their utilities. However, obtaining network structures is challenging. In this work, we propose an unsupervised learning model, called data-dependent gated-prior graph variational autoencoder (GPGVAE), that infers the underlying latent interaction type (strategic complement vs. substitute) among individuals and the latent network structure based on their observed actions. Specially, we propose a spectral graph neural network (GNN) based encoder to predict the interaction type and a data-dependent gated prior that models network structures conditioned on the interaction type. We further propose a Transformer based mixture of Bernoulli encoder of network structures and a GNN based decoder of game actions. We systematically study the Monte Carlo gradient estimation methods and effectively train our model in a stage-wise fashion. Extensive experiments across various synthetic and real-world network games demonstrate that our model achieves state-of-the-art performances in inferring network structures and well captures interaction types.