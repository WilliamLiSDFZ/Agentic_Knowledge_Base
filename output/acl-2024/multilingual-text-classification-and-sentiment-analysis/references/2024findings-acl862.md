---
title: "Leveraging Entailment Judgements in Cross-Lingual Summarisation"
source: "https://aclanthology.org/2024.findings-acl.862/"
categories: ['llm-hallucination-detection-and-mitigation', 'multilingual-text-classification-and-sentiment-analysis']
tags: ['cross-lingual-summarization', 'hallucination', 'entailment', 'faithfulness', 'data-quality']
venue: "ACL 2024"
tldr: "Uses entailment judgements to filter and improve faithfulness in synthetically created cross-lingual summarization datasets."
---

# Leveraging Entailment Judgements in Cross-Lingual Summarisation

**Source**: [https://aclanthology.org/2024.findings-acl.862/](https://aclanthology.org/2024.findings-acl.862/)

**TLDR**: Uses entailment judgements to filter and improve faithfulness in synthetically created cross-lingual summarization datasets.

## Abstract

AbstractSynthetically created Cross-Lingual Summarisation (CLS) datasets are prone to include document-summary pairs where the reference summary is unfaithful to the corresponding document as it contains content not supported by the document (i.e., hallucinated content). This low data quality misleads model learning and obscures evaluation results. Automatic ways to assess hallucinations and improve training have been proposed for monolingual summarisation, predominantly in English. For CLS, we propose to use off-the-shelf cross-lingual Natural Language Inference (X-NLI) to evaluate faithfulness of reference and model generated summaries. Then, we study training approaches that are aware of faithfulness issues in the training data and propose an approach that uses unlikelihood loss to teach a model about unfaithful summary sequences. Our results show that it is possible to train CLS models that yield more faithful and at the same time informative summaries.