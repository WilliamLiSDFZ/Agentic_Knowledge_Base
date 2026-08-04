---
title: "A Sober Look at LLMs for Material Discovery: Are They Actually Good for Bayesian Optimization Over Molecules?"
source: "https://proceedings.mlr.press/v235/kristiadi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kristiadi24a/kristiadi24a.pdf"
categories: ['bayesian-optimization-and-surrogate-methods', 'generative-models-for-molecular-protein-design']
tags: ['bayesian-optimization', 'material-discovery', 'LLM-priors', 'molecular-space']
venue: "ICML 2024"
tldr: "A critical evaluation of LLMs as prior knowledge sources for Bayesian optimization in molecular material discovery workflows."
---

# A Sober Look at LLMs for Material Discovery: Are They Actually Good for Bayesian Optimization Over Molecules?

**Source**: [https://proceedings.mlr.press/v235/kristiadi24a.html](https://proceedings.mlr.press/v235/kristiadi24a.html)

**TLDR**: A critical evaluation of LLMs as prior knowledge sources for Bayesian optimization in molecular material discovery workflows.

## Abstract

Automation is one of the cornerstones of contemporary material discovery. Bayesian optimization (BO) is an essential part of such workflows, enabling scientists to leverage prior domain knowledge into efficient exploration of a large molecular space. While such prior knowledge can take many forms, there has been significant fanfare around the ancillary scientific knowledge encapsulated in large language models (LLMs). However, existing work thus far has only explored LLMs for heuristic materials searches. Indeed, recent work obtains the uncertainty estimate—an integral part of BO—from point-estimated, non-Bayesian LLMs. In this work, we study the question of whether LLMs are actually useful to accelerate principled Bayesian optimization in the molecular space. We take a sober, dispassionate stance in answering this question. This is done by carefully (i) viewing LLMs as fixed feature extractors for standard but principled BO surrogate models and by (ii) leveraging parameter-efficient finetuning methods and Bayesian neural networks to obtain the posterior of the LLM surrogate. Our extensive experiments with real-world chemistry problems show that LLMs can be useful for BO over molecules, but only if they have been pretrained or finetuned with domain-specific data.