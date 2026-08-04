---
title: "Debiased Distribution Compression"
source: "https://proceedings.mlr.press/v235/li24r.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24r/li24r.pdf"
categories: ['sampling-compression-and-dimensionality-reduction', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['distribution-compression', 'debiasing', 'Markov-chain', 'coresets', 'kernel-methods']
venue: "ICML 2024"
tldr: "Introduces debiased distribution compression methods that summarize distributions from biased input sequences such as slowly mixing Markov chains."
---

# Debiased Distribution Compression

**Source**: [https://proceedings.mlr.press/v235/li24r.html](https://proceedings.mlr.press/v235/li24r.html)

**TLDR**: Introduces debiased distribution compression methods that summarize distributions from biased input sequences such as slowly mixing Markov chains.

## Abstract

Modern compression methods can summarize a target distribution $\mathbb{P}$ more succinctly than i.i.d. sampling but require access to a low-bias input sequence like a Markov chain converging quickly to $\mathbb{P}$. We introduce a new suite of compression methods suitable for compression with biased input sequences. Given $n$ points targeting the wrong distribution and quadratic time, Stein kernel thinning (SKT) returns $\sqrt{n}$ equal-weighted points with $\widetilde{O}(n^{-1/2})$ maximum mean discrepancy (MMD) to $\mathbb{P}$. For larger-scale compression tasks, low-rank SKT achieves the same feat in sub-quadratic time using an adaptive low-rank debiasing procedure that may be of independent interest. For downstream tasks that support simplex or constant-preserving weights, Stein recombination and Stein Cholesky achieve even greater parsimony, matching the guarantees of SKT with as few as $\text{poly-log}(n)$ weighted points. Underlying these advances are new guarantees for the quality of simplex-weighted coresets, the spectral decay of kernel matrices, and the covering numbers of Stein kernel Hilbert spaces. In our experiments, our techniques provide succinct and accurate posterior summaries while overcoming biases due to burn-in, approximate Markov chain Monte Carlo, and tempering.