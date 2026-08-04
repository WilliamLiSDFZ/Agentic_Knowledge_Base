---
title: "Promoting External and Internal Equities Under Ex-Ante/Ex-Post Metrics in Online Resource Allocation"
source: "https://proceedings.mlr.press/v235/sankararaman24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sankararaman24a/sankararaman24a.pdf"
categories: ['online-learning-matching-market-algorithms', 'fairness-aware-algorithmic-decision-making']
tags: ['online-resource-allocation', 'equity', 'fairness', 'ex-ante-ex-post', 'sequential-decision']
venue: "ICML 2024"
tldr: "Two models for equitable online resource allocation are proposed promoting internal and external equity under ex-ante and ex-post fairness metrics."
---

# Promoting External and Internal Equities Under Ex-Ante/Ex-Post Metrics in Online Resource Allocation

**Source**: [https://proceedings.mlr.press/v235/sankararaman24a.html](https://proceedings.mlr.press/v235/sankararaman24a.html)

**TLDR**: Two models for equitable online resource allocation are proposed promoting internal and external equity under ex-ante and ex-post fairness metrics.

## Abstract

This paper proposes two different models for equitable resource allocation in online settings. The first one is called external equity promotion, where sequentially arriving agents are heterogeneous in their external attributes, namely how many resources they demand, which are drawn from a probability distribution (accessible to the algorithm). The focus is then to devise an allocation policy such that every requester can get a fair share of resources proportional to their demands, regardless of their arrival time. The second is called internal equity promotion, where arriving requesters can be treated homogeneously in external attributes (demands) but are heterogeneous in internal traits such as demographics. In particular, each requester can be identified as belonging to one or several groups, and an allocation of resources is regarded as equitable when every group of requesters can receive a fair share of resources proportional to the percentage of that group in the whole population. For both models above, we consider as the benchmark a clairvoyant optimal solution that has the privilege to access all random demand realizations in advance. We consider two equity metrics, namely ex-post and ex-ante, and discuss the challenges under the two metrics in detail. Specifically, we present two linear program (LP)-based policies for external equity promotion under ex-ante with independent demands, each achieving an optimal CR of $1/2$ with respect to the benchmark LP. For internal equity promotion, we present optimal policies under both ex-ante and ex-post metrics.