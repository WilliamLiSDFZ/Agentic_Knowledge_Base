---
title: "Active Prompting with Chain-of-Thought for Large Language Models"
source: "https://aclanthology.org/2024.acl-long.73/"
categories: ['llm-agents-reasoning-and-planning', 'llm-training-alignment-and-evaluation']
tags: ['chain-of-thought', 'active-prompting', 'reasoning', 'LLM', 'uncertainty']
venue: "ACL 2024"
tldr: "Introduces active prompting with chain-of-thought by selecting the most uncertain questions for annotation to improve LLM reasoning."
---

# Active Prompting with Chain-of-Thought for Large Language Models

**Source**: [https://aclanthology.org/2024.acl-long.73/](https://aclanthology.org/2024.acl-long.73/)

**TLDR**: Introduces active prompting with chain-of-thought by selecting the most uncertain questions for annotation to improve LLM reasoning.

## Abstract

AbstractThe increasing scale of large language models (LLMs) brings emergent abilities to various complex tasks requiring reasoning, such as arithmetic and commonsense reasoning. It is known that the effective design of task-specific prompts is critical for LLMs’ ability to produce high-quality answers. In particular, an effective approach for complex question-and-answering tasks is example-based prompting with chain-of-thought (CoT) reasoning, which significantly improves the performance of LLMs. However, current CoT methods rely on a fixed set of human-annotated exemplars, which are not necessarily the most effective examples for different tasks. This paper proposes a new method, Active-Prompt, to adapt LLMs to different tasks with task-specific example prompts (annotated with human-designed CoT reasoning). For this purpose, we propose a solution to the key problem of determining which questions are the most important and helpful to annotate from a pool of task-specific queries. By borrowing ideas from the related problem of uncertainty-based active learning, we introduce several metrics to characterize the uncertainty so as to select the most uncertain questions for annotation. Experimental results demonstrate the superiority of our proposed method, achieving superior performance on eight complex reasoning tasks. Further analyses of different uncertainty metrics, pool sizes, zero-shot learning, and accuracy-uncertainty relationships demonstrate the effectiveness of our method.