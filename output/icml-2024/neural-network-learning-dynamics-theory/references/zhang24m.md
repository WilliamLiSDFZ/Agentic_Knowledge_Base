---
title: "Look Ahead or Look Around? A Theoretical Comparison Between Autoregressive and Masked Pretraining"
source: "https://proceedings.mlr.press/v235/zhang24m.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24m/zhang24m.pdf"
categories: ['neural-network-learning-dynamics-theory', 'large-language-model-alignment-and-capabilities']
tags: ['self-supervised-learning', 'autoregressive', 'masked-pretraining']
venue: "ICML 2024"
tldr: "A theoretical comparison between autoregressive and masked pretraining objectives revealing distinct properties that explain their downstream task behaviors."
---

# Look Ahead or Look Around? A Theoretical Comparison Between Autoregressive and Masked Pretraining

**Source**: [https://proceedings.mlr.press/v235/zhang24m.html](https://proceedings.mlr.press/v235/zhang24m.html)

**TLDR**: A theoretical comparison between autoregressive and masked pretraining objectives revealing distinct properties that explain their downstream task behaviors.

## Abstract

In recent years, the rise of generative self-supervised learning (SSL) paradigms has exhibited impressive performance across visual, language, and multi-modal domains. While the varied designs of generative SSL objectives lead to distinct properties in downstream tasks, a theoretical understanding of these differences remains largely unexplored. In this paper, we establish the first theoretical comparisons between two leading generative SSL paradigms: autoregressive SSL and masked SSL. Through establishing theoretical frameworks, we elucidate the strengths and limitations of autoregressive and masked SSL within the primary evaluation tasks of classification and content generation. Our findings demonstrate that in classification tasks, the flexibility of targeted tokens in masked SSL fosters more inter-sample connections compared to the fixed position of target tokens in autoregressive SSL, which yields superior clustering performance. In content generation tasks, the misalignment between the flexible lengths of test samples and the fixed length of unmasked texts in masked SSL (vs. flexible lengths of conditional texts in autoregressive SSL) hinders its generation performance. To leverage each other’s strengths and mitigate weaknesses, we propose diversity-enhanced autoregressive and variable-length masked objectives, which substantially improve the classification performance of autoregressive SSL and the generation performance of masked SSL. Code is available at https://github.com/PKU-ML/LookAheadLookAround.