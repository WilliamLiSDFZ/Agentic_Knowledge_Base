---
title: "Online Learning under Budget and ROI Constraints via Weak Adaptivity"
source: "https://proceedings.mlr.press/v235/castiglioni24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/castiglioni24a/castiglioni24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['online-learning', 'budget-constraints', 'ROI-constraints', 'primal-dual']
venue: "ICML 2024"
tldr: "Develops weakly adaptive primal-dual algorithms for online learning under simultaneous budget and return-on-investment constraints."
---

# Online Learning under Budget and ROI Constraints via Weak Adaptivity

**Source**: [https://proceedings.mlr.press/v235/castiglioni24a.html](https://proceedings.mlr.press/v235/castiglioni24a.html)

**TLDR**: Develops weakly adaptive primal-dual algorithms for online learning under simultaneous budget and return-on-investment constraints.

## Abstract

We study online learning problems in which a decision maker has to make a sequence of costly decisions, with the goal of maximizing their expected reward while adhering to budget and return-on-investment (ROI) constraints. Existing primal-dual algorithms designed for constrained online learning problems under adversarial inputs rely on two fundamental assumptions. First, the decision maker must know beforehand the value of parameters related to the degree of strict feasibility of the problem (i.e. Slater parameters). Second, a strictly feasible solution to the offline optimization problem must exist at each round. Both requirements are unrealistic for practical applications such as bidding in online ad auctions. In this paper, we show how such assumptions can be circumvented by endowing standard primal-dual templates with weakly adaptive regret minimizers. This results in a “dual-balancing” framework which ensures that dual variables stay sufficiently small, even in the absence of knowledge about Slater’s parameter. We prove the first best-of-both-worlds no-regret guarantees which hold in absence of the two aforementioned assumptions, under stochastic and adversarial inputs. Finally, we show how to instantiate the framework to optimally bid in various mechanisms of practical relevance, such as first- and second-price auctions.