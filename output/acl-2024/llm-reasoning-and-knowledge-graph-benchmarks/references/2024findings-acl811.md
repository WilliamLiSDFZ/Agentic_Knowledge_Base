---
title: "Exploring Reversal Mathematical Reasoning Ability for Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.811/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'llm-agents-reasoning-and-planning']
tags: ['reversal-curse', 'mathematical-reasoning', 'llm-reasoning']
venue: "ACL 2024"
tldr: "Investigates LLMs' ability to apply reversed logical structures in mathematical reasoning tasks, exposing the "reversal curse" limitation."
---

# Exploring Reversal Mathematical Reasoning Ability for Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.811/](https://aclanthology.org/2024.findings-acl.811/)

**TLDR**: Investigates LLMs' ability to apply reversed logical structures in mathematical reasoning tasks, exposing the "reversal curse" limitation.

## Abstract

AbstractLarge language models (LLMs) have presented remarkable capabilities in the wide range of natural language understanding and reasoning tasks. Despite their success, a few works indicate that LLMs suffer from the “reversal curse”, in which LLMs can’t employ the inverted structure “B is A” when they are trained based on “A is B”. To explore the effect of the “reversal curse” for LLMs on complex mathematical reasoning tasks, we present two reversal datasets upon GSM8K and MathQA and verify that LLMs also struggle to solve reversal mathematical problems. We analyze the potential reason and attribute it to the insufficient modeling of the relationship between reasoning steps caused by the left-to-right objective. Consequently, based on the characteristics of multi-step reasoning, we design a novel training method to improve the general and reversal reasoning abilities. Finally, we conduct experiments on four mathematical datasets, and the results demonstrate that our method significantly improves the general reasoning capacities and alleviates the reversal problem. Our datasets and codes are available at https: //github.com/AllForward/ReversalMath.