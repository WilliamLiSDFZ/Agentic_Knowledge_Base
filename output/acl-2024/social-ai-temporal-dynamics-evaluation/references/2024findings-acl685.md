---
title: "TimeToM: Temporal Space is the Key to Unlocking the Door of Large Language Models’ Theory-of-Mind"
source: "https://aclanthology.org/2024.findings-acl.685/"
pdf_url: ""
categories: ['language-model-human-cognitive-linguistic-alignment', 'social-ai-temporal-dynamics-evaluation']
tags: ['theory-of-mind', 'temporal-reasoning', 'llm', 'social-cognition', 'mental-state-reasoning']
venue: "ACL 2024"
tldr: "TimeToM introduces temporal space modeling to unlock LLMs' theory-of-mind capabilities for reasoning about dynamic mental states."
---

# TimeToM: Temporal Space is the Key to Unlocking the Door of Large Language Models’ Theory-of-Mind

**Source**: [https://aclanthology.org/2024.findings-acl.685/](https://aclanthology.org/2024.findings-acl.685/)

**TLDR**: TimeToM introduces temporal space modeling to unlock LLMs' theory-of-mind capabilities for reasoning about dynamic mental states.

## Abstract

AbstractTheory of Mind (ToM)—the cognitive ability to reason about mental states of ourselves and others, is the foundation of social interaction. Although ToM comes naturally to humans, it poses a significant challenge to even the most advanced Large Language Models (LLMs). Due to the complex logical chains in ToM reasoning, especially in higher-order ToM questions, simply utilizing reasoning methods like Chain of Thought (CoT) will not improve the ToM capabilities of LLMs. We present TimeToM, which constructs a temporal space and uses it as the foundation to improve the ToM capabilities of LLMs in multiple scenarios. Specifically, within the temporal space, we construct Temporal Belief State Chain (TBSC) for each character and inspired by the cognition perspective of the social world model, we divide TBSC into self-world beliefs and social world beliefs, aligning with first-order ToM (first-order beliefs) and higher-order ToM (higher-order beliefs) questions, respectively. Moreover, we design a novel tool-belief solver that, by considering belief communication between characters in temporal space, can transform a character’s higher-order beliefs into another character’s first-order beliefs under belief communication period.