---
title: "Tackling Non-Stationarity in Reinforcement Learning via Causal-Origin Representation"
source: "https://proceedings.mlr.press/v235/zhang24ah.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24ah/zhang24ah.pdf"
categories: ['causal-inference-and-discovery-methods', 'online-learning-and-sequential-decision-making']
tags: ['non-stationarity', 'causal-representation', 'reinforcement-learning']
venue: "ICML 2024"
tldr: "Addresses non-stationarity in RL by learning causal-origin representations that disentangle causal factors driving environment changes."
---

# Tackling Non-Stationarity in Reinforcement Learning via Causal-Origin Representation

**Source**: [https://proceedings.mlr.press/v235/zhang24ah.html](https://proceedings.mlr.press/v235/zhang24ah.html)

**TLDR**: Addresses non-stationarity in RL by learning causal-origin representations that disentangle causal factors driving environment changes.

## Abstract

In real-world scenarios, the application of reinforcement learning is significantly challenged by complex non-stationarity. Most existing methods attempt to model changes in the environment explicitly, often requiring impractical prior knowledge of environments. In this paper, we propose a new perspective, positing that non-stationarity can propagate and accumulate through complex causal relationships during state transitions, thereby compounding its sophistication and affecting policy learning. We believe that this challenge can be more effectively addressed by implicitly tracing the causal origin of non-stationarity. To this end, we introduce the Causal-Origin REPresentation (COREP) algorithm. COREP primarily employs a guided updating mechanism to learn a stable graph representation for the state, termed as causal-origin representation. By leveraging this representation, the learned policy exhibits impressive resilience to non-stationarity. We supplement our approach with a theoretical analysis grounded in the causal interpretation for non-stationary reinforcement learning, advocating for the validity of the causal-origin representation. Experimental results further demonstrate the superior performance of COREP over existing methods in tackling non-stationarity problems. The code is available at https://github.com/PKU-RL/COREP.