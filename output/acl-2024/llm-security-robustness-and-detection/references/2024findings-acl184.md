---
title: "A Chinese Dataset for Evaluating the Safeguards in Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.184/"
pdf_url: ""
categories: ['llm-security-robustness-and-detection', 'collaborative-llm-deployment-and-inference-optimization']
tags: ['LLM-safety', 'Chinese-dataset', 'harmful-content']
venue: "ACL 2024"
tldr: "Constructs a Chinese dataset to systematically evaluate safety safeguards and harmful response tendencies in large language models."
---

# A Chinese Dataset for Evaluating the Safeguards in Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.184/](https://aclanthology.org/2024.findings-acl.184/)

**TLDR**: Constructs a Chinese dataset to systematically evaluate safety safeguards and harmful response tendencies in large language models.

## Abstract

AbstractMany studies have demonstrated that large language models (LLMs) can produce harmful responses, exposing users to unexpected risks. Previous studies have proposed comprehensive taxonomies of LLM risks, as well as corresponding prompts that can be used to examine LLM safety. However, the focus has been almost exclusively on English. We aim to broaden LLM safety research by introducing a dataset for the safety evaluation of Chinese LLMs, and extending it to better identify false negative and false positive examples in terms of risky prompt rejections. We further present a set of fine-grained safety assessment criteria for each risk type, facilitating both manual annotation and automatic evaluation in terms of LLM response harmfulness. Our experiments over five LLMs show that region-specific risks are the prevalent risk type. Warning: this paper contains example data that may be offensive, harmful, or biased. Our data is available at https://github.com/Libr-AI/do-not-answer.