---
title: "On the Independence Assumption in Neurosymbolic Learning"
source: "https://proceedings.mlr.press/v235/van-krieken24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/van-krieken24a/van-krieken24a.pdf"
categories: ['probabilistic-generating-circuits-research', 'neural-symbolic-combinatorial-optimization-learning']
tags: ['neurosymbolic-learning', 'independence-assumption', 'probabilistic-reasoning']
venue: "ICML 2024"
tldr: "Analyzes the impact of the conditional independence assumption in neurosymbolic learning systems on learning and inference."
---

# On the Independence Assumption in Neurosymbolic Learning

**Source**: [https://proceedings.mlr.press/v235/van-krieken24a.html](https://proceedings.mlr.press/v235/van-krieken24a.html)

**TLDR**: Analyzes the impact of the conditional independence assumption in neurosymbolic learning systems on learning and inference.

## Abstract

State-of-the-art neurosymbolic learning systems use probabilistic reasoning to guide neural networks towards predictions that conform to logical constraints. Many such systems assume that the probabilities of the considered symbols are conditionally independent given the input to simplify learning and reasoning. We study and criticise this assumption, highlighting how it can hinder optimisation and prevent uncertainty quantification. We prove that loss functions bias conditionally independent neural networks to become overconfident in their predictions. As a result, they are unable to represent uncertainty over multiple valid options. Furthermore, we prove that the minima of such loss functions are usually highly disconnected and non-convex, and thus difficult to optimise. Our theoretical analysis gives the foundation for replacing the conditional independence assumption and designing more expressive neurosymbolic probabilistic models.