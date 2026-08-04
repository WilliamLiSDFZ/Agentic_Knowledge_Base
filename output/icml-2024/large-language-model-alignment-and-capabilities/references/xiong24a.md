---
title: "Iterative Preference Learning from Human Feedback: Bridging Theory and Practice for RLHF under KL-constraint"
source: "https://proceedings.mlr.press/v235/xiong24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xiong24a/xiong24a.pdf"
categories: ['large-language-model-alignment-and-capabilities']
tags: ['RLHF', 'KL-regularization', 'iterative-preference-learning']
venue: "ICML 2024"
tldr: "This paper develops a theoretical framework for iterative RLHF under KL-constraints and bridges the gap between theory and practice for aligning generative models."
---

# Iterative Preference Learning from Human Feedback: Bridging Theory and Practice for RLHF under KL-constraint

**Source**: [https://proceedings.mlr.press/v235/xiong24a.html](https://proceedings.mlr.press/v235/xiong24a.html)

**TLDR**: This paper develops a theoretical framework for iterative RLHF under KL-constraints and bridges the gap between theory and practice for aligning generative models.

## Abstract

This paper studies the theoretical framework of the alignment process of generative models with Reinforcement Learning from Human Feedback (RLHF). We consider a standard mathematical formulation, the reverse-KL regularized contextual bandit for RLHF. Despite its widespread practical application, a rigorous theoretical analysis of this formulation remains open. We investigate its behavior in three distinct settings—offline, online, and hybrid—and propose efficient algorithms with finite-sample theoretical guarantees. Moving towards practical applications, our framework, with a robust approximation of the information-theoretical policy improvement oracle, naturally gives rise to several novel RLHF algorithms. This includes an iterative version of the Direct Preference Optimization (DPO) algorithm for online settings, and a multi-step rejection sampling strategy for offline scenarios. Our empirical evaluations on real-world alignment experiment of large language model demonstrate that these proposed methods significantly surpass existing strong baselines, such as DPO and Rejection Sampling Optimization (RSO), showcasing the connections between solid theoretical foundations and their potent practical implementations.