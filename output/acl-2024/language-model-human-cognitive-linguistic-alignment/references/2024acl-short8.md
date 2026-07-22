---
title: "Language Models Do Hard Arithmetic Tasks Easily and Hardly Do Easy Arithmetic Tasks"
source: "https://aclanthology.org/2024.acl-short.8/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'language-model-human-cognitive-linguistic-alignment']
tags: ['arithmetic-reasoning', 'llm-limitations', 'digit-prediction']
venue: "ACL 2024"
tldr: "Shows LLMs can reliably predict leading digits of large multiplications but struggle with simpler arithmetic tasks, revealing inconsistent numerical reasoning."
---

# Language Models Do Hard Arithmetic Tasks Easily and Hardly Do Easy Arithmetic Tasks

**Source**: [https://aclanthology.org/2024.acl-short.8/](https://aclanthology.org/2024.acl-short.8/)

**TLDR**: Shows LLMs can reliably predict leading digits of large multiplications but struggle with simpler arithmetic tasks, revealing inconsistent numerical reasoning.

## Abstract

AbstractThe ability (and inability) of large language models (LLMs) to perform arithmetic tasks has been the subject of much theoretical and practical debate. We show that LLMs are frequently able to correctly and confidently predict the first digit of n-digit by m-digit multiplication tasks without using chain of thought reasoning, despite these tasks require compounding operations to solve. Simultaneously, LLMs in practice often fail to correctly or confidently predict the last digit of an n-digit by m-digit multiplication, a task equivalent to 1-digit by 1-digit multiplication which can be easily learned or memorized. We show that the latter task can be solved more robustly when the LLM is conditioned on all of the correct higher-order digits, which on average increases the confidence of the correct last digit on 5-digit by 5-digit multiplication tasks using Llama 2-13B by over 230% (0.13→0.43) and Mistral-7B by 150% (0.22→0.55).