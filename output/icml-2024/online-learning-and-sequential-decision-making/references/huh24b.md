---
title: "Nash Incentive-compatible Online Mechanism Learning via Weakly Differentially Private Online Learning"
source: "https://proceedings.mlr.press/v235/huh24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huh24b/huh24b.pdf"
categories: ['online-learning-matching-market-algorithms', 'online-learning-and-sequential-decision-making']
tags: ['mechanism-design', 'incentive-compatibility', 'online-learning', 'differential-privacy', 'nash-equilibrium']
venue: "ICML 2024"
tldr: "Designs Nash incentive-compatible online mechanism learning using weakly differentially private online learning to maximize objectives without prior agent knowledge."
---

# Nash Incentive-compatible Online Mechanism Learning via Weakly Differentially Private Online Learning

**Source**: [https://proceedings.mlr.press/v235/huh24b.html](https://proceedings.mlr.press/v235/huh24b.html)

**TLDR**: Designs Nash incentive-compatible online mechanism learning using weakly differentially private online learning to maximize objectives without prior agent knowledge.

## Abstract

We study a multi-round mechanism design problem, where we interact with a set of agents over a sequence of rounds. We wish to design an incentive-compatible (IC) online learning scheme to maximize an application-specific objective within a given class of mechanisms, without prior knowledge of the agents’ type distributions. Even if each mechanism in this class is IC in a single round, if an algorithm naively chooses from this class on each round, the entire learning process may not be IC against non-myopic buyers who appear over multiple rounds. On each round, our method randomly chooses between the recommendation of a weakly differentially private online learning algorithm (e.g., Hedge), and a commitment mechanism which penalizes non-truthful behavior. Our method is IC and achieves $O(T^{\frac{1+h}{2}})$ regret for the application-specific objective in an adversarial setting, where $h$ quantifies the long-sightedness of the agents. When compared to prior work, our approach is conceptually simpler, it applies to general mechanism design problems (beyond auctions), and its regret scales gracefully with the size of the mechanism class.