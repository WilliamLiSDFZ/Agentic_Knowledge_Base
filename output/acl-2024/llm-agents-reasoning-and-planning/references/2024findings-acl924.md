---
title: "Small Language Models Need Strong Verifiers to Self-Correct Reasoning"
source: "https://aclanthology.org/2024.findings-acl.924/"
pdf_url: ""
categories: ['llm-agents-reasoning-and-planning']
tags: ['self-correction', 'small-language-models', 'reasoning']
venue: "ACL 2024"
tldr: "Investigates self-correction in small language models, finding strong external verifiers are necessary to improve reasoning."
---

# Small Language Models Need Strong Verifiers to Self-Correct Reasoning

**Source**: [https://aclanthology.org/2024.findings-acl.924/](https://aclanthology.org/2024.findings-acl.924/)

**TLDR**: Investigates self-correction in small language models, finding strong external verifiers are necessary to improve reasoning.

## Abstract

AbstractSelf-correction has emerged as a promising solution to boost the reasoning performance of large language models (LLMs), where LLMs refine their solutions using self-generated critiques that pinpoint the errors. This work explores whether small (≤ 13B) language models (LMs) have the ability of self-correction on reasoning tasks with minimal inputs from stronger LMs. We propose a novel pipeline that prompts smaller LMs to collect self-correction data that supports the training of self-refinement abilities. First, we leverage correct solutions to guide the model in critiquing their incorrect responses. Second, the generated critiques, after filtering, are used for supervised fine-tuning of the self-correcting reasoner through solution refinement. Our experimental results show improved self-correction abilities of two models on five datasets spanning math and commonsense reasoning, with notable performance gains when paired with a strong GPT-4-based verifier, though limitations are identified when using a weak self-verifier for determining when to correct.