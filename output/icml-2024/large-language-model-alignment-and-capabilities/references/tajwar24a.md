---
title: "Preference Fine-Tuning of LLMs Should Leverage Suboptimal, On-Policy Data"
source: "https://proceedings.mlr.press/v235/tajwar24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tajwar24a/tajwar24a.pdf"
categories: ['large-language-model-alignment-and-capabilities']
tags: ['RLHF', 'preference-learning', 'on-policy-data']
venue: "ICML 2024"
tldr: "Empirical analysis shows that on-policy suboptimal data significantly improves preference fine-tuning of LLMs compared to offline contrastive approaches."
---

# Preference Fine-Tuning of LLMs Should Leverage Suboptimal, On-Policy Data

**Source**: [https://proceedings.mlr.press/v235/tajwar24a.html](https://proceedings.mlr.press/v235/tajwar24a.html)

**TLDR**: Empirical analysis shows that on-policy suboptimal data significantly improves preference fine-tuning of LLMs compared to offline contrastive approaches.

## Abstract

Learning from preference labels plays a crucial role in fine-tuning large language models — this is done via supervised learning, on-policy reinforcement learning (RL), or contrastive learning. Different methods come with different implementation tradeoffs, and existing empirical findings present different conclusions, for instance, some results show that online RL is quite important to attain good fine-tuning results, while others find offline methods sufficient. This raises a question: what kind of approaches are important for fine-tuning with preference data and why? In this paper, we answer this question by performing a rigorous analysis of a number of fine-tuning techniques on didactic and full-scale LLM problems. Our main finding is that approaches that use on-policy sampling and attempt to push down the likelihood on certain responses (i.e., employ a ”negative gradient”) outperform offline and maximum likelihood objectives. We conceptualize our insights and unify methods that use on-policy sampling or negative gradient under a notion of mode-seeking objectives for categorical distributions. Mode-seeking objectives are able to alter probability mass on specific bins of a categorical distribution at a fast rate compared to maximum likelihood, allowing them to relocate masses across bins more effectively. Our analysis prescribes actionable insights for preference fine-tuning of LLMs and informs how data should be collected for maximal improvement.