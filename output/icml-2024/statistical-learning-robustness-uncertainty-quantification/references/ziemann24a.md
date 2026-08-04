---
title: "Sharp Rates in Dependent Learning Theory: Avoiding Sample Size Deflation for the Square Loss"
source: "https://proceedings.mlr.press/v235/ziemann24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ziemann24a/ziemann24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'neural-network-learning-dynamics-theory']
tags: ['dependent-learning', 'statistical-learning-theory', 'square-loss', 'mixing-sequences', 'sharp-rates']
venue: "ICML 2024"
tldr: "This paper establishes sharp statistical learning rates for dependent data under square loss, avoiding sample size deflation through tight noise interaction bounds."
---

# Sharp Rates in Dependent Learning Theory: Avoiding Sample Size Deflation for the Square Loss

**Source**: [https://proceedings.mlr.press/v235/ziemann24a.html](https://proceedings.mlr.press/v235/ziemann24a.html)

**TLDR**: This paper establishes sharp statistical learning rates for dependent data under square loss, avoiding sample size deflation through tight noise interaction bounds.

## Abstract

In this work, we study statistical learning with dependent data and square loss in a hypothesis class with tail decay in Orlicz space: $\mathscr{F}\subset L_{\Psi_p}$. Our inquiry is motivated by the search for a sharp noise interaction term, or variance proxy, in learning with dependent (e.g. $\beta$-mixing) data. Typical non-asymptotic results exhibit variance proxies that are deflated multiplicatively in the mixing time of the underlying covariates process. We show that whenever the topologies of $L^2$ and $\Psi_p$ are comparable on our hypothesis class $\mathscr{F}$, the empirical risk minimizer achieves a rate that only depends on the complexity of the class and second order statistics in its leading term. We refer to this as a near mixing-free rate, since direct dependence on mixing is relegated to an additive higher order term. Our approach, reliant on mixed tail generic chaining, allows us to obtain sharp, instance-optimal rates. Examples that satisfy our framework include for instance sub-Gaussian linear regression and bounded smoothness classes.