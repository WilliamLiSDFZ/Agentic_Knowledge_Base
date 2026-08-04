---
title: "Attribute Based Interpretable Evaluation Metrics for Generative Models"
source: "https://proceedings.mlr.press/v235/kim24t.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24t/kim24t.pdf"
categories: ['generative-models-and-variational-inference', 'ai-explainability-uncertainty-human-decision-making']
tags: ['generative-model-evaluation', 'attribute-based-metrics', 'distribution-similarity']
venue: "ICML 2024"
tldr: "Introduces attribute-based interpretable evaluation metrics that capture fine-grained distributional properties of generative models."
---

# Attribute Based Interpretable Evaluation Metrics for Generative Models

**Source**: [https://proceedings.mlr.press/v235/kim24t.html](https://proceedings.mlr.press/v235/kim24t.html)

**TLDR**: Introduces attribute-based interpretable evaluation metrics that capture fine-grained distributional properties of generative models.

## Abstract

When the training dataset comprises a 1:1 proportion of dogs to cats, a generative model that produces 1:1 dogs and cats better resembles the training species distribution than another model with 3:1 dogs and cats. Can we capture this phenomenon using existing metrics? Unfortunately, we cannot, because these metrics do not provide any interpretability beyond “diversity". In this context, we propose a new evaluation protocol that measures the divergence of a set of generated images from the training set regarding the distribution of attribute strengths as follows. Singleattribute Divergence (SaD) reveals the attributes that are generated excessively or insufficiently by measuring the divergence of PDFs of individual attributes. Paired-attribute Divergence (PaD) reveals such pairs of attributes by measuring the divergence of joint PDFs of pairs of attributes. For measuring the attribute strengths of an image, we propose Heterogeneous CLIPScore (HCS) which measures the cosine similarity between image and text vectors with heterogeneous initial points. With SaD and PaD, we reveal the following about existing generative models. ProjectedGAN generates implausible attribute relationships such as baby with beard even though it has competitive scores of existing metrics. Diffusion models struggle to capture diverse colors in the datasets. The larger sampling timesteps of the latent diffusion model generate the more minor objects including earrings and necklace. Stable Diffusion v1.5 better captures the attributes than v2.1. Our metrics lay a foundation for explainable evaluations of generative models.