---
title: "Linear-time Minimum Bayes Risk Decoding with Reference Aggregation"
source: "https://aclanthology.org/2024.acl-short.71/"
pdf_url: ""
categories: ['minimum-bayes-risk-decoding-efficiency']
tags: ['minimum-bayes-risk', 'decoding-efficiency', 'machine-translation']
venue: "ACL 2024"
tldr: "Proposes reference aggregation to reduce MBR decoding complexity from quadratic to linear time without sacrificing translation quality."
---

# Linear-time Minimum Bayes Risk Decoding with Reference Aggregation

**Source**: [https://aclanthology.org/2024.acl-short.71/](https://aclanthology.org/2024.acl-short.71/)

**TLDR**: Proposes reference aggregation to reduce MBR decoding complexity from quadratic to linear time without sacrificing translation quality.

## Abstract

AbstractMinimum Bayes Risk (MBR) decoding is a text generation technique that has been shown to improve the quality of machine translations, but is expensive, even if a sampling-based approximation is used. Besides requiring a large number of sampled sequences, it requires the pairwise calculation of a utility metric, which has quadratic complexity. In this paper, we propose to approximate pairwise metric scores with scores calculated against aggregated reference representations. This changes the complexity of utility estimation from O(n2) to O(n), while empirically preserving most of the quality gains of MBR decoding. We release our source code.