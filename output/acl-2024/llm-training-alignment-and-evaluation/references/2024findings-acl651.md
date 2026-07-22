---
title: "PANDA: Preference Adaptation for Enhancing Domain-Specific Abilities of LLMs"
source: "https://aclanthology.org/2024.findings-acl.651/"
categories: ['llm-training-alignment-and-evaluation']
tags: ['domain-adaptation', 'preference-learning', 'LLM', 'fine-tuning']
venue: "ACL 2024"
tldr: "PANDA enhances domain-specific LLM capabilities by adapting model preferences toward domain expert outputs without supervised fine-tuning."
---

# PANDA: Preference Adaptation for Enhancing Domain-Specific Abilities of LLMs

**Source**: [https://aclanthology.org/2024.findings-acl.651/](https://aclanthology.org/2024.findings-acl.651/)

**TLDR**: PANDA enhances domain-specific LLM capabilities by adapting model preferences toward domain expert outputs without supervised fine-tuning.

## Abstract

AbstractWhile Large language models (LLMs) have demonstrated considerable capabilities across various natural language tasks, they often fall short of the performance achieved by domain-specific state-of-the-art models. One potential approach to enhance domain-specific capabilities of LLMs involves fine-tuning them using corresponding datasets. However, this method can be both resource and time-intensive, and not applicable to closed-source commercial LLMs. In this paper, we propose Preference Adaptation for Enhancing Domain-specific Abilities of LLMs (PANDA), a method designed to augment the domain-specific capabilities of LLMs by leveraging insights from the response preference of expert models without requiring fine-tuning. Our experimental results reveal that PANDA significantly enhances the domain-specific ability of LLMs on text classification and interactive decision tasks. Moreover, LLM with PANDA even outperforms the expert model that being learned on 4 tasks of ScienceWorld. This finding highlights the potential of exploring tuning-free approaches to achieve weak-to-strong generalization.