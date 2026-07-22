---
title: "TextGenSHAP: Scalable Post-Hoc Explanations in Text Generation with Long Documents"
source: "https://aclanthology.org/2024.findings-acl.832/"
pdf_url: ""
categories: ['causal-reasoning-and-explanation-in-nlp', 'text-simplification-evaluation-and-methods']
tags: ['shapley-values', 'llm-explainability', 'long-documents']
venue: "ACL 2024"
tldr: "TextGenSHAP provides scalable post-hoc Shapley value explanations for LLM text generation over long documents."
---

# TextGenSHAP: Scalable Post-Hoc Explanations in Text Generation with Long Documents

**Source**: [https://aclanthology.org/2024.findings-acl.832/](https://aclanthology.org/2024.findings-acl.832/)

**TLDR**: TextGenSHAP provides scalable post-hoc Shapley value explanations for LLM text generation over long documents.

## Abstract

AbstractLarge language models (LLMs) have attracted great interest in many real-world applications; however, their “black-box” nature necessitates scalable and faithful explanations. Shapley values have matured as an explainability method for deep learning, but extending them to LLMs is difficult due to long input contexts and autoregressive output generation. We introduce , an efficient post-hoc explanation method incorporating LLM-specific techniques, which leads to significant runtime improvements: token-level explanations in minutes not hours, and document-level explanations within seconds. We demonstrate how such explanations can improve end-to-end performance of retrieval augmented generation by localizing important words within long documents and reranking passages collected by retrieval systems. On various open-domain question answering benchmarks, we show TextGenSHAP improves the retrieval recall and prediction accuracy significantly.