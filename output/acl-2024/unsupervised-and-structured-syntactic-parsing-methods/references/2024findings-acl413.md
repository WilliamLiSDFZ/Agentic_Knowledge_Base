---
title: "Chinese Spelling Corrector Is Just a Language Learner"
source: "https://aclanthology.org/2024.findings-acl.413/"
pdf_url: ""
categories: ['nlp-for-asian-languages', 'unsupervised-and-structured-syntactic-parsing-methods']
tags: ['chinese-spelling-correction', 'self-supervised-learning', 'nlp']
venue: "ACL 2024"
tldr: "Chinese spelling correction can be achieved through self-supervised learning on clean text without requiring annotated error data."
---

# Chinese Spelling Corrector Is Just a Language Learner

**Source**: [https://aclanthology.org/2024.findings-acl.413/](https://aclanthology.org/2024.findings-acl.413/)

**TLDR**: Chinese spelling correction can be achieved through self-supervised learning on clean text without requiring annotated error data.

## Abstract

AbstractThis paper emphasizes Chinese spelling correction by means of self-supervised learning, which means there are no annotated errors within the training data. Our intuition is that humans are naturally good correctors with exposure to error-free sentences, which contrasts with current unsupervised methods that strongly rely on the usage of confusion sets to produce parallel sentences. In this paper, we demonstrate that learning a spelling correction model is identical to learning a language model from error-free data alone, with decoding it in a greater search space. We propose Denoising Decoding Correction (D2C), which selectively imposes noise upon the source sentence to determine the underlying correct characters. Our method is largely inspired by the ability of language models to perform correction, including both BERT-based models and large language models (LLMs). We show that the self-supervised learning manner generally outperforms the confusion set in specific domains because it bypasses the need to introduce error characters to the training data which can impair the error patterns not included in the introduced error characters.