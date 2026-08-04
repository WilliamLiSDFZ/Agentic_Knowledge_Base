---
title: "Temporal Spiking Neural Networks with Synaptic Delay for Graph Reasoning"
source: "https://proceedings.mlr.press/v235/xiao24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xiao24f/xiao24f.pdf"
categories: ['neuromorphic-computing-and-neural-dynamics-modeling', 'graph-neural-networks-and-topology']
tags: ['spiking-neural-networks', 'synaptic-delay', 'graph-reasoning']
venue: "ICML 2024"
tldr: "Proposes temporal spiking neural networks with synaptic delays for energy-efficient graph reasoning tasks."
---

# Temporal Spiking Neural Networks with Synaptic Delay for Graph Reasoning

**Source**: [https://proceedings.mlr.press/v235/xiao24f.html](https://proceedings.mlr.press/v235/xiao24f.html)

**TLDR**: Proposes temporal spiking neural networks with synaptic delays for energy-efficient graph reasoning tasks.

## Abstract

Spiking neural networks (SNNs) are investigated as biologically inspired models of neural computation, distinguished by their computational capability and energy efficiency due to precise spiking times and sparse spikes with event-driven computation. A significant question is how SNNs can emulate human-like graph-based reasoning of concepts and relations, especially leveraging the temporal domain optimally. This paper reveals that SNNs, when amalgamated with synaptic delay and temporal coding, are proficient in executing (knowledge) graph reasoning. It is elucidated that spiking time can function as an additional dimension to encode relation properties via a neural-generalized path formulation. Empirical results highlight the efficacy of temporal delay in relation processing and showcase exemplary performance in diverse graph reasoning tasks. The spiking model is theoretically estimated to achieve $20\times$ energy savings compared to non-spiking counterparts, deepening insights into the capabilities and potential of biologically inspired SNNs for efficient reasoning. The code is available at https://github.com/pkuxmq/GRSNN.