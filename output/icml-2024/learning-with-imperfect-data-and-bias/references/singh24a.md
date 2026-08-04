---
title: "Domain Generalisation via Imprecise Learning"
source: "https://proceedings.mlr.press/v235/singh24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/singh24a/singh24a.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['domain-generalization', 'imprecise-probabilities', 'out-of-distribution']
venue: "ICML 2024"
tldr: "Introduces an imprecise learning framework for domain generalization that defers between average-case and worst-case risk based on data evidence."
---

# Domain Generalisation via Imprecise Learning

**Source**: [https://proceedings.mlr.press/v235/singh24a.html](https://proceedings.mlr.press/v235/singh24a.html)

**TLDR**: Introduces an imprecise learning framework for domain generalization that defers between average-case and worst-case risk based on data evidence.

## Abstract

Out-of-distribution (OOD) generalisation is challenging because it involves not only learning from empirical data, but also deciding among various notions of generalisation, e.g. optimise based on the average-case risk, worst-case risk, or interpolations thereof. While this decision should in principle be decided by the model operator like medical doctors in practice, this information might not always be available at training time. This situation leads to arbitrary commitments to specific generalisation strategies by machine learners due to these deployment uncertainties. We introduce the Imprecise Domain Generalisation framework to mitigate this, featuring an imprecise risk optimisation that allows learners to stay imprecise by optimising against a continuous spectrum of generalisation strategies during training, and a model framework that allows operators to specify their generalisation preference at deployment. Our work, supported by theoretical and empirical evidence, showcases the benefits of integrating imprecision into domain generalisation.