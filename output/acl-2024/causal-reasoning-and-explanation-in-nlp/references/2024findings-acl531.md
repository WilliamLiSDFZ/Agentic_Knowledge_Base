---
title: "EVIT: Event-Oriented Instruction Tuning for Event Reasoning"
source: "https://aclanthology.org/2024.findings-acl.531/"
pdf_url: ""
categories: ['llm-agents-reasoning-and-planning', 'causal-reasoning-and-explanation-in-nlp']
tags: ['event-reasoning', 'instruction-tuning', 'event-relations']
venue: "ACL 2024"
tldr: "EVIT introduces event-oriented instruction tuning to improve LLMs' ability to reason about event relations and predict future events."
---

# EVIT: Event-Oriented Instruction Tuning for Event Reasoning

**Source**: [https://aclanthology.org/2024.findings-acl.531/](https://aclanthology.org/2024.findings-acl.531/)

**TLDR**: EVIT introduces event-oriented instruction tuning to improve LLMs' ability to reason about event relations and predict future events.

## Abstract

AbstractEvents refer to specific occurrences, incidents, or happenings that take place under a particular background. Event reasoning aims to infer events according to certain relations and predict future events. The cutting-edge techniques for event reasoning play a crucial role in various natural language processing applications. Large language models (LLMs) have made significant advancements in event reasoning owing to their wealth of knowledge and reasoning capabilities. However, smaller instruction-tuned models currently in use do not consistently demonstrate exceptional proficiency in managing these tasks. This discrepancy arises from the absence of explicit modeling of events and the interconnections of them within their instruction data. Consequently, these models face challenges in comprehending event structures and semantics while struggling to bridge the gap between their interpretations and human understanding of events. Additionally, their limitations in grasping event relations lead to constrained event reasoning abilities to effectively deduce and incorporate pertinent event knowledge. In this paper, we propose Event-Oriented Instruction Tuning to train our large language model named EvIT specializing in event reasoning tasks. Specifically, we first propose a novel structure named event quadruple which contains the structure and semantics of events and is complete in the event representation. We then design event-relation learning based on the structures. We encapsulate the learning into the instruction-tuning formulation to better stimulate the event reasoning capacity of our model. To implement our training, we design a heuristic unsupervised method to mine event quadruple from a large-scale corpus. At last, we finetune a Llama model on our Event-Oriented Instruction Tuning. We conduct extensive experiments on event reasoning tasks on several datasets. Automatic and human evaluations demonstrate EvIT achieves competitive performances on event reasoning.