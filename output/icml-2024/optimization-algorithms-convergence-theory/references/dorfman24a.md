---
title: "Dynamic Byzantine-Robust Learning: Adapting to Switching Byzantine Workers"
source: "https://proceedings.mlr.press/v235/dorfman24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dorfman24a/dorfman24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'optimization-algorithms-convergence-theory']
tags: ['byzantine-robustness', 'distributed-learning', 'fault-tolerance', 'dynamic-adversaries']
venue: "ICML 2024"
tldr: "A Byzantine-robust distributed learning framework that adapts to dynamically switching Byzantine workers during training."
---

# Dynamic Byzantine-Robust Learning: Adapting to Switching Byzantine Workers

**Source**: [https://proceedings.mlr.press/v235/dorfman24a.html](https://proceedings.mlr.press/v235/dorfman24a.html)

**TLDR**: A Byzantine-robust distributed learning framework that adapts to dynamically switching Byzantine workers during training.

## Abstract

Byzantine-robust learning has emerged as a prominent fault-tolerant distributed machine learning framework. However, most techniques focus on the static setting, wherein the identity of Byzantine workers remains unchanged throughout the learning process. This assumption fails to capture real-world dynamic Byzantine behaviors, which may include intermittent malfunctions or targeted, time-limited attacks. Addressing this limitation, we propose DynaBRO – a new method capable of withstanding any sub-linear number of identity changes across rounds. Specifically, when the number of such changes is $\mathcal{O}(\sqrt{T})$ (where $T$ is the total number of training rounds), DynaBRO nearly matches the state-of-the-art asymptotic convergence rate of the static setting. Our method utilizes a multi-level Monte Carlo (MLMC) gradient estimation technique applied at the server to robustly aggregated worker updates. By additionally leveraging an adaptive learning rate, we circumvent the need for prior knowledge of the fraction of Byzantine workers.