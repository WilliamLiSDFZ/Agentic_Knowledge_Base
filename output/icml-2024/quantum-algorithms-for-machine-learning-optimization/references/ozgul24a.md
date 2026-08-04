---
title: "Stochastic Quantum Sampling for Non-Logconcave Distributions and Estimating Partition Functions"
source: "https://proceedings.mlr.press/v235/ozgul24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ozgul24a/ozgul24a.pdf"
categories: ['quantum-algorithms-for-machine-learning-optimization']
tags: ['quantum-sampling', 'non-logconcave-distributions', 'partition-functions', 'stochastic-gradient']
venue: "ICML 2024"
tldr: "Develops quantum algorithms for sampling from non-logconcave distributions and estimating partition functions with stochastic gradient oracles."
---

# Stochastic Quantum Sampling for Non-Logconcave Distributions and Estimating Partition Functions

**Source**: [https://proceedings.mlr.press/v235/ozgul24a.html](https://proceedings.mlr.press/v235/ozgul24a.html)

**TLDR**: Develops quantum algorithms for sampling from non-logconcave distributions and estimating partition functions with stochastic gradient oracles.

## Abstract

We present quantum algorithms for sampling from possibly non-logconcave probability distributions expressed as $\pi(x) \propto \exp(-\beta f(x))$ as well as quantum algorithms for estimating the partition function for such distributions. We also incorporate a stochastic gradient oracle that implements the quantum walk operators inexactly by only using mini-batch gradients when $f$ can be written as a finite sum. One challenge of quantizing the resulting Markov chains is that they do not satisfy the detailed balance condition in general. Consequently, the mixing time of the algorithm cannot be expressed in terms of the spectral gap of the transition density matrix, making the quantum algorithms nontrivial to analyze. We overcame these challenges by first building a reference reversible Markov chain that converges to the target distribution, then controlling the discrepancy between our algorithm’s output and the target distribution by using the reference Markov chain as a bridge to establish the total complexity. Our quantum algorithms exhibit polynomial speedups in terms of dimension or precision dependencies when compared to best-known classical algorithms under similar assumptions.