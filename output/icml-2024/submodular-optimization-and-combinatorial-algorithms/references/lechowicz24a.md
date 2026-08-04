---
title: "Chasing Convex Functions with Long-term Constraints"
source: "https://proceedings.mlr.press/v235/lechowicz24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lechowicz24a/lechowicz24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'submodular-optimization-and-combinatorial-algorithms']
tags: ['online-convex-optimization', 'long-term-constraints', 'metric-spaces', 'competitive-algorithms']
venue: "ICML 2024"
tldr: "A new family of online metric problems with long-term constraints where an agent minimizes hitting and switching costs simultaneously over time."
---

# Chasing Convex Functions with Long-term Constraints

**Source**: [https://proceedings.mlr.press/v235/lechowicz24a.html](https://proceedings.mlr.press/v235/lechowicz24a.html)

**TLDR**: A new family of online metric problems with long-term constraints where an agent minimizes hitting and switching costs simultaneously over time.

## Abstract

We introduce and study a family of online metric problems with long-term constraints. In these problems, an online player makes decisions $\mathbf{x}_t$ in a metric space $(X,d)$ to simultaneously minimize their hitting cost $f_t(\mathbf{x}_t)$ and switching cost as determined by the metric. Over the time horizon $T$, the player must satisfy a long-term demand constraint $\sum_t c(\mathbf{x}_t) \geq 1$, where $c(\mathbf{x}_t)$ denotes the fraction of demand satisfied at time $t$. Such problems can find a wide array of applications to online resource allocation in sustainable energy/computing systems. We devise optimal competitive and learning-augmented algorithms for the case of bounded hitting cost gradients and weighted $\ell_1$ metrics, and further show that our proposed algorithms perform well in numerical experiments.