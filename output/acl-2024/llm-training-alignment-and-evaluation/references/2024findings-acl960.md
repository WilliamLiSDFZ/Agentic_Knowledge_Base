---
title: "Sowing the Wind, Reaping the Whirlwind: The Impact of Editing Language Models"
source: "https://aclanthology.org/2024.findings-acl.960/"
pdf_url: ""
categories: ['llm-security-robustness-and-detection', 'llm-training-alignment-and-evaluation']
tags: ['red-teaming', 'knowledge-editing', 'LLM-safety']
venue: "ACL 2024"
tldr: "Investigates how knowledge editing in LLMs affects safety and robustness against red-teaming and jailbreaking attacks."
---

# Sowing the Wind, Reaping the Whirlwind: The Impact of Editing Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.960/](https://aclanthology.org/2024.findings-acl.960/)

**TLDR**: Investigates how knowledge editing in LLMs affects safety and robustness against red-teaming and jailbreaking attacks.

## Abstract

AbstractIn the rapidly advancing field of artificial intelligence, the concept of ‘Red-Teaming’ or ‘Jailbreaking’ large language models (LLMs) has emerged as a crucial area of study. This approach is especially significant in terms of assessing and enhancing the safety and robustness of these models. This paper investigates the intricate consequences of such modifications through model editing, uncovering a complex relationship between enhancing model accuracy and preserving its ethical integrity. Our in-depth analysis reveals a striking paradox: while injecting accurate information is crucial for model reliability, it can paradoxically destabilize the model’s foundational framework, resulting in unpredictable and potentially unsafe behaviors. Additionally, we propose a benchmark dataset NicheHazardQA to investigate this unsafe behavior both within the same and cross topical domain. This aspect of our research sheds light on how the edits, impact the model’s safety metrics and guardrails. Our findings show that model editing serves as a cost-effective tool for topical red-teaming by methodically applying targeted edits and evaluating the resultant model behavior.