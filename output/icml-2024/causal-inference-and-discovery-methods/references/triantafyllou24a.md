---
title: "Agent-Specific Effects: A Causal Effect Propagation Analysis in Multi-Agent MDPs"
source: "https://proceedings.mlr.press/v235/triantafyllou24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/triantafyllou24a/triantafyllou24a.pdf"
categories: ['multi-agent-mdp-structure-and-dependencies', 'causal-inference-and-discovery-methods']
tags: ['multi-agent-MDPs', 'causal-attribution', 'agent-accountability']
venue: "ICML 2024"
tldr: "Analyzes causal effect propagation to quantify individual agent contributions to outcomes in multi-agent Markov decision processes."
---

# Agent-Specific Effects: A Causal Effect Propagation Analysis in Multi-Agent MDPs

**Source**: [https://proceedings.mlr.press/v235/triantafyllou24a.html](https://proceedings.mlr.press/v235/triantafyllou24a.html)

**TLDR**: Analyzes causal effect propagation to quantify individual agent contributions to outcomes in multi-agent Markov decision processes.

## Abstract

Establishing causal relationships between actions and outcomes is fundamental for accountable multi-agent decision-making. However, interpreting and quantifying agents’ contributions to such relationships pose significant challenges. These challenges are particularly prominent in the context of multi-agent sequential decision-making, where the causal effect of an agent’s action on the outcome depends on how other agents respond to that action. In this paper, our objective is to present a systematic approach for attributing the causal effects of agents’ actions to the influence they exert on other agents. Focusing on multi-agent Markov decision processes, we introduce agent-specific effects (ASE), a novel causal quantity that measures the effect of an agent’s action on the outcome that propagates through other agents. We then turn to the counterfactual counterpart of ASE (cf-ASE), provide a sufficient set of conditions for identifying cf-ASE, and propose a practical sampling-based algorithm for estimating it. Finally, we experimentally evaluate the utility of cf-ASE through a simulation-based testbed, which includes a sepsis management environment.