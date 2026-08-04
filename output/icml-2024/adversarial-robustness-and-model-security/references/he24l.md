---
title: "Be Your Own Neighborhood: Detecting Adversarial Examples by the Neighborhood Relations Built on Self-Supervised Learning"
source: "https://proceedings.mlr.press/v235/he24l.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/he24l/he24l.pdf"
categories: ['adversarial-robustness-and-model-security', 'anomaly-and-out-of-distribution-detection']
tags: ['adversarial-detection', 'self-supervised-learning', 'neighborhood-relations']
venue: "ICML 2024"
tldr: "Proposes BEYOND, an adversarial example detection framework leveraging neighborhood relations from self-supervised learning."
---

# Be Your Own Neighborhood: Detecting Adversarial Examples by the Neighborhood Relations Built on Self-Supervised Learning

**Source**: [https://proceedings.mlr.press/v235/he24l.html](https://proceedings.mlr.press/v235/he24l.html)

**TLDR**: Proposes BEYOND, an adversarial example detection framework leveraging neighborhood relations from self-supervised learning.

## Abstract

Deep Neural Networks (DNNs) are vulnerable to Adversarial Examples (AEs), hindering their use in safety-critical systems. In this paper, we present BEYOND, an innovative AE detection framework designed for reliable predictions. BEYOND identifies AEs by distinguishing the AE’s abnormal relation with its augmented versions, i.e. neighbors, from two prospects: representation similarity and label consistency. An off-the-shelf Self-Supervised Learning (SSL) model is used to extract the representation and predict the label for its highly informative representation capacity compared to supervised learning models. We found clean samples maintain a high degree of representation similarity and label consistency relative to their neighbors, in contrast to AEs which exhibit significant discrepancies. We explain this observation and show that leveraging this discrepancy BEYOND can accurately detect AEs. Additionally, we develop a rigorous justification for the effectiveness of BEYOND. Furthermore, as a plug-and-play model, BEYOND can easily cooperate with the Adversarial Trained Classifier (ATC), achieving state-of-the-art (SOTA) robustness accuracy. Experimental results show that BEYOND outperforms baselines by a large margin, especially under adaptive attacks. Empowered by the robust relationship built on SSL, we found that BEYOND outperforms baselines in terms of both detection ability and speed. Project page: https://huggingface.co/spaces/allenhzy/Be-Your-Own-Neighborhood.