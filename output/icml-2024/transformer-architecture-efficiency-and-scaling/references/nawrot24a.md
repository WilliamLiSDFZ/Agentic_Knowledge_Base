---
title: "Dynamic Memory Compression: Retrofitting LLMs for Accelerated Inference"
source: "https://proceedings.mlr.press/v235/nawrot24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nawrot24a/nawrot24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling']
tags: ['kv-cache-compression', 'llm-inference', 'dynamic-memory']
venue: "ICML 2024"
tldr: "Dynamic Memory Compression retrofits LLMs to adaptively compress key-value caches, accelerating autoregressive inference with minimal quality loss."
---

# Dynamic Memory Compression: Retrofitting LLMs for Accelerated Inference

**Source**: [https://proceedings.mlr.press/v235/nawrot24a.html](https://proceedings.mlr.press/v235/nawrot24a.html)

**TLDR**: Dynamic Memory Compression retrofits LLMs to adaptively compress key-value caches, accelerating autoregressive inference with minimal quality loss.

## Abstract

Transformers have emerged as the backbone of large language models (LLMs). However, generation remains inefficient due to the need to store in memory a cache of key–value representations for past tokens, whose size scales linearly with the input sequence length and batch size. As a solution, we propose Dynamic Memory Compression (DMC), a method for on-line key–value cache compression at inference time. Most importantly, the model learns to apply different compression ratios in different heads and layers. We retrofit pre-trained LLMs such as Llama 2 (7B, 13B and 70B) into DMC Transformers, achieving up to $\sim 3.7 \times$ throughput increase during auto-regressive inference on an NVIDIA H100 GPU. DMC is applied via continued pre-training on a negligible percentage of the original data without adding any extra parameters. We find that DMC preserves the original downstream performance with up to 4$\times$ cache compression, outperforming up-trained grouped-query attention (GQA) and key–value eviction policies (H$_2$O, TOVA). GQA and DMC can be even combined to obtain compounded gains. As a result DMC fits longer contexts and larger batches within any given memory budget. We release the DMC code and models at https://github.com/NVIDIA/Megatron-LM/tree/DMC.