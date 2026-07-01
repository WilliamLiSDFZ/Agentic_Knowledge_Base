---
title: "Streaming Bayes GFlowNets"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/2fb57276bfbaf1b832d7bfcba36bb41c-Abstract-Conference.html"
categories: ['diffusion-based-generative-modeling-and-inference']
tags: ['gflownets', 'streaming-inference', 'bayesian-updates', 'posterior-estimation', 'continual-learning']
venue: "NeurIPS 2024"
tldr: "Extends GFlowNets to streaming Bayesian inference, enabling efficient posterior updates as new data arrives without recomputing from scratch."
---

# Streaming Bayes GFlowNets

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/2fb57276bfbaf1b832d7bfcba36bb41c-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/2fb57276bfbaf1b832d7bfcba36bb41c-Abstract-Conference.html)

**TLDR**: Extends GFlowNets to streaming Bayesian inference, enabling efficient posterior updates as new data arrives without recomputing from scratch.

## Abstract

Bayes' rule naturally allows for inference refinement in a streaming fashion, without the need to recompute posteriors from scratch whenever new data arrives. In principle, Bayesian streaming is straightforward: we update our prior with the available data and use the resulting posterior as a prior when processing the next data chunk. In practice, however, this recipe entails i) approximating an intractable posterior at each time step; and ii) encapsulating results appropriately to allow for posterior propagation. For continuous state spaces, variational inference (VI) is particularly convenient due to its scalability and the tractability of variational posteriors, For discrete state spaces, however, state-of-the-art VI results in analytically intractable approximations that are ill-suited for streaming settings. To enable streaming Bayesian inference over discrete parameter spaces, we propose streaming Bayes GFlowNets (abbreviated as SB-GFlowNets) by leveraging the recently proposed GFlowNets --- a powerful class of amortized samplers for discrete compositional objects. Notably, SB-GFlowNet approximates the initial posterior using a standard GFlowNet and subsequently updates it using a tailored procedure that requires only the newly observed data. Our case studies in linear preference learning and phylogenetic inference showcase the effectiveness of SB-GFlowNets in sampling from an unnormalized posterior in a streaming setting. As expected, we also observe that SB-GFlowNets is significantly faster than repeatedly training a GFlowNet from scratch to sample from the full posterior.