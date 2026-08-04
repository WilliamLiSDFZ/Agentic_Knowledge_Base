---
title: "Algorithm and Hardness for Dynamic Attention Maintenance in Large Language Models"
source: "https://proceedings.mlr.press/v235/van-den-brand24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/van-den-brand24a/van-den-brand24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'dynamic-algorithms-and-complexity-theory']
tags: ['attention-mechanism', 'dynamic-algorithms', 'complexity-theory']
venue: "ICML 2024"
tldr: "Studies algorithmic and hardness results for dynamically maintaining attention computations in large language models."
---

# Algorithm and Hardness for Dynamic Attention Maintenance in Large Language Models

**Source**: [https://proceedings.mlr.press/v235/van-den-brand24a.html](https://proceedings.mlr.press/v235/van-den-brand24a.html)

**TLDR**: Studies algorithmic and hardness results for dynamically maintaining attention computations in large language models.

## Abstract

The attention scheme is one of the key components over all the LLMs, such as BERT, GPT-1, Transformers, GPT-2, 3, 3.5 and 4. Inspired by previous theoretical study of static version of the attention multiplication problem [Zandieh, Han, Daliri, and Karbasi ICML 2023, Alman and Song NeurIPS 2023], we formally define a dynamic version of attention matrix multiplication problem. In each iteration we update one entry in key matrix $K \in \mathbb{R}^{n \times d}$ or value matrix $V \in \mathbb{R}^{n \times d}$. In the query stage, we receive $(i,j) \in [n] \times [d]$ as input, and want to answer $(D^{-1} A V)_{i,j}$, where $A:=\exp(QK^\top) \in \mathbb{R}^{n \times n}$ is a square matrix and $D := \mathrm{diag}(A {\bf 1}_n) \in \mathbb{R}^{n \times n}$ is a diagonal matrix and ${\bf 1}_n$ denotes a length-$n$ vector that all the entries are ones. We provide two results: an algorithm and a conditional lower bound. Inspired by the lazy update idea from [Demetrescu and Italiano FOCS 2000, Sankowski FOCS 2004, Cohen, Lee and Song STOC 2019, Brand SODA 2020], we provide a data-structure that uses $O(n^{\omega(1,1,\tau)-\tau})$ amortized update time, and $O(n^{1+\tau})$ worst-case query time, where $n^{\omega(1,1,\tau)}$ denotes $\mathrm(n,n,n^\tau)$ with matrix multiplication exponent $\omega$ and $\tau$ denotes a constant in $(0,1]$. We also show that unless the hinted matrix vector multiplication conjecture [Brand, Nanongkai and Saranurak FOCS 2019] is false, there is no algorithm that can use both $O(n^{\omega(1,1,\tau) - \tau- \Omega(1)})$ amortized update time, and $O(n^{1+\tau-\Omega(1)})$ worst query time.