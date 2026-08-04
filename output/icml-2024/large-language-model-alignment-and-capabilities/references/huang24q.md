---
title: "BiLLM: Pushing the Limit of Post-Training Quantization for LLMs"
source: "https://proceedings.mlr.press/v235/huang24q.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24q/huang24q.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'large-language-model-alignment-and-capabilities']
tags: ['post-training-quantization', 'binarization', 'large-language-models']
venue: "ICML 2024"
tldr: "Pushes LLM quantization to 1-bit weights via a novel binarization method that preserves model performance while drastically reducing memory."
---

# BiLLM: Pushing the Limit of Post-Training Quantization for LLMs

**Source**: [https://proceedings.mlr.press/v235/huang24q.html](https://proceedings.mlr.press/v235/huang24q.html)

**TLDR**: Pushes LLM quantization to 1-bit weights via a novel binarization method that preserves model performance while drastically reducing memory.

## Abstract

Pretrained large language models (LLMs) exhibit exceptional general language processing capabilities but come with significant demands on memory and computational resources. As a powerful compression technology, binarization can extremely reduce model weights to a mere 1 bit, lowering the expensive computation and memory requirements. However, existing quantization techniques fall short of maintaining LLM performance under ultra-low bit-widths. In response to this challenge, we present BiLLM, a groundbreaking 1-bit post-training quantization scheme tailored for pretrained LLMs. Based on the weight distribution of LLMs, BiLLM first identifies and structurally selects salient weights, and minimizes the compression loss through an effective binary residual approximation strategy. Moreover, considering the bell-shaped distribution of the non-salient weights, we propose an optimal splitting search to group and binarize them accurately. BiLLM, for the first time, achieves high-accuracy inference (e.g. 8.41 perplexity on LLaMA2-70B) with only 1.08-bit weights across various LLM families and evaluation metrics, outperforms SOTA quantization methods of LLM by significant margins. Moreover, BiLLM enables the binarization process of a 7-billion LLM within 0.5 hours on a single GPU, demonstrating satisfactory time efficiency. Our code is available at https://github.com/Aaronhuang-778/BiLLM .