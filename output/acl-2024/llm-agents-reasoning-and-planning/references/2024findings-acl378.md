---
title: "ONSEP: A Novel Online Neural-Symbolic Framework for Event Prediction Based on Large Language Model"
source: "https://aclanthology.org/2024.findings-acl.378/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'llm-agents-reasoning-and-planning']
tags: ['temporal-knowledge-graph', 'event-prediction', 'neural-symbolic', 'online-learning', 'llm']
venue: "ACL 2024"
tldr: "Introduces an online neural-symbolic framework combining LLMs with temporal knowledge graph forecasting for improved event prediction."
---

# ONSEP: A Novel Online Neural-Symbolic Framework for Event Prediction Based on Large Language Model

**Source**: [https://aclanthology.org/2024.findings-acl.378/](https://aclanthology.org/2024.findings-acl.378/)

**TLDR**: Introduces an online neural-symbolic framework combining LLMs with temporal knowledge graph forecasting for improved event prediction.

## Abstract

AbstractIn the realm of event prediction, temporal knowledge graph forecasting (TKGF) stands as a pivotal technique. Previous approaches face the challenges of not utilizing experience during testing and relying on a single short-term history, which limits adaptation to evolving data. In this paper, we introduce the Online Neural-Symbolic Event Prediction (ONSEP) framework, which innovates by integrating dynamic causal rule mining (DCRM) and dual history augmented generation (DHAG). DCRM dynamically constructs causal rules from real-time data, allowing for swift adaptation to new causal relationships. In parallel, DHAG merges short-term and long-term historical contexts, leveraging a bi-branch approach to enrich event prediction. Our framework demonstrates notable performance enhancements across diverse datasets, with significant Hit@k (k=1,3,10) improvements, showcasing its ability to augment large language models (LLMs) for event prediction without necessitating extensive retraining. The ONSEP framework not only advances the field of TKGF but also underscores the potential of neural-symbolic approaches in adapting to dynamic data environments.