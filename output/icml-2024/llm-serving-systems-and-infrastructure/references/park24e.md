---
title: "Any-Precision LLM: Low-Cost Deployment of Multiple, Different-Sized LLMs"
source: "https://proceedings.mlr.press/v235/park24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/park24e/park24e.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'llm-serving-systems-and-infrastructure']
tags: ['LLM-compression', 'quantization', 'any-precision', 'efficient-deployment']
venue: "ICML 2024"
tldr: "Introduces Any-Precision LLM, a low-cost framework for deploying multiple LLMs of different sizes by enabling any-precision quantization from a single model."
---

# Any-Precision LLM: Low-Cost Deployment of Multiple, Different-Sized LLMs

**Source**: [https://proceedings.mlr.press/v235/park24e.html](https://proceedings.mlr.press/v235/park24e.html)

**TLDR**: Introduces Any-Precision LLM, a low-cost framework for deploying multiple LLMs of different sizes by enabling any-precision quantization from a single model.

## Abstract

Recently, considerable efforts have been directed towards compressing Large Language Models (LLMs), which showcase groundbreaking capabilities across diverse applications but entail significant deployment costs due to their large sizes. Meanwhile, much less attention has been given to mitigating the costs associated with deploying multiple LLMs of varying sizes despite its practical significance. Thus, this paper introduces any-precision LLM, extending the concept of any-precision DNN to LLMs. Addressing challenges in any-precision LLM, we propose a lightweight method for any-precision quantization of LLMs, leveraging a post-training quantization framework, and develop a specialized software engine for its efficient serving. As a result, our solution significantly reduces the high costs of deploying multiple, different-sized LLMs by overlaying LLMs quantized to varying bit-widths, such as 3, 4, ..., $n$ bits, into a memory footprint comparable to a single $n$-bit LLM. All the supported LLMs with varying bit-widths demonstrate state-of-the-art model quality and inference throughput, proving itself to be a compelling option for deployment of multiple, different-sized LLMs.