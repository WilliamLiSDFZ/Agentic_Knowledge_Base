---
title: "Personalized Topic Selection Model for Topic-Grounded Dialogue"
source: "https://aclanthology.org/2024.findings-acl.429/"
pdf_url: ""
categories: ['emotion-aware-dialogue-and-empathy-systems', 'topic-modeling-and-essay-evaluation']
tags: ['topic-grounded-dialogue', 'personalization', 'topic-selection']
venue: "ACL 2024"
tldr: "Proposes a personalized topic selection model that jointly leverages topics and personas to guide topic-grounded dialogue systems."
---

# Personalized Topic Selection Model for Topic-Grounded Dialogue

**Source**: [https://aclanthology.org/2024.findings-acl.429/](https://aclanthology.org/2024.findings-acl.429/)

**TLDR**: Proposes a personalized topic selection model that jointly leverages topics and personas to guide topic-grounded dialogue systems.

## Abstract

AbstractRecently, the topic-grounded dialogue (TGD) system has become increasingly popular as its powerful capability to actively guide users to accomplish specific tasks through topic-guided conversations. Most existing works utilize side information (e.g. topics or personas) in isolation to enhance the topic selection ability. However, due to disregarding the noise within these auxiliary information sources and their mutual influence, current models tend to predict user-uninteresting and contextually irrelevant topics. To build user-engaging and coherent dialogue agent, we propose a personalized topic selection model for topic-grounded dialogue, named PETD, which takes account of the interaction of side information to selectively aggregate such information for more accurately predicting subsequent topics. Specifically, we evaluate the correlation between global topics and personas and selectively incorporate the global topics aligned with user personas. Furthermore, we propose a contrastive learning based persona selector to filter relevant personas under the constraint of lacking pertinent persona annotations. Throughout the selection and generation, diverse relevant side information is considered. Extensive experiments demonstrate that our proposed method can generate engaging and diverse responses, outperforming state-of-the-art baselines across various evaluation metrics.