---
title: "URG: A Unified Ranking and Generation Method for Ensembling Language Models"
source: "https://aclanthology.org/2024.findings-acl.261/"
pdf_url: ""
categories: ['llm-based-ranking-and-recommendation', 'minimum-bayes-risk-decoding-efficiency']
tags: ['ensemble-llm', 'ranking-and-generation', 'unified-framework']
venue: "ACL 2024"
tldr: "Proposes URG, a unified method that jointly performs ranking and generation for ensembling multiple language models more efficiently."
---

# URG: A Unified Ranking and Generation Method for Ensembling Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.261/](https://aclanthology.org/2024.findings-acl.261/)

**TLDR**: Proposes URG, a unified method that jointly performs ranking and generation for ensembling multiple language models more efficiently.

## Abstract

AbstractPrior research endeavors of the ensemble Large Language Models (LLMs) achieved great success by employing an individual language model (LM) rank before the text generation. However, the use of an individual LM ranker faces two primary challenges: (1) The time-intensive nature of the ranking process, stemming from the comparisons between models; (2) The issue of error propagation arising from the separate ranking and generation models within the framework. In order to overcome these challenges, we propose a novel ensemble framework, namely Unified Ranking and Generation (URG). URG represents an end-to-end framework that jointly ranks the outputs of LLMs and generates fine-grained fusion results, via utilizing a dedicated cross-attention-based module and noise mitigation training against irrelevant information stemming from bad ranking results. Through extensive experimentation and evaluation, we demonstrate the efficiency and effectiveness of our framework in both the ranking and generation tasks. With the close coordination of the ranking and generation modules, our end-to-end framework achieves the state-of-the-art (SOTA) performance on these tasks, and exhibits substantial enhancements to any of the ensembled models.