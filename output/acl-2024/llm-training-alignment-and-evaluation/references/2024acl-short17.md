---
title: "DDPrompt: Differential Diversity Prompting in Large Language Models"
source: "https://aclanthology.org/2024.acl-short.17/"
categories: ['llm-agents-reasoning-and-planning', 'llm-training-alignment-and-evaluation']
tags: ['chain-of-thought', 'differential-prompting', 'llm-reasoning']
venue: "ACL 2024"
tldr: "DDPrompt improves LLM reasoning by designing differential and diverse prompts tailored to the varying characteristics of different question types."
---

# DDPrompt: Differential Diversity Prompting in Large Language Models

**Source**: [https://aclanthology.org/2024.acl-short.17/](https://aclanthology.org/2024.acl-short.17/)

**TLDR**: DDPrompt improves LLM reasoning by designing differential and diverse prompts tailored to the varying characteristics of different question types.

## Abstract

AbstractLarge Language Models (LLMs) have shown that their reasoning ability could be enhanced through approaches like Chain-of-Thought (CoT) prompting. However, these methods use single prompts for different types of questions and do not design appropriate prompts for questions with different characteristics. In this paper, we aim to explore a methodology that generates differentially diverse reasoning paths for different types of questions. To achieve this, we propose a novel prompting strategy called Differential Diversity Prompting (DDPrompt). Firstly, we generate the optimal prompts collection based on question characteristics. Then, we use this optimal prompts collection to generate multiple answers for a question and choose the final answer by voting. We evaluated DDPrompt on twelve reasoning benchmarks and significant improvement in the performance of LLMs on complex reasoning tasks (e.g., GSM8K 75%->84%, Tracking Shuffled Objects (68.8%->83.9%))