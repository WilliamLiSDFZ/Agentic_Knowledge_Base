---
title: "DocLens: Multi-aspect Fine-grained Evaluation for Medical Text Generation"
source: "https://aclanthology.org/2024.acl-long.39/"
pdf_url: ""
categories: ['llms-for-biomedical-and-clinical-nlp', 'nlp-benchmark-design-and-interpretability']
tags: ['medical-text-generation', 'evaluation-metrics', 'clinical-NLP']
venue: "ACL 2024"
tldr: "DocLens proposes multi-aspect fine-grained metrics evaluating completeness, conciseness, and attribution for medical text generation."
---

# DocLens: Multi-aspect Fine-grained Evaluation for Medical Text Generation

**Source**: [https://aclanthology.org/2024.acl-long.39/](https://aclanthology.org/2024.acl-long.39/)

**TLDR**: DocLens proposes multi-aspect fine-grained metrics evaluating completeness, conciseness, and attribution for medical text generation.

## Abstract

AbstractMedical text generation aims to assist with administrative work and highlight salient information to support decision-making.To reflect the specific requirements of medical text, in this paper, we propose a set of metrics to evaluate the completeness, conciseness, and attribution of the generated text at a fine-grained level. The metrics can be computed by various types of evaluators including instruction-following (both proprietary and open-source) and supervised entailment models. We demonstrate the effectiveness of the resulting framework, DocLens, with three evaluators on three tasks: clinical note generation, radiology report summarization, and patient question summarization. A comprehensive human study shows that DocLens exhibits substantially higher agreement with the judgments of medical experts than existing metrics. The results also highlight the need to improve open-source evaluators and suggest potential directions. We released the code at https://github.com/yiqingxyq/DocLens.