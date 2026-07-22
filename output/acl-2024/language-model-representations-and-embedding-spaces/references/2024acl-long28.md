---
title: "Explore Spurious Correlations at the Concept Level in Language Models for Text Classification"
source: "https://aclanthology.org/2024.acl-long.28/"
categories: ['language-model-representations-and-embedding-spaces', 'nlp-text-classification-applied-tasks']
tags: ['spurious-correlations', 'concept-level', 'text-classification']
venue: "ACL 2024"
tldr: "This paper exposes and analyzes spurious correlations at the concept level in language models used for text classification."
---

# Explore Spurious Correlations at the Concept Level in Language Models for Text Classification

**Source**: [https://aclanthology.org/2024.acl-long.28/](https://aclanthology.org/2024.acl-long.28/)

**TLDR**: This paper exposes and analyzes spurious correlations at the concept level in language models used for text classification.

## Abstract

AbstractLanguage models (LMs) have achieved notable success in numerous NLP tasks, employing both fine-tuning and in-context learning (ICL) methods. While language models demonstrate exceptional performance, they face robustness challenges due to spurious correlations arising from imbalanced label distributions in training data or ICL exemplars. Previous research has primarily concentrated on word, phrase, and syntax features, neglecting the concept level, often due to the absence of concept labels and difficulty in identifying conceptual content in input texts. This paper introduces two main contributions. First, we employ ChatGPT to assign concept labels to texts, assessing concept bias in models during fine-tuning or ICL on test data. We find that LMs, when encountering spurious correlations between a concept and a label in training or prompts, resort to shortcuts for predictions. Second, we introduce a data rebalancing technique that incorporates ChatGPT-generated counterfactual data, thereby balancing label distribution and mitigating spurious correlations. Our method’s efficacy, surpassing traditional token removal approaches, is validated through extensive testing.