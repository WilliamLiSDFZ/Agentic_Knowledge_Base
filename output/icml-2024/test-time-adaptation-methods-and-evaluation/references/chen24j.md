---
title: "Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models"
source: "https://proceedings.mlr.press/v235/chen24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24j/chen24j.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'test-time-adaptation-methods-and-evaluation']
tags: ['self-play', 'fine-tuning', 'LLM-alignment', 'weak-to-strong']
venue: "ICML 2024"
tldr: "Self-Play Fine-Tuning (SPIN) iteratively improves LLMs by having the model distinguish its own generations from human data without additional annotations."
---

# Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models

**Source**: [https://proceedings.mlr.press/v235/chen24j.html](https://proceedings.mlr.press/v235/chen24j.html)

**TLDR**: Self-Play Fine-Tuning (SPIN) iteratively improves LLMs by having the model distinguish its own generations from human data without additional annotations.

## Abstract

Harnessing the power of human-annotated data through Supervised Fine-Tuning (SFT) is pivotal for advancing Large Language Models (LLMs). In this paper, we delve into the prospect of growing a strong LLM out of a weak one without the need for acquiring additional human-annotated data. We propose a new fine-tuning method called Self-Play fIne-tuNing (SPIN), which starts from a supervised fine-tuned model. At the heart of SPIN lies a self-play mechanism, where the LLM refines its capability by playing against instances of itself. More specifically, the LLM generates its own training data from its previous iterations, refining its policy by discerning these self-generated responses from those obtained from human-annotated data. Our method progressively elevates the LLM from a nascent model to a formidable one, unlocking the full potential of human-annotated demonstration data for SFT. Theoretically, we prove that the global optimum to the training objective function of our method is achieved only when the LLM policy aligns with the target data distribution. Empirically, we evaluate our method on several benchmark datasets including the HuggingFace Open LLM Leaderboard, MT-Bench, and datasets from Big-Bench. Our results show that SPIN can significantly improve the LLM’s performance across a variety of benchmarks and even outperform models trained through direct preference optimization (DPO) supplemented with extra GPT-4 preference data. This sheds light on the promise of self-play, enabling the achievement of human-level performance in LLMs without the need for expert opponents.