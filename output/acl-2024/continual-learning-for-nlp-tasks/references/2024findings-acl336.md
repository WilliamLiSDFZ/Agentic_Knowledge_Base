---
title: "XMC-Agent : Dynamic Navigation over Scalable Hierarchical Index for Incremental Extreme Multi-label Classification"
source: "https://aclanthology.org/2024.findings-acl.336/"
categories: ['hierarchical-text-classification-methods', 'continual-learning-for-nlp-tasks']
tags: ['extreme-multi-label-classification', 'hierarchical-index', 'llm-agent']
venue: "ACL 2024"
tldr: "XMC-Agent uses dynamic navigation over a scalable hierarchical index to handle incremental extreme multi-label classification with LLM-based agents."
---

# XMC-Agent : Dynamic Navigation over Scalable Hierarchical Index for Incremental Extreme Multi-label Classification

**Source**: [https://aclanthology.org/2024.findings-acl.336/](https://aclanthology.org/2024.findings-acl.336/)

**TLDR**: XMC-Agent uses dynamic navigation over a scalable hierarchical index to handle incremental extreme multi-label classification with LLM-based agents.

## Abstract

AbstractThe eXtreme Multi-label Classification (XMC) aims at accurately assigning large-scale labels to instances, and is challenging for learning, managing, and predicting over the large-scale and rapidly growing set of labels. Traditional XMC methods, like one-vs-all and tree-based methods struggle with the growing set of labels due to their static label assumptions, and embedding-based methods struggle with the complex mapping relationships due to their late-interaction paradigm. In this paper, we propose a large language model (LLM) powered agent framework for extreme multi-label classification – XMC-Agent, which can effectively learn, manage and predict the extremely large and dynamically increasing set of labels. Specifically, XMC-Agent models the extreme multi-label classification task as a dynamic navigation problem, employing a scalable hierarchical label index to effectively manage the unified label space. Additionally, we propose two algorithms to enhance the dynamic navigation capabilities of XMC-Agent: a self-construction algorithm for building the scalable hierarchical index, and an iterative feedback learning algorithm for adjusting the agent to specific tasks. Experiments show that XMC-Agentachieves the state-of-the-art performance on three standard datasets.