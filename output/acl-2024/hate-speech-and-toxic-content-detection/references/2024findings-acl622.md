---
title: "SharedCon: Implicit Hate Speech Detection using Shared Semantics"
source: "https://aclanthology.org/2024.findings-acl.622/"
categories: ['hate-speech-and-toxic-content-detection', 'language-model-representations-and-embedding-spaces']
tags: ['implicit-hate-speech', 'shared-semantics', 'contrastive-learning']
venue: "ACL 2024"
tldr: "SharedCon detects implicit hate speech by leveraging shared semantic representations between surface-level and hateful interpretations."
---

# SharedCon: Implicit Hate Speech Detection using Shared Semantics

**Source**: [https://aclanthology.org/2024.findings-acl.622/](https://aclanthology.org/2024.findings-acl.622/)

**TLDR**: SharedCon detects implicit hate speech by leveraging shared semantic representations between surface-level and hateful interpretations.

## Abstract

AbstractThe ever-growing presence of hate speech on social network services and other online platforms not only fuels online harassment but also presents a growing challenge for hate speech detection. As this task is akin to binary classification, one of the promising approaches for hate speech detection is the utilization of contrastive learning. Recent studies suggest that classifying hateful posts in just a binary manner may not adequately address the nuanced task of detecting implicit hate speech. This challenge is largely due to the subtle nature and context dependency of such pejorative remarks. Previous studies proposed a modified contrastive learning approach equipped with additional aids such as human-written implications or machine-generated augmented data for better implicit hate speech detection. While this approach can potentially enhance the overall performance by its additional data in general, it runs the risk of overfitting as well as heightened cost and time to obtain. These drawbacks serve as motivation for us to design a methodology that is not dependent on human-written or machine-generated augmented data for training. We propose a straightforward, yet effective, clustering-based contrastive learning approach that leverages the shared semantics among the data.