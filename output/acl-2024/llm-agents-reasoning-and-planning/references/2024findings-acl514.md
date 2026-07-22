---
title: "PPTC Benchmark: Evaluating Large Language Models for PowerPoint Task Completion"
source: "https://aclanthology.org/2024.findings-acl.514/"
categories: ['llm-training-alignment-and-evaluation', 'llm-agents-reasoning-and-planning']
tags: ['llm-evaluation', 'powerpoint', 'task-completion']
venue: "ACL 2024"
tldr: "PPTC is a benchmark for evaluating LLMs on multi-turn, multi-step PowerPoint task completion using complex tool APIs."
---

# PPTC Benchmark: Evaluating Large Language Models for PowerPoint Task Completion

**Source**: [https://aclanthology.org/2024.findings-acl.514/](https://aclanthology.org/2024.findings-acl.514/)

**TLDR**: PPTC is a benchmark for evaluating LLMs on multi-turn, multi-step PowerPoint task completion using complex tool APIs.

## Abstract

AbstractRecent evaluations of Large Language Models (LLMs) have centered around testing their zero-shot/few-shot capabilities for basic natural language tasks and their ability to translate instructions into tool APIs. However, the evaluation of LLMs utilizing complex tools to finish multi-turn, multi-modal instructions in a complex multi-modal environment has not been investigated. To address this gap, we introduce the PowerPoint Task Completion (PPTC) benchmark to assess LLMs’ ability to create and edit PPT files based on user instructions. It contains 279 multi-turn sessions covering diverse topics and hundreds of instructions involving multi-modal operations. We also propose the PPTX-Match Evaluation System that evaluates if LLMs finish the instruction based on the prediction file rather than the label API sequence, thus it supports various LLM-generated API sequences. We measure 3 closed LLMs and 6 open-source LLMs. The results show that GPT-4 outperforms other LLMs with 75.1% accuracy in single-turn dialogue testing but faces challenges in completing entire sessions, achieving just 6% session accuracy. We find three main error causes in our benchmark: error accumulation in the multi-turn session, long PPT template processing, and multi-modality perception. These pose great challenges for future LLM and agent systems .