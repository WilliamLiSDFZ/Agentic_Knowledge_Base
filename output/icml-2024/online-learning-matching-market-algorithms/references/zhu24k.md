---
title: "Online Learning in Betting Markets: Profit versus Prediction"
source: "https://proceedings.mlr.press/v235/zhu24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhu24k/zhu24k.pdf"
categories: ['online-learning-matching-market-algorithms', 'online-learning-and-sequential-decision-making']
tags: ['betting-markets', 'prediction-markets', 'online-learning', 'bookmaker', 'belief-updating']
venue: "ICML 2024"
tldr: "This paper analyzes binary betting markets for profit and information, showing the interplay between belief and price-setting and the tension between bookmaker profit and prediction accuracy."
---

# Online Learning in Betting Markets: Profit versus Prediction

**Source**: [https://proceedings.mlr.press/v235/zhu24k.html](https://proceedings.mlr.press/v235/zhu24k.html)

**TLDR**: This paper analyzes binary betting markets for profit and information, showing the interplay between belief and price-setting and the tension between bookmaker profit and prediction accuracy.

## Abstract

We examine two types of binary betting markets, whose primary goal is for profit (such as sports gambling) or to gain information (such as prediction markets). We articulate the interplay between belief and price-setting to analyse both types of markets, and show that the goals of maximising bookmaker profit and eliciting information are fundamentally incompatible. A key insight is that profit hinges on the deviation between (the distribution of) bettor and true beliefs, and that heavier tails in bettor belief distribution implies higher profit. Our algorithmic contribution is to introduce online learning methods for price-setting. Traditionally bookmakers update their prices rather infrequently, we present two algorithms that guide price updates upon seeing each bet, assuming very little of bettor belief distributions. The online pricing algorithm achieves stochastic regret of $\mathcal{O}(\sqrt{T})$ against the worst local maximum, or $\mathcal{O}(\sqrt{T \log T})$ with high probability against the global maximum under fair odds. More broadly, the inherent tradeoff between profit and information-seeking in binary betting may inspire new understandings of large-scale multi-agent behaviour.