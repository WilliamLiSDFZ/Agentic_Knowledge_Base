---
title: "Harvesting Events from Multiple Sources: Towards a Cross-Document Event Extraction Paradigm"
source: "https://aclanthology.org/2024.findings-acl.114/"
categories: ['natural-language-processing-information-extraction', 'document-understanding-and-information-extraction']
tags: ['event-extraction', 'cross-document', 'information-extraction']
venue: "ACL 2024"
tldr: "Introduces a cross-document event extraction paradigm that harvests and aggregates event information from multiple sources to reduce information bias."
---

# Harvesting Events from Multiple Sources: Towards a Cross-Document Event Extraction Paradigm

**Source**: [https://aclanthology.org/2024.findings-acl.114/](https://aclanthology.org/2024.findings-acl.114/)

**TLDR**: Introduces a cross-document event extraction paradigm that harvests and aggregates event information from multiple sources to reduce information bias.

## Abstract

AbstractDocument-level event extraction aims to extract structured event information from unstructured text. However, a single document often contains limited event information and the roles of different event arguments may be biased due to the influence of the information source.This paper addresses the limitations of traditional document-level event extraction by proposing the task of cross-document event extraction (CDEE) to integrate event information from multiple documents and provide a comprehensive perspective on events. We construct a novel cross-document event extraction dataset, namely CLES, which contains 20,059 documents and 37,688 mention-level events, where over 70% of them are cross-document. To address the task, we propose a CDEE pipeline that includes 5 steps, namely event extraction, coreference resolution, entity normalization, role normalization and entity-role resolution. Our CDEE pipeline achieves about 72% F1 in end-to-end cross-document event extraction, suggesting the challenge of this task and setting up a benchmark for future research. Our work builds a new line of information extraction research and will attract new research attention.