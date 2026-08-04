---
title: "SelfIE: Self-Interpretation of Large Language Model Embeddings"
source: "https://proceedings.mlr.press/v235/chen24ao.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24ao/chen24ao.pdf"
categories: ['llm-geometry-and-interpretability-research', 'large-language-model-alignment-and-capabilities']
tags: ['LLM-interpretability', 'embedding-interpretation', 'self-explanation', 'inner-representations']
venue: "ICML 2024"
tldr: "Proposes SelfIE, a framework enabling LLMs to interpret their own internal embeddings in natural language."
---

# SelfIE: Self-Interpretation of Large Language Model Embeddings

**Source**: [https://proceedings.mlr.press/v235/chen24ao.html](https://proceedings.mlr.press/v235/chen24ao.html)

**TLDR**: Proposes SelfIE, a framework enabling LLMs to interpret their own internal embeddings in natural language.

## Abstract

How do large language models (LLMs) obtain their answers? The ability to explain and control an LLM’s reasoning process is key for reliability, transparency, and future model developments. We propose SelfIE (Self-Interpretation of Embeddings), a framework that enables LLMs to interpret their own embeddings in natural language by leveraging their ability to respond to inquiries about a given passage. Capable of interpreting open-world concepts in the hidden embeddings, SelfIE reveals LLM internal reasoning in cases such as making ethical decisions, internalizing prompt injection, and recalling harmful knowledge. SelfIE’s text descriptions on hidden embeddings open avenues to control LLM reasoning. We propose Supervised Control, which allows editing open-ended concepts while only requiring gradient computation of individual layer. We extend RLHF to hidden embeddings and propose Reinforcement Control that erases harmful knowledge in LLM without supervision targets.