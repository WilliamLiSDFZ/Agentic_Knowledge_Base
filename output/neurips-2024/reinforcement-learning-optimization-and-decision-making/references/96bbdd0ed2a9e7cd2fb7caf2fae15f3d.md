---
title: "RL in Latent MDPs is Tractable: Online Guarantees via Off-Policy Evaluation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/96bbdd0ed2a9e7cd2fb7caf2fae15f3d-Abstract-Conference.html"
categories: ['reinforcement-learning-optimization-and-decision-making', 'online-learning-augmented-algorithms-and-optimization']
tags: ['latent-MDPs', 'reinforcement-learning', 'off-policy-evaluation', 'online-learning', 'partial-observability']
venue: "NeurIPS 2024"
tldr: "Proves that RL in Latent MDPs is tractable by deriving online learning guarantees via off-policy evaluation techniques."
---

# RL in Latent MDPs is Tractable: Online Guarantees via Off-Policy Evaluation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/96bbdd0ed2a9e7cd2fb7caf2fae15f3d-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/96bbdd0ed2a9e7cd2fb7caf2fae15f3d-Abstract-Conference.html)

**TLDR**: Proves that RL in Latent MDPs is tractable by deriving online learning guarantees via off-policy evaluation techniques.

## Abstract

In many real-world decision problems there is partially observed, hidden or latent information that remains fixed throughout an interaction. Such decision problems can be modeled as Latent Markov Decision Processes (LMDPs), where a latent variable is selected at the beginning of an interaction and is not disclosed to the agent initially. In last decade, there has been significant progress in designing learning algorithms for solving LMDPs under different structural assumptions. However, for general LMDPs, there is no known learning algorithm that provably matches the existing lower bound. We effectively resolve this open question, introducing the first sample-efficient algorithm for LMDPs without any additional structural assumptions. Our result builds off a new perspective on the role off-policy evaluation guarantees and coverage coefficient in LMDPs, a perspective, which has been overlooked in the context of exploration in partially observed environments. Specifically, we establish a novel off-policy evaluation lemma and introduce a new coverage coefficient for LMDPs. Then, we show how these can be used to derive near-optimal guarantees of an optimistic exploration algorithm. These results, we believe, can be valuable for a wide range of interactive learning problems beyond the LMDP class, and especially, for partially observed environments.