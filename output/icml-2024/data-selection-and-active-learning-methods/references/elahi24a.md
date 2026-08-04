---
title: "Adaptive Online Experimental Design for Causal Discovery"
source: "https://proceedings.mlr.press/v235/elahi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/elahi24a/elahi24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'data-selection-and-active-learning-methods']
tags: ['causal-discovery', 'active-learning', 'interventional-data', 'experimental-design', 'sample-efficiency']
venue: "ICML 2024"
tldr: "Proposes an adaptive online experimental design framework for efficient causal discovery under limited interventional data budgets."
---

# Adaptive Online Experimental Design for Causal Discovery

**Source**: [https://proceedings.mlr.press/v235/elahi24a.html](https://proceedings.mlr.press/v235/elahi24a.html)

**TLDR**: Proposes an adaptive online experimental design framework for efficient causal discovery under limited interventional data budgets.

## Abstract

Causal discovery aims to uncover cause-and-effect relationships encoded in causal graphs by leveraging observational, interventional data, or their combination. The majority of existing causal discovery methods are developed assuming infinite interventional data. We focus on interventional data efficiency and formalize causal discovery from the perspective of online learning, inspired by pure exploration in bandit problems. A graph separating system, consisting of interventions that cut every edge of the graph at least once, is sufficient for learning causal graphs when infinite interventional data is available, even in the worst case. We propose a track-and-stop causal discovery algorithm that adaptively selects interventions from the graph separating system via allocation matching and learns the causal graph based on sampling history. Given any desired confidence value, the algorithm determines a termination condition and runs until it is met. We analyze the algorithm to establish a problem-dependent upper bound on the expected number of required interventional samples. Our proposed algorithm outperforms existing methods in simulations across various randomly generated causal graphs. It achieves higher accuracy, measured by the structural hamming distance (SHD) between the learned causal graph and the ground truth, with significantly fewer samples.