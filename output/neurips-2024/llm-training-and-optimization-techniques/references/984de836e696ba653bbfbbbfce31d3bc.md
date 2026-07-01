---
title: "Multi-language Diversity Benefits Autoformalization"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/984de836e696ba653bbfbbbfce31d3bc-Abstract-Conference.html"
categories: ['neural-networks-for-formal-reasoning-and-verification', 'llm-training-and-optimization-techniques']
tags: ['autoformalization', 'multilingual', 'formal-verification']
venue: "NeurIPS 2024"
tldr: "Demonstrates that leveraging multi-language diversity in training data significantly benefits autoformalization of mathematical statements into machine-verifiable proofs."
---

# Multi-language Diversity Benefits Autoformalization

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/984de836e696ba653bbfbbbfce31d3bc-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/984de836e696ba653bbfbbbfce31d3bc-Abstract-Conference.html)

**TLDR**: Demonstrates that leveraging multi-language diversity in training data significantly benefits autoformalization of mathematical statements into machine-verifiable proofs.

## Abstract

Autoformalization is the task of translating natural language materials into machine-verifiable formalisations. Progress in autoformalization research is hindered by the lack of a sizeable dataset consisting of informal-formal pairs expressing the same essence. Existing methods tend to circumvent this challenge by manually curating small corpora or using few-shot learning with large language models. But these methods suffer from data scarcity and formal language acquisition difficulty. In this work, we create mma, a large, flexible, multi-language, and multi-domain dataset of informal-formal pairs, by using a language model to translate in the reverse direction, that is, from formal mathematical statements into corresponding informal ones. Experiments show that language models fine-tuned on mma can produce up to $29-31$\% of statements acceptable with minimal corrections on the miniF2F and ProofNet benchmarks, up from $0$\% with the base model. We demonstrate that fine-tuning on multi-language formal data results in more capable autoformalization models even on single-language tasks.