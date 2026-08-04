---
title: "Centralized Selection with Preferences in the Presence of Biases"
source: "https://proceedings.mlr.press/v235/celis24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/celis24a/celis24a.pdf"
categories: ['fairness-aware-algorithmic-decision-making', 'learning-with-imperfect-data-and-bias']
tags: ['fairness', 'selection-bias', 'centralized-selection', 'preference-matching']
venue: "ICML 2024"
tldr: "Studies centralized candidate selection under institutional capacity constraints and evaluates how biases in utility estimates affect fairness outcomes."
---

# Centralized Selection with Preferences in the Presence of Biases

**Source**: [https://proceedings.mlr.press/v235/celis24a.html](https://proceedings.mlr.press/v235/celis24a.html)

**TLDR**: Studies centralized candidate selection under institutional capacity constraints and evaluates how biases in utility estimates affect fairness outcomes.

## Abstract

This paper considers the scenario in which there are multiple institutions, each with a limited capacity for candidates, and candidates, each with preferences over the institutions. A central entity evaluates the utility of each candidate to the institutions, and the goal is to select candidates for each institution in a way that maximizes utility while also considering the candidates’ preferences. The paper focuses on the setting in which candidates are divided into multiple groups and the observed utilities of candidates in some groups are biased–systematically lower than their true utilities. The first result is that, in these biased settings, prior algorithms can lead to selections with sub-optimal true utility and significant discrepancies in the fraction of candidates from each group that get their preferred choices. Subsequently, an algorithm is presented along with proof that it produces selections that achieve near-optimal group fairness with respect to preferences while also nearly maximizing the true utility under distributional assumptions. Further, extensive empirical validation of these results in real-world and synthetic settings, in which the distributional assumptions may not hold, are presented.