---
title: "StrWAEs to Invariant Representations"
source: "https://proceedings.mlr.press/v235/lee24u.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lee24u/lee24u.pdf"
categories: ['generative-models-and-variational-inference', 'clustering-methods-and-multi-view-learning']
tags: ['autoencoder', 'invariant-representation', 'Wasserstein', 'structural-constraints']
venue: "ICML 2024"
tldr: "Proposes structured Wasserstein autoencoders to learn invariant latent representations with conditional independence constraints."
---

# StrWAEs to Invariant Representations

**Source**: [https://proceedings.mlr.press/v235/lee24u.html](https://proceedings.mlr.press/v235/lee24u.html)

**TLDR**: Proposes structured Wasserstein autoencoders to learn invariant latent representations with conditional independence constraints.

## Abstract

Autoencoders have become an indispensable tool for generative modeling and representation learning in high dimensions. Imposing structural constraints such as conditional independence in order to capture invariance of latent variables to nuisance information has been attempted through adding ad hoc penalties to the loss function mostly in the variational autoencoder (VAE) context, often based on heuristics. This paper demonstrates that Wasserstein autoencoders (WAEs) are highly flexible in embracing such structural constraints. Well-known extensions of VAEs for this purpose are gracefully handled within the framework of WAEs. In particular, given a conditional independence structure of the generative model (decoder), corresponding encoder structure and penalties are derived from the functional constraints that define the WAE. These structural uses of WAEs, termed StrWAEs (“stairways”), open up a principled way of penalizing autoencoders to impose structural constraints. Utilizing these advantages, we present handful of results on semi-supervised classification, conditional generation, and invariant representation tasks.