---
title: "LESS: Selecting Influential Data for Targeted Instruction Tuning"
source: "https://proceedings.mlr.press/v235/xia24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xia24c/xia24c.pdf"
categories: ['data-selection-and-active-learning-methods', 'large-language-model-alignment-and-capabilities']
tags: ['instruction-tuning', 'data-selection', 'influence-functions']
venue: "ICML 2024"
tldr: "LESS proposes a gradient-based data selection method to identify the most influential training examples for targeted instruction tuning of LLMs."
---

# LESS: Selecting Influential Data for Targeted Instruction Tuning

**Source**: [https://proceedings.mlr.press/v235/xia24c.html](https://proceedings.mlr.press/v235/xia24c.html)

**TLDR**: LESS proposes a gradient-based data selection method to identify the most influential training examples for targeted instruction tuning of LLMs.

## Abstract

Instruction tuning has unlocked powerful capabilities in large language models (LLMs), using combined datasets to develop general-purpose chatbots. However, real-world applications often require a specialized suite of skills (e.g., reasoning). The challenge lies in identifying the most relevant data from these extensive datasets to effectively develop specific capabilities, a setting we frame as targeted instruction tuning. We propose LESS, an optimizer-aware and practically efficient algorithm to estimate data influences and perform Low-rank gradiEnt Similarity Search for instruction data selection. Crucially, LESS adapts existing influence formulations to work with the Adam optimizer and variable-length instruction data. LESS first constructs a highly reusable and transferable gradient datastore with low-dimensional gradient features and then selects examples based on their similarity to few-shot examples embodying a specific capability. Experiments show that training on a LESS-selected 5% of the data can often outperform training on the full dataset across diverse downstream tasks. Furthermore, the selected data is highly transferable: smaller models can be leveraged to select useful data for larger models and models from different families. Our qualitative analysis shows that our method goes beyond surface form cues to identify data that exemplifies the necessary reasoning skills for the intended downstream application. To facilitate future work, we release code and data at princeton-nlp/LESS.