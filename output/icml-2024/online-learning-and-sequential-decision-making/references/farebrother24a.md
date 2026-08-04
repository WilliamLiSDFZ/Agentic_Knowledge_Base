---
title: "Stop Regressing: Training Value Functions via Classification for Scalable Deep RL"
source: "https://proceedings.mlr.press/v235/farebrother24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/farebrother24a/farebrother24a.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['value-functions', 'classification', 'deep-reinforcement-learning']
venue: "ICML 2024"
tldr: "Proposes training value functions via classification instead of regression to improve scalability in deep RL."
---

# Stop Regressing: Training Value Functions via Classification for Scalable Deep RL

**Source**: [https://proceedings.mlr.press/v235/farebrother24a.html](https://proceedings.mlr.press/v235/farebrother24a.html)

**TLDR**: Proposes training value functions via classification instead of regression to improve scalability in deep RL.

## Abstract

Value functions are an essential component in deep reinforcement learning (RL), that are typically trained via mean squared error regression to match bootstrapped target values. However, scaling value-based RL methods to large networks has proven challenging. This difficulty is in stark contrast to supervised learning: by leveraging a cross-entropy classification loss, supervised methods have scaled reliably to massive networks. Observing this discrepancy, in this paper, we investigate whether the scalability of deep RL can also be improved simply by using classification in place of regression for training value functions. We show that training value functions with categorical cross-entropy significantly enhances performance and scalability across various domains, including single-task RL on Atari 2600 games, multi-task RL on Atari with large-scale ResNets, robotic manipulation with Q-transformers, playing Chess without search, and a language-agent Wordle task with high-capacity Transformers, achieving state-of-the-art results on these domains. Through careful analysis, we show that categorical cross-entropy mitigates issues inherent to value-based RL, such as noisy targets and non-stationarity. We argue that shifting to categorical cross-entropy for training value functions can substantially improve the scalability of deep RL at little-to-no cost.