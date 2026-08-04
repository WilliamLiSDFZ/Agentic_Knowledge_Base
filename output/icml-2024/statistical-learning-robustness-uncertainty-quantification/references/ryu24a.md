---
title: "Gambling-Based Confidence Sequences for Bounded Random Vectors"
source: "https://proceedings.mlr.press/v235/ryu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ryu24a/ryu24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'online-learning-and-sequential-decision-making']
tags: ['confidence-sequences', 'anytime-valid', 'bounded-random-vectors', 'gambling-based', 'multivariate']
venue: "ICML 2024"
tldr: "A gambling-based framework is proposed for constructing confidence sequences for means of bounded multivariate stochastic processes valid at any stopping time."
---

# Gambling-Based Confidence Sequences for Bounded Random Vectors

**Source**: [https://proceedings.mlr.press/v235/ryu24a.html](https://proceedings.mlr.press/v235/ryu24a.html)

**TLDR**: A gambling-based framework is proposed for constructing confidence sequences for means of bounded multivariate stochastic processes valid at any stopping time.

## Abstract

A confidence sequence (CS) is a sequence of confidence sets that contains a target parameter of an underlying stochastic process at any time step with high probability. This paper proposes a new approach to constructing CSs for means of bounded multivariate stochastic processes using a general gambling framework, extending the recently established coin toss framework for bounded random processes. The proposed gambling framework provides a general recipe for constructing CSs for categorical and probability-vector-valued observations, as well as for general bounded multidimensional observations through a simple reduction. This paper specifically explores the use of the mixture portfolio, akin to Cover’s universal portfolio, in the proposed framework and investigates the properties of the resulting CSs. Simulations demonstrate the tightness of these confidence sequences compared to existing methods. When applied to the sampling without-replacement setting for finite categorical data, it is shown that the resulting CS based on a universal gambling strategy is provably tighter than that of the posterior-prior ratio martingale proposed by Waudby-Smith and Ramdas.