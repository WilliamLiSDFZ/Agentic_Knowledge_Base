---
title: "MedAgents: Large Language Models as Collaborators for Zero-shot Medical Reasoning"
source: "https://aclanthology.org/2024.findings-acl.33/"
pdf_url: ""
categories: ['llms-for-biomedical-and-clinical-nlp', 'llm-agents-reasoning-and-planning']
tags: ['medical-reasoning', 'multi-agent', 'zero-shot']
venue: "ACL 2024"
tldr: "Introduces MedAgents, a framework where multiple LLM agents collaborate for zero-shot medical reasoning and decision-making."
---

# MedAgents: Large Language Models as Collaborators for Zero-shot Medical Reasoning

**Source**: [https://aclanthology.org/2024.findings-acl.33/](https://aclanthology.org/2024.findings-acl.33/)

**TLDR**: Introduces MedAgents, a framework where multiple LLM agents collaborate for zero-shot medical reasoning and decision-making.

## Abstract

AbstractLarge language models (LLMs), despite their remarkable progress across various general domains, encounter significant barriers in medicine and healthcare. This field faces unique challenges such as domain-specific terminologies and reasoning over specialized knowledge. To address these issues, we propose MedAgents, a novel multi-disciplinary collaboration framework for the medical domain. MedAgents leverages LLM-based agents in a role-playing setting that participate in a collaborative multi-round discussion, thereby enhancing LLM proficiency and reasoning capabilities. This training-free framework encompasses five critical steps: gathering domain experts, proposing individual analyses, summarising these analyses into a report, iterating over discussions until a consensus is reached, and ultimately making a decision. Our work focuses on the zero-shot setting, which is applicable in real-world scenarios. Experimental results on nine datasets (MedQA, MedMCQA, PubMedQA, and six subtasks from MMLU) establish that our proposed MedAgents framework excels at mining and harnessing the medical expertise within LLMs, as well as extending its reasoning abilities. Our code can be found at https://github.com/gersteinlab/MedAgents.