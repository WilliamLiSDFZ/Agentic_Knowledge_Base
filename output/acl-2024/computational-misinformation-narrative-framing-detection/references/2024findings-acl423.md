---
title: "Spotting AI’s Touch: Identifying LLM-Paraphrased Spans in Text"
source: "https://aclanthology.org/2024.findings-acl.423/"
pdf_url: ""
categories: ['llm-security-robustness-and-detection', 'computational-misinformation-narrative-framing-detection']
tags: ['ai-text-detection', 'paraphrase-detection', 'span-detection']
venue: "ACL 2024"
tldr: "Proposes a method to identify LLM-paraphrased spans within partially AI-modified texts for AI-generated content detection."
---

# Spotting AI’s Touch: Identifying LLM-Paraphrased Spans in Text

**Source**: [https://aclanthology.org/2024.findings-acl.423/](https://aclanthology.org/2024.findings-acl.423/)

**TLDR**: Proposes a method to identify LLM-paraphrased spans within partially AI-modified texts for AI-generated content detection.

## Abstract

AbstractAI-generated text detection has attracted increasing attention as powerful language models approach human-level generation. Limited work is devoted to detecting (partially) AI-paraphrased texts. However, AI paraphrasing is commonly employed in various application scenarios for text refinement and diversity. To this end, we propose a novel detection framework, paraphrased text span detection (PTD), aiming to identify paraphrased text spans within a text. Different from text-level detection, PTD takes in the full text and assigns each of the sentences with a score indicating the paraphrasing degree. We construct a dedicated dataset, PASTED, for paraphrased text span detection. Both in-distribution and out-of-distribution results demonstrate the effectiveness of PTD models in identifying AI-paraphrased text spans. Statistical and model analysis explains the crucial role of the surrounding context of the paraphrased text spans. Extensive experiments show that PTD models can generalize to versatile paraphrasing prompts as well as multiple paraphrased text spans.