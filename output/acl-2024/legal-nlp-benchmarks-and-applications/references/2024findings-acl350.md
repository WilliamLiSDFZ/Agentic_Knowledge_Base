---
title: "LJPCheck: Functional Tests for Legal Judgment Prediction"
source: "https://aclanthology.org/2024.findings-acl.350/"
categories: ['legal-nlp-benchmarks-and-applications', 'nlp-benchmark-design-and-interpretability']
tags: ['legal-judgment-prediction', 'functional-testing', 'behavioral-evaluation']
venue: "ACL 2024"
tldr: "Introduces LJPCheck, a functional test suite to evaluate robustness and reliability of legal judgment prediction models."
---

# LJPCheck: Functional Tests for Legal Judgment Prediction

**Source**: [https://aclanthology.org/2024.findings-acl.350/](https://aclanthology.org/2024.findings-acl.350/)

**TLDR**: Introduces LJPCheck, a functional test suite to evaluate robustness and reliability of legal judgment prediction models.

## Abstract

AbstractLegal Judgment Prediction (LJP) refers to the task of automatically predicting judgment results (e.g., charges, law articles and term of penalty) given the fact description of cases. While SOTA models have achieved high accuracy and F1 scores on public datasets, existing datasets fail to evaluate specific aspects of these models (e.g., legal fairness, which significantly impact their applications in real scenarios). Inspired by functional testing in software engineering, we introduce LJPCHECK, a suite of functional tests for LJP models, to comprehend LJP models’ behaviors and offer diagnostic insights. We illustrate the utility of LJPCHECK on five SOTA LJP models. Extensive experiments reveal vulnerabilities in these models, prompting an in-depth discussion into the underlying reasons of their shortcomings.