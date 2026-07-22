---
title: "Thinking about how to extract: Energizing LLMs’ emergence capabilities for document-level event argument extraction"
source: "https://aclanthology.org/2024.findings-acl.328/"
categories: ['natural-language-processing-information-extraction', 'llm-agents-reasoning-and-planning']
tags: ['event-argument-extraction', 'document-level', 'LLM', 'emergence-capabilities', 'information-extraction']
venue: "ACL 2024"
tldr: "This paper leverages emergent LLM capabilities with a structured prompting approach to address key-feature forgetting and cross-event confusion in document-level event argument extraction."
---

# Thinking about how to extract: Energizing LLMs’ emergence capabilities for document-level event argument extraction

**Source**: [https://aclanthology.org/2024.findings-acl.328/](https://aclanthology.org/2024.findings-acl.328/)

**TLDR**: This paper leverages emergent LLM capabilities with a structured prompting approach to address key-feature forgetting and cross-event confusion in document-level event argument extraction.

## Abstract

AbstractThere are two key challenges remaining for the document-level event argument extraction (D-EAE) tasks: key feature forgetting and cross-event argument confusion. The emergence capability of large language models (LLMs) holds promise for solving the above two challenges. In this paper, we propose a document-level event argument extraction method based on guided summarization and reasoning (EAESR), which leverages the emergence capabilities of LLMs to highlight key event information and to clarify the explicit and implicit association between multiple events. Specifically, we generate document summarization information that shorten the length of the event context while preserving the key event features. In addition, we generate inter-event reasoning information, which helps EAESR make sense of the correlations between events and reduces their dependence on the event context, especially to better cope with the few-shot D-EAE task. Then, we obtain named entity information to enable EAESR to learn argument boundary features to improve the sensitivity of its argument boundary recognition. Eventually, we fused the above features and sentence features to make EAESR have summarizing and reasoning capabilities simultaneously. Extensive experiments on WIKIEVENTS and RAMS have shown that EAESR achieves a new state-of-the-art that outperforms the baseline models by 1.3% F1 and 1.6% F1, respectively, and averages 11% F1 in few-shot settings.