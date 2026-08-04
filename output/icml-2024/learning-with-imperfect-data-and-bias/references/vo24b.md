---
title: "Optimal Transport for Structure Learning Under Missing Data"
source: "https://proceedings.mlr.press/v235/vo24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/vo24b/vo24b.pdf"
categories: ['causal-inference-and-discovery-methods', 'learning-with-imperfect-data-and-bias']
tags: ['causal-discovery', 'missing-data', 'optimal-transport', 'imputation', 'structure-learning']
venue: "ICML 2024"
tldr: "Addresses the chicken-and-egg problem of causal discovery under missing data by jointly learning causal structure and imputation via optimal transport."
---

# Optimal Transport for Structure Learning Under Missing Data

**Source**: [https://proceedings.mlr.press/v235/vo24b.html](https://proceedings.mlr.press/v235/vo24b.html)

**TLDR**: Addresses the chicken-and-egg problem of causal discovery under missing data by jointly learning causal structure and imputation via optimal transport.

## Abstract

Causal discovery in the presence of missing data introduces a chicken-and-egg dilemma. While the goal is to recover the true causal structure, robust imputation requires considering the dependencies or, preferably, causal relations among variables. Merely filling in missing values with existing imputation methods and subsequently applying structure learning on the complete data is empirically shown to be sub-optimal. To address this problem, we propose a score-based algorithm for learning causal structures from missing data based on optimal transport. This optimal transport viewpoint diverges from existing score-based approaches that are dominantly based on expectation maximization. We formulate structure learning as a density fitting problem, where the goal is to find the causal model that induces a distribution of minimum Wasserstein distance with the observed data distribution. Our framework is shown to recover the true causal graphs more effectively than competing methods in most simulations and real-data settings. Empirical evidence also shows the superior scalability of our approach, along with the flexibility to incorporate any off-the-shelf causal discovery methods for complete data.