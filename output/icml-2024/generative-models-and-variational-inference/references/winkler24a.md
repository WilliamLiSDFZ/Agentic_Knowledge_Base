---
title: "Bridging discrete and continuous state spaces: Exploring the Ehrenfest process in time-continuous diffusion models"
source: "https://proceedings.mlr.press/v235/winkler24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/winkler24a/winkler24a.pdf"
categories: ['generative-models-and-variational-inference', 'sampling-and-optimization-on-manifolds']
tags: ['diffusion-models', 'discrete-state-spaces', 'Ehrenfest-process', 'Markov-jump-processes']
venue: "ICML 2024"
tldr: "Studies time-continuous Markov jump processes on discrete state spaces via the Ehrenfest process as a bridge between discrete and continuous diffusion models."
---

# Bridging discrete and continuous state spaces: Exploring the Ehrenfest process in time-continuous diffusion models

**Source**: [https://proceedings.mlr.press/v235/winkler24a.html](https://proceedings.mlr.press/v235/winkler24a.html)

**TLDR**: Studies time-continuous Markov jump processes on discrete state spaces via the Ehrenfest process as a bridge between discrete and continuous diffusion models.

## Abstract

Generative modeling via stochastic processes has led to remarkable empirical results as well as to recent advances in their theoretical understanding. In principle, both space and time of the processes can be discrete or continuous. In this work, we study time-continuous Markov jump processes on discrete state spaces and investigate their correspondence to state-continuous diffusion processes given by SDEs. In particular, we revisit the $\textit{Ehrenfest process}$, which converges to an Ornstein-Uhlenbeck process in the infinite state space limit. Likewise, we can show that the time-reversal of the Ehrenfest process converges to the time-reversed Ornstein-Uhlenbeck process. This observation bridges discrete and continuous state spaces and allows to carry over methods from one to the respective other setting, such as for instance loss functions that lead to improved convergence. Additionally, we suggest an algorithm for training the time-reversal of Markov jump processes which relies on conditional expectations and can thus be directly related to denoising score matching. We demonstrate our methods in multiple convincing numerical experiments.