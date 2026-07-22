---
title: "ZeroStance: Leveraging ChatGPT for Open-Domain Stance Detection via Dataset Generation"
source: "https://aclanthology.org/2024.findings-acl.794/"
categories: ['computational-misinformation-narrative-framing-detection']
tags: ['stance-detection', 'zero-shot', 'dataset-generation']
venue: "ACL 2024"
tldr: "ZeroStance leverages ChatGPT to generate datasets for open-domain zero-shot stance detection across diverse targets."
---

# ZeroStance: Leveraging ChatGPT for Open-Domain Stance Detection via Dataset Generation

**Source**: [https://aclanthology.org/2024.findings-acl.794/](https://aclanthology.org/2024.findings-acl.794/)

**TLDR**: ZeroStance leverages ChatGPT to generate datasets for open-domain zero-shot stance detection across diverse targets.

## Abstract

AbstractZero-shot stance detection that aims to detect the stance (typically against, favor, or neutral) towards unseen targets has attracted considerable attention. However, most previous studies only focus on targets from a single or limited text domains (e.g., financial domain), and thus zero-shot models cannot generalize well to unseen targets of diverse domains (e.g., political domain). In this paper, we consider a more realistic task, i.e., open-domain stance detection, which aims at training a model that is able to generalize well to unseen targets across multiple domains of interest. Particularly, we propose a novel dataset generation method ZeroStance, which leverages ChatGPT to construct a synthetic open-domain dataset CHATStance that covers a wide range of domains. We then train an open-domain model on our synthetic dataset after proper data filtering. Extensive results indicate that our model, when trained on this synthetic dataset, shows superior generalization to unseen targets of diverse domains over baselines on most benchmarks. Our method requires only a task description in the form of a prompt and is much more cost-effective and data-efficient than previous methods. We will release our code and data to facilitate future research.