---
title: "AttnLRP: Attention-Aware Layer-Wise Relevance Propagation for Transformers"
source: "https://proceedings.mlr.press/v235/achtibat24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/achtibat24a/achtibat24a.pdf"
categories: ['llm-geometry-and-interpretability-research']
tags: ['layer-wise-relevance-propagation', 'attention', 'transformer-interpretability', 'attribution']
venue: "ICML 2024"
tldr: "AttnLRP extends layer-wise relevance propagation to handle attention mechanisms faithfully and efficiently in large transformer models."
---

# AttnLRP: Attention-Aware Layer-Wise Relevance Propagation for Transformers

**Source**: [https://proceedings.mlr.press/v235/achtibat24a.html](https://proceedings.mlr.press/v235/achtibat24a.html)

**TLDR**: AttnLRP extends layer-wise relevance propagation to handle attention mechanisms faithfully and efficiently in large transformer models.

## Abstract

Large Language Models are prone to biased predictions and hallucinations, underlining the paramount importance of understanding their model-internal reasoning process. However, achieving faithful attributions for the entirety of a black-box transformer model and maintaining computational efficiency is an unsolved challenge. By extending the Layer-wise Relevance Propagation attribution method to handle attention layers, we address these challenges effectively. While partial solutions exist, our method is the first to faithfully and holistically attribute not only input but also latent representations of transformer models with the computational efficiency similar to a single backward pass. Through extensive evaluations against existing methods on LLaMa 2, Mixtral 8x7b, Flan-T5 and vision transformer architectures, we demonstrate that our proposed approach surpasses alternative methods in terms of faithfulness and enables the understanding of latent representations, opening up the door for concept-based explanations. We provide an LRP library at https://github.com/rachtibat/LRP-eXplains-Transformers.