---
title: "SPHINX-X: Scaling Data and Parameters for a Family of Multi-modal Large Language Models"
source: "https://proceedings.mlr.press/v235/liu24cc.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24cc/liu24cc.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'large-language-model-alignment-and-capabilities']
tags: ['multimodal-LLM', 'visual-encoders', 'scaling', 'SPHINX', 'efficiency']
venue: "ICML 2024"
tldr: "SPHINX-X scales a multimodal large language model family by improving architecture efficiency through removing redundant encoders, skip tokens, and simplified multi-stage training."
---

# SPHINX-X: Scaling Data and Parameters for a Family of Multi-modal Large Language Models

**Source**: [https://proceedings.mlr.press/v235/liu24cc.html](https://proceedings.mlr.press/v235/liu24cc.html)

**TLDR**: SPHINX-X scales a multimodal large language model family by improving architecture efficiency through removing redundant encoders, skip tokens, and simplified multi-stage training.

## Abstract

We propose SPHINX-X, an extensive Multi-modality Large Language Model (MLLM) series developed upon SPHINX. To improve the architecture and training efficiency, we modify the SPHINX framework by removing redundant visual encoders, bypassing fully-padded sub-images with skip tokens, and simplifying multi-stage training into a one-stage all-in-one paradigm. To fully unleash the potential of MLLMs, we assemble a comprehensive multi-domain and multi-modal dataset covering publicly available resources in language, vision, and vision-language tasks. We further enrich this collection with our curated OCR intensive and Set-of-Mark datasets, extending the diversity and generality. By training over different base LLMs including TinyLlama-1.1B, InternLM2-7B, LLaMA2-13B, and Mixtral-8$\times$7B, we obtain a spectrum of MLLMs that vary in parameter size and multilingual capabilities. Comprehensive benchmarking reveals a strong correlation between the multi-modal performance with the data and parameter scales. Code and models are released at https://github.com/Alpha-VLLM/LLaMA2-Accessory.