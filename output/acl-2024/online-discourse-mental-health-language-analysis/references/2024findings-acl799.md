---
title: "InstructEval: Instruction-Tuned Text Evaluator from Human Preference"
source: "https://aclanthology.org/2024.findings-acl.799/"
categories: ['llm-training-alignment-and-evaluation', 'online-discourse-mental-health-language-analysis']
tags: ['text-evaluation', 'instruction-tuning', 'human-preference']
venue: "ACL 2024"
tldr: "Introduces InstructEval, an instruction-tuned open-source text evaluator aligned with human preferences for general NLP evaluation."
---

# InstructEval: Instruction-Tuned Text Evaluator from Human Preference

**Source**: [https://aclanthology.org/2024.findings-acl.799/](https://aclanthology.org/2024.findings-acl.799/)

**TLDR**: Introduces InstructEval, an instruction-tuned open-source text evaluator aligned with human preferences for general NLP evaluation.

## Abstract

AbstractThis paper explores to construct a general text evaluator based on open-source Large Language Models (LLMs), a domain predominantly occupied by commercial counterparts such as GPT-4. Recognizing the limitations of open-source models like Llama in evaluative tasks, we introduce InstructEval, a general multi-aspect text evaluator developed through instruction tuning of open-source LLMs. To overcome the shortage of annotated resources for multi-aspect evaluations, InstructEval combines extensive open Human Preference Modeling (HPM) datasets with a small set of multi-aspect annotated data.This approach not only enhances effectiveness in overall evaluation tasks but also exhibits improved performance in multi-aspect evaluation tasks.As demonstrated by our extensive experiments, InstructEval achieves comparable or superior performance to commercial LLMs like ChatGPT or GPT-4 in terms of both overall and multi-aspect evaluation.