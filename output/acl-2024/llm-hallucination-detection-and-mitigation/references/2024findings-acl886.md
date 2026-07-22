---
title: "AttributionBench: How Hard is Automatic Attribution Evaluation?"
source: "https://aclanthology.org/2024.findings-acl.886/"
pdf_url: ""
categories: ['llm-hallucination-detection-and-mitigation', 'nlp-benchmark-design-and-interpretability']
tags: ['attribution-evaluation', 'retrieval-augmented-generation', 'claim-verification']
venue: "ACL 2024"
tldr: "AttributionBench benchmarks automatic evaluation of whether LLM-generated responses are fully supported by cited evidence."
---

# AttributionBench: How Hard is Automatic Attribution Evaluation?

**Source**: [https://aclanthology.org/2024.findings-acl.886/](https://aclanthology.org/2024.findings-acl.886/)

**TLDR**: AttributionBench benchmarks automatic evaluation of whether LLM-generated responses are fully supported by cited evidence.

## Abstract

AbstractModern generative search engines enhance the reliability of large language model (LLM) responses by providing cited evidence. However, evaluating the answer’s attribution, i.e., whether every claim within the generated responses is fully supported by its cited evidence, remains an open problem. This verification, traditionally dependent on costly human evaluation, underscores the urgent need for automatic attribution evaluation methods. To bridge the gap in the absence of standardized benchmarks for these methods, we present AttributionBench, a comprehensive benchmark compiled from various existing attribution datasets. Our extensive experiments on AttributionBench reveal the challenges of automatic attribution evaluation, even for state-of-the-art LLMs. Specifically, our findings show that even a fine-tuned GPT-3.5 only achieves around 80% macro-F1 under a binary classification formulation. A detailed analysis of more than 300 error cases indicates that a majority of failures stem from the model’s inability to process nuanced information, and the discrepancy between the information the model has access to and that human annotators do.