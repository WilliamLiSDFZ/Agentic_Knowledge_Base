---
title: "Fewer Truncations Improve Language Modeling"
source: "https://proceedings.mlr.press/v235/ding24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ding24f/ding24f.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'transformer-architecture-efficiency-and-scaling']
tags: ['language-model-training', 'document-truncation', 'data-integrity', 'sequence-packing', 'pretraining']
venue: "ICML 2024"
tldr: "Shows that reducing document truncations during LLM pretraining by better sequence packing improves language modeling performance and data integrity."
---

# Fewer Truncations Improve Language Modeling

**Source**: [https://proceedings.mlr.press/v235/ding24f.html](https://proceedings.mlr.press/v235/ding24f.html)

**TLDR**: Shows that reducing document truncations during LLM pretraining by better sequence packing improves language modeling performance and data integrity.

## Abstract

In large language model training, input documents are typically concatenated together and then split into sequences of equal length to avoid padding tokens. Despite its efficiency, the concatenation approach compromises data integrity—it inevitably breaks many documents into incomplete pieces, leading to excessive truncations that hinder the model from learning to compose logically coherent and factually consistent content that is grounded on the complete context. To address the issue, we propose Best-fit Packing, a scalable and efficient method that packs documents into training sequences through length-aware combinatorial optimization. Our method completely eliminates unnecessary truncations while retaining the same training efficiency as concatenation. Empirical results from both text and code pre-training show that our method achieves superior performance (e.g., +4.7% on reading comprehension; +16.8% in context following; and +9.2% on program synthesis), and reduces closed-domain hallucination effectively by up to 58.3%.