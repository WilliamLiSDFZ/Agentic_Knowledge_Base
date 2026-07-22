---
title: "Towards Tracing Trustworthiness Dynamics: Revisiting Pre-training Period of Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.290/"
categories: ['llm-training-alignment-and-evaluation', 'llm-security-robustness-and-detection']
tags: ['trustworthiness', 'pre-training-dynamics', 'llm-safety']
venue: "ACL 2024"
tldr: "Investigates how LLM trustworthiness properties emerge and evolve during the pre-training phase rather than only post-training."
---

# Towards Tracing Trustworthiness Dynamics: Revisiting Pre-training Period of Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.290/](https://aclanthology.org/2024.findings-acl.290/)

**TLDR**: Investigates how LLM trustworthiness properties emerge and evolve during the pre-training phase rather than only post-training.

## Abstract

AbstractEnsuring the trustworthiness of large language models (LLMs) is crucial. Most studies concentrate on fully pre-trained LLMs to better understand and improve LLMs’ trustworthiness. In this paper, to reveal the untapped potential of pre-training, we pioneer the exploration of LLMs’ trustworthiness during this period, focusing on five key dimensions: reliability, privacy, toxicity, fairness, and robustness. To begin with, we apply linear probing to LLMs. The high probing accuracy suggests that LLMs in early pre-training can already distinguish concepts in each trustworthiness dimension. Therefore, to further uncover the hidden possibilities of pre-training, we extract steering vectors from a LLM’s pre-training checkpoints to enhance the LLM’s trustworthiness. Finally, inspired by the theoretical result that mutual information estimation is bounded by linear probing accuracy, we also probe LLMs with mutual information to investigate the dynamics of trustworthiness during pre-training. We are the first to observe a similar two-phase phenomenon: fitting and compression. This research provides an initial exploration of trustworthiness modeling during LLM pre-training, seeking to unveil new insights and spur further developments in the field.