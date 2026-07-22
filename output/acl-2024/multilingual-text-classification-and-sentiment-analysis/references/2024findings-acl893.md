---
title: "From One to Many: Expanding the Scope of Toxicity Mitigation in Language Models"
source: "https://aclanthology.org/2024.findings-acl.893/"
categories: ['hate-speech-and-toxic-content-detection', 'multilingual-text-classification-and-sentiment-analysis']
tags: ['toxicity-mitigation', 'multilingual', 'language-models']
venue: "ACL 2024"
tldr: "Toxicity mitigation is extended beyond single-language settings to improve safety across multilingual language model outputs."
---

# From One to Many: Expanding the Scope of Toxicity Mitigation in Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.893/](https://aclanthology.org/2024.findings-acl.893/)

**TLDR**: Toxicity mitigation is extended beyond single-language settings to improve safety across multilingual language model outputs.

## Abstract

AbstractTo date, toxicity mitigation in language models has almost entirely been focused on single-language settings. As language models embrace multilingual capabilities, it’s crucial our safety measures keep pace. Recognizing this research gap, our approach expands the scope of conventional toxicity mitigation to address the complexities presented by multiple languages. In the absence of sufficient annotated datasets across languages, we employ translated data to evaluate and enhance our mitigation techniques. We also compare finetuning mitigation approaches against retrieval-augmented techniques under both static and continual toxicity mitigation scenarios. This allows us to examine the effects of translation quality and the cross-lingual transfer on toxicity mitigation. We also explore how model size and data quantity affect the success of these mitigation efforts. Covering nine languages, our study represents a broad array of linguistic families and levels of resource availability, ranging from high to mid-resource languages. Through comprehensive experiments, we provide insights into the complexities of multilingual toxicity mitigation, offering valuable insights and paving the way for future research in this increasingly important field.