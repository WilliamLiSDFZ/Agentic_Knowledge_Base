---
title: "Kernel-Based Evaluation of Conditional Biological Sequence Models"
source: "https://proceedings.mlr.press/v235/glaser24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/glaser24a/glaser24a.pdf"
categories: ['generative-models-for-molecular-protein-design', 'information-retrieval-and-recommendation-systems']
tags: ['kernel-methods', 'conditional-sequence-models', 'biological-sequences']
venue: "ICML 2024"
tldr: "Develops kernel-based evaluation tools for conditional biological sequence generative models using a new conditional discrepancy measure."
---

# Kernel-Based Evaluation of Conditional Biological Sequence Models

**Source**: [https://proceedings.mlr.press/v235/glaser24a.html](https://proceedings.mlr.press/v235/glaser24a.html)

**TLDR**: Develops kernel-based evaluation tools for conditional biological sequence generative models using a new conditional discrepancy measure.

## Abstract

We propose a set of kernel-based tools to evaluate the designs and tune the hyperparameters of conditional sequence models, with a focus on problems in computational biology. The backbone of our tools is a new measure of discrepancy between the true conditional distribution and the model’s estimate, called the Augmented Conditional Maximum Mean Discrepancy (ACMMD). Provided that the model can be sampled from, the ACMMD can be estimated unbiasedly from data to quantify absolute model fit, integrated within hypothesis tests, and used to evaluate model reliability. We demonstrate the utility of our approach by analyzing a popular protein design model, ProteinMPNN. We are able to reject the hypothesis that ProteinMPNN fits its data for various protein families, and tune the model’s temperature hyperparameter to achieve a better fit.