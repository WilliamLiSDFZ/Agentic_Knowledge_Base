---
title: "Improving Context Understanding in Multimodal Large Language Models via Multimodal Composition Learning"
source: "https://proceedings.mlr.press/v235/li24s.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24s/li24s.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'transformer-architecture-efficiency-and-scaling']
tags: ['multimodal-LLM', 'compositional-learning', 'visual-understanding', 'context-comprehension', 'image-text']
venue: "ICML 2024"
tldr: "Proposes multimodal composition learning to improve context understanding in multimodal large language models for complex visual scenarios."
---

# Improving Context Understanding in Multimodal Large Language Models via Multimodal Composition Learning

**Source**: [https://proceedings.mlr.press/v235/li24s.html](https://proceedings.mlr.press/v235/li24s.html)

**TLDR**: Proposes multimodal composition learning to improve context understanding in multimodal large language models for complex visual scenarios.

## Abstract

Previous efforts using frozen Large Language Models (LLMs) for visual understanding, via image captioning or image-text retrieval tasks, face challenges when dealing with complex multimodal scenarios. In order to enhance the capabilities of Multimodal Large Language Models (MLLM) in comprehending the context of vision and language, we introduce Multimodal Composition Learning (MCL) for the purpose of mapping or aligning the vision and language input. In particular, we introduce two tasks: Multimodal-Context Captioning (MC-Cap) and Multimodal-Context Retrieval (MC-Ret) to guide a frozen LLM in comprehending the vision and language context. These specialized tasks are crafted to improve the LLM’s capacity for efficient processing and utilization of multimodal inputs, thereby enhancing its proficiency in generating more accurate text or visual representations. Extensive experiments on both retrieval tasks (i.e., zero-shot composed image retrieval, visual storytelling image retrieval and visual dialog image retrieval) and text generation tasks (i.e., visual question answering) demonstrate the effectiveness of the proposed method. The code is available at: https://github.com/dhg-wei/MCL.