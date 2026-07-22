---
title: "Learning Fine-Grained Grounded Citations for Attributed Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.838/"
categories: ['llm-hallucination-detection-and-mitigation', 'natural-language-processing-information-extraction']
tags: ['hallucination-mitigation', 'citations', 'attributed-LLMs']
venue: "ACL 2024"
tldr: "Fine-grained grounded citations are learned to improve verifiability and reduce hallucinations in attributed large language models."
---

# Learning Fine-Grained Grounded Citations for Attributed Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.838/](https://aclanthology.org/2024.findings-acl.838/)

**TLDR**: Fine-grained grounded citations are learned to improve verifiability and reduce hallucinations in attributed large language models.

## Abstract

AbstractDespite the impressive performance on information-seeking tasks, large language models (LLMs) still struggle with hallucinations. Attributed LLMs, which augment generated text with in-line citations, demonstrate potential in mitigating hallucinations and improving verifiability. However, current approaches suffer from suboptimal citation quality due to their reliance on in-context learning. Furthermore, the practice of merely citing document identifiers complicates the process for users to pinpoint specific supporting evidence. In this work, we introduce FRONT, a training framework that teaches LLMs to generate Fine-grained grounded citations. By initially grounding fine-grained supporting quotes, which then guide the generation process, these quotes not only provide supervision signals to improve citation quality but also serve as fine-grained attributions. Experiments on the ALCE benchmark demonstrate the efficacy of FRONT in generating superior grounded responses and highly supportive citations. With LLaMA-2-7B, the framework significantly outperforms all the baselines, achieving an average of 14.21% improvement in citation quality across all datasets, even surpassing ChatGPT.