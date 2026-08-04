---
title: "Fast Co-Training under Weak Dependence via Stream-Based Active Learning"
source: "https://proceedings.mlr.press/v235/diakonikolas24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/diakonikolas24b/diakonikolas24b.pdf"
categories: ['data-selection-and-active-learning-methods', 'online-learning-and-sequential-decision-making']
tags: ['co-training', 'semi-supervised-learning', 'active-learning', 'stream-based', 'weak-dependence']
venue: "ICML 2024"
tldr: "Develops efficient co-training algorithms under weak dependence via stream-based active learning, expanding the set of provably learnable hypothesis classes."
---

# Fast Co-Training under Weak Dependence via Stream-Based Active Learning

**Source**: [https://proceedings.mlr.press/v235/diakonikolas24b.html](https://proceedings.mlr.press/v235/diakonikolas24b.html)

**TLDR**: Develops efficient co-training algorithms under weak dependence via stream-based active learning, expanding the set of provably learnable hypothesis classes.

## Abstract

Co-training is a classical semi-supervised learning method which only requires a small number of labeled examples for learning, under reasonable assumptions. Despite extensive literature on the topic, very few hypothesis classes are known to be provably efficiently learnable via co-training, even under very strong distributional assumptions. In this work, we study the co-training problem in the stream-based active learning model. We show that a range of natural concept classes are efficiently learnable via co-training, in terms of both label efficiency and computational efficiency. We provide an efficient reduction of co-training under the standard assumption of weak dependence, in the stream-based active model, to online classification. As a corollary, we obtain efficient co-training algorithms with error independent label complexity for every concept class class efficiently learnable in the mistake bound online model. Our framework also gives co-training algorithms with label complexity $\tilde{O}(d\log (1/\epsilon))$ for any concept class with VC dimension $d$, though in general this reduction is not computationally efficient. Finally, using additional ideas from online learning, we design the first efficient co-training algorithms with label complexity $\tilde{O}(d^2\log (1/\epsilon))$ for several concept classes, including unions of intervals and homogeneous halfspaces.