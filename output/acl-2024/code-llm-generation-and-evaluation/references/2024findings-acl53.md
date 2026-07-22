---
title: "MARIO: MAth Reasoning with code Interpreter Output - A Reproducible Pipeline"
source: "https://aclanthology.org/2024.findings-acl.53/"
pdf_url: ""
categories: ['code-llm-generation-and-evaluation']
tags: ['mathematical-reasoning', 'code-interpreter', 'pipeline']
venue: "ACL 2024"
tldr: "Presents MARIO, a reproducible pipeline using code interpreter outputs to improve LLM mathematical reasoning."
---

# MARIO: MAth Reasoning with code Interpreter Output - A Reproducible Pipeline

**Source**: [https://aclanthology.org/2024.findings-acl.53/](https://aclanthology.org/2024.findings-acl.53/)

**TLDR**: Presents MARIO, a reproducible pipeline using code interpreter outputs to improve LLM mathematical reasoning.

## Abstract

AbstractLarge language models (LLMs) have significantly improved in understanding natural language but still lack in mathematical reasoning, a hurdle on the path to true artificial general intelligence. The training of large language models, based on next-token prediction, struggles to capture the precise nature of mathematical reasoning, presenting both practical and theoretical challenges. In this paper, we address this challenge by enriching the data landscape and introducing a reasonable data format, enhanced the text analysis of the LLM with a capability to utilize a Python code interpreter. This dataset is derived from GSM8K and MATH and has been further refined through a combination of GPT annotations, human review, and self-training processes. Additionally, we propose a tentative, easily replicable protocol for the fine-tuning of math-specific LLMs, which has led to a significant improvement in the performance of a 7B-parameter LLM on the GSM8K and MATH datasets. A solution generator and a value estimator are fine-tuned simultaneously in a multi-task fashion, while an outlier-free value model-based inference method is proposed to further boost the performance. We are committed to advancing the field of mathematical reasoning in LLMs and, to that end, we will make the source code and checkpoints publicly available.