---
title: "RAM-EHR: Retrieval Augmentation Meets Clinical Predictions on Electronic Health Records"
source: "https://aclanthology.org/2024.acl-short.68/"
pdf_url: ""
categories: ['llms-for-biomedical-and-clinical-nlp']
tags: ['retrieval-augmentation', 'electronic-health-records', 'clinical-prediction']
venue: "ACL 2024"
tldr: "RAM-EHR augments clinical EHR predictions by retrieving relevant medical knowledge through dense retrieval over multiple knowledge sources."
---

# RAM-EHR: Retrieval Augmentation Meets Clinical Predictions on Electronic Health Records

**Source**: [https://aclanthology.org/2024.acl-short.68/](https://aclanthology.org/2024.acl-short.68/)

**TLDR**: RAM-EHR augments clinical EHR predictions by retrieving relevant medical knowledge through dense retrieval over multiple knowledge sources.

## Abstract

AbstractWe present RAM-EHR, a Retrieval AugMentation pipeline to improve clinical predictions on Electronic Health Records (EHRs). RAM-EHR first collects multiple knowledge sources, converts them into text format, and uses dense retrieval to obtain information related to medical concepts. This strategy addresses the difficulties associated with complex names for the concepts. RAM-EHR then augments the local EHR predictive model co-trained with consistency regularization to capture complementary information from patient visits and summarized knowledge. Experiments on two EHR datasets show the efficacy of RAM-EHR over previous knowledge-enhanced baselines (3.4% gain in AUROC and 7.2% gain in AUPR), emphasizing the effectiveness of the summarized knowledge from RAM-EHR for clinical prediction tasks.