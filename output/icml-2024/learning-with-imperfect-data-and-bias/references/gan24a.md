---
title: "Erasing the Bias: Fine-Tuning Foundation Models for Semi-Supervised Learning"
source: "https://proceedings.mlr.press/v235/gan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gan24a/gan24a.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'test-time-adaptation-methods-and-evaluation']
tags: ['semi-supervised-learning', 'foundation-models', 'fine-tuning', 'bias-correction']
venue: "ICML 2024"
tldr: "A novel SSL approach fine-tunes foundation models to remove confirmation bias, significantly improving semi-supervised classification performance."
---

# Erasing the Bias: Fine-Tuning Foundation Models for Semi-Supervised Learning

**Source**: [https://proceedings.mlr.press/v235/gan24a.html](https://proceedings.mlr.press/v235/gan24a.html)

**TLDR**: A novel SSL approach fine-tunes foundation models to remove confirmation bias, significantly improving semi-supervised classification performance.

## Abstract

Semi-supervised learning (SSL) has witnessed remarkable progress, resulting in the emergence of numerous method variations. However, practitioners often encounter challenges when attempting to deploy these methods due to their subpar performance. In this paper, we present a novel SSL approach named FineSSL that significantly addresses this limitation by adapting pre-trained foundation models. We identify the aggregated biases and cognitive deviation problems inherent in foundation models, and propose a simple yet effective solution by imposing balanced margin softmax and decoupled label smoothing. Through extensive experiments, we demonstrate that FineSSL sets a new state of the art for SSL on multiple benchmark datasets, reduces the training cost by over six times, and can seamlessly integrate various fine-tuning and modern SSL algorithms. The source code is available at https://github.com/Gank0078/FineSSL.