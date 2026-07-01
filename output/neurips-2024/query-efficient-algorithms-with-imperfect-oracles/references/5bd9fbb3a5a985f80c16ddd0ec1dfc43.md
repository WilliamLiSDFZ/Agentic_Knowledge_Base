---
title: "Fast Proxy Experiment Design for Causal Effect Identification"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/5bd9fbb3a5a985f80c16ddd0ec1dfc43-Abstract-Conference.html"
categories: ['causal-discovery-and-inference-methods', 'query-efficient-algorithms-with-imperfect-oracles']
tags: ['causal-effect-identification', 'proxy-experiments', 'experimental-design']
venue: "NeurIPS 2024"
tldr: "Proposes fast proxy experiment design methods to efficiently identify causal effects when observational studies suffer from unmeasured confounding."
---

# Fast Proxy Experiment Design for Causal Effect Identification

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/5bd9fbb3a5a985f80c16ddd0ec1dfc43-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/5bd9fbb3a5a985f80c16ddd0ec1dfc43-Abstract-Conference.html)

**TLDR**: Proposes fast proxy experiment design methods to efficiently identify causal effects when observational studies suffer from unmeasured confounding.

## Abstract

Identifying causal effects is a key problem of interest across many disciplines. The two long-standing approaches to estimate causal effects are observational and experimental (randomized) studies. Observational studies can suffer from unmeasured confounding, which may render the causal effects unidentifiable. On the other hand, direct experiments on the target variable may be too costly or even infeasible to conduct. A middle ground between these two approaches is to estimate the causal effect of interest through proxy experiments, which are  conducted on variables with a lower cost to intervene on compared to the main target. In an earlier work, we studied this setting and demonstrated that the problem of designing the optimal (minimum-cost) experiment for  causal effect identification is NP-complete and provided a naive algorithm that may require solving exponentially many NP-hard problems as a sub-routine in the worst case. In this work, we provide a few reformulations of the problem that allow for designing significantly more efficient algorithms to solve it as witnessed by our extensive simulations. Additionally, we study the closely-related problem of designing experiments that enable us to identify a given effect through valid adjustments sets.