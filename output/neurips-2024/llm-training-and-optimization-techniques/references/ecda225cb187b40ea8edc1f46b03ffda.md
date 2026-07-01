---
title: "AutoMix: Automatically Mixing Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/ecda225cb187b40ea8edc1f46b03ffda-Abstract-Conference.html"
categories: ['llm-training-and-optimization-techniques', 'llm-agent-communication-and-cooperation']
tags: ['llm-routing', 'cost-optimization', 'model-mixing']
venue: "NeurIPS 2024"
tldr: "AutoMix automatically routes queries across LLMs of varying sizes to optimize the trade-off between computational cost and performance."
---

# AutoMix: Automatically Mixing Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/ecda225cb187b40ea8edc1f46b03ffda-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/ecda225cb187b40ea8edc1f46b03ffda-Abstract-Conference.html)

**TLDR**: AutoMix automatically routes queries across LLMs of varying sizes to optimize the trade-off between computational cost and performance.

## Abstract

Large language models (LLMs) are now available from cloud API providers in various sizes and configurations. While this diversity offers a broad spectrum of choices, effectively leveraging the options to optimize computational cost and performance remains challenging. In this work, we present AutoMix, an approach that strategically routes queries to larger LMs, based on the approximate correctness of outputs from a smaller LM. Central to AutoMix are two key technical contributions. First, it has a few-shot self-verification mechanism, which estimates the reliability of its own outputs without requiring extensive training. Second, given that self-verification can be noisy, it employs a POMDP based router that can effectively select an appropriately sized model, based on answer confidence. Experiments across five language models and five challenging datasets show that Automix consistently surpasses strong baselines, reducing computational cost by over 50\% for comparable performance.