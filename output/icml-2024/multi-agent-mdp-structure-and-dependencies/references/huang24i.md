---
title: "Model-Based RL for Mean-Field Games is not Statistically Harder than Single-Agent RL"
source: "https://proceedings.mlr.press/v235/huang24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24i/huang24i.pdf"
categories: ['multi-agent-mdp-structure-and-dependencies', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['mean-field-games', 'reinforcement-learning', 'sample-complexity']
venue: "ICML 2024"
tldr: "Shows that model-based RL for mean-field games has sample complexity comparable to single-agent RL via a novel eluder dimension notion."
---

# Model-Based RL for Mean-Field Games is not Statistically Harder than Single-Agent RL

**Source**: [https://proceedings.mlr.press/v235/huang24i.html](https://proceedings.mlr.press/v235/huang24i.html)

**TLDR**: Shows that model-based RL for mean-field games has sample complexity comparable to single-agent RL via a novel eluder dimension notion.

## Abstract

We study the sample complexity of reinforcement learning (RL) in Mean-Field Games (MFGs) with model-based function approximation that requires strategic exploration to find a Nash Equilibrium policy. We introduce the Partial Model-Based Eluder Dimension (P-MBED), a more effective notion to characterize the model class complexity. Notably, P-MBED measures the complexity of the single-agent model class converted from the given mean-field model class, and potentially, can be exponentially lower than the MBED proposed by Huang et al. (2024). We contribute a model elimination algorithm featuring a novel exploration strategy and establish sample complexity results polynomial w.r.t. P-MBED. Crucially, our results reveal that, under the basic realizability and Lipschitz continuity assumptions, learning Nash Equilibrium in MFGs is no more statistically challenging than solving a logarithmic number of single-agent RL problems. We further extend our results to Multi-Type MFGs, generalizing from conventional MFGs and involving multiple types of agents. This extension implies statistical tractability of a broader class of Markov Games through the efficacy of mean-field approximation. Finally, inspired by our theoretical algorithm, we present a heuristic approach with improved computational efficiency and empirically demonstrate its effectiveness.