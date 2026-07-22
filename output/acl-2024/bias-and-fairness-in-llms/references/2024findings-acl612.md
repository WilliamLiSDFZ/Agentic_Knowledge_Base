---
title: "Debiasing Large Language Models with Structured Knowledge"
source: "https://aclanthology.org/2024.findings-acl.612/"
pdf_url: ""
categories: ['bias-and-fairness-in-llms', 'llm-training-alignment-and-evaluation']
tags: ['debiasing', 'structured-knowledge', 'llm-fairness']
venue: "ACL 2024"
tldr: "Proposes a structured knowledge-based debiasing framework to reduce social biases in large language models during inference."
---

# Debiasing Large Language Models with Structured Knowledge

**Source**: [https://aclanthology.org/2024.findings-acl.612/](https://aclanthology.org/2024.findings-acl.612/)

**TLDR**: Proposes a structured knowledge-based debiasing framework to reduce social biases in large language models during inference.

## Abstract

AbstractDue to biases inherently present in data for pre-training, current pre-trained Large Language Models (LLMs) also ubiquitously manifest the same phenomena. Since the bias influences the output from the LLMs across various tasks, the widespread deployment of the LLMs is hampered. We propose a simple method that utilizes structured knowledge to alleviate this issue, aiming to reduce the bias embedded within the LLMs and ensuring they have an encompassing perspective when used in applications. Experimental results indicated that our method has good debiasing ability when applied to existing both autoregressive and masked language models. Additionally, it could ensure that the performances of LLMs on downstream tasks remain uncompromised.Our method outperforms state-of-the-art (SOTA) baselines in the debiasing ability. Importantly, our method obviates the need for training from scratch, thus offering enhanced scalability and cost-effectiveness.