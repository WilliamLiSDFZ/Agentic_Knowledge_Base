---
title: "PACIT: Unlocking the Power of Examples for Better In-Context Instruction Tuning"
source: "https://aclanthology.org/2024.findings-acl.36/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'state-memory-replay-sequence-modeling']
tags: ['instruction-tuning', 'in-context-learning', 'example-selection']
venue: "ACL 2024"
tldr: "PACIT improves in-context instruction tuning by strategically incorporating positive and negative examples into prompts for better LLM performance."
---

# PACIT: Unlocking the Power of Examples for Better In-Context Instruction Tuning

**Source**: [https://aclanthology.org/2024.findings-acl.36/](https://aclanthology.org/2024.findings-acl.36/)

**TLDR**: PACIT improves in-context instruction tuning by strategically incorporating positive and negative examples into prompts for better LLM performance.

## Abstract

AbstractInstruction tuning enhances the instruction following ability of large language models by finetuning with supervised instruction data. Previous work proposes in-context instruction tuning (ICIT) where specific positive or negative examples are incorporated into the prompt for better performance. In this work, we propose PACIT, a simple and effective in-context instruction tuning method, inspired by the pedagogical concept of desirable difficulty. The PACIT method unlocks the power of examples by encouraging the model to actively learn to grasp the distinctions between the positive and negative examples instead of merely reading. The model is expected to first verify the correctness of the provided example according to the task description, which is then set as the condition for generating a better response to the task instance. Our extensive experiments prove the effectiveness of PACIT, outperforming ICIT baseline on both in-domain and out-domain tasks up to 9.16 and 3.14 average ROUGE-L scores, respectively. Moreover, PACIT can notably enhance the performance of instruction tuning even when all positive and negative examples are generated with a self-instruct method.