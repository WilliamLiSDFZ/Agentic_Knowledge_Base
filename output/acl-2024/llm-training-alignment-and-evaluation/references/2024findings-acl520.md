---
title: "Error Analysis Prompting Enables Human-Like Translation Evaluation in Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.520/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation']
tags: ['machine-translation-evaluation', 'error-analysis', 'prompting', 'llm-evaluation']
venue: "ACL 2024"
tldr: "Proposes error analysis prompting to enable LLMs to perform human-like machine translation quality evaluation."
---

# Error Analysis Prompting Enables Human-Like Translation Evaluation in Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.520/](https://aclanthology.org/2024.findings-acl.520/)

**TLDR**: Proposes error analysis prompting to enable LLMs to perform human-like machine translation quality evaluation.

## Abstract

AbstractGenerative large language models (LLMs), e.g., ChatGPT, have demonstrated remarkable proficiency across several NLP tasks, such as machine translation, text summarization. Recent research (Kocmi and Federmann, 2023) has shown that utilizing LLMs for assessing the quality of machine translation (MT) achieves state-of-the-art performance at the system level but performs poorly at the segment level. To further improve the performance of LLMs on MT quality assessment, we conduct an investigation into several prompting designs, and propose a new prompting method called Error Analysis Prompting (EAPrompt) by combining Chain-of-Thoughts (Wei et al., 2022) and Error Analysis (Lu et al., 2023). This technique emulates the commonly accepted human evaluation framework - Multidimensional Quality Metrics (MQM, Freitag et al., (2021)) and produces explainable and reliable MT evaluations at both the system and segment level. Experimental Results from WMT22 metrics shared task validate the effectiveness of EAPrompt on various LLMs, with different structures. Further analysis confirms that EAPrompt effectively distinguishes major errors from minor ones, while also sharing a similar distribution of the number of errors with MQM. These findings highlight the potential of EAPrompt as a human-like evaluator prompting technique for MT evaluation. We will release our code and scripts to facilitate the community.