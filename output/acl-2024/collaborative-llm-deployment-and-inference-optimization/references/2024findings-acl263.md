---
title: "LoraRetriever: Input-Aware LoRA Retrieval and Composition for Mixed Tasks in the Wild"
source: "https://aclanthology.org/2024.findings-acl.263/"
categories: ['collaborative-llm-deployment-and-inference-optimization', 'llm-training-alignment-and-evaluation']
tags: ['LoRA', 'retrieval', 'composition', 'multi-task', 'LLM-fine-tuning']
venue: "ACL 2024"
tldr: "LoraRetriever dynamically retrieves and composes input-aware LoRA modules to handle mixed tasks for large language models."
---

# LoraRetriever: Input-Aware LoRA Retrieval and Composition for Mixed Tasks in the Wild

**Source**: [https://aclanthology.org/2024.findings-acl.263/](https://aclanthology.org/2024.findings-acl.263/)

**TLDR**: LoraRetriever dynamically retrieves and composes input-aware LoRA modules to handle mixed tasks for large language models.

## Abstract

AbstractLow-Rank Adaptation (LoRA) provides an effective yet efficient solution for fine-tuning large language models (LLMs). The modular and plug-and-play nature of LoRA enables the integration of diverse domain-specific LoRAs to enhance the capabilities of LLMs. Previous research on exploiting multiple LoRAs either focuses on specific isolated downstream tasks or fixes the selection of LoRAs during training. However, in real-world scenarios, LLMs receive diverse prompts covering different tasks, and the pool of candidate LoRAs is often dynamically updated. To bridge this gap, we propose LoraRetriever, a retrieve-then-compose framework that adaptively retrieves and composes multiple LoRAs according to the input prompts. LoraRetriever contains three main components: firstly, identifying and retrieving LoRAs relevant to the given input; secondly, formulating strategies for effectively integrating the retrieved LoRAs; and thirdly, developing efficient batch inference to accommodate heterogeneous requests. Experimental results indicate that LoraRetriever consistently outperforms the baselines, highlighting its practical effectiveness and versatility. Our code is available at https://github.com/StyxXuan/LoraRetriever.