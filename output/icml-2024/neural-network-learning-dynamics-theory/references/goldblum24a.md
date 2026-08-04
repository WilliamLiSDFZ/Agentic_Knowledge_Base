---
title: "Position: The No Free Lunch Theorem, Kolmogorov Complexity, and the Role of Inductive Biases in Machine Learning"
source: "https://proceedings.mlr.press/v235/goldblum24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/goldblum24a/goldblum24a.pdf"
categories: ['position-papers-on-ml-research-directions', 'neural-network-learning-dynamics-theory']
tags: ['no-free-lunch', 'kolmogorov-complexity', 'inductive-bias']
venue: "ICML 2024"
tldr: "This position paper reexamines no-free-lunch theorems through Kolmogorov complexity to clarify the role of inductive biases in machine learning."
---

# Position: The No Free Lunch Theorem, Kolmogorov Complexity, and the Role of Inductive Biases in Machine Learning

**Source**: [https://proceedings.mlr.press/v235/goldblum24a.html](https://proceedings.mlr.press/v235/goldblum24a.html)

**TLDR**: This position paper reexamines no-free-lunch theorems through Kolmogorov complexity to clarify the role of inductive biases in machine learning.

## Abstract

No free lunch theorems for supervised learning state that no learner can solve all problems or that all learners achieve exactly the same accuracy on average over a uniform distribution on learning problems. Accordingly, these theorems are often referenced in support of the notion that individual problems require specially tailored inductive biases. While virtually all uniformly sampled datasets have high complexity, real-world problems disproportionately generate low-complexity data, and we argue that neural network models share this same preference, formalized using Kolmogorov complexity. Notably, we show that architectures designed for a particular domain, such as computer vision, can compress datasets on a variety of seemingly unrelated domains. Our experiments show that pre-trained and even randomly initialized language models prefer to generate low-complexity sequences. Whereas no free lunch theorems seemingly indicate that individual problems require specialized learners, we explain how tasks that often require human intervention such as picking an appropriately sized model when labeled data is scarce or plentiful can be automated into a single learning algorithm. These observations justify the trend in deep learning of unifying seemingly disparate problems with an increasingly small set of machine learning models.