---
title: "Probabilistic Generating Circuits - Demystified"
source: "https://proceedings.mlr.press/v235/agarwal24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/agarwal24c/agarwal24c.pdf"
categories: ['probabilistic-generating-circuits-research']
tags: ['probabilistic-generating-circuits', 'determinantal-point-processes', 'probabilistic-circuits', 'unification']
venue: "ICML 2024"
tldr: "Demystifies probabilistic generating circuits by clarifying their relationship to probabilistic circuits and DPPs."
---

# Probabilistic Generating Circuits - Demystified

**Source**: [https://proceedings.mlr.press/v235/agarwal24c.html](https://proceedings.mlr.press/v235/agarwal24c.html)

**TLDR**: Demystifies probabilistic generating circuits by clarifying their relationship to probabilistic circuits and DPPs.

## Abstract

Zhang et al. (ICML 2021, PLMR 139, pp. 12447–12457) introduced probabilistic generating circuits (PGCs) as a probabilistic model to unify probabilistic circuits (PCs) and determinantal point processes (DPPs). At a first glance, PGCs store a distribution in a very different way, they compute the probability generating polynomial instead of the probability mass function and it seems that this is the main reason why PGCs are more powerful than PCs or DPPs. However, PGCs also allow for negative weights, whereas classical PCs assume that all weights are nonnegative. One main insight of this work is that the negative weights are the cause for the power of PGCs and not the different representation. PGCs are PCs in disguise: we show how to transform any PGC on binary variables into a PC with negative weights with only polynomial blowup. PGCs were defined by Zhang et al. only for binary random variables. As our second main result, we show that there is a good reason for this: we prove that PGCs for categorical variables with larger image size do not support tractable marginalization unless NP=P. On the other hand, we show that we can model categorical variables with larger image size as PC with negative weights computing set-multilinear polynomials. These allow for tractable marginalization. In this sense, PCs with negative weights strictly subsume PGCs.