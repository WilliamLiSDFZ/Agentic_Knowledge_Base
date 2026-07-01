---
title: "Latent Diffusion for Neural Spiking Data"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/d60b6b7f0ba6bf07d975b3bbdacea702-Abstract-Conference.html"
categories: ['diffusion-based-generative-modeling-and-inference', 'recurrent-and-spiking-neural-network-dynamics']
tags: ['latent-diffusion', 'neural-spiking-data', 'neuroscience']
venue: "NeurIPS 2024"
tldr: "A latent diffusion model for generating and analyzing high-dimensional neural spiking data that captures complex behavior-neural activity relationships."
---

# Latent Diffusion for Neural Spiking Data

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/d60b6b7f0ba6bf07d975b3bbdacea702-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/d60b6b7f0ba6bf07d975b3bbdacea702-Abstract-Conference.html)

**TLDR**: A latent diffusion model for generating and analyzing high-dimensional neural spiking data that captures complex behavior-neural activity relationships.

## Abstract

Modern datasets in neuroscience enable unprecedented inquiries into the relationship between complex behaviors and the activity of many simultaneously recorded neurons. While latent variable models can successfully extract low-dimensional embeddings from such recordings, using them to generate realistic spiking data, especially in a behavior-dependent manner, still poses a challenge. Here, we present Latent Diffusion for Neural Spiking data (LDNS), a diffusion-based generative model with a low-dimensional latent space: LDNS employs an autoencoder with structured state-space (S4) layers to project discrete high-dimensional spiking data into continuous time-aligned latents. On these inferred latents, we train expressive (conditional) diffusion models, enabling us to sample neural activity with realistic single-neuron and population spiking statistics. We validate LDNS on synthetic data, accurately recovering latent structure, firing rates, and spiking statistics. Next, we demonstrate its flexibility by generating variable-length data that mimics human cortical activity during attempted speech. We show how to equip LDNS with an expressive observation model that accounts for single-neuron dynamics not mediated by the latent state, further increasing the realism of generated samples. Finally, conditional LDNS trained on motor cortical activity during diverse reaching behaviors can generate realistic spiking data given reach direction or unseen reach trajectories. In summary, LDNS simultaneously enables inference of low-dimensional latents and realistic conditional generation of neural spiking datasets, opening up further possibilities for simulating experimentally testable hypotheses.