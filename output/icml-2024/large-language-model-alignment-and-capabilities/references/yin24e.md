---
title: "Outlier Weighed Layerwise Sparsity (OWL): A Missing Secret Sauce for Pruning LLMs to High Sparsity"
source: "https://proceedings.mlr.press/v235/yin24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yin24e/yin24e.pdf"
categories: ['large-language-model-alignment-and-capabilities']
tags: ['LLM-pruning', 'sparsity', 'outlier-weights', 'layerwise']
venue: "ICML 2024"
tldr: "An outlier-weighted layerwise sparsity method is proposed to enable effective high-sparsity pruning of large language models."
---

# Outlier Weighed Layerwise Sparsity (OWL): A Missing Secret Sauce for Pruning LLMs to High Sparsity

**Source**: [https://proceedings.mlr.press/v235/yin24e.html](https://proceedings.mlr.press/v235/yin24e.html)

**TLDR**: An outlier-weighted layerwise sparsity method is proposed to enable effective high-sparsity pruning of large language models.

## Abstract

Large Language Models (LLMs), renowned for their remarkable performance across diverse domains, present a challenge due to their colossal model size when it comes to practical deployment. In response to this challenge, efforts have been directed toward the application of traditional network pruning techniques to LLMs, uncovering a massive number of parameters can be pruned in one-shot without hurting performance. Building upon insights gained from pre-LLM models, particularly BERT-level language models, prevailing LLM pruning strategies have consistently adhered to the practice of uniformly pruning all layers at equivalent sparsity levels, resulting in robust performance. However, this observation stands in contrast to the prevailing trends observed in the field of vision models, where non-uniform layerwise sparsity typically yields substantially improved results. To elucidate the underlying reasons for this disparity, we conduct a comprehensive analysis of the distribution of token features within LLMs. In doing so, we discover a strong correlation with the emergence of outliers, defined as features exhibiting significantly greater magnitudes compared to their counterparts in feature dimensions. Inspired by this finding, we introduce a novel LLM pruning methodology that incorporates a tailored set of non-uniform layerwise sparsity ratios specifically designed for LLM pruning, termed as Outlier Weighed Layerwise sparsity (OWL). The sparsity ratio of OWL is directly proportional to the outlier ratio observed within each layer, facilitating a more effective alignment between layerwise weight sparsity and outlier ratios. Our empirical evaluation, conducted across the LLaMA-V1/V2, Vicuna, OPT, and Mistral, spanning various benchmarks, demonstrates the distinct advantages offered by OWL over previous methods. For instance, OWL exhibits a remarkable performance gain, surpassing the state-of-the-art Wanda and SparseGPT by 61.22 and 6.80 perplexity at a high sparsity level of 70%, respectively, while delivering 2.6$\times$ end-to-end inference speed-up in the DeepSparse inference engine. Code is available at https://github.com/luuyin/OWL.git.