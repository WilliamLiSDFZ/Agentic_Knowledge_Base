---
title: "Stay on Topic with Classifier-Free Guidance"
source: "https://proceedings.mlr.press/v235/sanchez24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sanchez24a/sanchez24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'transformer-architecture-efficiency-and-scaling']
tags: ['classifier-free-guidance', 'language-modeling', 'prompt-adherence', 'inference', 'text-generation']
venue: "ICML 2024"
tldr: "Classifier-Free Guidance is successfully adapted to language modeling to improve prompt adherence across a wide range of benchmarks."
---

# Stay on Topic with Classifier-Free Guidance

**Source**: [https://proceedings.mlr.press/v235/sanchez24a.html](https://proceedings.mlr.press/v235/sanchez24a.html)

**TLDR**: Classifier-Free Guidance is successfully adapted to language modeling to improve prompt adherence across a wide range of benchmarks.

## Abstract

Classifier-Free Guidance (CFG) has recently emerged in as a lightweight technique to encourage prompt-adherence in generations, yet has not yet been successfully applied to language modeling. In this work, we demonstrate across a wide array of benchmarks that CFG can be used broadly as an inference-time technique in pure language modeling. We show that CFG (1) improves the performance of Pythia, GPT-2 and LLaMA-family models across: Q&A, reasoning, code generation, and machine translation, achieving SOTA on LAMBADA with LLaMA-7B over PaLM-540B; (2) brings improvements equivalent to a model with twice the parameter-count; (3) can stack alongside other inference-time methods like Chain-of-Thought and Self-Consistency, yielding further improvements in difficult tasks; (4) can be used to increase the faithfulness and coherence of assistants in challenging form-driven and content-driven prompts: in human evaluations we show a 75% preference for using CFG over baseline.