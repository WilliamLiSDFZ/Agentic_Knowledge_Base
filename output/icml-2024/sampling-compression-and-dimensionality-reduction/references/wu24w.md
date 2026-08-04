---
title: "Profile Reconstruction from Private Sketches"
source: "https://proceedings.mlr.press/v235/wu24w.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24w/wu24w.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'sampling-compression-and-dimensionality-reduction']
tags: ['differential-privacy', 'profile-estimation', 'sketching', 'distributed-learning', 'frequency-estimation']
venue: "ICML 2024"
tldr: "Addresses differentially private profile reconstruction from distributed private sketches, estimating frequency distributions of items under space constraints."
---

# Profile Reconstruction from Private Sketches

**Source**: [https://proceedings.mlr.press/v235/wu24w.html](https://proceedings.mlr.press/v235/wu24w.html)

**TLDR**: Addresses differentially private profile reconstruction from distributed private sketches, estimating frequency distributions of items under space constraints.

## Abstract

Given a multiset of $n$ items from $\mathcal{D}$, the profile reconstruction problem is to estimate, for $t = 0, 1, …, n$, the fraction $\vec{f}[t]$ of items in $\mathcal{D}$ that appear exactly $t$ times. We consider differentially private profile estimation in a distributed, space-constrained setting where we wish to maintain an updatable, private sketch of the multiset that allows us to compute an approximation of $\vec{f} = (\vec{f}[0], …, \vec{f}[n])$. Using a histogram privatized using discrete Laplace noise, we show how to “reverse” the noise using an approach of Dwork et al. (ITCS ’10). We show how to speed up the algorithm from polynomial time to $O(d + n \log n)$, and analyze the achievable error in the $\ell_1$, $\ell_2$ and $\ell_\infty$ norms. In all cases the dependency of the error on $d = |\mathcal{D}|$ is $O( 1 / \sqrt{d})$ — we give an information-theoretic lower bound showing that this dependence on $d$ is asymptotically optimal among all private, updatable sketches for the profile reconstruction problem with a high-probability error guarantee.