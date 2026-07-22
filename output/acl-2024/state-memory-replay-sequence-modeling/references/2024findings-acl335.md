---
title: "On the Relationship Between RNN Hidden-State Vectors and Semantic Structures"
source: "https://aclanthology.org/2024.findings-acl.335/"
pdf_url: ""
categories: ['language-model-representations-and-embedding-spaces', 'state-memory-replay-sequence-modeling']
tags: ['rnn-hidden-states', 'semantic-clustering', 'representation-analysis']
venue: "ACL 2024"
tldr: "Empirically examines the clustering hypothesis for RNN hidden-state vectors and its relationship to semantic structure."
---

# On the Relationship Between RNN Hidden-State Vectors and Semantic Structures

**Source**: [https://aclanthology.org/2024.findings-acl.335/](https://aclanthology.org/2024.findings-acl.335/)

**TLDR**: Empirically examines the clustering hypothesis for RNN hidden-state vectors and its relationship to semantic structure.

## Abstract

AbstractWe examine the assumption that hidden-state vectors of recurrent neural networks (RNNs) tend to form clusters of semantically similar vectors, which we dub the clustering hypothesis. While this hypothesis has been assumed in RNN analyses in recent years, its validity has not been studied thoroughly on modern RNN architectures. We first consider RNNs that were trained to recognize regular languages. This enables us to draw on perfect ground-truth automata in our evaluation, against which we can compare the RNN’s accuracy and the distribution of the hidden-state vectors. Then, we consider context-free languages to examine if RNN states form clusters for more expressive languages.For our analysis, we fit (generalized) linear models to classify RNN states into automata states and we apply different unsupervised clustering techniques. With a new ambiguity score, derived from information entropy, we measure how well an abstraction function maps the hidden state vectors to abstract clusters. Our evaluation supports the validity of the clustering hypothesis for regular languages, especially if RNNs are well-trained, i.e., clustering techniques succeed in finding clusters of similar state vectors. However, the clustering accuracy decreases substantially for context-free languages. This suggests that clustering is not a reliable abstraction technique for RNNs used in tasks like natural language processing.