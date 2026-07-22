---
title: "DELL: Generating Reactions and Explanations for LLM-Based Misinformation Detection"
source: "https://aclanthology.org/2024.findings-acl.155/"
pdf_url: ""
categories: ['computational-misinformation-narrative-framing-detection', 'llm-hallucination-detection-and-mitigation']
tags: ['misinformation-detection', 'LLM-reasoning', 'explanation-generation']
venue: "ACL 2024"
tldr: "Proposes DELL, a framework generating reactions and explanations to improve LLM-based misinformation detection accuracy."
---

# DELL: Generating Reactions and Explanations for LLM-Based Misinformation Detection

**Source**: [https://aclanthology.org/2024.findings-acl.155/](https://aclanthology.org/2024.findings-acl.155/)

**TLDR**: Proposes DELL, a framework generating reactions and explanations to improve LLM-based misinformation detection accuracy.

## Abstract

AbstractLarge language models are limited by challenges in factuality and hallucinations to be directly employed off-the-shelf for judging the veracity of news articles, where factual accuracy is paramount. In this work, we propose DELL that identifies three key stages in misinformation detection where LLMs could be incorporated as part of the pipeline: 1) LLMs could generate news reactions to represent diverse perspectives and simulate user-news interaction networks; 2) LLMs could generate explanations for proxy tasks (e.g., sentiment, stance) to enrich the contexts of news articles and produce experts specializing in various aspects of news understanding; 3) LLMs could merge task-specific experts and provide an overall prediction by incorporating the predictions and confidence scores of varying experts. Extensive experiments on seven datasets with three LLMs demonstrate that DELL outperforms state-of-the-art baselines by up to 16.8% in macro f1-score. Further analysis reveals that the generated reactions and explanations are greatly helpful in misinformation detection, while our proposed LLM-guided expert merging helps produce better-calibrated predictions.