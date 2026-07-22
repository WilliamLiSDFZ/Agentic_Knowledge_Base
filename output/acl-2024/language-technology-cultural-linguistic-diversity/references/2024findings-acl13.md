---
title: "How Important is a Language Model for Low-resource ASR?"
source: "https://aclanthology.org/2024.findings-acl.13/"
categories: ['language-technology-cultural-linguistic-diversity', 'nlp-for-asian-languages']
tags: ['low-resource', 'ASR', 'language-model']
venue: "ACL 2024"
tldr: "Investigates the impact of language models on low-resource automatic speech recognition, finding they remain critical unlike in high-resource settings."
---

# How Important is a Language Model for Low-resource ASR?

**Source**: [https://aclanthology.org/2024.findings-acl.13/](https://aclanthology.org/2024.findings-acl.13/)

**TLDR**: Investigates the impact of language models on low-resource automatic speech recognition, finding they remain critical unlike in high-resource settings.

## Abstract

AbstractN-gram language models (LMs) are the innovation that first made large-vocabulary continuous automatic speech recognition (ASR) viable. With neural end-to-end ASR architectures, however, LMs have become an afterthought. While the effect on accuracy may be negligible for English and Mandarin, jettisoning the LM might not make sense for the world’s remaining 6000+ languages. In this paper, we investigate the role of the LM in low-resource ASR. First we ask: does using an n-gram LM in decoding in neural architectures help ASR performance? While it may seem obvious that it should, its absence in most implementations suggests otherwise. Second, we ask: when an n-gram LM is used in ASR, is there a relationship between the size of the LM and ASR accuracy? We have discovered that gut feelings on this question vary considerably, but there is little empirical work to support any particular claim. We explore these questions “in the wild” using a deliberately diverse set of 9 very small ASR corpora. The results show that: (1) decoding with an n-gram LM, regardless of its size, leads to lower word error rates; and (2) increasing the size of the LM appears to yield improvements only when the audio corpus itself is already relatively large. This suggests that collecting additional LM training text may benefit widely-spoken languages which typically have larger audio corpora. In contrast, for endangered languages where data of any kind will always be limited, efforts may be better spent collecting additional transcribed audio.