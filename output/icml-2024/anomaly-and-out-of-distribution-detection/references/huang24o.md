---
title: "Machine Vision Therapy: Multimodal Large Language Models Can Enhance Visual Robustness via Denoising In-Context Learning"
source: "https://proceedings.mlr.press/v235/huang24o.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24o/huang24o.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'anomaly-and-out-of-distribution-detection']
tags: ['CLIP', 'out-of-distribution-robustness', 'denoising-in-context-learning']
venue: "ICML 2024"
tldr: "Uses multimodal LLMs for denoising in-context learning to enhance visual robustness of pretrained models under distribution shift without human annotation."
---

# Machine Vision Therapy: Multimodal Large Language Models Can Enhance Visual Robustness via Denoising In-Context Learning

**Source**: [https://proceedings.mlr.press/v235/huang24o.html](https://proceedings.mlr.press/v235/huang24o.html)

**TLDR**: Uses multimodal LLMs for denoising in-context learning to enhance visual robustness of pretrained models under distribution shift without human annotation.

## Abstract

Although pre-trained models such as Contrastive Language-Image Pre-Training (CLIP) show impressive generalization results, their robustness is still limited under Out-of-Distribution (OOD) scenarios. Instead of undesirably leveraging human annotation as commonly done, it is possible to leverage the visual understanding power of Multi-modal Large Language Models (MLLMs). However, MLLMs struggle with vision problems due to task incompatibility, thus hindering their effectiveness. In this paper, we propose to effectively leverage MLLMs via Machine Vision Therapy which aims to rectify erroneous predictions of specific vision models. By supervising vision models using MLLM predictions, visual robustness can be boosted in a nearly unsupervised manner. Moreover, we propose a Denoising In-Context Learning (DICL) strategy to solve the incompatibility issue. Concretely, by examining the noise probability of each example through a transition matrix, we construct an instruction containing a correct exemplar and a probable erroneous one, which enables MLLMs to detect and rectify the incorrect predictions of vision models. Under mild assumptions, we theoretically show that our DICL method is guaranteed to find the ground truth. Through extensive experiments on various OOD datasets, our method demonstrates powerful capabilities for enhancing visual robustness under many OOD scenarios.