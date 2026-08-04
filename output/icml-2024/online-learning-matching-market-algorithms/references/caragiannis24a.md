---
title: "Can a Few Decide for Many? The Metric Distortion of Sortition"
source: "https://proceedings.mlr.press/v235/caragiannis24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/caragiannis24a/caragiannis24a.pdf"
categories: ['online-learning-matching-market-algorithms', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['sortition', 'metric-distortion', 'representative-panels', 'social-choice']
venue: "ICML 2024"
tldr: "Analyzes the metric distortion of sortition panels, showing they can approximately reflect full population opinions under mild conditions."
---

# Can a Few Decide for Many? The Metric Distortion of Sortition

**Source**: [https://proceedings.mlr.press/v235/caragiannis24a.html](https://proceedings.mlr.press/v235/caragiannis24a.html)

**TLDR**: Analyzes the metric distortion of sortition panels, showing they can approximately reflect full population opinions under mild conditions.

## Abstract

Recent works have studied the design of algorithms for selecting representative sortition panels. However, the most central question remains unaddressed: Do these panels reflect the entire population’s opinion? We present a positive answer by adopting the concept of metric distortion from computational social choice, which aims to quantify how much a panel’s decision aligns with the ideal decision of the population when preferences and agents lie on a metric space. We show that uniform selection needs only logarithmically many agents in terms of the number of alternatives to achieve almost optimal distortion. We also show that Fair Greedy Capture, a selection algorithm introduced recently by Ebadian and Micha (2024), matches uniform selection’s guarantees of almost optimal distortion and also achieves constant ex-post distortion, ensuring a “best of both worlds” performance.