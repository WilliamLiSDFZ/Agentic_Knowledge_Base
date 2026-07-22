---
title: "Harnessing Large Language Models as Post-hoc Correctors"
source: "https://aclanthology.org/2024.findings-acl.867/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'language-model-human-cognitive-linguistic-alignment']
tags: ['post-hoc-correction', 'LLM', 'model-correction', 'fine-tuning']
venue: "ACL 2024"
tldr: "Explores using large language models as post-hoc correctors for machine learning model outputs to reduce costly retraining and fine-tuning."
---

# Harnessing Large Language Models as Post-hoc Correctors

**Source**: [https://aclanthology.org/2024.findings-acl.867/](https://aclanthology.org/2024.findings-acl.867/)

**TLDR**: Explores using large language models as post-hoc correctors for machine learning model outputs to reduce costly retraining and fine-tuning.

## Abstract

AbstractAs Machine Learning (ML) models grow in size and demand higher-quality training data, the expenses associated with re-training and fine-tuning these models are escalating rapidly. Inspired by recent impressive achievements of Large Language Models (LLMs) in different fields, this paper delves into the question: can LLMs efficiently improve an ML’s performance at a minimal cost? We show that, through our proposed training-free framework LLMCorr, an LLM can work as a post-hoc corrector to propose corrections for the predictions of an arbitrary ML model. In particular, we form a contextual knowledge database by incorporating the dataset’s label information and the ML model’s predictions on the validation dataset. Leveraging the in-context learning capability of LLMs, we ask the LLM to summarise the instances in which the ML model makes mistakes and the correlation between primary predictions and true labels. Following this, the LLM can transfer its acquired knowledge to suggest corrections for the ML model’s predictions. Our experimental results on text analysis and the challenging molecular predictions show that LLMCorr improves the performance of a number of models by up to 39%.