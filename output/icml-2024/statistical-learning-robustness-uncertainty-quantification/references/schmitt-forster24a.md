---
title: "Regularized Q-learning through Robust Averaging"
source: "https://proceedings.mlr.press/v235/schmitt-forster24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/schmitt-forster24a/schmitt-forster24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['Q-learning', 'distributional-robustness', 'estimation-bias', 'reinforcement-learning', 'robust-averaging']
venue: "ICML 2024"
tldr: "2RA Q-learning uses distributionally robust averaging to control estimation bias in Q-learning, improving performance in a principled manner."
---

# Regularized Q-learning through Robust Averaging

**Source**: [https://proceedings.mlr.press/v235/schmitt-forster24a.html](https://proceedings.mlr.press/v235/schmitt-forster24a.html)

**TLDR**: 2RA Q-learning uses distributionally robust averaging to control estimation bias in Q-learning, improving performance in a principled manner.

## Abstract

We propose a new Q-learning variant, called 2RA Q-learning, that addresses some weaknesses of existing Q-learning methods in a principled manner. One such weakness is an underlying estimation bias which cannot be controlled and often results in poor performance. We propose a distributionally robust estimator for the maximum expected value term, which allows us to precisely control the level of estimation bias introduced. The distributionally robust estimator admits a closed-form solution such that the proposed algorithm has a computational cost per iteration comparable to Watkins’ Q-learning. For the tabular case, we show that 2RA Q-learning converges to the optimal policy and analyze its asymptotic mean-squared error. Lastly, we conduct numerical experiments for various settings, which corroborate our theoretical findings and indicate that 2RA Q-learning often performs better than existing methods.