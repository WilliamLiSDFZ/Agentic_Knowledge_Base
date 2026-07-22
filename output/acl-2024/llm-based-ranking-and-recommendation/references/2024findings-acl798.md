---
title: "Referral Augmentation for Zero-Shot Information Retrieval"
source: "https://aclanthology.org/2024.findings-acl.798/"
pdf_url: ""
categories: ['natural-language-processing-information-extraction', 'llm-based-ranking-and-recommendation']
tags: ['zero-shot-retrieval', 'referral-augmentation', 'document-indexing']
venue: "ACL 2024"
tldr: "Referral-Augmented Retrieval improves zero-shot information retrieval by appending citing document text to document indices."
---

# Referral Augmentation for Zero-Shot Information Retrieval

**Source**: [https://aclanthology.org/2024.findings-acl.798/](https://aclanthology.org/2024.findings-acl.798/)

**TLDR**: Referral-Augmented Retrieval improves zero-shot information retrieval by appending citing document text to document indices.

## Abstract

AbstractWe propose Referral-Augmented Retrieval (RAR), a simple technique that concatenates document indices with referrals: text from other documents that cite or link to the given document. We find that RAR provides significant performance gains for tasks across paper retrieval, entity retrieval, and open-domain question-answering in both zero-shot and in-domain (e.g., fine-tuned) settings. We examine how RAR provides especially strong improvements on more structured tasks, and can greatly outperform generative text expansion techniques such as DocT5Query and Query2Doc, with a 37% and 21% absolute improvement on ACL paper retrieval, respectively. We also compare three ways to aggregate referrals for RAR. Overall, we believe RAR can help revive and re-contextualize the classic information retrieval idea of using anchor texts to improve the representations of documents in a wide variety of corpuses in the age of neural retrieval.