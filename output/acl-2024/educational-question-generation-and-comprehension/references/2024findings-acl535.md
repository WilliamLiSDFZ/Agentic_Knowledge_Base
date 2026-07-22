---
title: "Towards Better Question Generation in QA-based Event Extraction"
source: "https://aclanthology.org/2024.findings-acl.535/"
pdf_url: ""
categories: ['natural-language-processing-information-extraction', 'educational-question-generation-and-comprehension']
tags: ['event-extraction', 'question-generation', 'qa-based-methods']
venue: "ACL 2024"
tldr: "Improves QA-based event extraction by addressing limitations in question generation quality for identifying event arguments."
---

# Towards Better Question Generation in QA-based Event Extraction

**Source**: [https://aclanthology.org/2024.findings-acl.535/](https://aclanthology.org/2024.findings-acl.535/)

**TLDR**: Improves QA-based event extraction by addressing limitations in question generation quality for identifying event arguments.

## Abstract

AbstractEvent Extraction (EE) is an essential information extraction task that aims to extract event-related information from unstructured texts.The paradigm of this task has shifted from conventional classification-based methods to more contemporary question-answering-based (QA-based) approaches. However, in QA-based EE, the quality of the questions dramatically affects the extraction accuracy, and how to generate high-quality questions for QA-based EE remains a challenge. In this work, to tackle this challenge, we suggest four criteria to evaluate the quality of a question and propose a reinforcement learning method, RLQG, for QA-based EE that can generate generalizable, high-quality, and context-dependent questions and provides clear guidance to QA models. The extensive experiments conducted on ACE and RAMS datasets have strongly validated our approach’s effectiveness, which also demonstrates its robustness in scenarios with limited training data. The corresponding code of RLQG is released for further research.