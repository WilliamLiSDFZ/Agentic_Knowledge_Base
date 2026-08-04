---
title: "Ambiguity-Aware Abductive Learning"
source: "https://proceedings.mlr.press/v235/he24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/he24j/he24j.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'learning-with-imperfect-data-and-bias']
tags: ['abductive-learning', 'neuro-symbolic', 'uncertainty']
venue: "ICML 2024"
tldr: "Proposes an ambiguity-aware abductive learning framework that handles uncertainty in the abduction process for neuro-symbolic integration."
---

# Ambiguity-Aware Abductive Learning

**Source**: [https://proceedings.mlr.press/v235/he24j.html](https://proceedings.mlr.press/v235/he24j.html)

**TLDR**: Proposes an ambiguity-aware abductive learning framework that handles uncertainty in the abduction process for neuro-symbolic integration.

## Abstract

Abductive Learning (ABL) is a promising framework for integrating sub-symbolic perception and logical reasoning through abduction. In this case, the abduction process provides supervision for the perception model from the background knowledge. Nevertheless, this process naturally contains uncertainty, since the knowledge base may be satisfied by numerous potential candidates. This implies that the result of the abduction process, i.e., a set of candidates, is ambiguous; both correct and incorrect candidates are mixed in this set. The prior art of abductive learning selects the candidate that has the minimal inconsistency of the knowledge base. However, this method overlooks the ambiguity in the abduction process and is prone to error when it fails to identify the correct candidates. To address this, we propose Ambiguity-Aware Abductive Learning ($\textrm{A}^3\textrm{BL}$), which evaluates all potential candidates and their probabilities, thus preventing the model from falling into sub-optimal solutions. Both experimental results and theoretical analyses prove that $\textrm{A}^3\textrm{BL}$ markedly enhances ABL by efficiently exploiting the ambiguous abduced supervision.