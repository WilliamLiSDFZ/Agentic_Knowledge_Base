---
title: "Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws"
source: "https://proceedings.mlr.press/v235/sardana24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sardana24a/sardana24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'llm-serving-systems-and-infrastructure']
tags: ['scaling-laws', 'LLM', 'inference-cost', 'Chinchilla', 'model-size-optimization']
venue: "ICML 2024"
tldr: "LLM scaling laws are extended beyond Chinchilla-optimal training by incorporating inference costs, shifting optimal model size and training data recommendations."
---

# Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws

**Source**: [https://proceedings.mlr.press/v235/sardana24a.html](https://proceedings.mlr.press/v235/sardana24a.html)

**TLDR**: LLM scaling laws are extended beyond Chinchilla-optimal training by incorporating inference costs, shifting optimal model size and training data recommendations.

## Abstract

Large language model (LLM) scaling laws are empirical formulas that estimate changes in model quality as a result of increasing parameter count and training data. However, these formulas, including the popular Deepmind Chinchilla scaling laws, neglect to include the cost of inference. We modify the Chinchilla scaling laws to calculate the optimal LLM parameter count and pre-training data size to train and deploy a model of a given quality and inference demand. We conduct our analysis both in terms of a compute budget and real-world costs and find that LLM researchers expecting reasonably large inference demand ($\sim$1B requests) should train models smaller and longer than Chinchilla-optimal. Furthermore, we train 47 models of varying sizes and parameter counts to validate our formula and find that model quality continues to improve as we scale tokens per parameter to extreme ranges (up to 10,000). Finally, we ablate the procedure used to fit the Chinchilla scaling law coefficients and find that developing scaling laws only from data collected at typical token/parameter ratios overestimates the impact of additional tokens at these extreme ranges.