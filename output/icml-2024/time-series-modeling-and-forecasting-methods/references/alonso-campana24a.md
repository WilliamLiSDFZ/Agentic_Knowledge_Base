---
title: "Predicting Dose-Response Curves with Deep Neural Networks"
source: "https://proceedings.mlr.press/v235/alonso-campana24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/alonso-campana24a/alonso-campana24a.pdf"
categories: ['causal-ml-for-clinical-decision-making', 'time-series-modeling-and-forecasting-methods']
tags: ['dose-response-curves', 'deep-neural-networks', 'drug-response']
venue: "ICML 2024"
tldr: "This paper proposes deep neural networks to predict dose-response curves beyond the simplistic Hill-equation model for complex drug interactions."
---

# Predicting Dose-Response Curves with Deep Neural Networks

**Source**: [https://proceedings.mlr.press/v235/alonso-campana24a.html](https://proceedings.mlr.press/v235/alonso-campana24a.html)

**TLDR**: This paper proposes deep neural networks to predict dose-response curves beyond the simplistic Hill-equation model for complex drug interactions.

## Abstract

Dose-response curves characterize the relationship between the concentration of drugs and their inhibitory effect on the growth of specific types of cells. The predominant Hill-equation model of an ideal enzymatic inhibition unduly simplifies the biochemical reality of many drugs; and for these drugs the widely-used drug performance indicator of the half-inhibitory concentration $IC_{50}$ can lead to poor therapeutic recommendations and poor selections of promising drug candidates. We develop a neural model that uses an embedding of the interaction between drug molecules and the tissue transcriptome to estimate the entire dose-response curve rather than a scalar aggregate. We find that, compared to the prior state of the art, this model excels at interpolating and extrapolating the inhibitory effect of untried concentrations. Unlike prevalent parametric models, it it able to accurately predict dose-response curves of drugs on previously unseen tumor tissues as well as of previously untested drug molecules on established tumor cell lines.