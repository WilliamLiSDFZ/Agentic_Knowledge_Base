---
title: "Open-Domain Text Evaluation via Contrastive Distribution Methods"
source: "https://proceedings.mlr.press/v235/lu24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lu24f/lu24f.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'information-retrieval-and-recommendation-systems']
tags: ['text-evaluation', 'open-domain-generation', 'contrastive-methods', 'LLM-evaluation']
venue: "ICML 2024"
tldr: "Proposes contrastive distribution methods for evaluating open-domain text generation quality from large language models."
---

# Open-Domain Text Evaluation via Contrastive Distribution Methods

**Source**: [https://proceedings.mlr.press/v235/lu24f.html](https://proceedings.mlr.press/v235/lu24f.html)

**TLDR**: Proposes contrastive distribution methods for evaluating open-domain text generation quality from large language models.

## Abstract

Recent advancements in open-domain text generation, driven by the power of large pre-trained language models (LLMs), have demonstrated remarkable performance. However, assessing these models’ generation quality remains a challenge. In this paper, we introduce a novel method for evaluating open-domain text generation called Contrastive Distribution Methods (CDM). Leveraging the connection between increasing model parameters and enhanced LLM performance, CDM creates a mapping from the contrast of two probabilistic distributions – one known to be superior to the other – to quality measures. We investigate CDM for open-domain text generation evaluation under two paradigms: 1) Generative CDM, which harnesses the contrast of two language models’ distributions to generate synthetic examples for training discriminator-based metrics; 2) Discriminative CDM, which directly uses distribution disparities between two language models for evaluation. Our experiments on coherence evaluation for multi-turn dialogue and commonsense evaluation for controllable generation demonstrate CDM’s superior correlate with human judgment than existing automatic evaluation metrics, highlighting the strong performance and generalizability of our approach.