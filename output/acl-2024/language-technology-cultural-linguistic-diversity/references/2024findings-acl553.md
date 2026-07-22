---
title: "Disentangling Dialect from Social Bias via Multitask Learning to Improve Fairness"
source: "https://aclanthology.org/2024.findings-acl.553/"
pdf_url: ""
categories: ['bias-and-fairness-in-llms', 'language-technology-cultural-linguistic-diversity']
tags: ['dialect-fairness', 'multitask-learning', 'social-bias']
venue: "ACL 2024"
tldr: "Uses multitask learning to disentangle dialect variation from social bias in NLP models to improve fairness toward dialect speakers."
---

# Disentangling Dialect from Social Bias via Multitask Learning to Improve Fairness

**Source**: [https://aclanthology.org/2024.findings-acl.553/](https://aclanthology.org/2024.findings-acl.553/)

**TLDR**: Uses multitask learning to disentangle dialect variation from social bias in NLP models to improve fairness toward dialect speakers.

## Abstract

AbstractDialects introduce syntactic and lexical variations in language that occur in regional or social groups. Most NLP methods are not sensitive to such variations. This may lead to unfair behavior of the methods, conveying negative bias towards dialect speakers. While previous work has studied dialect-related fairness for aspects like hate speech, other aspects of biased language, such as lewdness, remain fully unexplored. To fill this gap, we investigate performance disparities between dialects in the detection of five aspects of biased language and how to mitigate them. To alleviate bias, we present a multitask learning approach that models dialect language as an auxiliary task to incorporate syntactic and lexical variations. In our experiments with African-American English dialect, we provide empirical evidence that complementing common learning approaches with dialect modeling improves their fairness. Furthermore, the results suggest that multitask learning achieves state-of-the-art performance and helps to detect properties of biased language more reliably.