---
title: "Higher-Order Causal Message Passing for Experimentation with Complex Interference"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/94f008bcc2a5eb785fb8e0ad7aedd4fc-Abstract-Conference.html"
categories: ['causal-discovery-and-inference-methods', 'neural-geometric-shape-representation-learning']
tags: ['causal-inference', 'interference', 'higher-order-message-passing']
venue: "NeurIPS 2024"
tldr: "Higher-order causal message passing is introduced to estimate treatment effects under complex network interference in experiments."
---

# Higher-Order Causal Message Passing for Experimentation with Complex Interference

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/94f008bcc2a5eb785fb8e0ad7aedd4fc-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/94f008bcc2a5eb785fb8e0ad7aedd4fc-Abstract-Conference.html)

**TLDR**: Higher-order causal message passing is introduced to estimate treatment effects under complex network interference in experiments.

## Abstract

Accurate estimation of treatment effects is essential for decision-making across various scientific fields. This task, however, becomes challenging in areas like social sciences and online marketplaces, where treating one experimental unit can influence outcomes for others through direct or indirect interactions. Such interference can lead to biased treatment effect estimates, particularly when the structure of these interactions is unknown. We address this challenge by introducing a new class of estimators based on causal message-passing, specifically designed for settings with pervasive, unknown interference. Our estimator draws on information from the sample mean and variance of unit outcomes and treatments over time, enabling efficient use of observed data to estimate the evolution of the system state. Concretely, we construct non-linear features from the moments of unit outcomes and treatments and then learn a function that maps these features to future mean and variance of unit outcomes. This allows for the estimation of the treatment effect over time. Extensive simulations across multiple domains, using synthetic and real network data, demonstrate the efficacy of our approach in estimating total treatment effect dynamics, even in cases where interference exhibits non-monotonic behavior in the probability of treatment.