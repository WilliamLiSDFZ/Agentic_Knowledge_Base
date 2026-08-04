---
title: "SparQ Attention: Bandwidth-Efficient LLM Inference"
source: "https://proceedings.mlr.press/v235/ribar24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ribar24a/ribar24a.pdf"
categories: ['llm-serving-systems-and-infrastructure', 'transformer-architecture-efficiency-and-scaling']
tags: ['LLM-inference', 'attention', 'bandwidth-efficiency', 'KV-cache', 'sparse-attention']
venue: "ICML 2024"
tldr: "SparQ Attention reduces memory bandwidth bottlenecks in LLM inference by selectively retrieving only the most relevant cached attention values."
---

# SparQ Attention: Bandwidth-Efficient LLM Inference

**Source**: [https://proceedings.mlr.press/v235/ribar24a.html](https://proceedings.mlr.press/v235/ribar24a.html)

**TLDR**: SparQ Attention reduces memory bandwidth bottlenecks in LLM inference by selectively retrieving only the most relevant cached attention values.

## Abstract

The computational difficulties of large language model (LLM) inference remain a significant obstacle to their widespread deployment. The need for many applications to support long input sequences and process them in large batches typically causes token-generation to be bottlenecked by data transfer. For this reason, we introduce SparQ Attention, a technique for increasing the inference throughput of LLMs by utilising memory bandwidth more efficiently within the attention layers, through selective fetching of the cached history. Our proposed technique can be applied directly to off-the-shelf LLMs during inference, without requiring any modification to the pre-training setup or additional fine-tuning. We show that SparQ Attention brings up to 8x savings in attention data transfers without substantial drops in accuracy, by evaluating Llama 2 and 3, Mistral, Gemma and Pythia models on a wide range of downstream tasks.