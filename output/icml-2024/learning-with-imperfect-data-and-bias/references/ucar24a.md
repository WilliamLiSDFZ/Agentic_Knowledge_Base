---
title: "Improving Antibody Humanness Prediction using Patent Data"
source: "https://proceedings.mlr.press/v235/ucar24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ucar24a/ucar24a.pdf"
categories: ['geometry-aware-antibody-design-optimization', 'learning-with-imperfect-data-and-bias']
tags: ['antibody-humanness', 'patent-data', 'immunogenicity']
venue: "ICML 2024"
tldr: "Improves antibody humanness prediction by leveraging patent data through a multi-stage multi-loss training process."
---

# Improving Antibody Humanness Prediction using Patent Data

**Source**: [https://proceedings.mlr.press/v235/ucar24a.html](https://proceedings.mlr.press/v235/ucar24a.html)

**TLDR**: Improves antibody humanness prediction by leveraging patent data through a multi-stage multi-loss training process.

## Abstract

We investigate the potential of patent data for improving the antibody humanness prediction using a multi-stage, multi-loss training process. Humanness serves as a proxy for the immunogenic response to antibody therapeutics, one of the major causes of attrition in drug discovery and a challenging obstacle for their use in clinical settings. We pose the initial learning stage as a weakly-supervised contrastive-learning problem, where each antibody sequence is associated with possibly multiple identifiers of function and the objective is to learn an encoder that groups them according to their patented properties. We then freeze a part of the contrastive encoder and continue training it on the patent data using the cross-entropy loss to predict the humanness score of a given antibody sequence. We illustrate the utility of the patent data and our approach by performing inference on three different immunogenicity datasets, unseen during training. Our empirical results demonstrate that the learned model consistently outperforms the alternative baselines and establishes new state-of-the-art on five out of six inference tasks, irrespective of the used metric.