---
title: "Exciting Mood Changes: A Time-aware Hierarchical Transformer for Change Detection Modelling"
source: "https://aclanthology.org/2024.findings-acl.744/"
pdf_url: ""
categories: ['online-discourse-mental-health-language-analysis']
tags: ['mental-health', 'temporal-modeling', 'change-detection']
venue: "ACL 2024"
tldr: "Proposes a time-aware hierarchical transformer to model longitudinal linguistic changes for mental health monitoring on social media."
---

# Exciting Mood Changes: A Time-aware Hierarchical Transformer for Change Detection Modelling

**Source**: [https://aclanthology.org/2024.findings-acl.744/](https://aclanthology.org/2024.findings-acl.744/)

**TLDR**: Proposes a time-aware hierarchical transformer to model longitudinal linguistic changes for mental health monitoring on social media.

## Abstract

AbstractThrough the rise of social media platforms, longitudinal language modelling has received much attention over the latest years, especially in downstream tasks such as mental health monitoring of individuals where modelling linguistic content in a temporal fashion is crucial. A key limitation in existing work is how to effectively model temporal sequences within Transformer-based language models. In this work we address this challenge by introducing a novel approach for predicting ‘Moments of Change’ (MoC) in the mood of online users, by simultaneously considering user linguistic and time-aware context. A Hawkes process-inspired transformation layer is applied over the proposed architecture to model the influence of time on users’ posts – capturing both their immediate and historical dynamics. We perform experiments on the two existing datasets for the MoC task and showcase clear performance gains when leveraging the proposed layer. Our ablation study reveals the importance of considering temporal dynamics in detecting subtle and rare mood changes. Our results indicate that considering linguistic and temporal information in a hierarchical manner provide valuable insights into the temporal dynamics of modelling user generated content over time, with applications in mental health monitoring.