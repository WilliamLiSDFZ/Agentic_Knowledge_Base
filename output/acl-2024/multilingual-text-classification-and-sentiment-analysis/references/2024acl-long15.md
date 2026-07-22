---
title: "A Novel Cartography-Based Curriculum Learning Method Applied on RoNLI: The First Romanian Natural Language Inference Corpus"
source: "https://aclanthology.org/2024.acl-long.15/"
pdf_url: ""
categories: ['multilingual-text-classification-and-sentiment-analysis', 'label-noise-robust-annotation-learning']
tags: ['natural-language-inference', 'curriculum-learning', 'romanian']
venue: "ACL 2024"
tldr: "Presents a cartography-based curriculum learning method alongside RoNLI, the first Romanian natural language inference corpus."
---

# A Novel Cartography-Based Curriculum Learning Method Applied on RoNLI: The First Romanian Natural Language Inference Corpus

**Source**: [https://aclanthology.org/2024.acl-long.15/](https://aclanthology.org/2024.acl-long.15/)

**TLDR**: Presents a cartography-based curriculum learning method alongside RoNLI, the first Romanian natural language inference corpus.

## Abstract

AbstractNatural language inference (NLI), the task of recognizing the entailment relationship in sentence pairs, is an actively studied topic serving as a proxy for natural language understanding. Despite the relevance of the task in building conversational agents and improving text classification, machine translation and other NLP tasks, to the best of our knowledge, there is no publicly available NLI corpus for the Romanian language. To this end, we introduce the first Romanian NLI corpus (RoNLI) comprising 58K training sentence pairs, which are obtained via distant supervision, and 6K validation and test sentence pairs, which are manually annotated with the correct labels. We conduct experiments with multiple machine learning methods based on distant learning, ranging from shallow models based on word embeddings to transformer-based neural networks, to establish a set of competitive baselines. Furthermore, we improve on the best model by employing a new curriculum learning strategy based on data cartography. Our dataset and code to reproduce the baselines are available at https://github.com/Eduard6421/RONLI.