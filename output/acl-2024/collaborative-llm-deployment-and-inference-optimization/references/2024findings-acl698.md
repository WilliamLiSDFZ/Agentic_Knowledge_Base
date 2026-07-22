---
title: "Knowledge Fusion By Evolving Weights of Language Models"
source: "https://aclanthology.org/2024.findings-acl.698/"
categories: ['collaborative-llm-deployment-and-inference-optimization']
tags: ['model-merging', 'knowledge-fusion', 'weight-evolution']
venue: "ACL 2024"
tldr: "Proposes a method for fusing multiple fine-tuned language models by evolving their weights to combine domain knowledge."
---

# Knowledge Fusion By Evolving Weights of Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.698/](https://aclanthology.org/2024.findings-acl.698/)

**TLDR**: Proposes a method for fusing multiple fine-tuned language models by evolving their weights to combine domain knowledge.

## Abstract

AbstractFine-tuning pre-trained language models, particularly large language models, demands extensive computing resources and can result in varying performance outcomes across different domains and datasets. This paper examines the approach of integrating multiple models from diverse training scenarios into a unified model. This unified model excels across various data domains and exhibits the ability to generalize well on out-of-domain data. We propose a knowledge fusion method named Evolver, inspired by evolutionary algorithms, which does not need further training or additional training data. Specifically, our method involves aggregating the weights of different language models into a population and subsequently generating offspring models through mutation and crossover operations. These offspring models are then evaluated against their parents, allowing for the preservation of those models that show enhanced performance on development datasets. Importantly, our model evolving strategy can be seamlessly integrated with existing model merging frameworks, offering a versatile tool for model enhancement. Experimental results on mainstream language models (i.e., encoder-only, decoder-only, encoder-decoder) reveal that Evolver outperforms previous state-of-the-art models by large margins.