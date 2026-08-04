---
title: "Hybrid$^2$ Neural ODE Causal Modeling and an Application to Glycemic Response"
source: "https://proceedings.mlr.press/v235/zou24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zou24b/zou24b.pdf"
categories: ['amortized-hybrid-dynamical-system-discovery', 'causal-ml-for-clinical-decision-making']
tags: ['hybrid-neural-ODE', 'causal-modeling', 'glycemic-response', 'mechanistic-models', 'counterfactual']
venue: "ICML 2024"
tldr: "This paper proposes a hybrid neural ODE framework for causal modeling of physiological dynamics and applies it to glycemic response prediction."
---

# Hybrid$^2$ Neural ODE Causal Modeling and an Application to Glycemic Response

**Source**: [https://proceedings.mlr.press/v235/zou24b.html](https://proceedings.mlr.press/v235/zou24b.html)

**TLDR**: This paper proposes a hybrid neural ODE framework for causal modeling of physiological dynamics and applies it to glycemic response prediction.

## Abstract

Hybrid models composing mechanistic ODE-based dynamics with flexible and expressive neural network components have grown rapidly in popularity, especially in scientific domains where such ODE-based modeling offers important interpretability and validated causal grounding (e.g., for counterfactual reasoning). The incorporation of mechanistic models also provides inductive bias in standard blackbox modeling approaches, critical when learning from small datasets or partially observed, complex systems. Unfortunately, as the hybrid models become more flexible, the causal grounding provided by the mechanistic model can quickly be lost. We address this problem by leveraging another common source of domain knowledge: ranking of treatment effects for a set of interventions, even if the precise treatment effect is unknown. We encode this information in a causal loss that we combine with the standard predictive loss to arrive at a hybrid loss that biases our learning towards causally valid hybrid models. We demonstrate our ability to achieve a win-win, state-of-the-art predictive performance and causal validity, in the challenging task of modeling glucose dynamics post-exercise in individuals with type 1 diabetes.