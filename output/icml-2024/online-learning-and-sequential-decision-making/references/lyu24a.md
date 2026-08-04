---
title: "Cross-Domain Policy Adaptation by Capturing Representation Mismatch"
source: "https://proceedings.mlr.press/v235/lyu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lyu24a/lyu24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'test-time-adaptation-methods-and-evaluation']
tags: ['domain-adaptation', 'reinforcement-learning', 'dynamics-mismatch', 'representation-learning']
venue: "ICML 2024"
tldr: "A cross-domain policy adaptation method captures representation mismatch between source and target domains to enable effective policy transfer."
---

# Cross-Domain Policy Adaptation by Capturing Representation Mismatch

**Source**: [https://proceedings.mlr.press/v235/lyu24a.html](https://proceedings.mlr.press/v235/lyu24a.html)

**TLDR**: A cross-domain policy adaptation method captures representation mismatch between source and target domains to enable effective policy transfer.

## Abstract

It is vital to learn effective policies that can be transferred to different domains with dynamics discrepancies in reinforcement learning (RL). In this paper, we consider dynamics adaptation settings where there exists dynamics mismatch between the source domain and the target domain, and one can get access to sufficient source domain data, while can only have limited interactions with the target domain. Existing methods address this problem by learning domain classifiers, performing data filtering from a value discrepancy perspective, etc. Instead, we tackle this challenge from a decoupled representation learning perspective. We perform representation learning only in the target domain and measure the representation deviations on the transitions from the source domain, which we show can be a signal of dynamics mismatch. We also show that representation deviation upper bounds performance difference of a given policy in the source domain and target domain, which motivates us to adopt representation deviation as a reward penalty. The produced representations are not involved in either policy or value function, but only serve as a reward penalizer. We conduct extensive experiments on environments with kinematic and morphology mismatch, and the results show that our method exhibits strong performance on many tasks. Our code is publicly available at https://github.com/dmksjfl/PAR.