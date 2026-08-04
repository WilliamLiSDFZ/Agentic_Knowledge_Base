---
title: "Transformers Get Stable: An End-to-End Signal Propagation Theory for Language Models"
source: "https://proceedings.mlr.press/v235/kedia24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kedia24a/kedia24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'neural-network-learning-dynamics-theory']
tags: ['signal-propagation', 'transformer-scaling', 'depth-stability']
venue: "ICML 2024"
tldr: "Develops a unified signal propagation theory governing forward and backward moments in transformers to enable stable deep scaling."
---

# Transformers Get Stable: An End-to-End Signal Propagation Theory for Language Models

**Source**: [https://proceedings.mlr.press/v235/kedia24a.html](https://proceedings.mlr.press/v235/kedia24a.html)

**TLDR**: Develops a unified signal propagation theory governing forward and backward moments in transformers to enable stable deep scaling.

## Abstract

In spite of their huge success, transformer models remain difficult to scale in depth. In this work, we develop a unified signal propagation theory and provide formulae that govern the moments of the forward and backward signal through the transformer model. Our framework can be used to understand and mitigate vanishing/exploding gradients, rank collapse, and instability associated with high attention scores. We also propose DeepScaleLM, an initialization and scaling scheme that conserves unit output/gradient moments throughout the model, enabling the training of very deep models with 1000 layers. We find that transformer models could be much deeper - our deep models with fewer parameters outperform shallow models in Language Modeling, Speech Translation, and Image Classification, across encoder-only, decoder-only and encoder-decoder variants, for both Pre-LN and Post-LN transformers, for multiple datasets and model sizes. These improvements also translate into improved performance on downstream Question Answering tasks and improved robustness for Image Classification.