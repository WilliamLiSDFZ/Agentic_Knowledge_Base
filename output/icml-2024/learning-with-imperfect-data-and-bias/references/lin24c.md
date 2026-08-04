---
title: "Revisiting the Role of Language Priors in Vision-Language Models"
source: "https://proceedings.mlr.press/v235/lin24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24c/lin24c.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'learning-with-imperfect-data-and-bias']
tags: ['vision-language-models', 'language-priors', 'zero-shot']
venue: "ICML 2024"
tldr: "An investigation of the role of language priors in generative vision-language models for zero-shot visual understanding tasks."
---

# Revisiting the Role of Language Priors in Vision-Language Models

**Source**: [https://proceedings.mlr.press/v235/lin24c.html](https://proceedings.mlr.press/v235/lin24c.html)

**TLDR**: An investigation of the role of language priors in generative vision-language models for zero-shot visual understanding tasks.

## Abstract

Vision-language models (VLMs) are impactful in part because they can be applied to a variety of visual understanding tasks in a zero-shot fashion, without any fine-tuning. We study $\textit{generative VLMs}$ that are trained for next-word generation given an image. We explore their zero-shot performance on the illustrative task of image-text retrieval across nine popular vision-language benchmarks. Our first observation is that they can be repurposed for discriminative tasks (such as image-text retrieval) by simply computing the match score of generating a particular text string given an image. We call this probabilistic score the Visual Generative Pre-Training Score (VisualGPTScore). While the VisualGPTScore produces near-perfect accuracy on some retrieval benchmarks, it yields poor accuracy on others. We analyze this behavior through a probabilistic lens, pointing out that some benchmarks inadvertently capture unnatural language distributions by creating adversarial but unlikely text captions. In fact, we demonstrate that even a "blind" language model that ignores any image evidence can sometimes outperform all prior art, reminiscent of similar challenges faced by the visual-question answering (VQA) community many years ago. We derive a probabilistic post-processing scheme that controls for the amount of linguistic bias in generative VLMs at test time without having to retrain or fine-tune the model. We show that the VisualGPTScore, when appropriately debiased, is a strong zero-shot baseline for vision-language understanding, oftentimes producing state-of-the-art accuracy.