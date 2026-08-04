---
title: "BLO-SAM: Bi-level Optimization Based Finetuning of the Segment Anything Model for Overfitting-Preventing Semantic Segmentation"
source: "https://proceedings.mlr.press/v235/zhang24ai.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24ai/zhang24ai.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'optimization-algorithms-convergence-theory']
tags: ['segment-anything', 'bi-level-optimization', 'semantic-segmentation']
venue: "ICML 2024"
tldr: "Uses bi-level optimization to fine-tune the Segment Anything Model to prevent overfitting in domain-specific semantic segmentation."
---

# BLO-SAM: Bi-level Optimization Based Finetuning of the Segment Anything Model for Overfitting-Preventing Semantic Segmentation

**Source**: [https://proceedings.mlr.press/v235/zhang24ai.html](https://proceedings.mlr.press/v235/zhang24ai.html)

**TLDR**: Uses bi-level optimization to fine-tune the Segment Anything Model to prevent overfitting in domain-specific semantic segmentation.

## Abstract

The Segment Anything Model (SAM), a foundation model pretrained on millions of images and segmentation masks, has significantly advanced semantic segmentation, a fundamental task in computer vision. Despite its strengths, SAM encounters two major challenges. Firstly, it struggles with segmenting specific objects autonomously, as it relies on users to manually input prompts like points or bounding boxes to identify targeted objects. Secondly, SAM faces challenges in excelling at specific downstream tasks, like medical imaging, due to a disparity between the distribution of its pretraining data, which predominantly consists of general-domain images, and the data used in downstream tasks. Current solutions to these problems, which involve finetuning SAM, often lead to overfitting, a notable issue in scenarios with very limited data, like in medical imaging. To overcome these limitations, we introduce BLO-SAM, which finetunes SAM based on bi-level optimization (BLO). Our approach allows for automatic image segmentation without the need for manual prompts, by optimizing a learnable prompt embedding. Furthermore, it significantly reduces the risk of overfitting by training the model’s weight parameters and the prompt embedding on two separate subsets of the training dataset, each at a different level of optimization. We apply BLO-SAM to diverse semantic segmentation tasks in general and medical domains. The results demonstrate BLO-SAM’s superior performance over various state-of-the-art image semantic segmentation methods. The code of BLO-SAM is available at https://github.com/importZL/BLO-SAM.