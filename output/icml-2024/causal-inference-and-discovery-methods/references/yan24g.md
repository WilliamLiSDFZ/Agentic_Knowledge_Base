---
title: "Foundations of Testing for Finite-Sample Causal Discovery"
source: "https://proceedings.mlr.press/v235/yan24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yan24g/yan24g.pdf"
categories: ['causal-inference-and-discovery-methods', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['causal-discovery', 'finite-sample-testing', 'hypothesis-testing']
venue: "ICML 2024"
tldr: "Develops rigorous finite-sample statistical testing foundations for causal discovery under soft interventions without relying on infinite-sample assumptions."
---

# Foundations of Testing for Finite-Sample Causal Discovery

**Source**: [https://proceedings.mlr.press/v235/yan24g.html](https://proceedings.mlr.press/v235/yan24g.html)

**TLDR**: Develops rigorous finite-sample statistical testing foundations for causal discovery under soft interventions without relying on infinite-sample assumptions.

## Abstract

Discovery of causal relationships is a fundamental goal of science and vital for sound decision making. As such, there has been considerable interest in causal discovery methods with provable guarantees. Existing works have thus far largely focused on discovery under hard intervention and infinite-samples, in which intervening on a node readily reveals the orientation of every edge incident to the node. This setup however overlooks the stochasticity inherent in real-world, finite-sample settings. Our work takes a step towards studying finite-sample causal discovery, wherein multiple interventions on a node are now needed for edge orientation. In this work, we study the canonical setup in theoretical causal discovery literature, where one assumes causal sufficiency and access to the graph skeleton. Our key observation is that discovery may be viewed as structured, multiple testing, and we develop a novel testing framework to this end. Crucially, our framework allows for anytime valid testing as multiple tests are needed to conclude an edge orientation. It also allows for flexible combination of structured test-statistics (enabling one to use Meek rules to propagate edge orientation) as well as robust testing. Through empirical simulations, we confirm the usefulness of our framework. In closing, using this testing framework, we show how one may efficiently verify graph structure by drawing a connection to multi-constraint bandits and designing a novel algorithm to this end.