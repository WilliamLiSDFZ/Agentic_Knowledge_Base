---
title: "Fair Off-Policy Learning from Observational Data"
source: "https://proceedings.mlr.press/v235/frauen24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/frauen24a/frauen24a.pdf"
categories: ['fairness-aware-algorithmic-decision-making', 'causal-inference-and-discovery-methods']
tags: ['fairness', 'off-policy-learning', 'observational-data']
venue: "ICML 2024"
tldr: "A framework for fair off-policy learning from observational data ensures fairness constraints in learned decision policies."
---

# Fair Off-Policy Learning from Observational Data

**Source**: [https://proceedings.mlr.press/v235/frauen24a.html](https://proceedings.mlr.press/v235/frauen24a.html)

**TLDR**: A framework for fair off-policy learning from observational data ensures fairness constraints in learned decision policies.

## Abstract

Algorithmic decision-making in practice must be fair for legal, ethical, and societal reasons. To achieve this, prior research has contributed various approaches that ensure fairness in machine learning predictions, while comparatively little effort has focused on fairness in decision-making, specifically off-policy learning. In this paper, we propose a novel framework for fair off-policy learning: we learn decision rules from observational data under different notions of fairness, where we explicitly assume that observational data were collected under a different – potentially discriminatory – behavioral policy. Importantly, our framework applies to different fairness notions for off-policy learning, where fairness is formalized based on actions or policy values. As our main contribution, we propose a neural network-based framework to learn optimal policies under different fairness notions. We further provide theoretical guarantees in the form of generalization bounds for the finite-sample version of our framework. We demonstrate the effectiveness of our framework through extensive numerical experiments using both simulated and real-world data. Altogether, our work enables algorithmic decision-making in a wide array of practical applications where fairness must be ensured.