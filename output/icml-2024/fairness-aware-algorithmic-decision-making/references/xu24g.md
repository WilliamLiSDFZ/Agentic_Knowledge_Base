---
title: "Adapting Static Fairness to Sequential Decision-Making: Bias Mitigation Strategies towards Equal Long-term Benefit Rate"
source: "https://proceedings.mlr.press/v235/xu24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24g/xu24g.pdf"
categories: ['fairness-aware-algorithmic-decision-making']
tags: ['sequential-fairness', 'long-term-bias', 'dynamic-decision-making']
venue: "ICML 2024"
tldr: "This paper adapts static fairness criteria to sequential decision-making settings to achieve equal long-term benefit rates and mitigate compounding bias."
---

# Adapting Static Fairness to Sequential Decision-Making: Bias Mitigation Strategies towards Equal Long-term Benefit Rate

**Source**: [https://proceedings.mlr.press/v235/xu24g.html](https://proceedings.mlr.press/v235/xu24g.html)

**TLDR**: This paper adapts static fairness criteria to sequential decision-making settings to achieve equal long-term benefit rates and mitigate compounding bias.

## Abstract

Decisions made by machine learning models can have lasting impacts, making long-term fairness a critical consideration. It has been observed that ignoring the long-term effect and directly applying fairness criterion in static settings can actually worsen bias over time. To address biases in sequential decision-making, we introduce a long-term fairness concept named Equal Long-term Benefit Rate (ELBERT). This concept is seamlessly integrated into a Markov Decision Process (MDP) to consider the future effects of actions on long-term fairness, thus providing a unified framework for fair sequential decision-making problems. ELBERT effectively addresses the temporal discrimination issues found in previous long-term fairness notions. Additionally, we demonstrate that the policy gradient of Long-term Benefit Rate can be analytically simplified to standard policy gradients. This simplification makes conventional policy optimization methods viable for reducing bias, leading to our bias mitigation approach ELBERT-PO. Extensive experiments across various diverse sequential decision-making environments consistently reveal that ELBERT-PO significantly diminishes bias while maintaining high utility. Code is available at https://github.com/umd-huang-lab/ELBERT.