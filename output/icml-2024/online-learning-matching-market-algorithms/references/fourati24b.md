---
title: "Federated Combinatorial Multi-Agent Multi-Armed Bandits"
source: "https://proceedings.mlr.press/v235/fourati24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fourati24b/fourati24b.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'online-learning-matching-market-algorithms']
tags: ['federated-bandits', 'combinatorial-optimization', 'multi-agent']
venue: "ICML 2024"
tldr: "A federated learning framework is proposed for cooperative combinatorial bandit optimization with bandit feedback across multiple agents."
---

# Federated Combinatorial Multi-Agent Multi-Armed Bandits

**Source**: [https://proceedings.mlr.press/v235/fourati24b.html](https://proceedings.mlr.press/v235/fourati24b.html)

**TLDR**: A federated learning framework is proposed for cooperative combinatorial bandit optimization with bandit feedback across multiple agents.

## Abstract

This paper introduces a federated learning framework tailored for online combinatorial optimization with bandit feedback. In this setting, agents select subsets of arms, observe noisy rewards for these subsets without accessing individual arm information, and can cooperate and share information at specific intervals. Our framework transforms any offline resilient single-agent $(\alpha-\epsilon)$-approximation algorithm—having a complexity of $\tilde{\mathcal{O}}\left(\frac{\psi}{\epsilon^\beta}\right)$, where the logarithm is omitted, for some function $\psi$ and constant $\beta$—into an online multi-agent algorithm with $m$ communicating agents and an $\alpha$-regret of no more than $\tilde{\mathcal{O}}\left(m^{-\frac{1}{3+\beta}} \psi^\frac{1}{3+\beta} T^\frac{2+\beta}{3+\beta}\right)$. Our approach not only eliminates the $\epsilon$ approximation error but also ensures sublinear growth with respect to the time horizon $T$ and demonstrates a linear speedup with an increasing number of communicating agents. Additionally, the algorithm is notably communication-efficient, requiring only a sublinear number of communication rounds, quantified as $\tilde{\mathcal{O}}\left(\psi T^\frac{\beta}{\beta+1}\right)$. Furthermore, the framework has been successfully applied to online stochastic submodular maximization using various offline algorithms, yielding the first results for both single-agent and multi-agent settings and recovering specialized single-agent theoretical guarantees. We empirically validate our approach to a stochastic data summarization problem, illustrating the effectiveness of the proposed framework, even in single-agent scenarios.