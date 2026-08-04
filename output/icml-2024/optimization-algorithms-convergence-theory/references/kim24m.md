---
title: "Double-Step Alternating Extragradient with Increasing Timescale Separation for Finding Local Minimax Points: Provable Improvements"
source: "https://proceedings.mlr.press/v235/kim24m.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24m/kim24m.pdf"
categories: ['optimization-algorithms-convergence-theory', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['minimax-optimization', 'two-timescale-methods', 'extragradient']
venue: "ICML 2024"
tldr: "Introduces a double-step alternating extragradient method with increasing timescale separation to provably improve convergence to local minimax points."
---

# Double-Step Alternating Extragradient with Increasing Timescale Separation for Finding Local Minimax Points: Provable Improvements

**Source**: [https://proceedings.mlr.press/v235/kim24m.html](https://proceedings.mlr.press/v235/kim24m.html)

**TLDR**: Introduces a double-step alternating extragradient method with increasing timescale separation to provably improve convergence to local minimax points.

## Abstract

In nonconvex-nonconcave minimax optimization, two-timescale gradient methods have shown their potential to find local minimax (optimal) points, provided that the timescale separation between the min and the max player is sufficiently large. However, existing two-timescale variants of gradient descent ascent and extragradient methods face two shortcomings, especially when we search for non-strict local minimax points that are prevalent in modern overparameterized setting. In specific, (1) these methods can be unstable at some non-strict local minimax points even with sufficiently large timescale separation, and even (2) computing a proper amount of timescale separation is infeasible in practice. To remedy these two issues, we propose to incorporate two simple but provably effective schemes, double-step alternating update and increasing timescale separation, into the two-timescale extragradient method, respectively. Under mild conditions, we show that the proposed methods converge to non-strict local minimax points that all existing two-timescale methods fail to converge.