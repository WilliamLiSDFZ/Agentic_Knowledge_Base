---
title: "A Two-Stage Adaptation of Large Language Models for Text Ranking"
source: "https://aclanthology.org/2024.findings-acl.706/"
pdf_url: ""
categories: ['llm-based-ranking-and-recommendation', 'llm-training-alignment-and-evaluation']
tags: ['text-ranking', 'LLM-fine-tuning', 'information-retrieval']
venue: "ACL 2024"
tldr: "Presents a two-stage LLM adaptation pipeline combining supervised fine-tuning and preference learning for text ranking."
---

# A Two-Stage Adaptation of Large Language Models for Text Ranking

**Source**: [https://aclanthology.org/2024.findings-acl.706/](https://aclanthology.org/2024.findings-acl.706/)

**TLDR**: Presents a two-stage LLM adaptation pipeline combining supervised fine-tuning and preference learning for text ranking.

## Abstract

AbstractText ranking is a critical task in information retrieval. Recent advances in pre-trained language models (PLMs), especially large language models (LLMs), present new opportunities for applying them to text ranking. While supervised fine-tuning (SFT) with ranking data has been widely explored to better align PLMs with text ranking goals, previous studies have focused primarily on encoder-only and encoder-decoder PLMs. Research on leveraging decoder-only LLMs for text ranking remains scarce. An exception to this is RankLLaMA, which uses direct SFT to explore LLaMA’s potential for text ranking. In this work, we propose a two-stage progressive paradigm to better adapt LLMs to text ranking. First, we conduct continual pre-training (CPT) of LLMs on a large weakly-supervised corpus. Second, we perform SFT, and propose an improved optimization strategy building upon RankLLaMA. Our experimental results on multiple benchmarks show that our approach outperforms previous methods in both in-domain and out-domain scenarios.