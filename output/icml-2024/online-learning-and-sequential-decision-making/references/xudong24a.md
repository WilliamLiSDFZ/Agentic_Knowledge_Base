---
title: "Iterative Regularized Policy Optimization with Imperfect Demonstrations"
source: "https://proceedings.mlr.press/v235/xudong24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xudong24a/xudong24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'learning-with-imperfect-data-and-bias']
tags: ['imitation-learning', 'imperfect-demonstrations', 'KL-regularization']
venue: "ICML 2024"
tldr: "Proposes iterative regularized policy optimization to refine policies via online RL fine-tuning when demonstrations are imperfect and scarce."
---

# Iterative Regularized Policy Optimization with Imperfect Demonstrations

**Source**: [https://proceedings.mlr.press/v235/xudong24a.html](https://proceedings.mlr.press/v235/xudong24a.html)

**TLDR**: Proposes iterative regularized policy optimization to refine policies via online RL fine-tuning when demonstrations are imperfect and scarce.

## Abstract

Imitation learning heavily relies on the quality of provided demonstrations. In scenarios where demonstrations are imperfect and rare, a prevalent approach for refining policies is through online fine-tuning with reinforcement learning, in which a Kullback–Leibler (KL) regularization is often employed to stabilize the learning process. However, our investigation reveals that on the one hand, imperfect demonstrations can bias the online learning process, the KL regularization will further constrain the improvement of online policy exploration. To address the above issues, we propose Iterative Regularized Policy Optimization (IRPO), a framework that involves iterative offline imitation learning and online reinforcement exploration. Specifically, the policy learned online is used to serve as the demonstrator for successive learning iterations, with a demonstration boosting to consistently enhance the quality of demonstrations. Experimental validations conducted across widely used benchmarks and a novel fixed-wing UAV control task consistently demonstrate the effectiveness of IRPO in improving both the demonstration quality and the policy performance. Our code is available at https://github.com/GongXudong/IRPO.