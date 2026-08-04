---
title: "Learning and Forgetting Unsafe Examples in Large Language Models"
source: "https://proceedings.mlr.press/v235/zhao24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhao24e/zhao24e.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'learning-with-imperfect-data-and-bias']
tags: ['LLM-safety', 'fine-tuning', 'unsafe-content']
venue: "ICML 2024"
tldr: "Explores how LLMs learn and forget unsafe examples when fine-tuned on noisy custom data containing unsafe content."
---

# Learning and Forgetting Unsafe Examples in Large Language Models

**Source**: [https://proceedings.mlr.press/v235/zhao24e.html](https://proceedings.mlr.press/v235/zhao24e.html)

**TLDR**: Explores how LLMs learn and forget unsafe examples when fine-tuned on noisy custom data containing unsafe content.

## Abstract

As the number of large language models (LLMs) released to the public grows, there is a pressing need to understand the safety implications associated with these models learning from third-party custom finetuning data. We explore the behavior of LLMs finetuned on noisy custom data containing unsafe content, represented by datasets that contain biases, toxicity, and harmfulness, finding that while aligned LLMs can readily learn this unsafe content, they also tend to forget it more significantly than other examples when subsequently finetuned on safer content. Drawing inspiration from the discrepancies in forgetting, we introduce the “ForgetFilter” algorithm, which filters unsafe data based on how strong the model’s forgetting signal is for that data. We demonstrate that the ForgetFilter algorithm ensures safety in customized finetuning without compromising downstream task performance, unlike sequential safety finetuning. ForgetFilter outperforms alternative strategies like replay and moral self-correction in curbing LLMs’ ability to assimilate unsafe content during custom finetuning, e.g. 75% lower than not applying any safety measures and 62% lower than using self-correction in toxicity score.