---
title: "Post-hoc Part-Prototype Networks"
source: "https://proceedings.mlr.press/v235/tan24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tan24g/tan24g.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making']
tags: ['post-hoc-explainability', 'part-prototypes', 'interpretability']
venue: "ICML 2024"
tldr: "Post-hoc Part-Prototype Networks explain not just where but what a model looks for by associating predictions with interpretable part prototypes."
---

# Post-hoc Part-Prototype Networks

**Source**: [https://proceedings.mlr.press/v235/tan24g.html](https://proceedings.mlr.press/v235/tan24g.html)

**TLDR**: Post-hoc Part-Prototype Networks explain not just where but what a model looks for by associating predictions with interpretable part prototypes.

## Abstract

Post-hoc explainability methods such as Grad-CAM are popular because they do not influence the performance of a trained model. However, they mainly reveal ”where” a model looks at for a given input, fail to explain ”what” the model looks for (e.g., what is important to classify a bird image to a Scott Oriole?). Existing part-prototype networks leverage part-prototypes (e.g., characteristic Scott Oriole’s wing and head) to answer both ”where" and ”what", but often under-perform their black box counterparts in the accuracy. Therefore, a natural question is: can one construct a network that answers both ”where” and ”what" in a post-hoc manner to guarantee the model’s performance? To this end, we propose the first post-hoc part-prototype network via decomposing the classification head of a trained model into a set of interpretable part-prototypes. Concretely, we propose an unsupervised prototype discovery and refining strategy to obtain prototypes that can precisely reconstruct the classification head, yet being interpretable. Besides guaranteeing the performance, we show that our network offers more faithful explanations qualitatively and yields even better part-prototypes quantitatively than prior part-prototype networks.