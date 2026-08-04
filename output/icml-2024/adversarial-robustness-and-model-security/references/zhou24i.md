---
title: "Attack-free Evaluating and Enhancing Adversarial Robustness on Categorical Data"
source: "https://proceedings.mlr.press/v235/zhou24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhou24i/zhou24i.pdf"
categories: ['adversarial-robustness-and-model-security', 'learning-with-imperfect-data-and-bias']
tags: ['adversarial-robustness', 'categorical-data', 'tabular-attributes']
venue: "ICML 2024"
tldr: "Proposes an attack-free framework for evaluating and enhancing adversarial robustness of classifiers on categorical and tabular data."
---

# Attack-free Evaluating and Enhancing Adversarial Robustness on Categorical Data

**Source**: [https://proceedings.mlr.press/v235/zhou24i.html](https://proceedings.mlr.press/v235/zhou24i.html)

**TLDR**: Proposes an attack-free framework for evaluating and enhancing adversarial robustness of classifiers on categorical and tabular data.

## Abstract

Research on adversarial robustness has predominantly focused on continuous inputs, leaving categorical inputs, especially tabular attributes, less examined. To echo this challenge, our work aims to evaluate and enhance the robustness of classification over categorical attributes against adversarial perturbations through efficient attack-free approaches. We propose a robustness evaluation metric named Integrated Gradient-Smoothed Gradient (IGSG). It is designed to evaluate the attributional sensitivity of each feature and the decision boundary of the classifier, two aspects that significantly influence adversarial risk, according to our theoretical analysis. Leveraging this metric, we develop an IGSG-based regularization to reduce adversarial risk by suppressing the sensitivity of categorical attributes. We conduct extensive empirical studies over categorical datasets of various application domains. The results affirm the efficacy of both IGSG and IGSG-based regularization. Notably, IGSG-based regularization surpasses the state-of-the-art robust training methods by a margin of approximately 0.4% to 12.2% on average in terms of adversarial accuracy, especially on high-dimension datasets. The code is available at https://github.com/YujunZhou/IGSG.