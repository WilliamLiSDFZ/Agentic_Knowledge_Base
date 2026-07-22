---
title: "Discovering influential text using convolutional neural networks"
source: "https://aclanthology.org/2024.findings-acl.714/"
categories: ['language-technology-cultural-linguistic-diversity', 'topic-modeling-and-essay-evaluation']
tags: ['convolutional-neural-networks', 'influential-text', 'causal-text-effects']
venue: "ACL 2024"
tldr: "Uses CNNs to discover influential text patterns and estimate their causal impacts on human evaluation."
---

# Discovering influential text using convolutional neural networks

**Source**: [https://aclanthology.org/2024.findings-acl.714/](https://aclanthology.org/2024.findings-acl.714/)

**TLDR**: Uses CNNs to discover influential text patterns and estimate their causal impacts on human evaluation.

## Abstract

AbstractExperimental methods for estimating the impacts of text on human evaluation have been widely used in the social sciences. However, researchers in experimental settings are usually limited to testing a small number of pre-specified text treatments. While efforts to mine unstructured texts for features that causally affect outcomes have been ongoing in recent years, these models have primarily focused on the topics or specific words of text, which may not always be the mechanism of the effect. We connect these efforts with NLP interpretability techniques and present a method for flexibly discovering clusters of similar text phrases that are predictive of human reactions to texts using convolutional neural networks. When used in an experimental setting, this method can identify text treatments and their effects under certain assumptions. We apply the method to two data sets. The first enables direct validation of the model’s ability to detect phrases known to cause the outcome. The second demonstrates its ability to flexibly discover text treatments with varying textual structures. In both cases, the model learns a greater variety of text treatments compared to benchmark methods, and these text features quantitatively meet or exceed the ability of benchmark methods to predict the outcome.