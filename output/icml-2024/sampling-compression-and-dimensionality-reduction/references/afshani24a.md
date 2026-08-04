---
title: "Optimal Coresets for Low-Dimensional Geometric Median"
source: "https://proceedings.mlr.press/v235/afshani24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/afshani24a/afshani24a.pdf"
categories: ['sampling-compression-and-dimensionality-reduction']
tags: ['coresets', 'geometric-median', 'low-dimensional', 'approximation']
venue: "ICML 2024"
tldr: "Derives optimal coresets for approximating geometric median queries in low-dimensional Euclidean spaces."
---

# Optimal Coresets for Low-Dimensional Geometric Median

**Source**: [https://proceedings.mlr.press/v235/afshani24a.html](https://proceedings.mlr.press/v235/afshani24a.html)

**TLDR**: Derives optimal coresets for approximating geometric median queries in low-dimensional Euclidean spaces.

## Abstract

We investigate coresets for approximating the cost with respect to median queries. In this problem, we are given a set of points $P\subset \mathbb{R}^d$ and median queries are $\sum_{p\in P} ||p-c||$ for any point $c\in \mathbb{R}^d$. Our goal is to compute a small weighted summary $S\subset P$ such that the cost of any median query is approximated within a multiplicative $(1\pm\varepsilon)$ factor. We provide matching upper and lower bounds on the number of points contained in $S$ of the order $\tilde{\Theta}\left(\varepsilon^{-d/(d+1)}\right)$.