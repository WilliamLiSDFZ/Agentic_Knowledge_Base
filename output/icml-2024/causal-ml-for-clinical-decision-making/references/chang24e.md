---
title: "From Biased Selective Labels to Pseudo-Labels: An Expectation-Maximization Framework for Learning from Biased Decisions"
source: "https://proceedings.mlr.press/v235/chang24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chang24e/chang24e.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'causal-ml-for-clinical-decision-making']
tags: ['selective-labels', 'disparate-censorship', 'EM-framework', 'clinical-bias']
venue: "ICML 2024"
tldr: "An EM-based pseudo-labeling framework for learning from biased selective labels arising from subgroup-varying labeling disparities in clinical settings."
---

# From Biased Selective Labels to Pseudo-Labels: An Expectation-Maximization Framework for Learning from Biased Decisions

**Source**: [https://proceedings.mlr.press/v235/chang24e.html](https://proceedings.mlr.press/v235/chang24e.html)

**TLDR**: An EM-based pseudo-labeling framework for learning from biased selective labels arising from subgroup-varying labeling disparities in clinical settings.

## Abstract

Selective labels occur when label observations are subject to a decision-making process; e.g., diagnoses that depend on the administration of laboratory tests. We study a clinically-inspired selective label problem called disparate censorship, where labeling biases vary across subgroups and unlabeled individuals are imputed as “negative” (i.e., no diagnostic test = no illness). Machine learning models naively trained on such labels could amplify labeling bias. Inspired by causal models of selective labels, we propose Disparate Censorship Expectation-Maximization (DCEM), an algorithm for learning in the presence of disparate censorship. We theoretically analyze how DCEM mitigates the effects of disparate censorship on model performance. We validate DCEM on synthetic data, showing that it improves bias mitigation (area between ROC curves) without sacrificing discriminative performance (AUC) compared to baselines. We achieve similar results in a sepsis classification task using clinical data.