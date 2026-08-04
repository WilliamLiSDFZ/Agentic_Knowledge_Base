---
title: "Evaluating Quantized Large Language Models"
source: "https://proceedings.mlr.press/v235/li24bb.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24bb/li24bb.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'transformer-architecture-efficiency-and-scaling']
tags: ['post-training-quantization', 'large-language-models', 'evaluation']
venue: "ICML 2024"
tldr: "Comprehensively evaluates post-training quantization methods for large language models across efficiency and performance dimensions."
---

# Evaluating Quantized Large Language Models

**Source**: [https://proceedings.mlr.press/v235/li24bb.html](https://proceedings.mlr.press/v235/li24bb.html)

**TLDR**: Comprehensively evaluates post-training quantization methods for large language models across efficiency and performance dimensions.

## Abstract

Post-training quantization (PTQ) has emerged as a promising technique to reduce the cost of large language models (LLMs). Specifically, PTQ can effectively mitigate memory consumption and reduce computational overhead in LLMs. To meet the requirements of both high efficiency and performance across diverse scenarios, a comprehensive evaluation of quantized LLMs is essential to guide the selection of quantization methods. This paper presents a thorough evaluation of these factors by evaluating the effect of PTQ on Weight, Activation, and KV Cache on 11 model families, including OPT, LLaMA2, Falcon, Bloomz, Mistral, ChatGLM, Vicuna, LongChat, StableLM, Gemma, and Mamba, with parameters ranging from 125M to 180B. The evaluation encompasses five types of tasks: basic NLP, emergent ability, trustworthiness, dialogue, and long-context tasks. Moreover, we also evaluate the state-of-the-art (SOTA) quantization methods to demonstrate their applicability. Based on the extensive experiments, we systematically summarize the effect of quantization, provide recommendations to apply quantization techniques, and point out future directions. The code can be found in https://github.com/thu-nics/qllm-eval.