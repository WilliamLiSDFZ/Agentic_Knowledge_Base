---
title: "Two-timescale Derivative Free Optimization for Performative Prediction with Markovian Data"
source: "https://proceedings.mlr.press/v235/liu24aj.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24aj/liu24aj.pdf"
categories: ['optimization-algorithms-convergence-theory', 'probabilistic-generating-circuits-research']
tags: ['performative-prediction', 'derivative-free-optimization', 'markovian-data']
venue: "ICML 2024"
tldr: "A two-timescale derivative-free optimization algorithm for performative prediction with state-dependent Markovian data distributions."
---

# Two-timescale Derivative Free Optimization for Performative Prediction with Markovian Data

**Source**: [https://proceedings.mlr.press/v235/liu24aj.html](https://proceedings.mlr.press/v235/liu24aj.html)

**TLDR**: A two-timescale derivative-free optimization algorithm for performative prediction with state-dependent Markovian data distributions.

## Abstract

This paper studies the performative prediction problem where a learner aims to minimize the expected loss with a decision-dependent data distribution. Such setting is motivated when outcomes can be affected by the prediction model, e.g., in strategic classification. We consider a state-dependent setting where the data distribution evolves according to an underlying controlled Markov chain. We focus on stochastic derivative free optimization (DFO) where the learner is given access to a loss function evaluation oracle with the above Markovian data. We propose a two-timescale DFO($\lambda$) algorithm that features (i) a sample accumulation mechanism that utilizes every observed sample to estimate the overall gradient of performative risk, and (ii) a two-timescale diminishing step size that balances the rates of DFO updates and bias reduction. Under a general non-convex optimization setting, we show that DFO($\lambda$) requires ${\cal O}( 1 /\epsilon^3)$ samples (up to a log factor) to attain a near-stationary solution with expected squared gradient norm less than $\epsilon > 0$. Numerical experiments verify our analysis.