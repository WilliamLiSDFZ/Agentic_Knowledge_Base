---
title: "Expert Proximity as Surrogate Rewards for Single Demonstration Imitation Learning"
source: "https://proceedings.mlr.press/v235/chiang24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chiang24a/chiang24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'simulation-scaling-limits-for-robot-manipulation']
tags: ['imitation-learning', 'single-demonstration', 'surrogate-rewards']
venue: "ICML 2024"
tldr: "Expert proximity is used as a surrogate reward to enable effective imitation learning from a single expert demonstration."
---

# Expert Proximity as Surrogate Rewards for Single Demonstration Imitation Learning

**Source**: [https://proceedings.mlr.press/v235/chiang24a.html](https://proceedings.mlr.press/v235/chiang24a.html)

**TLDR**: Expert proximity is used as a surrogate reward to enable effective imitation learning from a single expert demonstration.

## Abstract

In this paper, we focus on single-demonstration imitation learning (IL), a practical approach for real-world applications where acquiring multiple expert demonstrations is costly or infeasible and the ground truth reward function is not available. In contrast to typical IL settings with multiple demonstrations, single-demonstration IL involves an agent having access to only one expert trajectory. We highlight the issue of sparse reward signals in this setting and propose to mitigate this issue through our proposed Transition Discriminator-based IL (TDIL) method. TDIL is an IRL method designed to address reward sparsity by introducing a denser surrogate reward function that considers environmental dynamics. This surrogate reward function encourages the agent to navigate towards states that are proximal to expert states. In practice, TDIL trains a transition discriminator to differentiate between valid and non-valid transitions in a given environment to compute the surrogate rewards. The experiments demonstrate that TDIL outperforms existing IL approaches and achieves expert-level performance in the single-demonstration IL setting across five widely adopted MuJoCo benchmarks as well as the "Adroit Door" robotic environment.