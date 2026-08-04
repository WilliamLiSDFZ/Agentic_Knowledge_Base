---
title: "More Flexible PAC-Bayesian Meta-Learning by Learning Learning Algorithms"
source: "https://proceedings.mlr.press/v235/zakerinia24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zakerinia24a/zakerinia24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'online-learning-and-sequential-decision-making']
tags: ['PAC-Bayes', 'meta-learning', 'learning-algorithms', 'generalization']
venue: "ICML 2024"
tldr: "A flexible PAC-Bayesian meta-learning framework that allows direct transfer of learning algorithms across tasks beyond shared parameter initialization."
---

# More Flexible PAC-Bayesian Meta-Learning by Learning Learning Algorithms

**Source**: [https://proceedings.mlr.press/v235/zakerinia24a.html](https://proceedings.mlr.press/v235/zakerinia24a.html)

**TLDR**: A flexible PAC-Bayesian meta-learning framework that allows direct transfer of learning algorithms across tasks beyond shared parameter initialization.

## Abstract

We introduce a new framework for studying meta-learning methods using PAC-Bayesian theory. Its main advantage over previous work is that it allows for more flexibility in how the transfer of knowledge between tasks is realized. For previous approaches, this could only happen indirectly, by means of learning prior distributions over models. In contrast, the new generalization bounds that we prove express the process of meta-learning much more directly as learning the learning algorithm that should be used for future tasks. The flexibility of our framework makes it suitable to analyze a wide range of meta-learning mechanisms and even design new mechanisms. Other than our theoretical contributions we also show empirically that our framework improves the prediction quality in practical meta-learning mechanisms.