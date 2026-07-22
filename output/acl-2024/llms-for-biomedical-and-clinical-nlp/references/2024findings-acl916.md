---
title: "Knowledge-Infused Prompting: Assessing and Advancing Clinical Text Data Generation with Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.916/"
pdf_url: ""
categories: ['llms-for-biomedical-and-clinical-nlp', 'llm-training-alignment-and-evaluation']
tags: ['clinical-NLP', 'data-generation', 'knowledge-infused', 'LLM-prompting', 'privacy']
venue: "ACL 2024"
tldr: "Knowledge-infused prompting improves LLM-based clinical text data generation while addressing privacy and resource constraints."
---

# Knowledge-Infused Prompting: Assessing and Advancing Clinical Text Data Generation with Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.916/](https://aclanthology.org/2024.findings-acl.916/)

**TLDR**: Knowledge-infused prompting improves LLM-based clinical text data generation while addressing privacy and resource constraints.

## Abstract

AbstractClinical natural language processing faces challenges like complex medical terminology and clinical contexts. Recently, large language models (LLMs) have shown promise in this domain. Yet, their direct deployment can lead to privacy issues and are constrained by resources. To address this challenge, we delve into synthetic clinical text generation with LLMs for clinical NLP tasks. We propose an innovative, resource-efficient approach, ClinGen, which infuses knowledge into the process. Our model involves clinical knowledge extraction and context-informed LLM prompting. Both clinical topics and writing styles are drawn from external domain-specific knowledge graphs and LLMs to guide data generation. Our extensive empirical study across 8 clinical NLP tasks and 18 datasets reveals that ClinGen consistently enhances performance across various tasks by 7.7%-8.7% on average, effectively aligning the distribution of real datasets and enriching the diversity of generated training instances.