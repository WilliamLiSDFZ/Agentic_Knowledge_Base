---
title: "An Effective Pronunciation Assessment Approach Leveraging Hierarchical Transformers and Pre-training Strategies"
source: "https://aclanthology.org/2024.acl-long.95/"
pdf_url: ""
categories: ['online-discourse-mental-health-language-analysis']
tags: ['pronunciation-assessment', 'hierarchical-transformers', 'pre-training']
venue: "ACL 2024"
tldr: "A hierarchical transformer with pre-training strategies is proposed for fine-grained automatic second-language pronunciation assessment."
---

# An Effective Pronunciation Assessment Approach Leveraging Hierarchical Transformers and Pre-training Strategies

**Source**: [https://aclanthology.org/2024.acl-long.95/](https://aclanthology.org/2024.acl-long.95/)

**TLDR**: A hierarchical transformer with pre-training strategies is proposed for fine-grained automatic second-language pronunciation assessment.

## Abstract

AbstractAutomatic pronunciation assessment (APA) manages to quantify a second language (L2) learner’s pronunciation proficiency in a target language by providing fine-grained feedback with multiple pronunciation aspect scores at various linguistic levels. Most existing efforts on APA typically parallelize the modeling process, namely predicting multiple aspect scores across various linguistic levels simultaneously. This inevitably makes both the hierarchy of linguistic units and the relatedness among the pronunciation aspects sidelined. Recognizing such a limitation, we in this paper first introduce HierTFR, a hierarchal APA method that jointly models the intrinsic structures of an utterance while considering the relatedness among the pronunciation aspects. We also propose a correlation-aware regularizer to strengthen the connection between the estimated scores and the human annotations. Furthermore, novel pre-training strategies tailored for different linguistic levels are put forward so as to facilitate better model initialization. An extensive set of empirical experiments conducted on the speechocean762 benchmark dataset suggest the feasibility and effectiveness of our approach in relation to several competitive baselines.