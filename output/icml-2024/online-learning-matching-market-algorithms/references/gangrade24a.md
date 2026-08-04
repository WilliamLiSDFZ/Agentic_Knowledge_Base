---
title: "Testing the Feasibility of Linear Programs with Bandit Feedback"
source: "https://proceedings.mlr.press/v235/gangrade24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gangrade24a/gangrade24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'online-learning-matching-market-algorithms']
tags: ['bandit-feedback', 'linear-programming', 'feasibility-testing', 'constrained-optimization']
venue: "ICML 2024"
tldr: "This paper introduces and studies the novel problem of testing feasibility of linear programs when feedback is obtained via bandit observations."
---

# Testing the Feasibility of Linear Programs with Bandit Feedback

**Source**: [https://proceedings.mlr.press/v235/gangrade24a.html](https://proceedings.mlr.press/v235/gangrade24a.html)

**TLDR**: This paper introduces and studies the novel problem of testing feasibility of linear programs when feedback is obtained via bandit observations.

## Abstract

While the recent literature has seen a surge in the study of constrained bandit problems, all existing methods for these begin by assuming the feasibility of the underlying problem. We initiate the study of testing such feasibility assumptions, and in particular address the problem in the linear bandit setting, thus characterising the costs of feasibility testing for an unknown linear program using bandit feedback. Concretely, we test if $\exists x: Ax \ge 0$ for an unknown $A \in \mathbb{R}^{m \times d}$, by playing a sequence of actions $x_t\in \mathbb{R}^d$, and observing $Ax_t + \mathrm{noise}$ in response. By identifying the hypothesis as determining the sign of the value of a minimax game, we construct a novel test based on low-regret algorithms and a nonasymptotic law of iterated logarithms. We prove that this test is reliable, and adapts to the ‘signal level,’ $\Gamma,$ of any instance, with mean sample costs scaling as $\widetilde{O}(d^2/\Gamma^2)$. We complement this by a minimax lower bound of $\Omega(d/\Gamma^2)$ for sample costs of reliable tests, dominating prior asymptotic lower bounds by capturing the dependence on $d$, and thus elucidating a basic insight missing in the extant literature on such problems.