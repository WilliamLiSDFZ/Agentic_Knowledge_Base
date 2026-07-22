---
title: "Training a Better Chinese Spelling Correction Model via Prior-knowledge Guided Teacher"
source: "https://aclanthology.org/2024.findings-acl.806/"
categories: ['nlp-for-asian-languages', 'llm-training-alignment-and-evaluation']
tags: ['Chinese-spelling-correction', 'prior-knowledge', 'teacher-model', 'PLM']
venue: "ACL 2024"
tldr: "Proposes a prior-knowledge guided teacher framework to train better Chinese spelling correction models and reduce over-correction in fine-tuned PLMs."
---

# Training a Better Chinese Spelling Correction Model via Prior-knowledge Guided Teacher

**Source**: [https://aclanthology.org/2024.findings-acl.806/](https://aclanthology.org/2024.findings-acl.806/)

**TLDR**: Proposes a prior-knowledge guided teacher framework to train better Chinese spelling correction models and reduce over-correction in fine-tuned PLMs.

## Abstract

AbstractRecent advancements in Chinese Spelling Correction (CSC) predominantly leverage pre-trained language models (PLMs). However, a notable challenge with fine-tuned PLM-based CSC models is their tendency to over-correct, leading to poor generalization for error patterns outside the standard distribution. To address this, we developed a teacher network guided by prior knowledge for distillation learning of CSC models. Unlike traditional teacher networks, which depend on task-related pre-training, our method infuses task-related prior information into the teacher network, offering guidance beyond mere labels to the student network. This strategy significantly enhances the CSC model’s language modeling capabilities, crucial for minimizing over-correction. Importantly, our approach is model-independent and the teacher network does not require task-related pre-training, making it broadly applicable for enhancing various PLM-based CSC models with minimal additional computational resources. Extensive experiments on widely used benchmarks demonstrate that our method achieves new state-of-the-art results. Additionally, we explored the potential of generalizing our method to other non-autoregressive text-generation tasks.