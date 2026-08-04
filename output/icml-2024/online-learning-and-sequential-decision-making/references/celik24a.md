---
title: "Acquiring Diverse Skills using Curriculum Reinforcement Learning with Mixture of Experts"
source: "https://proceedings.mlr.press/v235/celik24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/celik24a/celik24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['curriculum-reinforcement-learning', 'mixture-of-experts', 'diverse-skills', 'policy-learning']
venue: "ICML 2024"
tldr: "Proposes Di-SkilL, combining curriculum reinforcement learning with mixture-of-experts to learn diverse motor skills efficiently."
---

# Acquiring Diverse Skills using Curriculum Reinforcement Learning with Mixture of Experts

**Source**: [https://proceedings.mlr.press/v235/celik24a.html](https://proceedings.mlr.press/v235/celik24a.html)

**TLDR**: Proposes Di-SkilL, combining curriculum reinforcement learning with mixture-of-experts to learn diverse motor skills efficiently.

## Abstract

Reinforcement learning (RL) is a powerful approach for acquiring a good-performing policy. However, learning diverse skills is challenging in RL due to the commonly used Gaussian policy parameterization. We propose Diverse Skill Learning (Di-SkilL), an RL method for learning diverse skills using Mixture of Experts, where each expert formalizes a skill as a contextual motion primitive. Di-SkilL optimizes each expert and its associate context distribution to a maximum entropy objective that incentivizes learning diverse skills in similar contexts. The per-expert context distribution enables automatic curricula learning, allowing each expert to focus on its best-performing sub-region of the context space. To overcome hard discontinuities and multi-modalities without any prior knowledge of the environment’s unknown context probability space, we leverage energy-based models to represent the per-expert context distributions and demonstrate how we can efficiently train them using the standard policy gradient objective. We show on challenging robot simulation tasks that Di-SkilL can learn diverse and performant skills.