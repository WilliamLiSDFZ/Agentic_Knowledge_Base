---
title: "MAPLE: Multilingual Evaluation of Parameter Efficient Finetuning of Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.881/"
categories: ['llm-training-alignment-and-evaluation', 'multilingual-text-classification-and-sentiment-analysis']
tags: ['parameter-efficient-finetuning', 'multilingual-evaluation', 'llm']
venue: "ACL 2024"
tldr: "Evaluates parameter-efficient finetuning methods for LLMs across multiple languages, highlighting performance gaps beyond English."
---

# MAPLE: Multilingual Evaluation of Parameter Efficient Finetuning of Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.881/](https://aclanthology.org/2024.findings-acl.881/)

**TLDR**: Evaluates parameter-efficient finetuning methods for LLMs across multiple languages, highlighting performance gaps beyond English.

## Abstract

AbstractParameter efficient finetuning has emerged as a viable solution for improving the performance of Large Language Models without requiring massive resources and compute. Prior work on multilingual evaluation has shown that there is a large gap between the performance of LLMs on English and other languages. Further, there is also a large gap between the performance of smaller open-source models and larger LLMs. Finetuning can be an effective way to bridge this gap and make language models more equitable. In this work, we finetune the Llama-2 and Mistral models on two synthetic multilingual instruction tuning datasets to determine its effect on model performance on six downstream tasks covering forty one languages in all. Additionally, we experiment with various parameters, such as rank for low-rank adaptation and values of quantisation to determine their effects on downstream performance and find that higher rank and higher quantisation values benefit low-resource languages. We find that parameter efficient finetuning of smaller open-source models sometimes bridges the gap between the performance of these models and the larger ones, however, English performance can take a hit. We also find that finetuning sometimes improves performance on low-resource languages, while degrading performance on high-resource languages.