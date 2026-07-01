---
title: "Spectral Learning of Shared Dynamics Between Generalized-Linear Processes"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/a267f6a1ea2bc9e0ec15ed4af7d5ae3f-Abstract-Conference.html"
categories: ['recurrent-and-spiking-neural-network-dynamics']
tags: ['generalized-linear-dynamical-models', 'spectral-learning', 'neuroscience']
venue: "NeurIPS 2024"
tldr: "Spectral learning framework for identifying shared latent dynamics across multiple generalized-linear processes such as neural spiking data."
---

# Spectral Learning of Shared Dynamics Between Generalized-Linear Processes

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/a267f6a1ea2bc9e0ec15ed4af7d5ae3f-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/a267f6a1ea2bc9e0ec15ed4af7d5ae3f-Abstract-Conference.html)

**TLDR**: Spectral learning framework for identifying shared latent dynamics across multiple generalized-linear processes such as neural spiking data.

## Abstract

Generalized-linear dynamical models (GLDMs) remain a widely-used framework within neuroscience for modeling time-series data, such as neural spiking activity or categorical decision outcomes. Whereas the standard usage of GLDMs is to model a single data source, certain applications require jointly modeling two generalized-linear time-series sources while also dissociating their shared and private dynamics. Most existing GLDM variants and their associated learning algorithms do not support this capability. Here we address this challenge by developing a multi-step analytical subspace identification algorithm for learning a GLDM that explicitly models shared vs. private dynamics within two generalized-linear time-series. In simulations, we demonstrate our algorithm's ability to dissociate and model the dynamics within two time-series sources while being agnostic to their respective observation distributions. In neural data, we consider two specific applications of our algorithm for modeling discrete population spiking activity with respect to a secondary time-series. In both synthetic and real data, GLDMs learned with our algorithm more accurately decoded one time-series from the other using lower-dimensional latent states, as compared to models identified using existing GLDM learning algorithms.