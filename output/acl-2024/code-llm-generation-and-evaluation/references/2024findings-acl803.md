---
title: "Competition-Level Problems are Effective LLM Evaluators"
source: "https://aclanthology.org/2024.findings-acl.803/"
categories: ['code-llm-generation-and-evaluation', 'llm-training-alignment-and-evaluation']
tags: ['LLM-evaluation', 'competition-problems', 'reasoning', 'code', 'data-contamination']
venue: "ACL 2024"
tldr: "This paper demonstrates that recent competition-level problems are effective evaluators of LLM reasoning capabilities while mitigating data contamination concerns."
---

# Competition-Level Problems are Effective LLM Evaluators

**Source**: [https://aclanthology.org/2024.findings-acl.803/](https://aclanthology.org/2024.findings-acl.803/)

**TLDR**: This paper demonstrates that recent competition-level problems are effective evaluators of LLM reasoning capabilities while mitigating data contamination concerns.

## Abstract

AbstractLarge language models (LLMs) have demonstrated impressive reasoning capabilities, yet there is ongoing debate about these abilities and the potential data contamination problem recently. This paper aims to evaluate the reasoning capacities of LLMs, specifically in solving recent competition-level programming problems in Codeforces, which are expert-crafted and unique, requiring deep understanding and robust reasoning skills. We first provide a comprehensive evaluation of GPT-4’s perceived zero-shot performance on this task, considering various aspects such as problems’ release time, difficulties, and types of errors encountered. Surprisingly, the perceived performance of GPT-4 has experienced a cliff like decline in problems after September 2021 consistently across all the difficulties and types of problems, which shows the potential data contamination, as well as the challenges for any existing LLM to solve unseen complex reasoning problems. We further explore various approaches such as fine-tuning, Chain-of-Thought prompting and problem description simplification. Unfortunately, none of them is able to consistently mitigate the challenges. Through our work, we emphasize the importance of this excellent data source for assessing the genuine reasoning capabilities of LLMs, and foster the development of LLMs with stronger reasoning abilities and better generalization in the future.