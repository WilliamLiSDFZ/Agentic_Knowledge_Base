---
title: "Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models"
source: "https://proceedings.mlr.press/v235/ghandeharioun24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ghandeharioun24a/ghandeharioun24a.pdf"
categories: ['llm-geometry-and-interpretability-research', 'large-language-model-alignment-and-capabilities']
tags: ['LLM-interpretability', 'hidden-representations', 'patchscopes']
venue: "ICML 2024"
tldr: "Proposes Patchscopes, a framework that uses LLMs themselves to interpret their own hidden representations via targeted generation."
---

# Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models

**Source**: [https://proceedings.mlr.press/v235/ghandeharioun24a.html](https://proceedings.mlr.press/v235/ghandeharioun24a.html)

**TLDR**: Proposes Patchscopes, a framework that uses LLMs themselves to interpret their own hidden representations via targeted generation.

## Abstract

Understanding the internal representations of large language models (LLMs) can help explain models’ behavior and verify their alignment with human values. Given the capabilities of LLMs in generating human-understandable text, we propose leveraging the model itself to explain its internal representations in natural language. We introduce a framework called Patchscopes and show how it can be used to answer a wide range of questions about an LLM’s computation. We show that many prior interpretability methods based on projecting representations into the vocabulary space and intervening on the LLM computation can be viewed as instances of this framework. Moreover, several of their shortcomings such as failure in inspecting early layers or lack of expressivity can be mitigated by Patchscopes. Beyond unifying prior inspection techniques, Patchscopes also opens up new possibilities such as using a more capable model to explain the representations of a smaller model, and multihop reasoning error correction.