---
title: "Knowledge of Knowledge: Exploring Known-Unknowns Uncertainty with Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.383/"
categories: ['llm-hallucination-detection-and-mitigation', 'llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['known-unknowns', 'uncertainty-estimation', 'LLM-self-knowledge']
venue: "ACL 2024"
tldr: "Explores LLMs' ability to recognize and reason about questions they cannot answer due to inherent knowledge uncertainty."
---

# Knowledge of Knowledge: Exploring Known-Unknowns Uncertainty with Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.383/](https://aclanthology.org/2024.findings-acl.383/)

**TLDR**: Explores LLMs' ability to recognize and reason about questions they cannot answer due to inherent knowledge uncertainty.

## Abstract

AbstractThis paper investigates the capabilities of Large Language Models (LLMs) in understanding their knowledge and uncertainty over questions. Specifically, we focus on addressing known-unknown questions, characterized by high uncertainty due to the absence of definitive answers. To facilitate our study, we collect a new dataset with Known-Unknown Questions (KUQ) and establish a categorization framework to clarify the origins of uncertainty in such queries. Subsequently, we examine the performance of open-source LLMs, fine-tuned using this dataset, in distinguishing between known and unknown queries within open-ended question-answering scenarios. The fine-tuned models demonstrated a significant improvement, achieving a considerable increase in F1-score relative to their pre-fine-tuning state. Through a comprehensive analysis, we reveal insights into the models’ improved uncertainty articulation and their consequent efficacy in multi-agent debates. These findings help us understand how LLMs can be trained to identify and express uncertainty, improving our knowledge of how they understand and express complex or unclear information.