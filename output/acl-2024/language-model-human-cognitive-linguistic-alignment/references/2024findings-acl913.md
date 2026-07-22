---
title: "What Makes Language Models Good-enough?"
source: "https://aclanthology.org/2024.findings-acl.913/"
pdf_url: ""
categories: ['language-model-human-cognitive-linguistic-alignment', 'transformer-architecture-analysis-and-design']
tags: ['good-enough-processing', 'psycholinguistics', 'language-model-architecture', 'layers', 'cognitive-alignment']
venue: "ACL 2024"
tldr: "Examines which architectural features of language models lead to human-like good-enough language processing as studied in psycholinguistics."
---

# What Makes Language Models Good-enough?

**Source**: [https://aclanthology.org/2024.findings-acl.913/](https://aclanthology.org/2024.findings-acl.913/)

**TLDR**: Examines which architectural features of language models lead to human-like good-enough language processing as studied in psycholinguistics.

## Abstract

AbstractPsycholinguistic research suggests that humans may build a representation of linguistic input that is ‘good-enough’ for the task at hand. This study examines what architectural features make language models learn human-like good-enough language processing. We focus on the number of layers and self-attention heads in Transformers. We create a good-enough language processing (GELP) evaluation dataset (7,680 examples), which is designed to test the effects of two plausibility types, eight construction types, and three degrees of memory cost on language processing. To annotate GELP, we first conduct a crowdsourcing experiment whose design follows prior psycholinguistic studies. Our model evaluation against the annotated GELP then reveals that the full model as well as models with fewer layers and/or self-attention heads exhibit a good-enough performance. This result suggests that models with shallower depth and fewer heads can learn good-enough language processing.