---
title: "It’s Not Easy Being Wrong: Large Language Models Struggle with Process of Elimination Reasoning"
source: "https://aclanthology.org/2024.findings-acl.604/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['chain-of-thought', 'process-of-elimination', 'reasoning']
venue: "ACL 2024"
tldr: "Demonstrates that LLMs struggle with process-of-elimination reasoning using chain-of-thought prompting toward incorrect answers."
---

# It’s Not Easy Being Wrong: Large Language Models Struggle with Process of Elimination Reasoning

**Source**: [https://aclanthology.org/2024.findings-acl.604/](https://aclanthology.org/2024.findings-acl.604/)

**TLDR**: Demonstrates that LLMs struggle with process-of-elimination reasoning using chain-of-thought prompting toward incorrect answers.

## Abstract

AbstractChain-of-thought (COT) prompting can help large language models (LLMs) reason toward correct answers, but its efficacy in reasoning toward incorrect answers is unexplored. This process of elimination (PoE), when used with COT, can enhance self-consistency, interpretability, and tasks such as medical diagnoses of exclusion. Thus, we propose PoE with COT, where LLMs must reason toward incorrect options on multiple-choice questions. We evaluate the ability of GPT-3.5, LLaMA-2, and Falcon to perform PoE with COT on a total of four commonsense and scientific reasoning datasets. We find that the strategy of PoE always underperforms the strategy of choosing the correct answer. The agreement of these strategies is also lower than the self-consistency of each strategy. To study these issues further, we conduct error analyses and give suggestions for future work.