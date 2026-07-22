---
title: "Speech-based Slot Filling using Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.379/"
categories: ['lexical-semantic-change-detection-methods', 'natural-language-processing-information-extraction']
tags: ['slot-filling', 'ASR', 'large-language-models']
venue: "ACL 2024"
tldr: "LLMs are applied to speech-based slot filling with noisy ASR transcriptions via in-context learning and fine-tuning."
---

# Speech-based Slot Filling using Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.379/](https://aclanthology.org/2024.findings-acl.379/)

**TLDR**: LLMs are applied to speech-based slot filling with noisy ASR transcriptions via in-context learning and fine-tuning.

## Abstract

AbstractRecently, advancements in large language models (LLMs) have shown an unprecedented ability across various language tasks. This paper investigates the potential application of LLMs to slot filling with noisy ASR transcriptions, via both in-context learning and task-specific fine-tuning. Dedicated prompt designs and noise-robust LoRA fine-tuning are proposed to improve the robustness of LLMs for slot filling with noisy ASR transcriptions. Moreover, a linearised knowledge injection (LKI) scheme is also proposed to integrate dynamic external knowledge into LLMs. Experiments were performed on SLURP to quantify the performance of LLMs, including GPT-3.5-turbo, GPT-4, LLaMA-13B, LLaMA-2-13B and Vicuna-13B (v1.1 and v1.5) with different ASR error rates. The use of the noise-robust fine-tuning together with LKI for Vicuna-13B-v1.5 achieved 6.7% and 17.6% absolute SLU-F1 improvements compared to a fully fine-tuned Flan-T5-XL model on the limited data setup and the zero-shot setup respectively.