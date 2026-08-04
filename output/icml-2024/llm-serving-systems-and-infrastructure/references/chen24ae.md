---
title: "EE-LLM: Large-Scale Training and Inference of Early-Exit Large Language Models with 3D Parallelism"
source: "https://proceedings.mlr.press/v235/chen24ae.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24ae/chen24ae.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'llm-serving-systems-and-infrastructure']
tags: ['early-exit', 'LLM-inference', '3D-parallelism', 'large-scale-training']
venue: "ICML 2024"
tldr: "Presents EE-LLM, a scalable framework for training and inference of early-exit LLMs using 3D parallelism to accelerate inference."
---

# EE-LLM: Large-Scale Training and Inference of Early-Exit Large Language Models with 3D Parallelism

**Source**: [https://proceedings.mlr.press/v235/chen24ae.html](https://proceedings.mlr.press/v235/chen24ae.html)

**TLDR**: Presents EE-LLM, a scalable framework for training and inference of early-exit LLMs using 3D parallelism to accelerate inference.

## Abstract

We present EE-LLM, a framework for large-scale training and inference of early-exit large language models (LLMs). While recent works have shown preliminary evidence for the efficacy of early exiting in accelerating LLM inference, EE-LLM makes a foundational step towards scaling up early-exit LLMs by supporting their training and inference with massive 3D parallelism. Built upon Megatron-LM, EE-LLM implements a variety of algorithmic innovations and performance optimizations tailored to early exiting, including a lightweight method that facilitates backpropagation for the early-exit training objective with pipeline parallelism, techniques of leveraging idle resources in the original pipeline schedule for computation related to early-exit layers, and two approaches of early-exit inference that are compatible with KV caching for autoregressive generation. Our analytical and empirical study shows that EE-LLM achieves great training efficiency with negligible computational overhead compared to standard LLM training, as well as outstanding inference speedup without compromising output quality. To facilitate further research and adoption, we release EE-LLM at https://github.com/pan-x-c/EE-LLM.