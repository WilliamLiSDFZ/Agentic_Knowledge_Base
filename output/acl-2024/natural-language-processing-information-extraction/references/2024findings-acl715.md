---
title: "LC4EE: LLMs as Good Corrector for Event Extraction"
source: "https://aclanthology.org/2024.findings-acl.715/"
pdf_url: ""
categories: ['natural-language-processing-information-extraction', 'llm-hallucination-detection-and-mitigation']
tags: ['event-extraction', 'llm-correction', 'hybrid-system']
venue: "ACL 2024"
tldr: "LC4EE uses LLMs as correctors to refine outputs of specialized event extraction models, combining the strengths of both approaches."
---

# LC4EE: LLMs as Good Corrector for Event Extraction

**Source**: [https://aclanthology.org/2024.findings-acl.715/](https://aclanthology.org/2024.findings-acl.715/)

**TLDR**: LC4EE uses LLMs as correctors to refine outputs of specialized event extraction models, combining the strengths of both approaches.

## Abstract

AbstractEvent extraction (EE) is a critical task in natural language processing, yet deploying a practical EE system remains challenging. On one hand, powerful large language models (LLMs) currently show poor performance because EE task is more complex than other tasks. On the other hand, state-of-the-art (SOTA) small language models (SLMs) for EE tasks are typically developed through fine-tuning, lack flexibility, and have considerable room for improvement. We propose an approach, **L**LMs-as-**C**orrector for **E**vent **E**xtraction (**LC4EE**), aiming to leverage the superior extraction capability of SLMs and the instruction-following ability of LLMs to construct a robust and highly available EE system. By utilizing LLMs to identify and correct errors of SLMs predictions based on automatically generated feedback information, EE performances can be improved significantly. Experimental results on the representative datasets ACE2005 and MAVEN-Arg for Event Detection (ED) and EE tasks validated the effectiveness of our method.