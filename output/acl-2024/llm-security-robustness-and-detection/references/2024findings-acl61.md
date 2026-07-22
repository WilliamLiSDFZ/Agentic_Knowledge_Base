---
title: "Realistic Evaluation of Toxicity in Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.61/"
categories: ['hate-speech-and-toxic-content-detection', 'llm-security-robustness-and-detection']
tags: ['toxicity', 'LLM-evaluation', 'bias', 'realistic-evaluation', 'safety']
venue: "ACL 2024"
tldr: "Evaluates toxicity in large language models under realistic conditions, revealing gaps between benchmark scores and real-world toxic outputs."
---

# Realistic Evaluation of Toxicity in Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.61/](https://aclanthology.org/2024.findings-acl.61/)

**TLDR**: Evaluates toxicity in large language models under realistic conditions, revealing gaps between benchmark scores and real-world toxic outputs.

## Abstract

AbstractLarge language models (LLMs) have become integral to our professional workflows and daily lives. Nevertheless, these machine companions of ours have a critical flaw: the huge amount of data which endows them with vast and diverse knowledge, also exposes them to the inevitable toxicity and bias. While most LLMs incorporate defense mechanisms to prevent the generation of harmful content, these safeguards can be easily bypassed with minimal prompt engineering. In this paper, we introduce the new Thoroughly Engineered Toxicity (TET) dataset, comprising manually crafted prompts designed to nullify the protective layers of such models. Through extensive evaluations, we demonstrate the pivotal role of TET in providing a rigorous benchmark for evaluation of toxicity awareness in several popular LLMs: it highlights the toxicity in the LLMs that might remain hidden when using normal prompts, thus revealing subtler issues in their behavior.