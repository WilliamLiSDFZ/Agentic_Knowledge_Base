---
title: "Learning Adverbs with Spectral Mixture Kernels"
source: "https://aclanthology.org/2024.findings-acl.461/"
pdf_url: ""
categories: ['topic-modeling-and-essay-evaluation']
tags: ['adverbs', 'spectral-mixture-kernels', 'topic-model', 'motion-understanding']
venue: "ACL 2024"
tldr: "A Hierarchical Dirichlet Process model with spectral mixture kernels is proposed to learn adverb meanings from human motion descriptions."
---

# Learning Adverbs with Spectral Mixture Kernels

**Source**: [https://aclanthology.org/2024.findings-acl.461/](https://aclanthology.org/2024.findings-acl.461/)

**TLDR**: A Hierarchical Dirichlet Process model with spectral mixture kernels is proposed to learn adverb meanings from human motion descriptions.

## Abstract

AbstractFor humans and robots to collaborate more in the real world, robots need to understand human intentions from the different manner of their behaviors. In our study, we focus on the meaning of adverbs which describe human motions. We propose a topic model, Hierarchical Dirichlet Process-Spectral Mixture Latent Dirichlet Allocation, which concurrently learns the relationship between those human motions and those adverbs by capturing the frequency kernels that represent motion characteristics and the shared topics of adverbs that depict such motions. We trained the model on datasets we made from movies about “walking” and “dancing”, and found that our model outperforms representative neural network models in terms of perplexity score. We also demonstrate our model’s ability to determine the adverbs for a given motion and confirmed that the model predicts more appropriate adverbs.