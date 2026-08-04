---
title: "Analysis for Abductive Learning and Neural-Symbolic Reasoning Shortcuts"
source: "https://proceedings.mlr.press/v235/yang24ac.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24ac/yang24ac.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'neural-network-learning-dynamics-theory']
tags: ['abductive-learning', 'neural-symbolic', 'reasoning-shortcuts']
venue: "ICML 2024"
tldr: "An analysis of reasoning shortcuts in abductive and neural-symbolic learning models that reveals generalization failures from spurious concept-label correlations."
---

# Analysis for Abductive Learning and Neural-Symbolic Reasoning Shortcuts

**Source**: [https://proceedings.mlr.press/v235/yang24ac.html](https://proceedings.mlr.press/v235/yang24ac.html)

**TLDR**: An analysis of reasoning shortcuts in abductive and neural-symbolic learning models that reveals generalization failures from spurious concept-label correlations.

## Abstract

Abductive learning models (ABL) and neural-symbolic predictive models (NeSy) have been recently shown effective, as they allow us to infer labels that are consistent with some prior knowledge by reasoning over high-level concepts extracted from sub-symbolic inputs. However, their generalization ability is affected by reasoning shortcuts: high accuracy on given targets but leveraging intermediate concepts with unintended semantics. Although there have been techniques to alleviate reasoning shortcuts, theoretical efforts on this issue remain to be limited. This paper proposes a simple and effective analysis to quantify harm caused by it and how can mitigate it. We quantify three main factors in how NeSy algorithms are affected by reasoning shortcuts: the complexity of the knowledge base, the sample size, and the hypothesis space. In addition, we demonstrate that ABL can reduce shortcut risk by selecting specific distance functions in consistency optimization, thereby demonstrating its potential and approach to solving shortcut problems. Empirical studies demonstrate the rationality of the analysis. Moreover, the proposal is suitable for many ABL and NeSy algorithms and can be easily extended to handle other cases of reasoning shortcuts.