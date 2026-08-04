---
title: "Ditto: Quantization-aware Secure Inference of Transformers upon MPC"
source: "https://proceedings.mlr.press/v235/wu24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24d/wu24d.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'transformer-architecture-efficiency-and-scaling']
tags: ['secure-inference', 'multi-party-computation', 'quantization', 'transformers']
venue: "ICML 2024"
tldr: "Ditto integrates quantization-aware training with MPC to reduce overhead in secure transformer inference while preserving accuracy."
---

# Ditto: Quantization-aware Secure Inference of Transformers upon MPC

**Source**: [https://proceedings.mlr.press/v235/wu24d.html](https://proceedings.mlr.press/v235/wu24d.html)

**TLDR**: Ditto integrates quantization-aware training with MPC to reduce overhead in secure transformer inference while preserving accuracy.

## Abstract

Due to the rising privacy concerns on sensitive client data and trained models like Transformers, secure multi-party computation (MPC) techniques are employed to enable secure inference despite attendant overhead. Existing works attempt to reduce the overhead using more MPC-friendly non-linear function approximations. However, the integration of quantization widely used in plaintext inference into the MPC domain remains unclear. To bridge this gap, we propose the framework named Ditto to enable more efficient quantization-aware secure Transformer inference. Concretely, we first incorporate an MPC-friendly quantization into Transformer inference and employ a quantization-aware distillation procedure to maintain the model utility. Then, we propose novel MPC primitives to support the type conversions that are essential in quantization and implement the quantization-aware MPC execution of secure quantized inference. This approach significantly decreases both computation and communication overhead, leading to improvements in overall efficiency. We conduct extensive experiments on Bert and GPT2 models to evaluate the performance of Ditto. The results demonstrate that Ditto is about $3.14\sim 4.40\times$ faster than MPCFormer (ICLR 2023) and $1.44\sim 2.35\times$ faster than the state-of-the-art work PUMA with negligible utility degradation.