---
title: "Bringing Motion Taxonomies to Continuous Domains via GPLVM on Hyperbolic manifolds"
source: "https://proceedings.mlr.press/v235/jaquier24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jaquier24a/jaquier24a.pdf"
categories: ['sampling-and-optimization-on-manifolds', '3d-vision-and-scene-understanding']
tags: ['motion-taxonomy', 'GPLVM', 'hyperbolic-manifolds', 'human-motion', 'continuous-domains']
venue: "ICML 2024"
tldr: "This paper lifts discrete human motion taxonomies to continuous hyperbolic manifolds using Gaussian Process Latent Variable Models for richer motion representation."
---

# Bringing Motion Taxonomies to Continuous Domains via GPLVM on Hyperbolic manifolds

**Source**: [https://proceedings.mlr.press/v235/jaquier24a.html](https://proceedings.mlr.press/v235/jaquier24a.html)

**TLDR**: This paper lifts discrete human motion taxonomies to continuous hyperbolic manifolds using Gaussian Process Latent Variable Models for richer motion representation.

## Abstract

Human motion taxonomies serve as high-level hierarchical abstractions that classify how humans move and interact with their environment. They have proven useful to analyse grasps, manipulation skills, and whole-body support poses. Despite substantial efforts devoted to design their hierarchy and underlying categories, their use remains limited. This may be attributed to the lack of computational models that fill the gap between the discrete hierarchical structure of the taxonomy and the high-dimensional heterogeneous data associated to its categories. To overcome this problem, we propose to model taxonomy data via hyperbolic embeddings that capture the associated hierarchical structure. We achieve this by formulating a novel Gaussian process hyperbolic latent variable model that incorporates the taxonomy structure through graph-based priors on the latent space and distance-preserving back constraints. We validate our model on three different human motion taxonomies to learn hyperbolic embeddings that faithfully preserve the original graph structure. We show that our model properly encodes unseen data from existing or new taxonomy categories, and outperforms its Euclidean and VAE-based counterparts. Finally, through proof-of-concept experiments, we show that our model may be used to generate realistic trajectories between the learned embeddings.