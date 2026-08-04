---
title: "Offline Inverse RL: New Solution Concepts and Provably Efficient Algorithms"
source: "https://proceedings.mlr.press/v235/lazzati24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lazzati24a/lazzati24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'fast-sketching-methods-for-large-scale-optimization']
tags: ['inverse-reinforcement-learning', 'offline-IRL', 'reward-recovery', 'solution-concepts']
venue: "ICML 2024"
tldr: "New solution concepts and provably efficient algorithms for offline inverse reinforcement learning addressing the ill-posedness of reward recovery."
---

# Offline Inverse RL: New Solution Concepts and Provably Efficient Algorithms

**Source**: [https://proceedings.mlr.press/v235/lazzati24a.html](https://proceedings.mlr.press/v235/lazzati24a.html)

**TLDR**: New solution concepts and provably efficient algorithms for offline inverse reinforcement learning addressing the ill-posedness of reward recovery.

## Abstract

Inverse reinforcement learning (IRL) aims to recover the reward function of an expert agent from demonstrations of behavior. It is well-known that the IRL problem is fundamentally ill-posed, i.e., many reward functions can explain the demonstrations. For this reason, IRL has been recently reframed in terms of estimating the feasible reward set (Metelli et al., 2021), thus, postponing the selection of a single reward. However, so far, the available formulations and algorithmic solutions have been proposed and analyzed mainly for the online setting, where the learner can interact with the environment and query the expert at will. This is clearly unrealistic in most practical applications, where the availability of an offline dataset is a much more common scenario. In this paper, we introduce a novel notion of feasible reward set capturing the opportunities and limitations of the offline setting and we analyze the complexity of its estimation. This requires the introduction an original learning framework that copes with the intrinsic difficulty of the setting, for which data coverage is not under control. Then, we propose two computationally and statistically efficient algorithms, IRLO and PIRLO, for addressing the problem. In particular, the latter adopts a specific form of pessimism to enforce the novel, desirable property of inclusion monotonicity of the delivered feasible set. With this work, we aim to provide a panorama of the challenges of the offline IRL problem and how they can be fruitfully addressed.