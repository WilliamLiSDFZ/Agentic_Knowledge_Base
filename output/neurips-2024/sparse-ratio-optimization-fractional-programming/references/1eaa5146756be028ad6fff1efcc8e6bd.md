---
title: "A Globally Optimal Portfolio for m-Sparse Sharpe Ratio Maximization"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/1eaa5146756be028ad6fff1efcc8e6bd-Abstract-Conference.html"
categories: ['sparse-ratio-optimization-fractional-programming', 'statistical-learning-theory-and-matrix-methods']
tags: ['sharpe-ratio', 'sparse-portfolio', 'fractional-programming']
venue: "NeurIPS 2024"
tldr: "Derives a globally optimal algorithm for maximizing the Sharpe ratio under m-sparsity constraints in portfolio optimization."
---

# A Globally Optimal Portfolio for m-Sparse Sharpe Ratio Maximization

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/1eaa5146756be028ad6fff1efcc8e6bd-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/1eaa5146756be028ad6fff1efcc8e6bd-Abstract-Conference.html)

**TLDR**: Derives a globally optimal algorithm for maximizing the Sharpe ratio under m-sparsity constraints in portfolio optimization.

## Abstract

The Sharpe ratio is an important and widely-used risk-adjusted return in financial engineering. In modern portfolio management, one may require an m-sparse (no more than m active assets) portfolio to save managerial and financial costs. However, few existing methods can optimize the Sharpe ratio with the m-sparse constraint, due to the nonconvexity and the complexity of this constraint. We propose to convert the m-sparse fractional optimization problem into an equivalent m-sparse quadratic programming problem. The semi-algebraic property of the resulting objective function allows us to exploit the Kurdyka-Lojasiewicz property to develop an efficient Proximal Gradient Algorithm (PGA) that leads to a portfolio which achieves the globally optimal m-sparse Sharpe ratio under certain conditions. The convergence rates of PGA are also provided. To the best of our knowledge, this is the first proposal that achieves a globally optimal m-sparse Sharpe ratio with a theoretically-sound guarantee.