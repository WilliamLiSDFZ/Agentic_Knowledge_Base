---
title: "APT: Adaptive Pruning and Tuning Pretrained Language Models for Efficient Training and Inference"
source: "https://proceedings.mlr.press/v235/zhao24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhao24g/zhao24g.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'knowledge-distillation-methods-and-applications']
tags: ['model-pruning', 'parameter-efficient-fine-tuning', 'inference-efficiency']
venue: "ICML 2024"
tldr: "Proposes APT, combining adaptive pruning and tuning to improve both training and inference efficiency of pretrained language models."
---

# APT: Adaptive Pruning and Tuning Pretrained Language Models for Efficient Training and Inference

**Source**: [https://proceedings.mlr.press/v235/zhao24g.html](https://proceedings.mlr.press/v235/zhao24g.html)

**TLDR**: Proposes APT, combining adaptive pruning and tuning to improve both training and inference efficiency of pretrained language models.

## Abstract

Fine-tuning and inference with large Language Models (LM) are generally known to be expensive. Parameter-efficient fine-tuning over pretrained LMs reduces training memory by updating a small number of LM parameters but does not improve inference efficiency. Structured pruning improves LM inference efficiency by removing consistent parameter blocks, yet often increases training memory and time. To improve both training and inference efficiency, we introduce APT that adaptively prunes and tunes parameters for the LMs. At the early stage of fine-tuning, APT dynamically adds salient tuning parameters for fast and accurate convergence while discarding unimportant parameters for efficiency. Compared to baselines, our experiments show that APT maintains up to 98% task performance when pruning RoBERTa and T5 models with 40% parameters left while keeping 86.4% LLaMA models’ performance with 70% parameters remaining. Furthermore, APT speeds up LMs’ fine-tuning by up to 8$\times$ and reduces large LMs’ memory training footprint by up to 70%. Our code and models are publicly available at https://github.com/ROIM1998/APT.