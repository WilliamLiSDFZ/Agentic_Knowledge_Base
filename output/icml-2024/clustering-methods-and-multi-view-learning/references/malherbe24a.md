---
title: "Measures of diversity and space-filling designs for categorical data"
source: "https://proceedings.mlr.press/v235/malherbe24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/malherbe24a/malherbe24a.pdf"
categories: ['sampling-compression-and-dimensionality-reduction', 'clustering-methods-and-multi-view-learning']
tags: ['diversity-measures', 'categorical-data', 'space-filling-designs']
venue: "ICML 2024"
tldr: "New measures of diversity and space-filling designs tailored for categorical data to enable representative subset selection."
---

# Measures of diversity and space-filling designs for categorical data

**Source**: [https://proceedings.mlr.press/v235/malherbe24a.html](https://proceedings.mlr.press/v235/malherbe24a.html)

**TLDR**: New measures of diversity and space-filling designs tailored for categorical data to enable representative subset selection.

## Abstract

Selecting a small subset of items that represent the diversity of a larger population lies at the heart of many data analysis and machine learning applications. However, when it comes to items described by discrete features, the lack of natural ordering and the combinatorial nature of the search space pose significant challenges to the current selection techniques and make existing methods ill-suited. In this paper, we propose to make a step in that direction by proposing novel methods to select subsets of diverse categorical data based on the advances in combinatorial optimization. First, we start to cast the subset selection problem through the lens of the optimization of three diversity metrics. We then provide novel bounds for this problem and present exact solvers that unfortunately come with a high computational cost. To overcome this bottleneck, we go on and show how to employ tools from linear programming and submodular optimization by introducing two computationally plausible methods that still present approximation guarantees about the diversity metrics. Finally, a numerical assessment is provided to illustrate the potential of the designs with respect to state-of-the-art methods.