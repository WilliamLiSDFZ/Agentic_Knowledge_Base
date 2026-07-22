---
title: "Unveiling Imitation Learning: Exploring the impact of Data Falsity to Large Language Model"
source: "https://aclanthology.org/2024.findings-acl.6/"
categories: ['llm-training-alignment-and-evaluation', 'label-noise-robust-annotation-learning']
tags: ['imitation-learning', 'noisy-data', 'synthetic-instructions']
venue: "ACL 2024"
tldr: "This study investigates how data falsity in synthetic instruction datasets from proprietary models negatively affects imitation-learned LLMs."
---

# Unveiling Imitation Learning: Exploring the impact of Data Falsity to Large Language Model

**Source**: [https://aclanthology.org/2024.findings-acl.6/](https://aclanthology.org/2024.findings-acl.6/)

**TLDR**: This study investigates how data falsity in synthetic instruction datasets from proprietary models negatively affects imitation-learned LLMs.

## Abstract

AbstractMany recent studies endeavor to improve open-sourced language models through imitation learning, re-training on the synthetic instruction data from state-of-the-art proprietary models like ChatGPT and GPT-4.However, the innate nature of synthetic data inherently contains noisy data, giving rise to a substantial presence of low-quality data replete with misleading queries, erroneous responses, and flawed reasoning.Although we intuitively grasp the potential harm of noisy data, we lack a quantitative understanding of its impact.To this end, this paper explores correlation between the degree of noise and its impact on language models through instruction tuning.We first introduce the Falsity-Controllable () dataset, which comprises pairs of true answers and corresponding reasoning, as well as false pairs to manually control the factuality ratio of the dataset.Through our extensive experiments, we found multiple intriguing findings of the correlation between factuality and instruction tuning. Specifically, factuality can significantly impact various benchmark characteristics especially when benchmarks are related to knowledge domain, and initial data quality plays a critical role, whereas the number of learning steps has a lesser impact.Additionally, we noted that once the language model is trained with a dataset contaminated by noise, restoring its original performance becomes exceptionally challenging, verging on irreversible.