---
title: "Can Language Models Serve as Text-Based World Simulators?"
source: "https://aclanthology.org/2024.acl-short.1/"
pdf_url: ""
categories: ['language-models-physical-grounding-limitations', 'llm-agents-reasoning-and-planning']
tags: ['world-simulation', 'planning', 'action-prediction']
venue: "ACL 2024"
tldr: "Investigates whether language models can serve as text-based world simulators by accurately predicting state changes from actions."
---

# Can Language Models Serve as Text-Based World Simulators?

**Source**: [https://aclanthology.org/2024.acl-short.1/](https://aclanthology.org/2024.acl-short.1/)

**TLDR**: Investigates whether language models can serve as text-based world simulators by accurately predicting state changes from actions.

## Abstract

AbstractVirtual environments play a key role in benchmarking advances in complex planning and decision-making tasks but are expensive and complicated to build by hand. Can current language models themselves serve as world simulators, correctly predicting how actions change different world states, thus bypassing the need for extensive manual coding? Our goal is to answer this question in the context of text-based simulators. Our approach is to build and use a new benchmark, called ByteSized32-State-Prediction, containing a dataset of text game state transitions and accompanying game tasks. We use this to directly quantify, for the first time, how well LLMs can serve as text-based world simulators. We test GPT-4 on this dataset and find that, despite its impressive performance, it is still an unreliable world simulator without further innovations. This work thus contributes both new insights into current LLM’s capabilities and weaknesses, as well as a novel benchmark to track future progress as new models appear.