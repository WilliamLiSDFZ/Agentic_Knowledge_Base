---
title: "Inferring the Long-Term Causal Effects of Long-Term Treatments from Short-Term Experiments"
source: "https://proceedings.mlr.press/v235/tran24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tran24b/tran24b.pdf"
categories: ['causal-inference-and-discovery-methods', 'difference-in-differences-based-policy-evaluation']
tags: ['long-term-causal-effects', 'short-term-experiments', 'treatment-inference']
venue: "ICML 2024"
tldr: "Studies inference on long-term causal effects of continual interventions using only short-term experimental observations."
---

# Inferring the Long-Term Causal Effects of Long-Term Treatments from Short-Term Experiments

**Source**: [https://proceedings.mlr.press/v235/tran24b.html](https://proceedings.mlr.press/v235/tran24b.html)

**TLDR**: Studies inference on long-term causal effects of continual interventions using only short-term experimental observations.

## Abstract

We study inference on the long-term causal effect of a continual exposure to a novel intervention, which we term a long-term treatment, based on an experiment involving only short-term observations. Key examples include the long-term health effects of regularly-taken medicine or of environmental hazards and the long-term effects on users of changes to an online platform. This stands in contrast to short-term treatments or "shocks," whose long-term effect can reasonably be mediated by short-term observations, enabling the use of surrogate methods. Long-term treatments by definition have direct effects on long-term outcomes via continual exposure, so surrogacy conditions cannot reasonably hold. We connect the problem with offline reinforcement learning, leveraging doubly-robust estimators to estimate long-term causal effects for long-term treatments and construct confidence intervals.