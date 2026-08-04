---
title: "S$Ω$I: Score-based O-INFORMATION Estimation"
source: "https://proceedings.mlr.press/v235/bounoua24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bounoua24a/bounoua24a.pdf"
categories: ['information-retrieval-and-recommendation-systems', 'sufficient-dimension-reduction-correlation-methods']
tags: ['score-based-estimation', 'O-information', 'multivariate-information', 'higher-order-dependencies']
venue: "ICML 2024"
tldr: "This paper introduces a score-based method for estimating O-information to capture higher-order statistical dependencies among multiple random variables."
---

# S$Ω$I: Score-based O-INFORMATION Estimation

**Source**: [https://proceedings.mlr.press/v235/bounoua24a.html](https://proceedings.mlr.press/v235/bounoua24a.html)

**TLDR**: This paper introduces a score-based method for estimating O-information to capture higher-order statistical dependencies among multiple random variables.

## Abstract

The analysis of scientific data and complex multivariate systems requires information quantities that capture relationships among multiple random variables. Recently, new information-theoretic measures have been developed to overcome the shortcomings of classical ones, such as mutual information, that are restricted to considering pairwise interactions. Among them, the concept of information synergy and redundancy is crucial for understanding the high-order dependencies between variables. One of the most prominent and versatile measures based on this concept is O-information, which provides a clear and scalable way to quantify the synergy-redundancy balance in multivariate systems. However, its practical application is limited to simplified cases. In this work, we introduce S$\Omega$I, which allows to compute O-information without restrictive assumptions about the system while leveraging a unique model. Our experiments validate our approach on synthetic data, and demonstrate the effectiveness of S$\Omega$I in the context of a real-world use case.