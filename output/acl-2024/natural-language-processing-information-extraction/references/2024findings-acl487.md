---
title: "ULTRA: Unleash LLMs’ Potential for Event Argument Extraction through Hierarchical Modeling and Pair-wise Self-Refinement"
source: "https://aclanthology.org/2024.findings-acl.487/"
categories: ['natural-language-processing-information-extraction']
tags: ['event-argument-extraction', 'hierarchical-modeling', 'self-refinement']
venue: "ACL 2024"
tldr: "Proposes a hierarchical and pair-wise self-refinement framework for LLM-based event argument extraction."
---

# ULTRA: Unleash LLMs’ Potential for Event Argument Extraction through Hierarchical Modeling and Pair-wise Self-Refinement

**Source**: [https://aclanthology.org/2024.findings-acl.487/](https://aclanthology.org/2024.findings-acl.487/)

**TLDR**: Proposes a hierarchical and pair-wise self-refinement framework for LLM-based event argument extraction.

## Abstract

AbstractStructural extraction of events within discourse is critical since it avails a deeper understanding of communication patterns and behavior trends. Event argument extraction (EAE), at the core of event-centric understanding, is the task of identifying role-specific text spans (i.e., arguments) for a given event. Document-level EAE (DocEAE) focuses on arguments that are scattered across an entire document. In this work, we explore open-source Large Language Models (LLMs) for DocEAE, and propose ULTRA, a hierarchical framework that extracts event arguments more cost-effectively. Further, it alleviates the positional bias issue intrinsic to LLMs. ULTRA sequentially reads text chunks of a document to generate a candidate argument set, upon which non-pertinent candidates are dropped through self-refinement. We introduce LEAFER to address the challenge LLMs face in locating the exact boundary of an argument. ULTRA outperforms strong baselines, including strong supervised models and ChatGPT, by 9.8% when evaluated by Exact Match (EM).