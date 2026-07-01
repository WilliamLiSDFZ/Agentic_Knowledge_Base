---
title: "Dynamic Tuning Towards Parameter and Inference Efficiency for ViT Adaptation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/d0241a0fb1fc9be477bdfde5e0da276a-Abstract-Conference.html"
categories: ['llm-training-and-optimization-techniques', 'self-distillation-knowledge-transfer-gains']
tags: ['parameter-efficient-fine-tuning', 'vision-transformers', 'inference-efficiency', 'dynamic-tuning', 'adaptation']
venue: "NeurIPS 2024"
tldr: "A dynamic tuning method improves both parameter and inference efficiency for adapting vision transformers by selectively activating tokens and modules."
---

# Dynamic Tuning Towards Parameter and Inference Efficiency for ViT Adaptation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/d0241a0fb1fc9be477bdfde5e0da276a-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/d0241a0fb1fc9be477bdfde5e0da276a-Abstract-Conference.html)

**TLDR**: A dynamic tuning method improves both parameter and inference efficiency for adapting vision transformers by selectively activating tokens and modules.

## Abstract

Existing parameter-efficient fine-tuning (PEFT) methods have achieved significant success on vision transformers (ViTs) adaptation by improving parameter efficiency. However, the exploration of enhancing inference efficiency during adaptation remains underexplored. This limits the broader application of pre-trained ViT models, especially when the model is computationally extensive. In this paper, we propose Dynamic Tuning (DyT), a novel approach to improve both parameter and inference efficiency for ViT adaptation. Specifically, besides using the lightweight adapter modules, we propose a token dispatcher to distinguish informative tokens from less important ones, allowing the latter to dynamically skip the original block, thereby reducing the redundant computation during inference. Additionally, we explore multiple design variants to find the best practice of DyT. Finally, inspired by the mixture-of-experts (MoE) mechanism, we introduce an enhanced adapter to further boost the adaptation performance. We validate DyT across various tasks, including image/video recognition and semantic segmentation. For instance, DyT achieves superior performance compared to existing PEFT methods while evoking only 71% of their FLOPs on the VTAB-1K benchmark.