---
title: "Centroid-Based Efficient Minimum Bayes Risk Decoding"
source: "https://aclanthology.org/2024.findings-acl.654/"
pdf_url: ""
categories: ['minimum-bayes-risk-decoding-efficiency']
tags: ['minimum-bayes-risk', 'centroid-approximation', 'machine-translation']
venue: "ACL 2024"
tldr: "Proposes centroid-based approximation to reduce MBR decoding from quadratic to linear time while maintaining translation quality."
---

# Centroid-Based Efficient Minimum Bayes Risk Decoding

**Source**: [https://aclanthology.org/2024.findings-acl.654/](https://aclanthology.org/2024.findings-acl.654/)

**TLDR**: Proposes centroid-based approximation to reduce MBR decoding from quadratic to linear time while maintaining translation quality.

## Abstract

AbstractMinimum Bayes risk (MBR) decoding achieved state-of-the-art translation performance by using COMET, a neural metric that has a high correlation with human evaluation.However, MBR decoding requires quadratic time since it computes the expected score between a translation hypothesis and all reference translations.We propose centroid-based MBR (CBMBR) decoding to improve the speed of MBR decoding.Our method clusters the reference translations in the feature space, and then calculates the score using the centroids of each cluster.The experimental results show that our CBMBR not only improved the decoding speed of the expected score calculation 5.7 times, but also outperformed vanilla MBR decoding in translation quality by up to 0.5 COMET in the WMT’22 En↔Ja, En↔De, En↔Zh, and WMT’23 En↔Ja translation tasks.