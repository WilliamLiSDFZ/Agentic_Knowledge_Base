---
title: "Causal Inference from Competing Treatments"
source: "https://proceedings.mlr.press/v235/stoica24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/stoica24a/stoica24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'probabilistic-generating-circuits-research']
tags: ['causal-inference', 'competing-treatments', 'RCT', 'position-bias', 'advertising']
venue: "ICML 2024"
tldr: "A causal inference framework is developed to estimate treatment effects in RCTs where multiple administrators compete for subject attention, introducing position bias."
---

# Causal Inference from Competing Treatments

**Source**: [https://proceedings.mlr.press/v235/stoica24a.html](https://proceedings.mlr.press/v235/stoica24a.html)

**TLDR**: A causal inference framework is developed to estimate treatment effects in RCTs where multiple administrators compete for subject attention, introducing position bias.

## Abstract

Many applications of RCTs involve the presence of multiple treatment administrators—from field experiments to online advertising—that compete for the subjects’ attention. In the face of competition, estimating a causal effect becomes difficult, as the position at which a subject sees a treatment influences their response, and thus the treatment effect. In this paper, we build a game-theoretic model of agents who wish to estimate causal effects in the presence of competition, through a bidding system and a utility function that minimizes estimation error. Our main technical result establishes an approximation with a tractable objective that maximizes the sample value obtained through strategically allocating budget on subjects. This allows us to find an equilibrium in our model: we show that the tractable objective has a pure Nash equilibrium, and that any Nash equilibrium is an approximate equilibrium for our general objective that minimizes estimation error under broad conditions. Conceptually, our work successfully combines elements from causal inference and game theory to shed light on the equilibrium behavior of experimentation under competition.