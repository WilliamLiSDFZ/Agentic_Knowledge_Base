---
title: "Progressive Tuning: Towards Generic Sentiment Abilities for Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.855/"
pdf_url: ""
categories: ['multilingual-text-classification-and-sentiment-analysis', 'llm-training-alignment-and-evaluation']
tags: ['sentiment-analysis', 'progressive-tuning', 'llm', 'multitask', 'aspect-based-sentiment']
venue: "ACL 2024"
tldr: "Proposes progressive tuning to develop generic and interrelated sentiment capabilities across multiple subtasks in large language models."
---

# Progressive Tuning: Towards Generic Sentiment Abilities for Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.855/](https://aclanthology.org/2024.findings-acl.855/)

**TLDR**: Proposes progressive tuning to develop generic and interrelated sentiment capabilities across multiple subtasks in large language models.

## Abstract

AbstractUnderstanding sentiment is arguably an advanced and important capability of AI agents in the physical world. In previous works, many efforts have been devoted to individual sentiment subtasks, without considering interrelated sentiment knowledge among these subtasks. Although some recent works model multiple sentiment subtasks in a unified manner, they merely simply combine these subtasks without deeply exploring the hierarchical relationships among subtasks. In this paper, we introduce GSA-7B, an open-source large language model specific to the sentiment domain. Specifically, we deeply explore the hierarchical relationships between sentiment subtasks, proposing progressive sentiment reasoning benchmark and progressive task instructions. Subsequently, we use Llama2-7B as the backbone model and propose parameter-efficient progressive tuning paradigm which is implemented by constructing chain of LoRA, resulting in the creation of GSA-7B. Experimental results show that GSA-7B as a unified model performs well across all datasets in the progressive sentiment reasoning benchmark. Additionally, under the few-shot setting, GSA-7B also exhibits good generalization ability for sentiment subtasks and datasets that were not encountered during its training phase.