---
title: "Information-Directed Pessimism for Offline Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/koppel24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/koppel24a/koppel24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'anomaly-and-out-of-distribution-detection']
tags: ['offline-reinforcement-learning', 'pessimism', 'information-directed', 'distribution-mismatch', 'batch-RL']
venue: "ICML 2024"
tldr: "An information-directed pessimism framework for offline RL that addresses distribution mismatch between training data and current policy trajectories."
---

# Information-Directed Pessimism for Offline Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/koppel24a.html](https://proceedings.mlr.press/v235/koppel24a.html)

**TLDR**: An information-directed pessimism framework for offline RL that addresses distribution mismatch between training data and current policy trajectories.

## Abstract

Policy optimization from batch data, i.e., offline reinforcement learning (RL) is important when collecting data from a current policy is not possible. This setting incurs distribution mismatch between batch training data and trajectories from the current policy. Pessimistic offsets estimate mismatch using concentration bounds, which possess strong theoretical guarantees and simplicity of implementation. Mismatch may be conservative in sparse data regions and less so otherwise, which can result in under-performing their no-penalty variants in practice. We derive a new pessimistic penalty as the distance between the data and the true distribution using an evaluable one-sample test known as Stein Discrepancy that requires minimal smoothness conditions, and noticeably, allows a mixture family representation of distribution over next states. This entity forms a quantifier of information in offline data, which justifies calling this approach information-directed pessimism (IDP) for offline RL. We further establish that this new penalty based on discrete Stein discrepancy yields practical gains in performance while generalizing the regret of prior art to multimodal distributions.