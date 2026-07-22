---
title: "Non-compositional Expression Generation and its Continual Learning"
source: "https://aclanthology.org/2024.findings-acl.166/"
categories: ['continual-learning-for-nlp-tasks', 'moral-figurative-language-nlp-analysis']
tags: ['non-compositional-expressions', 'idioms', 'continual-learning']
venue: "ACL 2024"
tldr: "Investigates generation of non-compositional expressions and proposes continual learning methods to handle their evolving nature."
---

# Non-compositional Expression Generation and its Continual Learning

**Source**: [https://aclanthology.org/2024.findings-acl.166/](https://aclanthology.org/2024.findings-acl.166/)

**TLDR**: Investigates generation of non-compositional expressions and proposes continual learning methods to handle their evolving nature.

## Abstract

AbstractNon-compositional expressions are an integral part of natural language and their meanings cannot be directly derived from the meanings of their component words. Recent work has shown how their processing remains a challenge for pre-trained language models. Here we consider the fact that prior knowledge of their component words is inadequate to infer their meaning as a whole and that these expressions constitute a long-tailed process in language (based on their occurrence in corpora and their coming into use as an idiomatic expression in a continual manner). Against this backdrop, this paper studies the ability of recent pre-trained language models to generate non-compositional expressions in English and their continual learning. Formulating this as a mask infilling task termed as CLoNE, the study uncovers the combined challenges of non-compositionality and their continual learning. Using a set of three diverse idiomatic expression datasets repurposed for this task, we benchmark different large pre-trained language models and different continual learning methods on the task of non-compositional expression generation. Our experiments on the CLoNE task show that large pre-trained language models are limited in their ability to generate non-compositional expressions and available continual learning methods are inadequate for our proposed CLoNE task which calls for more effective methods for continual learning of non-compositionality. Our datasets and code will be released publicly upon acceptance.