---
title: "LongLLMLingua: Accelerating and Enhancing LLMs in Long Context Scenarios via Prompt Compression"
source: "https://aclanthology.org/2024.acl-long.91/"
pdf_url: ""
categories: ['collaborative-llm-deployment-and-inference-optimization', 'emotion-aware-dialogue-and-empathy-systems']
tags: ['prompt-compression', 'long-context', 'LLM-efficiency']
venue: "ACL 2024"
tldr: "Presents LongLLMLingua, a prompt compression method that accelerates and improves LLM performance in long-context scenarios."
---

# LongLLMLingua: Accelerating and Enhancing LLMs in Long Context Scenarios via Prompt Compression

**Source**: [https://aclanthology.org/2024.acl-long.91/](https://aclanthology.org/2024.acl-long.91/)

**TLDR**: Presents LongLLMLingua, a prompt compression method that accelerates and improves LLM performance in long-context scenarios.

## Abstract

AbstractIn long context scenarios, large language models (LLMs) face three main challenges: higher computational cost, performance reduction, and position bias. Research indicates that LLM performance hinges on the density and position of key information in the input prompt. Inspired by these findings, we propose LongLLMLingua for prompt compression towards improving LLMs’ perception of the key information to simultaneously address the three challenges. Our extensive evaluation across various long context scenarios demonstrates that LongLLMLingua not only enhances performance but also significantly reduces costs and latency. For instance, in the NaturalQuestions benchmark, LongLLMLingua boosts performance by up to 21.4% with around 4x fewer tokens in GPT-3.5-Turbo, leading to substantial cost savings. It achieves a 94.0% cost reduction in the LooGLE benchmark. Moreover, when compressing prompts of about 10k tokens at ratios of 2x-6x, LongLLMLingua can accelerate end-to-end latency by 1.4x-2.6x.