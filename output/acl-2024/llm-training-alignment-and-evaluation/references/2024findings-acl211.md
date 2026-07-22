---
title: "Lost in the Source Language: How Large Language Models Evaluate the Quality of Machine Translation"
source: "https://aclanthology.org/2024.findings-acl.211/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'multilingual-text-classification-and-sentiment-analysis']
tags: ['machine-translation-evaluation', 'llm-evaluation', 'source-reference-bias']
venue: "ACL 2024"
tldr: "Investigates how LLMs use source and reference data in translation quality evaluation through controlled experiments."
---

# Lost in the Source Language: How Large Language Models Evaluate the Quality of Machine Translation

**Source**: [https://aclanthology.org/2024.findings-acl.211/](https://aclanthology.org/2024.findings-acl.211/)

**TLDR**: Investigates how LLMs use source and reference data in translation quality evaluation through controlled experiments.

## Abstract

AbstractThis study investigates how Large Language Models (LLMs) leverage source and reference data in machine translation evaluation task, aiming to better understand the mechanisms behind their remarkable performance in this task.We design the controlled experiments across various input modes and model types, and employ both coarse-grained and fine-grained prompts to discern the utility of source versus reference information.We find that reference information significantly enhances the evaluation accuracy, while surprisingly, source information sometimes is counterproductive, indicating LLMs’ inability to fully leverage the cross-lingual capability when evaluating translations.Further analysis of the fine-grained evaluation and fine-tuning experiments show similar results.These findings also suggest a potential research direction for LLMs that fully exploits the cross-lingual capability of LLMs to achieve better performance in machine translation evaluation tasks.