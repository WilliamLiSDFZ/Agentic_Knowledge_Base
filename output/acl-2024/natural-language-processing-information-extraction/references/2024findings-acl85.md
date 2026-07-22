---
title: "RIFF: Learning to Rephrase Inputs for Few-shot Fine-tuning of Language Models"
source: "https://aclanthology.org/2024.findings-acl.85/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'natural-language-processing-information-extraction']
tags: ['input-rephrasing', 'few-shot-fine-tuning', 'prompt-optimization']
venue: "ACL 2024"
tldr: "Proposes RIFF, a method that learns to rephrase task inputs to improve few-shot fine-tuning of pre-trained language models."
---

# RIFF: Learning to Rephrase Inputs for Few-shot Fine-tuning of Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.85/](https://aclanthology.org/2024.findings-acl.85/)

**TLDR**: Proposes RIFF, a method that learns to rephrase task inputs to improve few-shot fine-tuning of pre-trained language models.

## Abstract

AbstractPre-trained Language Models (PLMs) can be accurately fine-tuned for downstream text processing tasks. Recently, researchers have introduced several parameter-efficient fine-tuning methods that optimize input prompts or adjust a small number of model parameters (e.g LoRA). In this study, we explore the impact of altering the input text of the original task in conjunction with parameter-efficient fine-tuning methods. To most effectively rewrite the input text, we train a few-shot paraphrase model with a Maximum-Marginal Likelihood objective. Using six few-shot text classification datasets, we show that enriching data with paraphrases at train and test time enhances the performance beyond what can be achieved with parameter-efficient fine-tuning alone. The code used for our experiments can be found at https://github.com/SaeedNajafi/RIFF.