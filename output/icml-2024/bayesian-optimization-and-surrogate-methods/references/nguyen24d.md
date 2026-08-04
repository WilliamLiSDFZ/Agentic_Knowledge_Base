---
title: "Quality-Weighted Vendi Scores And Their Application To Diverse Experimental Design"
source: "https://proceedings.mlr.press/v235/nguyen24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nguyen24d/nguyen24d.pdf"
categories: ['bayesian-optimization-and-surrogate-methods']
tags: ['diversity-metrics', 'vendi-score', 'experimental-design']
venue: "ICML 2024"
tldr: "Quality-weighted Vendi scores are proposed to balance quality and diversity in experimental design for Bayesian optimization and active search."
---

# Quality-Weighted Vendi Scores And Their Application To Diverse Experimental Design

**Source**: [https://proceedings.mlr.press/v235/nguyen24d.html](https://proceedings.mlr.press/v235/nguyen24d.html)

**TLDR**: Quality-weighted Vendi scores are proposed to balance quality and diversity in experimental design for Bayesian optimization and active search.

## Abstract

Experimental design techniques such as active search and Bayesian optimization are widely used in the natural sciences for data collection and discovery. However, existing techniques tend to favor exploitation over exploration of the search space, which causes them to get stuck in local optima. This collapse problem prevents experimental design algorithms from yielding diverse high-quality data. In this paper, we extend the Vendi scores—a family of interpretable similarity-based diversity metrics—to account for quality. We then leverage these quality-weighted Vendi scores to tackle experimental design problems across various applications, including drug discovery, materials discovery, and reinforcement learning. We found that quality-weighted Vendi scores allow us to construct policies for experimental design that flexibly balance quality and diversity, and ultimately assemble rich and diverse sets of high-performing data points. Our algorithms led to a 70%–170% increase in the number of effective discoveries compared to baselines.