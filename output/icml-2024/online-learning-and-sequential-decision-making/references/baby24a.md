---
title: "Online Matrix Completion: A Collaborative Approach with Hott Items"
source: "https://proceedings.mlr.press/v235/baby24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/baby24a/baby24a.pdf"
categories: ['online-learning-matching-market-algorithms', 'online-learning-and-sequential-decision-making']
tags: ['online-matrix-completion', 'low-rank', 'collaborative-filtering', 'hott-items', 'recommendation']
venue: "ICML 2024"
tldr: "Studies online low-rank matrix completion with collaborative multi-user strategies accounting for hott (popular) items effects."
---

# Online Matrix Completion: A Collaborative Approach with Hott Items

**Source**: [https://proceedings.mlr.press/v235/baby24a.html](https://proceedings.mlr.press/v235/baby24a.html)

**TLDR**: Studies online low-rank matrix completion with collaborative multi-user strategies accounting for hott (popular) items effects.

## Abstract

We investigate the low rank matrix completion problem in an online setting with ${M}$ users, ${N}$ items, ${T}$ rounds, and an unknown rank-$r$ reward matrix ${R}\in \mathbb{R}^{{M}\times {N}}$. This problem has been well-studied in the literature and has several applications in practice. In each round, we recommend ${S}$ carefully chosen distinct items to every user and observe noisy rewards. In the regime where ${M},{N} >> {T}$, we propose two distinct computationally efficient algorithms for recommending items to users and analyze them under the benign hott items assumption 1) First, for ${S}=1$, under additional incoherence/smoothness assumptions on ${R}$, we propose the phased algorithm PhasedClusterElim. Our algorithm obtains a near-optimal per-user regret of $\tilde{O}({N}{M}^{-1}(\Delta^{-1}+\Delta_{\text{hott}}^{-2}))$ where $\Delta_{\text{hott}},\Delta$ are problem-dependent gap parameters with $\Delta_{\text{hott}} >> \Delta$ almost always. 2) Second, we consider a simplified setting with ${S}=r$ where we make significantly milder assumptions on ${R}$. Here, we introduce another phased algorithm, DeterminantElim, to derive a regret guarantee of $\tilde{O}({N}{M}^{-1/r}\Delta_\text{det}^{-1}))$ where $\Delta_{\text{det}}$ is another problem-dependent gap. Both algorithms crucially use collaboration among users to jointly eliminate sub-optimal items for groups of users successively in phases, but with distinctive and novel approaches.