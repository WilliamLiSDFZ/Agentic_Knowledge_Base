---
title: "Prospective Side Information for Latent MDPs"
source: "https://proceedings.mlr.press/v235/kwon24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kwon24a/kwon24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-mdp-structure-and-dependencies']
tags: ['latent-MDPs', 'side-information', 'contextual-bandits', 'partial-observability']
venue: "ICML 2024"
tldr: "A framework for leveraging prospective side information in latent MDPs to improve sequential decision-making under partial context observability."
---

# Prospective Side Information for Latent MDPs

**Source**: [https://proceedings.mlr.press/v235/kwon24a.html](https://proceedings.mlr.press/v235/kwon24a.html)

**TLDR**: A framework for leveraging prospective side information in latent MDPs to improve sequential decision-making under partial context observability.

## Abstract

In many interactive decision-making problems, there is contextual side information that remains fixed within the course of an interaction. This problem has been studied quite extensively under the assumption the context is fully observed, as well as in the opposing limit when the context is unobserved, a special type of POMDP also referred to as a Latent MDP (LMDP). In this work, we consider a class of decision problems that interpolates between the settings, namely, between the case the context is fully observed, and the case the context is unobserved. We refer to this class of decision problems as LMDPs with prospective side information. In such an environment an agent receives additional, weakly revealing, information on the latent context at the beginning of each episode. We show that, surprisingly, this problem is not captured by contemporary POMDP settings and is not solved by RL algorithms designed for partially observed environments. We then establish that any sample efficient algorithm must suffer at least $\Omega(K^{2/3})$-regret, as opposed to standard $\Omega(\sqrt{K})$ lower bounds. We design an algorithm with a matching upper bound that depends only polynomially on the problem parameters. This establishes exponential improvement in the sample complexity relative to the existing LMDP lower bound, when prospective information is not given in prior work.