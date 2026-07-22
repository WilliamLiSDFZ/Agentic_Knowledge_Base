---
title: "Characterizing Large Language Models as Rationalizers of Knowledge-intensive Tasks"
source: "https://aclanthology.org/2024.findings-acl.484/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'causal-reasoning-and-explanation-in-nlp']
tags: ['rationale-generation', 'knowledge-intensive-tasks', 'LLM-evaluation']
venue: "ACL 2024"
tldr: "This paper characterizes LLMs as rationalizers for knowledge-intensive tasks and evaluates their ability to generate faithful rationales."
---

# Characterizing Large Language Models as Rationalizers of Knowledge-intensive Tasks

**Source**: [https://aclanthology.org/2024.findings-acl.484/](https://aclanthology.org/2024.findings-acl.484/)

**TLDR**: This paper characterizes LLMs as rationalizers for knowledge-intensive tasks and evaluates their ability to generate faithful rationales.

## Abstract

AbstractLarge language models (LLMs) are proficient at generating fluent text with minimal task-specific supervision. However, their ability to generate rationales for knowledge-intensive tasks (KITs) remains under-explored. Generating rationales for KIT solutions, such as commonsense multiple-choice QA, requires external knowledge to support predictions and refute alternate options. In this work, we consider the task of generating retrieval-augmented rationalization of KIT model predictions via external knowledge guidance within a few-shot setting. Surprisingly, crowd-workers preferred LLM-generated rationales over existing crowd-sourced rationales, generated in a similar knowledge-guided setting, on aspects such as factuality, sufficiency, and convincingness. However, fine-grained evaluation of such rationales highlights the need for further improvements in conciseness, novelty, and domain invariance. Additionally, through an expert-sourced study evaluating the reliability of the rationales, we demonstrate that humans’ trust in LLM-generated rationales erodes when communicated faithfully, i.e., without taking model prediction accuracy into account. We find that even instrumenting simple guardrails can be effective for reliable rationalization.