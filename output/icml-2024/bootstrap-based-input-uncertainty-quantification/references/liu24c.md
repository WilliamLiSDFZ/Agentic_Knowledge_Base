---
title: "Orthogonal Bootstrap: Efficient Simulation of Input Uncertainty"
source: "https://proceedings.mlr.press/v235/liu24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24c/liu24c.pdf"
categories: ['bootstrap-based-input-uncertainty-quantification']
tags: ['bootstrap', 'input-uncertainty', 'monte-carlo']
venue: "ICML 2024"
tldr: "Orthogonal Bootstrap is proposed to reduce Monte Carlo replications needed for input uncertainty simulation by decomposing the estimation target."
---

# Orthogonal Bootstrap: Efficient Simulation of Input Uncertainty

**Source**: [https://proceedings.mlr.press/v235/liu24c.html](https://proceedings.mlr.press/v235/liu24c.html)

**TLDR**: Orthogonal Bootstrap is proposed to reduce Monte Carlo replications needed for input uncertainty simulation by decomposing the estimation target.

## Abstract

Bootstrap is a popular methodology for simulating input uncertainty. However, it can be computationally expensive when the number of samples is large. We propose a new approach called Orthogonal Bootstrap that reduces the number of required Monte Carlo replications. We decomposes the target being simulated into two parts: the non-orthogonal part which has a closed-form result known as Infinitesimal Jackknife and the orthogonal part which is easier to be simulated. We theoretically and numerically show that Orthogonal Bootstrap significantly reduces the computational cost of Bootstrap while improving empirical accuracy and maintaining the same width of the constructed interval.