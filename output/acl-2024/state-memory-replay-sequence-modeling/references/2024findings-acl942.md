---
title: "No perspective, no perception!! Perspective-aware Healthcare Answer Summarization"
source: "https://aclanthology.org/2024.findings-acl.942/"
pdf_url: ""
categories: ['llms-for-biomedical-and-clinical-nlp', 'state-memory-replay-sequence-modeling']
tags: ['healthcare-QA', 'perspective-aware', 'answer-summarization']
venue: "ACL 2024"
tldr: "Proposes perspective-aware summarization of healthcare community forum answers to address different stakeholder viewpoints."
---

# No perspective, no perception!! Perspective-aware Healthcare Answer Summarization

**Source**: [https://aclanthology.org/2024.findings-acl.942/](https://aclanthology.org/2024.findings-acl.942/)

**TLDR**: Proposes perspective-aware summarization of healthcare community forum answers to address different stakeholder viewpoints.

## Abstract

AbstractHealthcare Community Question Answering (CQA) forums offer an accessible platform for individuals seeking information on various healthcare-related topics. People find such platforms suitable for self-disclosure, seeking medical opinions, finding simplified explanations for their medical conditions, and answering others’ questions. However, answers on these forums are typically diverse and prone to off-topic discussions. It can be challenging for readers to sift through numerous answers and extract meaningful insights, making answer summarization a crucial task for CQA forums. While several efforts have been made to summarize the community answers, most of them are limited to the open domain and overlook the different perspectives offered by these answers. To address this problem, this paper proposes a novel task of perspective-specific answer summarization. We identify various perspectives, within healthcare-related responses and frame a perspective-driven abstractive summary covering all responses. To achieve this, we annotate 3167 CQA threads with 6193 perspective-aware summaries in our PUMA dataset. Further, we propose PLASMA, a prompt-driven controllable summarization model. To encapsulate the perspective-specific conditions, we design an energy-controlled loss function for the optimization. We also leverage the prefix tuner to learn the intricacies of the healthcare perspective summarization. Our evaluation against five baselines suggests the superior performance of PLASMA by a margin of ~1.5 - 21% improvement. We supplement our experiments with ablation and qualitative analysis.