---
title: "SyCoCa: Symmetrizing Contrastive Captioners with Attentive Masking for Multimodal Alignment"
source: "https://proceedings.mlr.press/v235/ma24q.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ma24q/ma24q.pdf"
categories: ['generative-models-and-variational-inference', 'knowledge-distillation-methods-and-applications']
tags: ['multimodal-alignment', 'contrastive-learning', 'vision-language-pretraining']
venue: "ICML 2024"
tldr: "A symmetrized contrastive captioner framework with attentive masking for improved multimodal alignment between language and vision."
---

# SyCoCa: Symmetrizing Contrastive Captioners with Attentive Masking for Multimodal Alignment

**Source**: [https://proceedings.mlr.press/v235/ma24q.html](https://proceedings.mlr.press/v235/ma24q.html)

**TLDR**: A symmetrized contrastive captioner framework with attentive masking for improved multimodal alignment between language and vision.

## Abstract

Multimodal alignment between language and vision is the fundamental topic in current vision-language model research. Contrastive Captioners (CoCa), as a representative method, integrates Contrastive Language-Image Pretraining (CLIP) and Image Caption (IC) into a unified framework, resulting in impressive results. CLIP imposes a bidirectional constraints on global representations of entire images and sentences. Although IC conducts an unidirectional image-to-text generation on local representation, it lacks any constraint on local text-to-image reconstruction, which limits the ability to understand images at a fine-grained level when aligned with texts. To achieve multimodal alignment from both global and local perspectives, this paper proposes Symmetrizing Contrastive Captioners (SyCoCa), which introduces bidirectional interactions on images and texts across the global and local representation levels. Specifically, we expand a Text-Guided Masked Image Modeling (TG-MIM) head based on ITC and IC heads. The improved SyCoCa further leverages textual cues to reconstruct contextual images and visual cues to predict textual contents. When implementing bidirectional local interactions, the local contents of images tend to be cluttered or unrelated to their textual descriptions. Thus, we employ an attentive masking strategy to select effective image patches for interaction. Extensive experiments on five vision-language tasks, including image-text retrieval, image-captioning, visual question answering, and zero-shot/finetuned image classification, validate the effectiveness of our proposed method.