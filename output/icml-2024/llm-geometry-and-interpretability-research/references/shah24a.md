---
title: "Decomposing and Editing Predictions by Modeling Model Computation"
source: "https://proceedings.mlr.press/v235/shah24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shah24a/shah24a.pdf"
categories: ['llm-geometry-and-interpretability-research', 'ai-explainability-uncertainty-human-decision-making']
tags: ['model-interpretability', 'component-decomposition', 'prediction-analysis']
venue: "ICML 2024"
tldr: "A framework called component modeling decomposes model predictions in terms of architectural building blocks to enable editing and understanding of internal computations."
---

# Decomposing and Editing Predictions by Modeling Model Computation

**Source**: [https://proceedings.mlr.press/v235/shah24a.html](https://proceedings.mlr.press/v235/shah24a.html)

**TLDR**: A framework called component modeling decomposes model predictions in terms of architectural building blocks to enable editing and understanding of internal computations.

## Abstract

How does the internal computation of a machine learning model transform inputs into predictions? To tackle this question, we introduce a framework called component modeling for decomposing a model prediction in terms of its components—architectural "building blocks" such as convolution filters or attention heads. We focus on a special case of this framework, component attribution, where the goal is to estimate the counterfactual impact of individual components on a given prediction. We then present COAR, a scalable algorithm for estimating component attributions, and demonstrate its effectiveness across models, datasets and modalities. Finally, we show that COAR directly enables effective model editing. Our code is available at github.com/MadryLab/modelcomponents.