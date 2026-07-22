---
title: "PiVe: Prompting with Iterative Verification Improving Graph-based Generative Capability of LLMs"
source: "https://aclanthology.org/2024.findings-acl.400/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'llm-agents-reasoning-and-planning']
tags: ['graph-generation', 'iterative-verification', 'structured-data']
venue: "ACL 2024"
tldr: "PiVe uses iterative verification prompting to improve LLM performance on structured graph-based generation tasks."
---

# PiVe: Prompting with Iterative Verification Improving Graph-based Generative Capability of LLMs

**Source**: [https://aclanthology.org/2024.findings-acl.400/](https://aclanthology.org/2024.findings-acl.400/)

**TLDR**: PiVe uses iterative verification prompting to improve LLM performance on structured graph-based generation tasks.

## Abstract

AbstractLarge language models (LLMs) have shown great abilities of solving various natural language tasks in different domains. Due to the training objective of LLMs and their pre-training data, LLMs are not very well equipped for tasks involving structured data generation. We propose a framework, Prompting with Iterative Verification (PiVe), to improve graph-based generative capability of LLMs. We show how a small language model could be trained to act as a verifier module for the output of an LLM(i.e., ChatGPT, GPT-4), and to iteratively improve its performance via fine-grained corrective instructions. We also show how the verifier module could apply iterative corrections offline for a more cost-effective solution to the text-to-graph generation task. Experiments on three graph-based datasets show consistent improvement gained via PiVe. Additionally, we create GenWiki-HIQ and highlight that the verifier module can be used as a data augmentation tool to help improve the quality of automatically generated parallel text-graph datasets.