---
title: "Stealthy Imitation: Reward-guided Environment-free Policy Stealing"
source: "https://proceedings.mlr.press/v235/zhuang24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhuang24a/zhuang24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['policy-stealing', 'imitation-learning', 'reinforcement-learning', 'reward-guided', 'intellectual-property']
venue: "ICML 2024"
tldr: "This paper proposes a stealthy reward-guided policy stealing attack that imitates deep RL policies without access to the environment."
---

# Stealthy Imitation: Reward-guided Environment-free Policy Stealing

**Source**: [https://proceedings.mlr.press/v235/zhuang24a.html](https://proceedings.mlr.press/v235/zhuang24a.html)

**TLDR**: This paper proposes a stealthy reward-guided policy stealing attack that imitates deep RL policies without access to the environment.

## Abstract

Deep reinforcement learning policies, which are integral to modern control systems, represent valuable intellectual property. The development of these policies demands considerable resources, such as domain expertise, simulation fidelity, and real-world validation. These policies are potentially vulnerable to model stealing attacks, which aim to replicate their functionality using only black-box access. In this paper, we propose Stealthy Imitation, the first attack designed to steal policies without access to the environment or knowledge of the input range. This setup has not been considered by previous model stealing methods. Lacking access to the victim’s input states distribution, Stealthy Imitation fits a reward model that allows to approximate it. We show that the victim policy is harder to imitate when the distribution of the attack queries matches that of the victim. We evaluate our approach across diverse, high-dimensional control tasks and consistently outperform prior data-free approaches adapted for policy stealing. Lastly, we propose a countermeasure that significantly diminishes the effectiveness of the attack.