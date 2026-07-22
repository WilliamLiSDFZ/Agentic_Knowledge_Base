---
title: "Label-aware Hard Negative Sampling Strategies with Momentum Contrastive Learning for Implicit Hate Speech Detection"
source: "https://aclanthology.org/2024.findings-acl.957/"
categories: ['hate-speech-and-toxic-content-detection', 'text-clustering-with-limited-labels']
tags: ['implicit-hate-speech', 'contrastive-learning', 'hard-negative-sampling']
venue: "ACL 2024"
tldr: "Improves implicit hate speech detection using label-aware hard negative sampling with momentum contrastive learning."
---

# Label-aware Hard Negative Sampling Strategies with Momentum Contrastive Learning for Implicit Hate Speech Detection

**Source**: [https://aclanthology.org/2024.findings-acl.957/](https://aclanthology.org/2024.findings-acl.957/)

**TLDR**: Improves implicit hate speech detection using label-aware hard negative sampling with momentum contrastive learning.

## Abstract

AbstractDetecting implicit hate speech that is not directly hateful remains a challenge. Recent research has attempted to detect implicit hate speech by applying contrastive learning to pre-trained language models such as BERT and RoBERTa, but the proposed models still do not have a significant advantage over cross-entropy loss-based learning. We found that contrastive learning based on randomly sampled batch data does not encourage the model to learn hard negative samples. In this work, we propose Label-aware Hard Negative sampling strategies (LAHN) that encourage the model to learn detailed features from hard negative samples, instead of naive negative samples in random batch, using momentum-integrated contrastive learning. LAHN outperforms the existing models for implicit hate speech detection both in- and cross-datasets. The code is available at https://github.com/Hanyang-HCC-Lab/LAHN