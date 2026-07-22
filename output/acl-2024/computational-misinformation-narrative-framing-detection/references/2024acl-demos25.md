---
title: "VeraCT Scan: Retrieval-Augmented Fake News Detection with Justifiable Reasoning"
source: "https://aclanthology.org/2024.acl-demos.25/"
categories: ['computational-misinformation-narrative-framing-detection', 'llm-hallucination-detection-and-mitigation']
tags: ['fake-news-detection', 'retrieval-augmented', 'reasoning']
venue: "ACL 2024"
tldr: "Presents a retrieval-augmented fake news detection system with justifiable reasoning using generative AI."
---

# VeraCT Scan: Retrieval-Augmented Fake News Detection with Justifiable Reasoning

**Source**: [https://aclanthology.org/2024.acl-demos.25/](https://aclanthology.org/2024.acl-demos.25/)

**TLDR**: Presents a retrieval-augmented fake news detection system with justifiable reasoning using generative AI.

## Abstract

AbstractThe proliferation of fake news poses a significant threat not only by disseminating misleading information but also by undermining the very foundations of democracy. The recent advance of generative artificial intelligence has further exacerbated the challenge of distinguishing genuine news from fabricated stories. In response to this challenge, we introduce VeraCT Scan, a novel retrieval-augmented system for fake news detection. This system operates by extracting the core facts from a given piece of news and subsequently conducting an internet-wide search to identify corroborating or conflicting reports. Then sources’ credibility is leveraged for information verification. Besides determining the veracity of news, we also provide transparent evidence and reasoning to support its conclusions, resulting in the interpretability and trust in the results. In addition to GPT-4 Turbo, Llama-2 13B is also fine-tuned for news content understanding, information verification, and reasoning. Both implementations have demonstrated state-of-the-art accuracy in the realm of fake news detection.