---
title: "No-regret Learning in Harmonic Games: Extrapolation in the Face of Conflicting Interests"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/df5a8051be8bf4eaaabceb67c6d48332-Abstract-Conference.html"
categories: ['online-learning-augmented-algorithms-and-optimization', 'stochastic-optimization-convergence-and-variance-reduction']
tags: ['no-regret-learning', 'harmonic-games', 'extrapolation']
venue: "NeurIPS 2024"
tldr: "The long-run behavior of no-regret learning in harmonic games is analyzed, showing how extrapolation addresses conflicting player interests."
---

# No-regret Learning in Harmonic Games: Extrapolation in the Face of Conflicting Interests

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/df5a8051be8bf4eaaabceb67c6d48332-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/df5a8051be8bf4eaaabceb67c6d48332-Abstract-Conference.html)

**TLDR**: The long-run behavior of no-regret learning in harmonic games is analyzed, showing how extrapolation addresses conflicting player interests.

## Abstract

The long-run behavior of multi-agent online learning -- and, in particular, no-regret learning -- is relatively well-understood in potential games, where players have common interests. By contrast, in general harmonic games -- the strategic complement of potential games, where players have competing interests -- very little is known outside the narrow subclass of $2$-player zero-sum games with a fully-mixed equilibrium. Our paper seeks to partially fill this gap by focusing on the full class of (generalized) harmonic games and examining the convergence properties of "follow-the-regularized-leader" (FTRL), the most widely studied class of no-regret learning schemes. As a first result, we show that the continuous-time dynamics of FTRL are Poincaré recurrent, i.e., they return arbitrarily close to their starting point infinitely often, and hence fail to converge. In discrete time, the standard, "vanilla" implementation of FTRL may lead to even worse outcomes, eventually trapping the players in a perpetual cycle of best-responses. However, if FTRL is augmented with a suitable extrapolation step -- which includes as special cases the optimistic and mirror-prox variants of FTRL -- we show that learning converges to a Nash equilibrium from any initial condition, and all players are guaranteed at most $\mathcal{O}(1)$ regret. These results provide an in-depth understanding of no-regret learning in harmonic games, nesting prior work on $2$-player zero-sum games, and showing at a high level that potential and harmonic games are complementary not only from the strategic but also from the dynamic viewpoint.