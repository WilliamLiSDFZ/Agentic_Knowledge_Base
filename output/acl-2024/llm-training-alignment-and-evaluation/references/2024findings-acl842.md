---
title: "Self-Para-Consistency: Improving Reasoning Tasks at Low Cost for Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.842/"
pdf_url: ""
categories: ['llm-agents-reasoning-and-planning', 'llm-training-alignment-and-evaluation']
tags: ['self-consistency', 'reasoning', 'paraphrase', 'low-cost', 'chain-of-thought']
venue: "ACL 2024"
tldr: "Proposes self-para-consistency, a cost-efficient reasoning improvement method using paraphrased prompts instead of repeated sampling."
---

# Self-Para-Consistency: Improving Reasoning Tasks at Low Cost for Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.842/](https://aclanthology.org/2024.findings-acl.842/)

**TLDR**: Proposes self-para-consistency, a cost-efficient reasoning improvement method using paraphrased prompts instead of repeated sampling.

## Abstract

AbstractRecently, the self-consistency decoding strategy has shown the ability to improve performance for complex reasoning tasks with large language models (LLMs). However, the costs may be high because the sampling process of the strategy generates some low-probability text, resulting in low-quality reasoning paths. As a consequence, it requires a relatively large sampling number to obtain good aggregation performance. In this paper, we propose an alternative strategy, self-para-consistency. It first generates multiple paraphrases for each test question, then generates reasoning paths for the original and all the paraphrased questions based on greedy decoding, and finally selects the most consistent answer. Since all the candidate paths have relatively high probabilities, the sampling number could be much smaller than the self-consistency strategy. Extensive experiments on complex reasoning datasets demonstrate the effectiveness of our method in reducing the sampling number.