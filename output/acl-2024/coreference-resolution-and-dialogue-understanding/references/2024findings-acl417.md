---
title: "Plan, Generate and Complicate: Improving Low-resource Dialogue State Tracking via Easy-to-Difficult Zero-shot Data Augmentation"
source: "https://aclanthology.org/2024.findings-acl.417/"
pdf_url: ""
categories: ['coreference-resolution-and-dialogue-understanding', 'continual-learning-for-nlp-tasks']
tags: ['dialogue-state-tracking', 'data-augmentation', 'low-resource']
venue: "ACL 2024"
tldr: "Proposes easy-to-difficult zero-shot data augmentation to improve low-resource dialogue state tracking performance."
---

# Plan, Generate and Complicate: Improving Low-resource Dialogue State Tracking via Easy-to-Difficult Zero-shot Data Augmentation

**Source**: [https://aclanthology.org/2024.findings-acl.417/](https://aclanthology.org/2024.findings-acl.417/)

**TLDR**: Proposes easy-to-difficult zero-shot data augmentation to improve low-resource dialogue state tracking performance.

## Abstract

AbstractData augmentation methods have been a promising direction to improve the performance of small models for low-resource dialogue state tracking. However, traditional methods rely on pre-defined user goals and neglect the importance of data complexity in this task. In this paper, we propose EDZ-DA, an Easy-to-Difficult Zero-shot Data Augmentation framework for low-resource dialogue state tracking that utilizes large language models to automatically catch the relationships of different domains and then generate the dialogue data. We also complicate the dialogues based on the domain relation to enhance the model’s capability for co-reference slot tracking. Furthermore, we permute slot values to mitigate the influence of output orders and the problem of incomplete value generation. Experimental results illustrate the superiority of our proposed method compared to previous strong data augmentation baselines on MultiWOZ.