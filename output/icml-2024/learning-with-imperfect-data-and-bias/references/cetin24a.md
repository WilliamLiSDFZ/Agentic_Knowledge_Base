---
title: "Simple Ingredients for Offline Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/cetin24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cetin24a/cetin24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'learning-with-imperfect-data-and-bias']
tags: ['offline-reinforcement-learning', 'heterogeneous-data', 'diverse-trajectories', 'benchmark']
venue: "ICML 2024"
tldr: "Introduces the MOOD testbed to expose weaknesses of offline RL algorithms on heterogeneous data and proposes simple ingredients for improvement."
---

# Simple Ingredients for Offline Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/cetin24a.html](https://proceedings.mlr.press/v235/cetin24a.html)

**TLDR**: Introduces the MOOD testbed to expose weaknesses of offline RL algorithms on heterogeneous data and proposes simple ingredients for improvement.

## Abstract

Offline reinforcement learning algorithms have proven effective on datasets highly connected to the target downstream task. Yet, by leveraging a novel testbed (MOOD) in which trajectories come from heterogeneous sources, we show that existing methods struggle with diverse data: their performance considerably deteriorates as data collected for related but different tasks is simply added to the offline buffer. In light of this finding, we conduct a large empirical study where we formulate and test several hypotheses to explain this failure. Surprisingly, we find that targeted scale, more than algorithmic considerations, is the key factor influencing performance. We show that simple methods like AWAC and IQL with increased policy size overcome the paradoxical failure modes from the inclusion of additional data in MOOD, and notably outperform prior state-of-the-art algorithms on the canonical D4RL benchmark.