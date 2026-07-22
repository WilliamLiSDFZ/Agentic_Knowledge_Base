---
title: "Boosting Zero-Shot Crosslingual Performance using LLM-Based Augmentations with Effective Data Selection"
source: "https://aclanthology.org/2024.findings-acl.795/"
pdf_url: ""
categories: ['multilingual-text-classification-and-sentiment-analysis']
tags: ['cross-lingual-transfer', 'data-augmentation', 'low-resource-languages']
venue: "ACL 2024"
tldr: "Uses LLM-generated task-specific augmentations with effective data selection to boost zero-shot cross-lingual transfer for low-resource languages."
---

# Boosting Zero-Shot Crosslingual Performance using LLM-Based Augmentations with Effective Data Selection

**Source**: [https://aclanthology.org/2024.findings-acl.795/](https://aclanthology.org/2024.findings-acl.795/)

**TLDR**: Uses LLM-generated task-specific augmentations with effective data selection to boost zero-shot cross-lingual transfer for low-resource languages.

## Abstract

AbstractLarge language models (LLMs) are very proficient text generators. We leverage this capability of LLMs to generate task-specific data via zero-shot prompting and promote cross-lingual transfer for low-resource target languages. Given task-specific data in a source language and a teacher model trained on this data, we propose using this teacher to label LLM generations and employ a set of simple data selection strategies that use the teacher’s label probabilities. Our data selection strategies help us identify a representative subset of diverse generations that help boost zero-shot accuracies while being efficient, in comparison to using all the LLM generations (without any subset selection). We also highlight other important design choices that affect cross-lingual performance such as the use of translations of source data and what labels are best to use for the LLM generations. We observe significant performance gains across sentiment analysis and natural language inference tasks (of up to a maximum of 7.13 absolute points and 1.5 absolute points on average) across a number of target languages (Hindi, Marathi, Urdu, Swahili) and domains.