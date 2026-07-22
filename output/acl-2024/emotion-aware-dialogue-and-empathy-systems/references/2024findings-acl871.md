---
title: "CAUSE: Counterfactual Assessment of User Satisfaction Estimation in Task-Oriented Dialogue Systems"
source: "https://aclanthology.org/2024.findings-acl.871/"
pdf_url: ""
categories: ['emotion-aware-dialogue-and-empathy-systems', 'nlp-benchmark-design-and-interpretability']
tags: ['task-oriented-dialogue', 'user-satisfaction', 'counterfactual-evaluation']
venue: "ACL 2024"
tldr: "Introduces counterfactual assessment to evaluate robustness of user satisfaction estimation in task-oriented dialogue systems."
---

# CAUSE: Counterfactual Assessment of User Satisfaction Estimation in Task-Oriented Dialogue Systems

**Source**: [https://aclanthology.org/2024.findings-acl.871/](https://aclanthology.org/2024.findings-acl.871/)

**TLDR**: Introduces counterfactual assessment to evaluate robustness of user satisfaction estimation in task-oriented dialogue systems.

## Abstract

AbstractAn important unexplored aspect in previous work on user satisfaction estimation for Task-Oriented Dialogue (TOD) systems is their evaluation in terms of robustness for the identification of user dissatisfaction: current benchmarks for user satisfaction estimation in TOD systems are highly skewed towards dialogues for which the user is satisfied. The effect of having a more balanced set of satisfaction labels on performance is unknown. However, balancing the data with more dissatisfactory dialogue samples requires further data collection and human annotation, which is costly and time-consuming. In this work, we leverage large language models (LLMs) and unlock their ability to generate satisfaction-aware counterfactual dialogues to augment the set of original dialogues of a test collection. We gather human annotations to ensure the reliability of the generated samples. We evaluate two open-source LLMs as user satisfaction estimators on our augmented collection against state-of-the-art fine-tuned models. Our experiments show that when used as few-shot user satisfaction estimators, open-source LLMs show higher robustness to the increase in the number of dissatisfaction labels in the test collection than the fine-tuned state-of-the-art models. Our results shed light on the need for data augmentation approaches for user satisfaction estimation in TOD systems. We release our aligned counterfactual dialogues, which are curated by human annotation, to facilitate further research on this topic.