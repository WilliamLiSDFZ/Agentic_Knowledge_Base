---
title: "Multigroup Robustness"
source: "https://proceedings.mlr.press/v235/hu24l.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hu24l/hu24l.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['robust-learning', 'data-corruption', 'multigroup-fairness']
venue: "ICML 2024"
tldr: "Extends robust learning algorithms to handle structured, group-localized data corruption patterns rather than arbitrary indiscriminate corruption."
---

# Multigroup Robustness

**Source**: [https://proceedings.mlr.press/v235/hu24l.html](https://proceedings.mlr.press/v235/hu24l.html)

**TLDR**: Extends robust learning algorithms to handle structured, group-localized data corruption patterns rather than arbitrary indiscriminate corruption.

## Abstract

To address the shortcomings of real-world datasets, robust learning algorithms have been designed to overcome arbitrary and indiscriminate data corruption. However, practical processes of gathering data may lead to patterns of data corruption that are localized to specific partitions of the training dataset. Motivated by critical applications where the learned model is deployed to make predictions about people from a rich collection of overlapping subpopulations, we initiate the study of multigroup robust algorithms whose robustness guarantees for each subpopulation only degrade with the amount of data corruption inside that subpopulation. When the data corruption is not distributed uniformly over subpopulations, our algorithms provide more meaningful robustness guarantees than standard guarantees that are oblivious to how the data corruption and the affected subpopulations are related. Our techniques establish a new connection between multigroup fairness and robustness.