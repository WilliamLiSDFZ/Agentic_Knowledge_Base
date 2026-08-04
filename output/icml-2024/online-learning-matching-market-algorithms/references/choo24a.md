---
title: "Online bipartite matching with imperfect advice"
source: "https://proceedings.mlr.press/v235/choo24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/choo24a/choo24a.pdf"
categories: ['online-learning-matching-market-algorithms', 'online-learning-and-sequential-decision-making']
tags: ['online-bipartite-matching', 'learning-augmented-algorithms', 'competitive-analysis']
venue: "ICML 2024"
tldr: "An online bipartite matching algorithm that leverages imperfect advice to outperform classical competitive ratio bounds."
---

# Online bipartite matching with imperfect advice

**Source**: [https://proceedings.mlr.press/v235/choo24a.html](https://proceedings.mlr.press/v235/choo24a.html)

**TLDR**: An online bipartite matching algorithm that leverages imperfect advice to outperform classical competitive ratio bounds.

## Abstract

We study the problem of online unweighted bipartite matching with $n$ offline vertices and $n$ online vertices where one wishes to be competitive against the optimal offline algorithm. While the classic RANKING algorithm of (Karp et al., 1990) provably attains competitive ratio of $1-1/e > 1/2$, we show that no learning-augmented method can be both 1-consistent and strictly better than 1/2-robust under the adversarial arrival model. Meanwhile, under the random arrival model, we show how one can utilize methods from distribution testing to design an algorithm that takes in external advice about the online vertices and provably achieves competitive ratio interpolating between any ratio attainable by advice-free methods and the optimal ratio of 1, depending on the advice quality.