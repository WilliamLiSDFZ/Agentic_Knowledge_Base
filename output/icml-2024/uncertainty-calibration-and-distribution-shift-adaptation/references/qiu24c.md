---
title: "To Cool or not to Cool? Temperature Network Meets Large Foundation Models via DRO"
source: "https://proceedings.mlr.press/v235/qiu24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/qiu24c/qiu24c.pdf"
categories: ['uncertainty-calibration-and-distribution-shift-adaptation', 'large-language-model-alignment-and-capabilities']
tags: ['temperature-scaling', 'foundation-models', 'distributionally-robust-optimization', 'LLMs', 'CLIP', 'calibration']
venue: "ICML 2024"
tldr: "A temperature network trained via DRO to dynamically set temperature parameters for large foundation models."
---

# To Cool or not to Cool? Temperature Network Meets Large Foundation Models via DRO

**Source**: [https://proceedings.mlr.press/v235/qiu24c.html](https://proceedings.mlr.press/v235/qiu24c.html)

**TLDR**: A temperature network trained via DRO to dynamically set temperature parameters for large foundation models.

## Abstract

The temperature parameter plays a profound role during training and/or inference with large foundation models (LFMs) such as large language models (LLMs) and CLIP models. Particularly, it adjusts the logits in the softmax function in LLMs, which is crucial for next token generation, and it scales the similarities in the contrastive loss for training CLIP models. A significant question remains: “ Is it viable to learn a neural network to predict a personalized temperature of any input data for enhancing LFMs?" In this paper, we present a principled framework for learning a small yet generalizable temperature prediction network (TempNet) to improve LFMs. Our solution is composed of a novel learning framework with robust losses underpinned by constrained distributionally robust optimization (DRO), and a properly designed TempNet with theoretical inspiration. TempNet can be trained together with a large foundation model from scratch or learned separately given a pretrained foundation model. It is not only useful for predicting personalized temperature to promote the training of LFMs but also generalizable and transferable to new tasks. Our experiments on LLMs and CLIP models demonstrate that TempNet greatly improves the performance of existing solutions or models.