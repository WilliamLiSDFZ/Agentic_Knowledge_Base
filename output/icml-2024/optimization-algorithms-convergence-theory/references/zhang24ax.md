---
title: "Riemannian Preconditioned LoRA for Fine-Tuning Foundation Models"
source: "https://proceedings.mlr.press/v235/zhang24ax.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24ax/zhang24ax.pdf"
categories: ['optimization-algorithms-convergence-theory', 'transformer-architecture-efficiency-and-scaling']
tags: ['LoRA', 'fine-tuning', 'Riemannian-optimization', 'preconditioning', 'parameter-efficient']
venue: "ICML 2024"
tldr: "Introduces a Riemannian preconditioner into LoRA fine-tuning to improve optimization efficiency for foundation models."
---

# Riemannian Preconditioned LoRA for Fine-Tuning Foundation Models

**Source**: [https://proceedings.mlr.press/v235/zhang24ax.html](https://proceedings.mlr.press/v235/zhang24ax.html)

**TLDR**: Introduces a Riemannian preconditioner into LoRA fine-tuning to improve optimization efficiency for foundation models.

## Abstract

Low-Rank Adaptation (LoRA) emerges as a popular parameter-efficient fine-tuning (PEFT) method, which proposes to freeze pretrained model weights and update an additive low-rank trainable matrix. In this work, we study the enhancement of LoRA training by introducing an $r\times r$ preconditioner in each gradient step where $r$ is the LoRA rank. We theoretically verify that the proposed preconditioner stabilizes feature learning with LoRA under infinite-width NN setting. Empirically, the implementation of this new preconditioner requires a small change to existing optimizer code and creates virtually minuscule storage and runtime overhead. Our experimental results with both large language models and text-to-image diffusion models show that with this new preconditioner, the convergence and reliability of SGD and AdamW can be significantly enhanced. Moreover, the training process becomes much more robust to hyperparameter choices such as learning rate. The new preconditioner can be derived from a novel Riemannian metric in low-rank matrix field.