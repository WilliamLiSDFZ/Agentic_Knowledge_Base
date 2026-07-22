---
title: "Debiasing In-Context Learning by Instructing LLMs How to Follow Demonstrations"
source: "https://aclanthology.org/2024.findings-acl.430/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'bias-and-fairness-in-llms']
tags: ['in-context-learning', 'demonstration-bias', 'debiasing', 'llm', 'few-shot']
venue: "ACL 2024"
tldr: "This paper proposes an instruction-based method to debias LLMs in in-context learning by teaching them how to properly follow demonstrations."
---

# Debiasing In-Context Learning by Instructing LLMs How to Follow Demonstrations

**Source**: [https://aclanthology.org/2024.findings-acl.430/](https://aclanthology.org/2024.findings-acl.430/)

**TLDR**: This paper proposes an instruction-based method to debias LLMs in in-context learning by teaching them how to properly follow demonstrations.

## Abstract

AbstractIn-context learning(ICL) has gained considerable attention due to its data efficiency and task adaptability. Unfortunately, ICL suffers from the demonstration bias, i.e., its performance and robustness are severely affected by the selection and ordering of demonstrations. In this paper, we identify that such demonstration bias may primarily stem from the semantic ambiguity induced by demonstrations, i.e., a demonstration may indicate multiple input-to-label mappings and its mapping can be interpreted differently in different contexts by LLMs. Such semantic ambiguity disrupts task comprehension during ICL and results in performance fluctuations. To resolve the semantic ambiguity problem, this paper further proposes two de-biasing strategies to mitigate demonstration bias in in-context learning. Experiments on six datasets show that our methods can effectively alleviate demonstration bias and significantly improve task performance.