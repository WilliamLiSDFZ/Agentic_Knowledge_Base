---
title: "Beyond Single-Event Extraction: Towards Efficient Document-Level Multi-Event Argument Extraction"
source: "https://aclanthology.org/2024.findings-acl.564/"
pdf_url: ""
categories: ['natural-language-processing-information-extraction', 'document-understanding-and-information-extraction']
tags: ['event-extraction', 'multi-event', 'argument-extraction']
venue: "ACL 2024"
tldr: "Proposes DEEIA, a dependency-guided model for efficient document-level multi-event argument extraction that captures inter-event correlations."
---

# Beyond Single-Event Extraction: Towards Efficient Document-Level Multi-Event Argument Extraction

**Source**: [https://aclanthology.org/2024.findings-acl.564/](https://aclanthology.org/2024.findings-acl.564/)

**TLDR**: Proposes DEEIA, a dependency-guided model for efficient document-level multi-event argument extraction that captures inter-event correlations.

## Abstract

AbstractRecent mainstream event argument extraction methods process each event in isolation, resulting in inefficient inference and ignoring the correlations among multiple events. To address these limitations, here we propose a multiple-event argument extraction model DEEIA (Dependency-guided Encoding and Event-specific Information Aggregation), capable of extracting arguments from all events within a document simultaneously. The proposed DEEIA model employs a multi-event prompt mechanism, comprising DE and EIA modules. The DE module is designed to improve the correlation between prompts and their corresponding event contexts, whereas the EIA module provides event-specific information to improve contextual understanding. Extensive experiments show that our method achieves new state-of-the-art performance on four public datasets (RAMS, WikiEvents, MLEE, and ACE05), while significantly saving the inference time compared to the baselines. Further analyses demonstrate the effectiveness of the proposed modules.