---
title: "Publicly Shareable Clinical Large Language Model Built on Synthetic Clinical Notes"
source: "https://aclanthology.org/2024.findings-acl.305/"
pdf_url: ""
categories: ['llms-for-biomedical-and-clinical-nlp', 'privacy-risks-in-language-model-embeddings']
tags: ['clinical-LLM', 'synthetic-clinical-notes', 'privacy']
venue: "ACL 2024"
tldr: "Builds a publicly shareable clinical LLM trained on synthetic clinical notes to overcome privacy restrictions on real patient data."
---

# Publicly Shareable Clinical Large Language Model Built on Synthetic Clinical Notes

**Source**: [https://aclanthology.org/2024.findings-acl.305/](https://aclanthology.org/2024.findings-acl.305/)

**TLDR**: Builds a publicly shareable clinical LLM trained on synthetic clinical notes to overcome privacy restrictions on real patient data.

## Abstract

AbstractThe development of large language models tailored for handling patients’ clinical notes is often hindered by the limited accessibility and usability of these notes due to strict privacy regulations. To address these challenges, we first create synthetic large-scale clinical notes using publicly available case reports extracted from biomedical literature. We then use these synthetic notes to train our specialized clinical large language model, Asclepius. While Asclepius is trained on synthetic data, we assess its potential performance in real-world applications by evaluating it using real clinical notes. We benchmark Asclepius against several other large language models, including GPT-3.5-turbo and other open-source alternatives. To further validate our approach using synthetic notes, we also compare Asclepius with its variants trained on real clinical notes. Our findings convincingly demonstrate that synthetic clinical notes can serve as viable substitutes for real ones when constructing high-performing clinical language models. This conclusion is supported by detailed evaluations conducted by both GPT-4 and medical professionals. All resources—including weights, codes, and data—used in the development of Asclepius will be made publicly accessible for future research.