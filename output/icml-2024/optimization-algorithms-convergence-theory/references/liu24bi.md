---
title: "Differentiable Model Scaling using Differentiable Topk"
source: "https://proceedings.mlr.press/v235/liu24bi.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24bi/liu24bi.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'optimization-algorithms-convergence-theory']
tags: ['neural-architecture-search', 'differentiable-top-k', 'model-scaling', 'large-language-models', 'network-pruning']
venue: "ICML 2024"
tldr: "A differentiable model scaling method using differentiable TopK operators to automate and improve the efficiency of neural architecture search for scaling networks."
---

# Differentiable Model Scaling using Differentiable Topk

**Source**: [https://proceedings.mlr.press/v235/liu24bi.html](https://proceedings.mlr.press/v235/liu24bi.html)

**TLDR**: A differentiable model scaling method using differentiable TopK operators to automate and improve the efficiency of neural architecture search for scaling networks.

## Abstract

Over the past few years, as large language models have ushered in an era of intelligence emergence, there has been an intensified focus on scaling networks. Although Neural Architecture Search (NAS) methods have been proposed to automate this process, they suffer from low search efficiency. This study introduces Differentiable Model Scaling (DMS), increasing the efficiency for searching optimal width and depth in networks. DMS can model both width and depth in a direct and fully differentiable way, making it easy to optimize. We have evaluated our DMS across diverse tasks, ranging from vision tasks to NLP tasks and various network architectures, including CNNs and Transformers. Results consistently indicate that our DMS can find improved structures and outperforms state-of-the-art NAS methods. Specifically, for image classification on ImageNet, our DMS improves the top-1 accuracy of EfficientNet-B0 and Deit-Tiny by 1.4% and 0.6%, respectively, and outperforms the state-of-the-art zero-shot NAS method, ZiCo, by 1.3% while requiring only 0.4 GPU days for searching. For object detection on COCO, DMS improves the mAP of Yolo-v8-n by 2.0%. For language modeling, our pruned Llama-7B outperforms the prior method with lower perplexity and higher zero-shot classification accuracy. Our code is available at https://github.com/LKJacky/Differentiable-Model-Scaling.