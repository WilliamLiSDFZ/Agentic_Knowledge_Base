---
title: "Prompt Engineering a Prompt Engineer"
source: "https://aclanthology.org/2024.findings-acl.21/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'llm-agents-reasoning-and-planning']
tags: ['prompt-engineering', 'automated-optimization', 'LLM-reasoning']
venue: "ACL 2024"
tldr: "Proposes a meta-framework that uses LLMs to automatically engineer and optimize prompts for downstream tasks."
---

# Prompt Engineering a Prompt Engineer

**Source**: [https://aclanthology.org/2024.findings-acl.21/](https://aclanthology.org/2024.findings-acl.21/)

**TLDR**: Proposes a meta-framework that uses LLMs to automatically engineer and optimize prompts for downstream tasks.

## Abstract

AbstractPrompt engineering is a challenging yet crucial task for optimizing the performance of large language models on customized tasks. It requires complex reasoning to examine the model’s errors, hypothesize what is missing or misleading in the current prompt, and communicate the task with clarity. While recent works indicate that large language models can be meta-prompted to perform automatic prompt engineering, we argue that their potential is limited due to insufficient guidance for complex reasoning in the meta-prompt. We fill this gap by infusing into the meta-prompt three key components: detailed descriptions, context specification, and a step-by-step reasoning template. The resulting method, named PE2, showcases remarkable versatility across diverse language tasks. It finds prompts that outperform “let’s think step by step” by 6.3% on MultiArith and 3.1% on GSM8K, and outperforms competitive baselines on counterfactual tasks by 6.9%. Further, we show that PE2 can make targeted prompt edits, rectify erroneous prompts, and induce multi-step plans for complex tasks.