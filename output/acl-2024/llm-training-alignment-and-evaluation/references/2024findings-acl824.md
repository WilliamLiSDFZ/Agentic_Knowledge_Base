---
title: "Towards Demonstration-Aware Large Language Models for Machine Translation"
source: "https://aclanthology.org/2024.findings-acl.824/"
pdf_url: ""
categories: ['multilingual-text-classification-and-sentiment-analysis', 'llm-training-alignment-and-evaluation']
tags: ['machine-translation', 'in-context-learning', 'LLMs']
venue: "ACL 2024"
tldr: "A demonstration-aware tuning approach improves large language models' ability to leverage translation examples at inference."
---

# Towards Demonstration-Aware Large Language Models for Machine Translation

**Source**: [https://aclanthology.org/2024.findings-acl.824/](https://aclanthology.org/2024.findings-acl.824/)

**TLDR**: A demonstration-aware tuning approach improves large language models' ability to leverage translation examples at inference.

## Abstract

AbstractTuning-based large language models for machine translation (aka large translation model, LTM) have demonstrated significant performance in the field of machine translation. Despite their success, these models often face difficulties in leveraging demonstrations to further improve their performance. To tackle this challenge, we introduce a novel approach that integrates demonstration-aware training and inference strategies within the framework of tuning-based LTMs, hereby referred to as demonstration-aware LTMs. During training, we enrich the model’s learning process by incorporating both sentence- and document-level demonstrations derived from its original training dataset. During inference, the model synergizes its own contextual translations with retrieved high-quality demonstrations, leading to more precise and contextually appropriate outputs. Empirical results reveal that our demonstration-aware LTM not only mitigates the negative impacts traditionally associated with demonstrations but also secures substantial improvements in translation accuracy, particularly in domain-specific and document-level translation tasks. Source code and scripts are freely available at https://github.com/ChenLi0620/Demo-Aware-LLM-MT.