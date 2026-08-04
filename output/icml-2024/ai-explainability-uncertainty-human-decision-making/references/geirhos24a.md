---
title: "Don’t trust your eyes: on the (un)reliability of feature visualizations"
source: "https://proceedings.mlr.press/v235/geirhos24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/geirhos24a/geirhos24a.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'adversarial-robustness-and-model-security']
tags: ['feature-visualization', 'neural-network-interpretability', 'reliability']
venue: "ICML 2024"
tldr: "Demonstrates that feature visualizations used to interpret neural networks are unreliable and can be misleading."
---

# Don’t trust your eyes: on the (un)reliability of feature visualizations

**Source**: [https://proceedings.mlr.press/v235/geirhos24a.html](https://proceedings.mlr.press/v235/geirhos24a.html)

**TLDR**: Demonstrates that feature visualizations used to interpret neural networks are unreliable and can be misleading.

## Abstract

How do neural networks extract patterns from pixels? Feature visualizations attempt to answer this important question by visualizing highly activating patterns through optimization. Today, visualization methods form the foundation of our knowledge about the internal workings of neural networks, as a type of mechanistic interpretability. Here we ask: How reliable are feature visualizations? We start our investigation by developing network circuits that trick feature visualizations into showing arbitrary patterns that are completely disconnected from normal network behavior on natural input. We then provide evidence for a similar phenomenon occurring in standard, unmanipulated networks: feature visualizations are processed very differently from standard input, casting doubt on their ability to "explain" how neural networks process natural images. This can be used as a sanity check for feature visualizations. We underpin our empirical findings by theory proving that the set of functions that can be reliably understood by feature visualization is extremely small and does not include general black-box neural networks. Therefore, a promising way forward could be the development of networks that enforce certain structures in order to ensure more reliable feature visualizations.