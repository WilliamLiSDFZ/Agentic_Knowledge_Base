---
title: "Can Large Language Model Summarizers Adapt to Diverse Scientific Communication Goals?"
source: "https://aclanthology.org/2024.findings-acl.508/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'llm-agents-for-scientific-data-tasks']
tags: ['scientific-summarization', 'LLM-controllability', 'stylistic-control', 'content-coverage']
venue: "ACL 2024"
tldr: "This paper investigates LLM controllability for scientific summarization by analyzing stylistic and content factors across different summary types like reviews, abstracts, and lay summaries."
---

# Can Large Language Model Summarizers Adapt to Diverse Scientific Communication Goals?

**Source**: [https://aclanthology.org/2024.findings-acl.508/](https://aclanthology.org/2024.findings-acl.508/)

**TLDR**: This paper investigates LLM controllability for scientific summarization by analyzing stylistic and content factors across different summary types like reviews, abstracts, and lay summaries.

## Abstract

AbstractIn this work, we investigate the controllability of large language models (LLMs) on scientific summarization tasks. We identify key stylistic and content coverage factors that characterize different types of summaries such as paper reviews, abstracts, and lay summaries. By controlling stylistic features, we find that non-fine-tuned LLMs outperform humans in the MuP review generation task, both in terms of similarity to reference summaries and human preferences. Also, we show that we can improve the controllability of LLMs with keyword-based classifier-free guidance (CFG) while achieving lexical overlap comparable to strong fine-tuned baselines on arXiv and PubMed. However, our results also indicate that LLMs cannot consistently generate long summaries with more than 8 sentences. Furthermore, these models exhibit limited capacity to produce highly abstractive lay summaries. Although LLMs demonstrate strong generic summarization competency, sophisticated content control without costly fine-tuning remains an open problem for domain-specific applications.