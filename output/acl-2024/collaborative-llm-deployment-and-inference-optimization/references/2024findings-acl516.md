---
title: "DB-LLM: Accurate Dual-Binarization for Efficient LLMs"
source: "https://aclanthology.org/2024.findings-acl.516/"
categories: ['collaborative-llm-deployment-and-inference-optimization']
tags: ['model-quantization', 'binarization', 'efficient-inference']
venue: "ACL 2024"
tldr: "A dual-binarization method for LLMs that reduces memory and computation costs while maintaining accuracy."
---

# DB-LLM: Accurate Dual-Binarization for Efficient LLMs

**Source**: [https://aclanthology.org/2024.findings-acl.516/](https://aclanthology.org/2024.findings-acl.516/)

**TLDR**: A dual-binarization method for LLMs that reduces memory and computation costs while maintaining accuracy.

## Abstract

AbstractLarge language models (LLMs) have significantly advanced the field of natural language processing, while the expensive memory and computation consumption impede their practical deployment. Quantization emerges as one of the most effective methods for improving the computational efficiency of LLMs. However, existing ultra-low-bit quantization always causes severe accuracy drops. In this paper, we empirically investigate the micro and macro characteristics of ultra-low bit quantization and present a novel Dual-Binarization method for LLMs, namely DB-LLM. For the micro-level, we take both the accuracy advantage of 2-bit-width and the efficiency advantage of binarization into account, introducing Flexible Dual Binarization (FDB). By splitting 2-bit quantized weights into two independent sets of binaries, FDB ensures the accuracy of representations and introduces flexibility, utilizing the efficient bitwise operations of binarization while retaining the inherent high sparsity of ultra-low bit quantization. For the macro-level, we find the distortion that exists in the prediction of LLM after quantization, which is specified as the deviations related to the ambiguity of samples. We propose the Deviation-Aware Distillation (DAD) method, enabling the model to focus differently on various samples. Comprehensive experiments show that our DB-LLM not only significantly surpasses the current State-of-The-Art (SoTA) in ultra-low bit quantization (, perplexity decreased from 9.64 to 7.23), but also achieves an additional 20% reduction in computational consumption compared to the SOTA method under the same bit-width. Our code is available at https://github.com/Hon-Chen/DB-LLM.