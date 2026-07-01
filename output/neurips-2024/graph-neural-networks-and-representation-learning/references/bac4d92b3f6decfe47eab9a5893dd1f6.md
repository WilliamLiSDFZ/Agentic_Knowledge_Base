---
title: "Graph-based Unsupervised Disentangled Representation Learning via Multimodal Large Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/bac4d92b3f6decfe47eab9a5893dd1f6-Abstract-Conference.html"
categories: ['disentangled-representation-learning-cognitive-diagnosis', 'graph-neural-networks-and-representation-learning']
tags: ['disentangled-representation', 'graph-based', 'multimodal-LLM', 'unsupervised', 'semantic-factors']
venue: "NeurIPS 2024"
tldr: "Proposes a graph-based disentangled representation learning method using multimodal LLMs to relax the unrealistic statistical independence assumption among semantic factors."
---

# Graph-based Unsupervised Disentangled Representation Learning via Multimodal Large Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/bac4d92b3f6decfe47eab9a5893dd1f6-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/bac4d92b3f6decfe47eab9a5893dd1f6-Abstract-Conference.html)

**TLDR**: Proposes a graph-based disentangled representation learning method using multimodal LLMs to relax the unrealistic statistical independence assumption among semantic factors.

## Abstract

Disentangled representation learning (DRL) aims to identify and decompose underlying factors behind observations, thus facilitating data perception and generation. However, current DRL approaches often rely on the unrealistic assumption that semantic factors are statistically independent. In reality, these factors may exhibit correlations, which off-the-shelf solutions have yet to properly address. To tackle this challenge, we introduce a bidirectional weighted graph-based framework, to learn factorized attributes and their interrelations within complex data. Specifically, we propose a $\beta$-VAE based module to extract factors as the initial nodes of the graph, and leverage the multimodal large language model (MLLM) to discover and rank latent correlations, thereby updating the weighted edges. By integrating these complementary modules, our model successfully achieves fine-grained, practical and unsupervised disentanglement. Experiments demonstrate our method's superior performance in disentanglement and reconstruction. Furthermore, the model inherits enhanced interpretability and generalizability from MLLMs.