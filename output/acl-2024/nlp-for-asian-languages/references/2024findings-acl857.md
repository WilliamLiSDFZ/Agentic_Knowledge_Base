---
title: "Part-of-speech Tagging for Extremely Low-resource Indian Languages"
source: "https://aclanthology.org/2024.findings-acl.857/"
pdf_url: ""
categories: ['language-technology-cultural-linguistic-diversity', 'nlp-for-asian-languages']
tags: ['pos-tagging', 'low-resource', 'indian-languages']
venue: "ACL 2024"
tldr: "Develops part-of-speech tagging systems for extremely low-resource Indian regional languages with sparse digital resources."
---

# Part-of-speech Tagging for Extremely Low-resource Indian Languages

**Source**: [https://aclanthology.org/2024.findings-acl.857/](https://aclanthology.org/2024.findings-acl.857/)

**TLDR**: Develops part-of-speech tagging systems for extremely low-resource Indian regional languages with sparse digital resources.

## Abstract

AbstractModern natural language processing (NLP) systems thrive when given access to large datasets. However, a large fraction of the world’s languages are not privy to such benefits due to sparse documentation and inadequate digital representation. This is especially true for Indian regional languages. As a first step towards expanding the reach of NLP technologies to extremely low-resource Indian languages, we present a new parallel part-of-speech (POS) evaluation dataset for Angika, Magahi, Bhojpuri and Hindi. Angika, Magahi, Bhojpuri, along with the more well-known Hindi, are all languages spoken in the Indian states of Bihar, Jharkhand and West Bengal. Ours is notably the first NLP resource, even for a shallow NLP task like POS-tagging, for Angika. We establish POS-tagging baselines using state-of-the-art multilingual pretrained language models (PLMs) finetuned on Hindi data, and show zero-shot evaluations on the other three languages. While all four languages use the same Devanagari script, pretrained tokenizers underperform in zero-shot on the three languages. We propose a simple look-back fix to address the tokenization challenge yielding F1-score improvements of up to 8% on Angika and show how it comes very close to an oracle setting when the underlying Hindi word is known (and can be accurately tokenized).