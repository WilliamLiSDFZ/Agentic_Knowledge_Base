---
title: "Diffusion of Thought: Chain-of-Thought Reasoning in Diffusion Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/be30024e7fa2c29cac7a6dafcbb8571f-Abstract-Conference.html"
categories: ['diffusion-based-generative-modeling-and-inference', 'llm-training-and-optimization-techniques']
tags: ['diffusion-language-models', 'chain-of-thought', 'reasoning']
venue: "NeurIPS 2024"
tldr: "Diffusion-of-Thought integrates chain-of-thought reasoning into diffusion language models to enable iterative multi-step reasoning during the diffusion process."
---

# Diffusion of Thought: Chain-of-Thought Reasoning in Diffusion Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/be30024e7fa2c29cac7a6dafcbb8571f-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/be30024e7fa2c29cac7a6dafcbb8571f-Abstract-Conference.html)

**TLDR**: Diffusion-of-Thought integrates chain-of-thought reasoning into diffusion language models to enable iterative multi-step reasoning during the diffusion process.

## Abstract

Recently, diffusion models have garnered significant interest in the field of text processing due to their many potential advantages compared to conventional autoregressive models.In this work, we propose Diffusion-of-Thought (DoT),  a novel approach that integrates diffusion models with Chain-of-Thought, a well-established technique for improving the reasoning ability of autoregressive language models. In contrast to autoregressive language models that make decisions in a left-to-right, token-by-token manner, DoT allows reasoning steps to diffuse over time through a diffusion language model and offers greater flexibility in trading-off computation for reasoning performance. Our experimental results demonstrate the effectiveness of DoT in multi-digit multiplication, boolean logic, and grade school math problems. In addition to that, DoT showcases promising self-correction abilities and benefits from existing reasoning-enhancing techniques like self-consistency decoding. Our findings contribute to the understanding and development of reasoning with diffusion language models.