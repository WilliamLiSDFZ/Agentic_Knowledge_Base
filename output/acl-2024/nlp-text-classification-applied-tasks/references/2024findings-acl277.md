---
title: "SPIN: Sparsifying and Integrating Internal Neurons in Large Language Models for Text Classification"
source: "https://aclanthology.org/2024.findings-acl.277/"
pdf_url: ""
categories: ['nlp-text-classification-applied-tasks', 'language-model-representations-and-embedding-spaces']
tags: ['text-classification', 'internal-neurons', 'sparsification', 'LLM', 'representation']
venue: "ACL 2024"
tldr: "Proposes SPIN, a method that sparsifies and integrates internal neuron representations from LLMs to improve text classification."
---

# SPIN: Sparsifying and Integrating Internal Neurons in Large Language Models for Text Classification

**Source**: [https://aclanthology.org/2024.findings-acl.277/](https://aclanthology.org/2024.findings-acl.277/)

**TLDR**: Proposes SPIN, a method that sparsifies and integrates internal neuron representations from LLMs to improve text classification.

## Abstract

AbstractAmong the many tasks that Large Language Models (LLMs) have revolutionized is text classification. Current text classification paradigms, however, rely solely on the output of the final layer in the LLM, with the rich information contained in internal neurons largely untapped. In this study, we present SPIN: a model-agnostic framework that sparsifies and integrates internal neurons of intermediate layers of LLMs for text classification. Specifically, SPIN sparsifies internal neurons by linear probing-based salient neuron selection layer by layer, avoiding noise from unrelated neurons and ensuring efficiency. The cross-layer salient neurons are then integrated to serve as multi-layered features for the classification head. Extensive experimental results show our proposed SPIN significantly improves text classification accuracy, efficiency, and interpretability.