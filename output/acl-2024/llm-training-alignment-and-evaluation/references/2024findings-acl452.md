---
title: "What Have We Achieved on Non-autoregressive Translation?"
source: "https://aclanthology.org/2024.findings-acl.452/"
categories: ['minimum-bayes-risk-decoding-efficiency', 'llm-training-alignment-and-evaluation']
tags: ['non-autoregressive-translation', 'evaluation', 'human-judgment']
venue: "ACL 2024"
tldr: "A comprehensive evaluation reveals that NAT models, though BLEU-competitive, still lag behind autoregressive translation in human judgments."
---

# What Have We Achieved on Non-autoregressive Translation?

**Source**: [https://aclanthology.org/2024.findings-acl.452/](https://aclanthology.org/2024.findings-acl.452/)

**TLDR**: A comprehensive evaluation reveals that NAT models, though BLEU-competitive, still lag behind autoregressive translation in human judgments.

## Abstract

AbstractRecent advances have made non-autoregressive (NAT) translation comparable to autoregressive methods (AT). However, their evaluation using BLEU has been shown to weakly correlate with human annotations. Limited research compares non-autoregressive translation and autoregressive translation comprehensively, leaving uncertainty about the true proximity of NAT to AT. To address this gap, we systematically evaluate four representative NAT methods across various dimensions, including human evaluation. Our empirical results demonstrate that despite narrowing the performance gap, state-of-the-art NAT still underperforms AT under more reliable evaluation metrics. Furthermore, we discover that explicitly modeling dependencies is crucial for generating natural language and generalizing to out-of-distribution sequences.