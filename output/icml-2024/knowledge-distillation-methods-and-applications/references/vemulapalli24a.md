---
title: "Knowledge Transfer from Vision Foundation Models for Efficient Training of Small Task-specific Models"
source: "https://proceedings.mlr.press/v235/vemulapalli24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/vemulapalli24a/vemulapalli24a.pdf"
categories: ['knowledge-distillation-methods-and-applications', 'transformer-architecture-efficiency-and-scaling']
tags: ['knowledge-distillation', 'vision-foundation-models', 'efficient-training', 'transfer-learning', 'small-models']
venue: "ICML 2024"
tldr: "Proposes a method to transfer knowledge from large vision foundation models to small task-specific models for efficient inference with limited labeled data."
---

# Knowledge Transfer from Vision Foundation Models for Efficient Training of Small Task-specific Models

**Source**: [https://proceedings.mlr.press/v235/vemulapalli24a.html](https://proceedings.mlr.press/v235/vemulapalli24a.html)

**TLDR**: Proposes a method to transfer knowledge from large vision foundation models to small task-specific models for efficient inference with limited labeled data.

## Abstract

Vision Foundation Models (VFMs) pretrained on massive datasets exhibit impressive performance on various downstream tasks, especially with limited labeled target data. However, due to their high inference compute cost, these models cannot be deployed for many real-world applications. Motivated by this, we ask the following important question, "How can we leverage the knowledge from a large VFM to train a small task-specific model for a new target task with limited labeled training data?", and propose a simple task-oriented knowledge transfer approach as a highly effective solution to this problem. Our experimental results on five target tasks show that the proposed approach outperforms task-agnostic VFM distillation, web-scale CLIP pretraining, supervised ImageNet pretraining, and self-supervised DINO pretraining by up to 11.6%, 22.1%, 13.7%, and 29.8%, respectively. Furthermore, the proposed approach also demonstrates up to 9x, 4x and 15x reduction in pretraining compute cost when compared to task-agnostic VFM distillation, ImageNet pretraining and DINO pretraining, respectively, while outperforming them. We also show that the dataset used for transferring knowledge has a significant effect on the final target task performance, and introduce a retrieval-augmented knowledge transfer strategy that uses web-scale image retrieval to curate effective transfer sets.