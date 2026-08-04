---
title: "Time Weaver: A Conditional Time Series Generation Model"
source: "https://proceedings.mlr.press/v235/narasimhan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/narasimhan24a/narasimhan24a.pdf"
categories: ['time-series-modeling-and-forecasting-methods']
tags: ['conditional-time-series-generation', 'contextual-metadata', 'diffusion-models']
venue: "ICML 2024"
tldr: "Time Weaver conditions time series generation on heterogeneous contextual metadata for realistic and contextually consistent synthesis."
---

# Time Weaver: A Conditional Time Series Generation Model

**Source**: [https://proceedings.mlr.press/v235/narasimhan24a.html](https://proceedings.mlr.press/v235/narasimhan24a.html)

**TLDR**: Time Weaver conditions time series generation on heterogeneous contextual metadata for realistic and contextually consistent synthesis.

## Abstract

Imagine generating a city’s electricity demand pattern based on weather, the presence of an electric vehicle, and location, which could be used for capacity planning during a winter freeze. Such real-world time series are often enriched with paired heterogeneous contextual metadata (e.g., weather and location). Current approaches to time series generation often ignore this paired metadata. Additionally, the heterogeneity in metadata poses several practical challenges in adapting existing conditional generation approaches from the image, audio, and video domains to the time series domain. To address this gap, we introduce TIME WEAVER, a novel diffusion-based model that leverages the heterogeneous metadata in the form of categorical, continuous, and even time-variant variables to significantly improve time series generation. Additionally, we show that naive extensions of standard evaluation metrics from the image to the time series domain are insufficient. These metrics do not penalize conditional generation approaches for their poor specificity in reproducing the metadata-specific features in the generated time series. Thus, we innovate a novel evaluation metric that accurately captures the specificity of conditional generation and the realism of the generated time series. We show that TIME WEAVER outperforms state-of-the-art benchmarks, such as Generative Adversarial Networks (GANs), by up to 30% in downstream classification tasks on real-world energy, medical, air quality, and traffic datasets.