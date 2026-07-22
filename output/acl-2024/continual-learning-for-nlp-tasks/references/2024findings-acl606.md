---
title: "Efficient Continual Pre-training for Building Domain Specific Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.606/"
categories: ['continual-learning-for-nlp-tasks', 'llm-training-alignment-and-evaluation']
tags: ['continual-pretraining', 'domain-specific-llm', 'efficient-training']
venue: "ACL 2024"
tldr: "Explores continual pre-training as an efficient strategy for building domain-specific large language models."
---

# Efficient Continual Pre-training for Building Domain Specific Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.606/](https://aclanthology.org/2024.findings-acl.606/)

**TLDR**: Explores continual pre-training as an efficient strategy for building domain-specific large language models.

## Abstract

AbstractLarge language models (LLMs) have demonstrated remarkable open-domain capabilities. LLMs tailored for a domain are typically trained entirely on domain corpus to excel at handling domain-specific tasks. In this work, we explore an alternative strategy of continual pre-training as a means to develop domain-specific LLMs over an existing open-domain LLM. We introduce FinPythia-6.9B, developed through domain-adaptive continual pre-training on the financial domain.Continual pre-trained FinPythia showcases consistent improvements on financial tasks over the original foundational model. We further explore simple but effective data selection strategies for continual pre-training. Our data selection strategies outperform vanilla continual pre-training’s performance with just 10% of corpus size and cost, without any degradation on open-domain standard tasks. Our work proposes an alternative solution to building domain-specific LLMs cost-effectively.