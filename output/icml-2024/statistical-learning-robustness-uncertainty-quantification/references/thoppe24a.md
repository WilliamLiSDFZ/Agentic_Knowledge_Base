---
title: "Risk Estimation in a Markov Cost Process: Lower and Upper Bounds"
source: "https://proceedings.mlr.press/v235/thoppe24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/thoppe24a/thoppe24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'online-learning-and-sequential-decision-making']
tags: ['risk-estimation', 'Markov-cost-process', 'CVaR']
venue: "ICML 2024"
tldr: "Lower and upper bounds on the sample complexity of estimating variance, VaR, and CVaR for infinite-horizon discounted Markov cost processes are established."
---

# Risk Estimation in a Markov Cost Process: Lower and Upper Bounds

**Source**: [https://proceedings.mlr.press/v235/thoppe24a.html](https://proceedings.mlr.press/v235/thoppe24a.html)

**TLDR**: Lower and upper bounds on the sample complexity of estimating variance, VaR, and CVaR for infinite-horizon discounted Markov cost processes are established.

## Abstract

We tackle the problem of estimating risk measures of the infinite-horizon discounted cost of a Markov cost process. The risk measures we study include variance, Value-at-Risk (VaR), and Conditional Value-at-Risk (CVaR). First, we show that estimating any of these risk measures with $\epsilon$-accuracy, either in expected or high-probability sense, requires at least $\Omega(1/\epsilon^2)$ samples. Then, using a truncation scheme, we derive an upper bound for the CVaR and variance estimation. This bound matches our lower bound up to logarithmic factors. Finally, we discuss an extension of our estimation scheme that covers more general risk measures satisfying a certain continuity criterion, such as spectral risk measures and utility-based shortfall risk. To the best of our knowledge, our work is the first to provide lower and upper bounds for estimating any risk measure beyond the mean within a Markovian setting. Our lower bounds also extend to the infinite-horizon discounted costs’ mean. Even in that case, our lower bound of $\Omega(1/\epsilon^2) $ improves upon the existing $\Omega(1/\epsilon)$ bound (Metelli et al. 2023.