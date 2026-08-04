---
title: "Triple Changes Estimator for Targeted Policies"
source: "https://proceedings.mlr.press/v235/akbari24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/akbari24a/akbari24a.pdf"
categories: ['difference-in-differences-based-policy-evaluation']
tags: ['triple-difference', 'difference-in-differences', 'parallel-trends', 'causal-inference', 'targeted-policies']
venue: "ICML 2024"
tldr: "Proposes a triple changes estimator extending DiD to targeted policies without requiring parallel trends assumptions."
---

# Triple Changes Estimator for Targeted Policies

**Source**: [https://proceedings.mlr.press/v235/akbari24a.html](https://proceedings.mlr.press/v235/akbari24a.html)

**TLDR**: Proposes a triple changes estimator extending DiD to targeted policies without requiring parallel trends assumptions.

## Abstract

The renowned difference-in-differences (DiD) estimator relies on the assumption of ’parallel trends,’ which may not hold in many practical applications. To address this issue, economists are increasingly considering the triple difference estimator as a more credible alternative. Both DiD and triple difference are limited to assessing average effects exclusively. An alternative avenue is offered by the changes-in-changes (CiC) estimator, which provides an estimate of the entire counterfactual distribution by relying on assumptions imposed on the distribution of potential outcomes. In this work, we extend the triple difference estimator to accommodate the CiC framework, presenting the ‘triple changes estimator’ and its identification assumptions, thereby expanding the scope of the CiC paradigm. Subsequently, we empirically evaluate the proposed framework and apply it to a study examining the impact of Medicaid expansion on children’s preventive care.