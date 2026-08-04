---
title: "On Online Experimentation without Device Identifiers"
source: "https://proceedings.mlr.press/v235/shankar24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shankar24a/shankar24a.pdf"
categories: ['difference-in-differences-based-policy-evaluation', 'sampling-compression-and-dimensionality-reduction']
tags: ['online-experimentation', 'randomized-experimentation', 'user-identifiers']
venue: "ICML 2024"
tldr: "This paper addresses the challenge of measuring user preferences via randomized experimentation when device identifiers are unavailable in online settings."
---

# On Online Experimentation without Device Identifiers

**Source**: [https://proceedings.mlr.press/v235/shankar24a.html](https://proceedings.mlr.press/v235/shankar24a.html)

**TLDR**: This paper addresses the challenge of measuring user preferences via randomized experimentation when device identifiers are unavailable in online settings.

## Abstract

Measuring human feedback via randomized experimentation is a cornerstone of data-driven decision-making. The methodology used to estimate user preferences from their online behaviours is critically dependent on user identifiers. However, in today’s digital landscape, consumers frequently interact with content across multiple devices, which are often recorded with different identifiers for the same consumer. The inability to match different device identities across consumers poses significant challenges for accurately estimating human preferences and other causal effects. Moreover, without strong assumptions about the device-user graph, the causal effects might not be identifiable. In this paper, we propose HIFIVE, a variational method to solve the problem of estimating global average treatment effects (GATE) from a fragmented view of exposures and outcomes. Experiments show that our estimator is superior to standard estimators, with a lower bias and greater robustness to network uncertainty.