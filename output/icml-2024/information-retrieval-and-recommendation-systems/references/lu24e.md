---
title: "WebLINX: Real-World Website Navigation with Multi-Turn Dialogue"
source: "https://proceedings.mlr.press/v235/lu24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lu24e/lu24e.pdf"
categories: ['information-retrieval-and-recommendation-systems', 'large-language-model-alignment-and-capabilities']
tags: ['web-navigation', 'dialogue-agent', 'benchmark', 'multi-turn', 'LLM-agent']
venue: "ICML 2024"
tldr: "Introduces WEBLINX, a benchmark for conversational web navigation where agents follow multi-turn dialogue instructions to complete real-world browser tasks."
---

# WebLINX: Real-World Website Navigation with Multi-Turn Dialogue

**Source**: [https://proceedings.mlr.press/v235/lu24e.html](https://proceedings.mlr.press/v235/lu24e.html)

**TLDR**: Introduces WEBLINX, a benchmark for conversational web navigation where agents follow multi-turn dialogue instructions to complete real-world browser tasks.

## Abstract

We propose the problem of conversational web navigation, where a digital agent controls a web browser and follows user instructions to solve real-world tasks in a multi-turn dialogue fashion. To support this problem, we introduce WEBLINX - a large-scale benchmark of 100K interactions across 2300 expert demonstrations of conversational web navigation. Our benchmark covers a broad range of patterns on over 150 real-world websites and can be used to train and evaluate agents in diverse scenarios. Due to the magnitude of information present, Large Language Models (LLMs) cannot process entire web pages in real-time. To solve this bottleneck, we design a retrieval-inspired model that efficiently prunes HTML pages by ranking relevant elements. We use the selected elements, along with screenshots and action history, to assess a variety of models for their ability to replicate human behavior when navigating the web. Our experiments span from small text-only to proprietary multimodal LLMs. We find that smaller finetuned decoders surpass the best zero-shot LLMs (including GPT-4V), but also larger finetuned multimodal models which were explicitly pretrained on screenshots. However, all finetuned models struggle to generalize to unseen websites. Our findings highlight the need for large multimodal models that can generalize to novel settings.