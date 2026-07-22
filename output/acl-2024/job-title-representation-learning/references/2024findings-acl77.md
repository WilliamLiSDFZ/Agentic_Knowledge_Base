---
title: "Learning Job Title Representation from Job Description Aggregation Network"
source: "https://aclanthology.org/2024.findings-acl.77/"
pdf_url: ""
categories: ['job-title-representation-learning']
tags: ['job-title-representation', 'job-description', 'aggregation-network']
venue: "ACL 2024"
tldr: "A job description aggregation network is proposed to learn richer job title representations by leveraging diverse job description content."
---

# Learning Job Title Representation from Job Description Aggregation Network

**Source**: [https://aclanthology.org/2024.findings-acl.77/](https://aclanthology.org/2024.findings-acl.77/)

**TLDR**: A job description aggregation network is proposed to learn richer job title representations by leveraging diverse job description content.

## Abstract

AbstractLearning job title representation is a vital process for developing automatic human resource tools. To do so, existing methods primarily rely on learning the title representation through skills extracted from the job description, neglecting the rich and diverse content within. Thus, we propose an alternative framework for learning job titles through their respective job description (JD) and utilize a Job Description Aggregator component to handle the lengthy description and bidirectional contrastive loss to account for the bidirectional relationship between the job title and its description. We evaluated the performance of our method on both in-domain and out-of-domain settings, achieving a superior performance over the skill-based approach.