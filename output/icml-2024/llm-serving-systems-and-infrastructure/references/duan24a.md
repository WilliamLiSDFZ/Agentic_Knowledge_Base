---
title: "MuxServe: Flexible Spatial-Temporal Multiplexing for Multiple LLM Serving"
source: "https://proceedings.mlr.press/v235/duan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/duan24a/duan24a.pdf"
categories: ['llm-serving-systems-and-infrastructure']
tags: ['LLM-serving', 'multiplexing', 'spatial-temporal', 'inference-efficiency']
venue: "ICML 2024"
tldr: "MuxServe enables efficient serving of multiple LLMs simultaneously through flexible spatial-temporal multiplexing of GPU resources."
---

# MuxServe: Flexible Spatial-Temporal Multiplexing for Multiple LLM Serving

**Source**: [https://proceedings.mlr.press/v235/duan24a.html](https://proceedings.mlr.press/v235/duan24a.html)

**TLDR**: MuxServe enables efficient serving of multiple LLMs simultaneously through flexible spatial-temporal multiplexing of GPU resources.

## Abstract

Large language models (LLMs) have demonstrated remarkable performance, and organizations are racing to serve LLMs of varying sizes as endpoints for use-cases like chat, programming and search. However, efficiently serving multiple LLMs poses significant challenges for existing approaches due to varying popularity of LLMs. In the paper, we present MuxServe, a flexible spatial-temporal multiplexing system for efficient multiple LLM serving. The key insight behind is to colocate LLMs considering their popularity to multiplex memory resources, and leverage the characteristics of prefill and decoding phases to separate and flexibly colocate them to multiplex computation resources. MuxServe formally formulates the multiplexing problem, and proposes a novel placement algorithm and adaptive batch scheduling strategy to identify optimal colocations and maximize utilization. MuxServe designs a unified resource manager to enable flexible and efficient multiplexing. Evaluation results show that MuxServe can achieves up to $1.8\times$ higher throughput or processes $2.9\times$ more requests within $99%$ SLO attainment. The code is available at: https://github.com/hao-ai-lab/MuxServe.