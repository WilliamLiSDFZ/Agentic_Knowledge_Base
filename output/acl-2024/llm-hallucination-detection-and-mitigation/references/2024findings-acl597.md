---
title: "ACUEval: Fine-grained Hallucination Evaluation and Correction for Abstractive Summarization"
source: "https://aclanthology.org/2024.findings-acl.597/"
pdf_url: ""
categories: ['llm-hallucination-detection-and-mitigation', 'llms-for-biomedical-and-clinical-nlp']
tags: ['hallucination-evaluation', 'abstractive-summarization', 'fine-grained', 'correction', 'LLMs']
venue: "ACL 2024"
tldr: "ACUEval provides fine-grained hallucination evaluation and correction for abstractive summarization by detecting subtle factual errors in LLM-generated summaries."
---

# ACUEval: Fine-grained Hallucination Evaluation and Correction for Abstractive Summarization

**Source**: [https://aclanthology.org/2024.findings-acl.597/](https://aclanthology.org/2024.findings-acl.597/)

**TLDR**: ACUEval provides fine-grained hallucination evaluation and correction for abstractive summarization by detecting subtle factual errors in LLM-generated summaries.

## Abstract

AbstractThe impressive generation capabilities of large language models (LLMs) have made it harder to detect the subtle hallucinations they make in abstractive summarization, where generated summaries consist of a blend of correct and incorrect information w.r.t. a given document. Recently-proposed LLM-based evaluation metrics attempt to capture this, but still face challenges: (1) they are biased towards summaries generated from the same underlying LLM, and (2) they lack interpretability, offering only a single score. In this work, we present ACUEval, a metric that leverages the power of LLMs to perform two sub-tasks: decomposing summaries into atomic content units (ACUs), and validating them against the source document. Compared to current strong LLM-based metrics, our two-step evaluation strategy improves correlation with human judgments of faithfulness on three summarization evaluation benchmarks by 3% in balanced accuracy compared to the next-best metric, and also shows reduced preference bias towards LLM-generated summary. Further, we show that errors detected by ACUEval can be used to generate actionable feedback for refining the summary, improving the faithfulness scores by more than 10%.