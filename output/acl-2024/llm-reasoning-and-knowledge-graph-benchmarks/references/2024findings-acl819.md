---
title: "Complex Logical Query Answering by Calibrating Knowledge Graph Completion Models"
source: "https://aclanthology.org/2024.findings-acl.819/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['knowledge-graph', 'complex-logical-queries', 'KG-completion']
venue: "ACL 2024"
tldr: "Knowledge graph completion models are calibrated to improve complex logical query answering over incomplete knowledge graphs."
---

# Complex Logical Query Answering by Calibrating Knowledge Graph Completion Models

**Source**: [https://aclanthology.org/2024.findings-acl.819/](https://aclanthology.org/2024.findings-acl.819/)

**TLDR**: Knowledge graph completion models are calibrated to improve complex logical query answering over incomplete knowledge graphs.

## Abstract

AbstractComplex logical query answering (CLQA) is a challenging task that involves finding answer entities for complex logical queries over incomplete knowledge graphs (KGs). Previous research has explored the use of pre-trained knowledge graph completion (KGC) models, which can predict the missing facts in KGs, to answer complex logical queries. However, KGC models are typically evaluated using ranking evaluation metrics, which may result in values of predictions of KGC models that are not well-calibrated. In this paper, we propose a method for calibrating KGC models, namely CKGC, which enables KGC models to adapt to answering complex logical queries. Notably, CKGC is lightweight and effective. The adaptation function is simple, allowing the model to quickly converge during the adaptation process. The core concept of CKGC is to map the values of predictions of KGC models to the range [0, 1], ensuring that values associated with true facts are close to 1, while values linked to false facts are close to 0. Through experiments on three benchmark datasets, we demonstrate that our proposed calibration method can significantly boost model performance in the CLQA task. Moreover, our approach can enhance the performance of CLQA while preserving the ranking evaluation metrics of KGC models. The code is available at https://github.com/changyi7231/CKGC.