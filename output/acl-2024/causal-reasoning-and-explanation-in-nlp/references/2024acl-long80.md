---
title: "Transitive Consistency Constrained Learning for Entity-to-Entity Stance Detection"
source: "https://aclanthology.org/2024.acl-long.80/"
categories: ['natural-language-processing-information-extraction', 'causal-reasoning-and-explanation-in-nlp']
tags: ['stance-detection', 'entity-to-entity', 'transitive-consistency', 'sentiment-analysis', 'graph']
venue: "ACL 2024"
tldr: "Introduces transitive consistency constraints for entity-to-entity stance detection to improve polarity prediction across entity pairs."
---

# Transitive Consistency Constrained Learning for Entity-to-Entity Stance Detection

**Source**: [https://aclanthology.org/2024.acl-long.80/](https://aclanthology.org/2024.acl-long.80/)

**TLDR**: Introduces transitive consistency constraints for entity-to-entity stance detection to improve polarity prediction across entity pairs.

## Abstract

AbstractEntity-to-entity stance detection identifies the stance between a pair of entities with a directed link that indicates the source, target and polarity. It is a streamlined task without the complex dependency structure for structural sentiment analysis, while it is more informative compared to most previous work assuming that the source is the author. Previous work performs entity-to-entity stance detection training on individual entity pairs. However, stances between inter-connected entity pairs may be correlated. In this paper, we propose transitive consistency constrained learning, which first finds connected entity pairs and their stances, and adds an additional objective to enforce the transitive consistency. We explore consistency training on both classification-based and generation-based models and conduct experiments to compare consistency training with previous work and large language models with in-context learning. Experimental results illustrate that the inter-correlation of stances in political news can be used to improve the entity-to-entity stance detection model, while overly strict consistency enforcement may have a negative impact. In addition, we find that large language models struggle with predicting link direction and neutral labels in this task.