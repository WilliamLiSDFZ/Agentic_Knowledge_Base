---
title: "PGODE: Towards High-quality System Dynamics Modeling"
source: "https://proceedings.mlr.press/v235/luo24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/luo24b/luo24b.pdf"
categories: ['graph-neural-networks-and-topology', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['multi-agent-systems', 'dynamical-systems', 'graph-neural-networks', 'ODE']
venue: "ICML 2024"
tldr: "PGODE improves multi-agent dynamical system modeling by combining geometric graphs with high-quality system-level modeling using GNNs and ODEs."
---

# PGODE: Towards High-quality System Dynamics Modeling

**Source**: [https://proceedings.mlr.press/v235/luo24b.html](https://proceedings.mlr.press/v235/luo24b.html)

**TLDR**: PGODE improves multi-agent dynamical system modeling by combining geometric graphs with high-quality system-level modeling using GNNs and ODEs.

## Abstract

This paper studies the problem of modeling multi-agent dynamical systems, where agents could interact mutually to influence their behaviors. Recent research predominantly uses geometric graphs to depict these mutual interactions, which are then captured by powerful graph neural networks (GNNs). However, predicting interacting dynamics in challenging scenarios such as out-of-distribution shift and complicated underlying rules remains unsolved. In this paper, we propose a new approach named Prototypical Graph ODE (PGODE) to address the problem. The core of PGODE is to incorporate prototype decomposition from contextual knowledge into a continuous graph ODE framework. Specifically, PGODE employs representation disentanglement and system parameters to extract both object-level and system-level contexts from historical trajectories, which allows us to explicitly model their independent influence and thus enhances the generalization capability under system changes. Then, we integrate these disentangled latent representations into a graph ODE model, which determines a combination of various interacting prototypes for enhanced model expressivity. The entire model is optimized using an end-to-end variational inference framework to maximize the likelihood. Extensive experiments in both in-distribution and out-of-distribution settings validate the superiority of PGODE compared to various baselines.