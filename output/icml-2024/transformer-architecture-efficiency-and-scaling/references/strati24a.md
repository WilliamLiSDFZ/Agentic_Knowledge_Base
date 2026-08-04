---
title: "DéjàVu: KV-cache Streaming for Fast, Fault-tolerant Generative LLM Serving"
source: "https://proceedings.mlr.press/v235/strati24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/strati24a/strati24a.pdf"
categories: ['llm-serving-systems-and-infrastructure', 'transformer-architecture-efficiency-and-scaling']
tags: ['LLM-serving', 'KV-cache', 'pipeline-parallelism', 'fault-tolerance', 'inference-efficiency']
venue: "ICML 2024"
tldr: "DéjàVu introduces KV-cache streaming to reduce latency, GPU memory overprovisioning, and recovery time in distributed LLM serving."
---

# DéjàVu: KV-cache Streaming for Fast, Fault-tolerant Generative LLM Serving

**Source**: [https://proceedings.mlr.press/v235/strati24a.html](https://proceedings.mlr.press/v235/strati24a.html)

**TLDR**: DéjàVu introduces KV-cache streaming to reduce latency, GPU memory overprovisioning, and recovery time in distributed LLM serving.

## Abstract

Distributed LLM serving is costly and often underutilizes hardware accelerators due to three key challenges: bubbles in pipeline-parallel deployments caused by the bimodal latency of prompt and token processing, GPU memory overprovisioning, and long recovery times in case of failures. DéjàVu addresses all these challenges using a versatile and efficient KV cache streaming library (DéjàVuLib). Using DéjàVuLib, we propose and implement efficient prompt-token disaggregation to reduce pipeline bubbles, microbatch swapping for efficient GPU memory management, and state replication for fault-tolerance. We highlight the efficacy of these solutions on a range of large models across cloud deployments.