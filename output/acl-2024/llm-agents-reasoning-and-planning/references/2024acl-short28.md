---
title: "Soft Self-Consistency Improves Language Models Agents"
source: "https://aclanthology.org/2024.acl-short.28/"
pdf_url: ""
categories: ['llm-agents-reasoning-and-planning', 'minimum-bayes-risk-decoding-efficiency']
tags: ['self-consistency', 'sampling-strategies', 'llm-agents']
venue: "ACL 2024"
tldr: "Introduces soft self-consistency to improve LLM agent performance by replacing majority voting with softer scoring across multiple solutions."
---

# Soft Self-Consistency Improves Language Models Agents

**Source**: [https://aclanthology.org/2024.acl-short.28/](https://aclanthology.org/2024.acl-short.28/)

**TLDR**: Introduces soft self-consistency to improve LLM agent performance by replacing majority voting with softer scoring across multiple solutions.

## Abstract

AbstractGenerations from large language models (LLMs) can be improved by sampling and scoring multiple solutions to select a final answer. Current “sample and select” methods such as self-consistency (SC) rely on majority voting to score answers. However, when tasks have many distinct and valid answers, selection by voting requires a large number of samples. This makes SC prohibitively expensive for interactive tasks that involve generating multiple actions (answers) sequentially. After establishing that majority voting fails to provide consistent gains on such tasks, we demonstrate how to increase success rates by softening the scoring criterion. We introduce Soft Self-Consistency (SOFT-SC), which replaces SC’s discontinuous scoring with a continuous score computed from model likelihoods, allowing for selection even when actions are sparsely distributed. SOFT-SC improves both performance and efficiency on long-horizon interactive tasks, requiring half as many samples as SC for comparable or better performance. For a fixed number of samples, SOFT-SC leads to a 1.3% increase over SC in absolute success rate on writing bash programs, a 6.6% increase on online shopping (WebShop), and a 4.7% increase for an interactive household game (ALFWorld). Finally, we show that SOFT-SC can be applied to both open-source and black-box models.