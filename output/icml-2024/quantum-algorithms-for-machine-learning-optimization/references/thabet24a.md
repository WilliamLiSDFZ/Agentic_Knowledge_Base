---
title: "Quantum Positional Encodings for Graph Neural Networks"
source: "https://proceedings.mlr.press/v235/thabet24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/thabet24a/thabet24a.pdf"
categories: ['quantum-algorithms-for-machine-learning-optimization', 'graph-neural-networks-and-topology']
tags: ['positional-encodings', 'quantum-computing', 'graph-neural-networks']
venue: "ICML 2024"
tldr: "Novel quantum-computed positional encodings for GNNs are proposed that leverage long-range quantum correlations to capture graph topology more expressively."
---

# Quantum Positional Encodings for Graph Neural Networks

**Source**: [https://proceedings.mlr.press/v235/thabet24a.html](https://proceedings.mlr.press/v235/thabet24a.html)

**TLDR**: Novel quantum-computed positional encodings for GNNs are proposed that leverage long-range quantum correlations to capture graph topology more expressively.

## Abstract

In this work, we propose novel families of positional encodings tailored to graph neural networks obtained with quantum computers. These encodings leverage the long-range correlations inherent in quantum systems that arise from mapping the topology of a graph onto interactions between qubits in a quantum computer. Our inspiration stems from the recent advancements in quantum processing units, which offer computational capabilities beyond the reach of classical hardware. We prove that some of these quantum features are theoretically more expressive for certain graphs than the commonly used relative random walk probabilities. Empirically, we show that the performance of state-of-the-art models can be improved on standard benchmarks and large-scale datasets by computing tractable versions of quantum features. Our findings highlight the potential of leveraging quantum computing capabilities to enhance the performance of transformers in handling graph data.