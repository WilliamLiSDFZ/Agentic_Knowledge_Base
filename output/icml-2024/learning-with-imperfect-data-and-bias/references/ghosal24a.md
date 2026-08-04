---
title: "Understanding Finetuning for Factual Knowledge Extraction"
source: "https://proceedings.mlr.press/v235/ghosal24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ghosal24a/ghosal24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'learning-with-imperfect-data-and-bias']
tags: ['finetuning', 'factual-knowledge', 'language-models']
venue: "ICML 2024"
tldr: "Shows that fine-tuning on poorly-stored facts degrades factuality even when those facts were seen during pretraining."
---

# Understanding Finetuning for Factual Knowledge Extraction

**Source**: [https://proceedings.mlr.press/v235/ghosal24a.html](https://proceedings.mlr.press/v235/ghosal24a.html)

**TLDR**: Shows that fine-tuning on poorly-stored facts degrades factuality even when those facts were seen during pretraining.

## Abstract

In this work, we study the impact of QA fine-tuning data on downstream factuality. We show that fine-tuning on lesser-known facts that are poorly stored during pretraining yields significantly worse factuality than fine-tuning on well-known facts, even when all facts are seen during pretraining. We prove this phenomenon theoretically, showing that training on lesser-known facts can lead the model to ignore subject entity names and instead output a generic plausible response even when the relevant factual knowledge is encoded in the model. On three question answering benchmarks (PopQA, Entity Questions, and MMLU) and two language models (Llama-2-7B and Mistral-7B), we find that (i) finetuning on a completely factual but lesser-known subset of the data deteriorates downstream factuality (5-10%) and (ii) finetuning on a subset of better-known examples matches or outperforms finetuning on the entire dataset. Ultimately, our results shed light on the interaction between pretrained knowledge and finetuning data and demonstrate the importance of taking into account how facts are stored in the pretrained model when fine-tuning for knowledge-intensive tasks.