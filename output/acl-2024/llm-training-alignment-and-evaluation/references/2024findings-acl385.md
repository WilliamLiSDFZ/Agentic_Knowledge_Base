---
title: "Better Synthetic Data by Retrieving and Transforming Existing Datasets"
source: "https://aclanthology.org/2024.findings-acl.385/"
categories: ['llm-training-alignment-and-evaluation', 'nlp-text-classification-applied-tasks']
tags: ['synthetic-data', 'data-augmentation', 'retrieval-based']
venue: "ACL 2024"
tldr: "Proposes a method to generate better synthetic training data by retrieving and transforming existing datasets for NLP tasks."
---

# Better Synthetic Data by Retrieving and Transforming Existing Datasets

**Source**: [https://aclanthology.org/2024.findings-acl.385/](https://aclanthology.org/2024.findings-acl.385/)

**TLDR**: Proposes a method to generate better synthetic training data by retrieving and transforming existing datasets for NLP tasks.

## Abstract

AbstractDespite recent advances in large language models, building dependable and deployable NLP models typically requires abundant, high-quality training data. However, task-specific data is not available for many use cases, and manually curating task-specific data is labor-intensive. Recent work has studied prompt-driven synthetic data generation using large language models, but these generated datasets tend to lack complexity and diversity. To address these limitations, we introduce a method, _DataTune_, to make better use of existing, publicly available datasets to improve automatic dataset generation. DataTune performs _dataset transformation_, enabling the repurposing of publicly available datasets into a format that is directly aligned with the specific requirements of target tasks. On a diverse set of language-based tasks from the BIG-Bench benchmark, we find that finetuning language models via DataTune improves over a few-shot prompting baseline by 49% and improves over existing methods that use synthetic or retrieved training data by 34%. We find that dataset transformation significantly increases the diversity and difficulty of generated data on many tasks. We release a Python package and open-source repository to make this method accessible to the community (URL will be added upon acceptance).