---
title: "JORA: JAX Tensor-Parallel LoRA Library for Retrieval Augmented Fine-Tuning"
source: "https://aclanthology.org/2024.acl-demos.15/"
pdf_url: ""
categories: ['collaborative-llm-deployment-and-inference-optimization']
tags: ['retrieval-augmented-generation', 'lora', 'tensor-parallelism']
venue: "ACL 2024"
tldr: "JORA is a JAX-based tensor-parallel LoRA library enabling memory-efficient fine-tuning of large LLMs for retrieval-augmented generation tasks."
---

# JORA: JAX Tensor-Parallel LoRA Library for Retrieval Augmented Fine-Tuning

**Source**: [https://aclanthology.org/2024.acl-demos.15/](https://aclanthology.org/2024.acl-demos.15/)

**TLDR**: JORA is a JAX-based tensor-parallel LoRA library enabling memory-efficient fine-tuning of large LLMs for retrieval-augmented generation tasks.

## Abstract

AbstractThe scaling of Large Language Models (LLMs) for retrieval-based tasks, particularly in Retrieval Augmented Generation (RAG), faces significant memory constraints, especially when fine-tuning extensive prompt sequences. Current open-source libraries support full-model inference and fine-tuning across multiple GPUs but fall short of accommodating the efficient parameter distribution required for retrieved context. Addressing this gap, we introduce a novel framework for PEFT-compatible fine-tuning of GPT models, leveraging distributed training. Our framework uniquely utilizes JAX’s just-in-time (JIT) compilation and tensor-sharding for efficient resource management, thereby enabling accelerated fine-tuning with reduced memory requirements. This advancement significantly improves the scalability and feasibility of fine-tuning LLMs for complex RAG applications, even on systems with limited GPU resources. Our experiments show more than 12x improvement in runtime compared to Hugging Face/DeepSpeed implementation with four GPUs while consuming less than half the VRAM per GPU.