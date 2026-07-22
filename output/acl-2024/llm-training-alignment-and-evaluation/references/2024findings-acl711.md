---
title: "Prompting open-source and commercial language models for grammatical error correction of English learner text"
source: "https://aclanthology.org/2024.findings-acl.711/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'nlp-for-asian-languages']
tags: ['grammatical-error-correction', 'LLM-prompting', 'English-learner-text']
venue: "ACL 2024"
tldr: "Evaluates open-source and commercial LLMs prompted for grammatical error correction of English learner text."
---

# Prompting open-source and commercial language models for grammatical error correction of English learner text

**Source**: [https://aclanthology.org/2024.findings-acl.711/](https://aclanthology.org/2024.findings-acl.711/)

**TLDR**: Evaluates open-source and commercial LLMs prompted for grammatical error correction of English learner text.

## Abstract

AbstractThanks to recent advances in generative AI, we are able to prompt large language models (LLMs) to produce texts which are fluent and grammatical. In addition, it has been shown that we can elicit attempts at grammatical error correction (GEC) from LLMs when prompted with ungrammatical input sentences. We evaluate how well LLMs can perform at GEC by measuring their performance on established benchmark datasets. We go beyond previous studies, which only examined GPT* models on a selection of English GEC datasets, by evaluating seven open-source and three commercial LLMs on four established GEC benchmarks. We investigate model performance and report results against individual error types. Our results indicate that LLMs do not always outperform supervised English GEC models except in specific contexts – namely commercial LLMs on benchmarks annotated with fluency corrections as opposed to minimal edits. We find that several open-source models outperform commercial ones on minimal edit benchmarks, and that in some settings zero-shot prompting is just as competitive as few-shot prompting.