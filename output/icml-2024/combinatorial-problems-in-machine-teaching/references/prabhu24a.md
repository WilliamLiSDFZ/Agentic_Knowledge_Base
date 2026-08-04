---
title: "Learning Multiple Secrets in Mastermind"
source: "https://proceedings.mlr.press/v235/prabhu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/prabhu24a/prabhu24a.pdf"
categories: ['combinatorial-problems-in-machine-teaching', 'data-selection-and-active-learning-methods']
tags: ['mastermind', 'combinatorial-learning', 'adaptive-queries']
venue: "ICML 2024"
tldr: "A two-round adaptive algorithm for learning multiple secrets in the Generalized Mastermind problem on the hypercube."
---

# Learning Multiple Secrets in Mastermind

**Source**: [https://proceedings.mlr.press/v235/prabhu24a.html](https://proceedings.mlr.press/v235/prabhu24a.html)

**TLDR**: A two-round adaptive algorithm for learning multiple secrets in the Generalized Mastermind problem on the hypercube.

## Abstract

In the Generalized Mastermind problem, there is an unknown subset $H$ of the hypercube 0,1$^d$ containing $n$ points. The goal is to learn $H$ by making a few queries to an oracle which given a point $q$ in 0,1$^d$, returns the point in $H$ nearest to $q$. We give a two-round adaptive algorithm for this problem that learns $H$ while making at most $\exp(\widetilde{O}(\sqrt{d \log n}))$. Furthermore, we show that any $r$-round adaptive randomized algorithm that learns $H$ with constant probability must make $\exp(\Omega(d^{3^{-(r-1)}}))$ queries even when the input has poly$(d)$ points; thus, any poly$(d)$ query algorithm must necessarily use $\Omega(\log \log d)$ rounds of adaptivity. We give optimal query complexity bounds for the variant of the problem where queries are allowed to be from 0,1,2$^d$. We also study a continuous variant of the problem in which $H$ is a subset of unit vectors in $\mathbb{R}^d$ and one can query unit vectors in $\mathbb{R}^d$. For this setting, we give a $O(n^{\lfloor d/2 \rfloor})$ query deterministic algorithm to learn the hidden set of points.