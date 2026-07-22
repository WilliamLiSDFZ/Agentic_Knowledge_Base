---
title: "CTC-based Non-autoregressive Textless Speech-to-Speech Translation"
source: "https://aclanthology.org/2024.findings-acl.543/"
categories: ['speech-and-language-multimodal-generation-systems', 'continuous-discrete-representation-tradeoffs']
tags: ['speech-to-speech-translation', 'non-autoregressive', 'CTC', 'textless', 'decoding-speed']
venue: "ACL 2024"
tldr: "A CTC-based non-autoregressive model for direct textless speech-to-speech translation achieving faster decoding with competitive quality."
---

# CTC-based Non-autoregressive Textless Speech-to-Speech Translation

**Source**: [https://aclanthology.org/2024.findings-acl.543/](https://aclanthology.org/2024.findings-acl.543/)

**TLDR**: A CTC-based non-autoregressive model for direct textless speech-to-speech translation achieving faster decoding with competitive quality.

## Abstract

AbstractDirect speech-to-speech translation (S2ST) has achieved impressive translation quality, but it often faces the challenge of slow decoding due to the considerable length of speech sequences. Recently, some research has turned to non-autoregressive (NAR) models to expedite decoding, yet the translation quality typically lags behind autoregressive (AR) models significantly. In this paper, we investigate the performance of CTC-based NAR models in S2ST, as these models have shown impressive results in machine translation. Experimental results demonstrate that by combining pretraining, knowledge distillation, and advanced NAR training techniques such as glancing training and non-monotonic latent alignments, CTC-based NAR models achieve translation quality comparable to the AR model, while preserving up to 26.81× decoding speedup.