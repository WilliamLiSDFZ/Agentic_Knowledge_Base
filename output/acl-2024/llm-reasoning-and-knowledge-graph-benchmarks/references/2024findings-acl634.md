---
title: "Automatic Engineering of Long Prompts"
source: "https://aclanthology.org/2024.findings-acl.634/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'llm-training-alignment-and-evaluation']
tags: ['prompt-optimization', 'automated-prompt-engineering', 'llm-instructions']
venue: "ACL 2024"
tldr: "Proposes an automated method for engineering long, complex prompts to improve LLM performance on open-domain tasks."
---

# Automatic Engineering of Long Prompts

**Source**: [https://aclanthology.org/2024.findings-acl.634/](https://aclanthology.org/2024.findings-acl.634/)

**TLDR**: Proposes an automated method for engineering long, complex prompts to improve LLM performance on open-domain tasks.

## Abstract

AbstractLarge language models (LLMs) have demonstrated remarkable capabilities in solving complex open-domain tasks, guided by comprehensive instructions and demonstrations provided in the form of prompts. However, these prompts can be lengthy, often comprising hundreds of lines and thousands of tokens, and their design often requires considerable human effort. Recent research has explored automatic prompt engineering for short prompts, typically consisting of one or a few sentences. However, the automatic design of long prompts remains a challenging problem due to its immense search space. In this paper, we propose an algorithm named Automated Prompt Engineering Xpert (APEX), a novel algorithm that automatically improves long prompts. Leveraging a greedy algorithm with beam-search for efficiency, APEX utilizes search history to significantly enhance the effectiveness of LLM-based mutation in its search process. Our results show that APEX achieves an average of 9.2% accuracy gain on eight tasks in Big Bench Hard and a consistent improvements on GSM8K with various models, highlighting the significance of automating prompt designs to fully harness the capabilities of LLMs.