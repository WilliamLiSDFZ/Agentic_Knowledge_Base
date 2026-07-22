---
title: "SKGSum: Structured Knowledge-Guided Document Summarization"
source: "https://aclanthology.org/2024.findings-acl.110/"
pdf_url: ""
categories: ['document-understanding-and-information-extraction', 'causal-reasoning-and-explanation-in-nlp']
tags: ['summarization', 'structured-knowledge', 'genre-theory', 'document-structure', 'NLP']
venue: "ACL 2024"
tldr: "Proposes a structured knowledge-guided summarization framework that leverages genre-aware summary structures to improve informativeness and organization."
---

# SKGSum: Structured Knowledge-Guided Document Summarization

**Source**: [https://aclanthology.org/2024.findings-acl.110/](https://aclanthology.org/2024.findings-acl.110/)

**TLDR**: Proposes a structured knowledge-guided summarization framework that leverages genre-aware summary structures to improve informativeness and organization.

## Abstract

AbstractA summary structure is inherent to certain types of texts according to the Genre Theory of Linguistics. Such structures aid readers in efficiently locating information within summaries. However, most existing automatic summarization methods overlook the importance of summary structure, resulting in summaries that emphasize the most prominent information while omitting essential details from other sections. While a few summarizers recognize the importance of summary structure, they rely heavily on the predefined labels of summary structures in the source document and ground truth summaries. To address these shortcomings, we developed a Structured Knowledge-Guided Summarization (SKGSum) and its variant, SKGSum-W, which do not require structure labels. Instead, these methods rely on a set of automatically extracted summary points to generate summaries. We evaluate the proposed methods using three real-world datasets. The results indicate that our methods not only improve the quality of summaries, in terms of ROUGE and BERTScore, but also broaden the types of documents that can be effectively summarized.