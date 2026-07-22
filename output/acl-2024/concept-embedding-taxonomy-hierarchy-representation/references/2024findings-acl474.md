---
title: "Ranking Entities along Conceptual Space Dimensions with LLMs: An Analysis of Fine-Tuning Strategies"
source: "https://aclanthology.org/2024.findings-acl.474/"
pdf_url: ""
categories: ['concept-embedding-taxonomy-hierarchy-representation', 'language-model-representations-and-embedding-spaces']
tags: ['conceptual-spaces', 'LLM', 'fine-tuning', 'entity-ranking', 'semantic-features']
venue: "ACL 2024"
tldr: "This paper analyzes fine-tuning strategies for distilling conceptual space dimensions from LLMs to rank entities along perceptual and subjective semantic features."
---

# Ranking Entities along Conceptual Space Dimensions with LLMs: An Analysis of Fine-Tuning Strategies

**Source**: [https://aclanthology.org/2024.findings-acl.474/](https://aclanthology.org/2024.findings-acl.474/)

**TLDR**: This paper analyzes fine-tuning strategies for distilling conceptual space dimensions from LLMs to rank entities along perceptual and subjective semantic features.

## Abstract

AbstractConceptual spaces represent entities in terms of their primitive semantic features. Such representations are highly valuable but they are notoriously difficult to learn, especially when it comes to modelling perceptual and subjective features. Distilling conceptual spaces from Large Language Models (LLMs) has recently emerged as a promising strategy, but existing work has been limited to probing pre-trained LLMs using relatively simple zero-shot strategies. We focus in particular on the task of ranking entities according to a given conceptual space dimension. Unfortunately, we cannot directly fine-tune LLMs on this task, because ground truth rankings for conceptual space dimensions are rare. We therefore use more readily available features as training data and analyse whether the ranking capabilities of the resulting models transfer to perceptual and subjective features. We find that this is indeed the case, to some extent, but having at least some perceptual and subjective features in the training data seems essential for achieving the best results.