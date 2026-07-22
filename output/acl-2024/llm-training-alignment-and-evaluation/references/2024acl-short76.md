---
title: "Getting Serious about Humor: Crafting Humor Datasets with Unfunny Large Language Models"
source: "https://aclanthology.org/2024.acl-short.76/"
categories: ['llm-based-computational-humor-generation', 'llm-training-alignment-and-evaluation']
tags: ['humor-detection', 'dataset-creation', 'unfunny-LLMs', 'humor-datasets', 'NLP']
venue: "ACL 2024"
tldr: "This paper investigates using LLMs to generate non-humorous counterparts to humorous texts, crafting better humor detection datasets."
---

# Getting Serious about Humor: Crafting Humor Datasets with Unfunny Large Language Models

**Source**: [https://aclanthology.org/2024.acl-short.76/](https://aclanthology.org/2024.acl-short.76/)

**TLDR**: This paper investigates using LLMs to generate non-humorous counterparts to humorous texts, crafting better humor detection datasets.

## Abstract

AbstractHumor is a fundamental facet of human cognition and interaction. Yet, despite recent advances in natural language processing, humor detection remains a challenging task that is complicated by the scarcity of datasets that pair humorous texts with similar non-humorous counterparts. We investigate whether large language models (LLMs) can generate synthetic data for humor detection via editing texts. We benchmark LLMs on an existing human dataset and show that current LLMs display an impressive ability to “unfun” jokes, as judged by humans and as measured on the downstream task of humor detection. We extend our approach to a code-mixed English-Hindi humor dataset where we find that GPT-4’s synthetic data is highly rated by bilingual annotators and provides challenging adversarial examples for humor classifiers.