---
title: "Recognizing Everything from All Modalities at Once: Grounded Multimodal Universal Information Extraction"
source: "https://aclanthology.org/2024.findings-acl.863/"
categories: ['natural-language-processing-information-extraction']
tags: ['multimodal-information-extraction', 'cross-modal-grounding', 'universal-framework']
venue: "ACL 2024"
tldr: "Introduces a unified framework for grounded multimodal universal information extraction across diverse modality combinations."
---

# Recognizing Everything from All Modalities at Once: Grounded Multimodal Universal Information Extraction

**Source**: [https://aclanthology.org/2024.findings-acl.863/](https://aclanthology.org/2024.findings-acl.863/)

**TLDR**: Introduces a unified framework for grounded multimodal universal information extraction across diverse modality combinations.

## Abstract

AbstractIn the field of information extraction (IE), tasks across a wide range of modalities and their combinations have been traditionally studied in isolation, leaving a gap in deeply recognizing and analyzing cross-modal information. To address this, this work for the first time introduces the concept of grounded Multimodal Universal Information Extraction (MUIE), providing a unified task framework to analyze any IE tasks over various modalities, along with their fine-grained groundings. To tackle MUIE, we tailor a multimodal large language model (MLLM), Reamo, capable of extracting and grounding information from all modalities, i.e., recognizing everything from all modalities at once. Reamo is updated via varied tuning strategies, equipping it with powerful capabilities for information recognition and fine-grained multimodal grounding. To address the absence of a suitable benchmark for grounded MUIE, we curate a high-quality, diverse, and challenging test set, which encompasses IE tasks across 9 common modality combinations with the corresponding multimodal groundings. The extensive comparison of Reamo with existing MLLMs integrated into pipeline approaches demonstrates its advantages across all evaluation dimensions, establishing a strong benchmark for the follow-up research. Our resources are publicly released at https://haofei.vip/MUIE.