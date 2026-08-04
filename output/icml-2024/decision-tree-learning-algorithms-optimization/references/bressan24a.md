---
title: "Fully-Dynamic Approximate Decision Trees With Worst-Case Update Time Guarantees"
source: "https://proceedings.mlr.press/v235/bressan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bressan24a/bressan24a.pdf"
categories: ['dynamic-algorithms-and-complexity-theory', 'decision-tree-learning-algorithms-optimization']
tags: ['dynamic-algorithms', 'decision-trees', 'worst-case-update-time']
venue: "ICML 2024"
tldr: "First fully-dynamic algorithm for maintaining decision trees with worst-case update time guarantees under adversarial insertions and deletions."
---

# Fully-Dynamic Approximate Decision Trees With Worst-Case Update Time Guarantees

**Source**: [https://proceedings.mlr.press/v235/bressan24a.html](https://proceedings.mlr.press/v235/bressan24a.html)

**TLDR**: First fully-dynamic algorithm for maintaining decision trees with worst-case update time guarantees under adversarial insertions and deletions.

## Abstract

We study the problem of maintaining a decision tree in the fully-dynamic setting, where the dataset is updated by an adversarial sequence of insertions and deletions. We present the first algorithm with strong guarantees on both the quality of the tree and the worst-case update time (the maximum time spent between two consecutive dataset updates). For instance, we can maintain a tree where each node has Gini gain within $\beta$ of the optimum, while guaranteeing an update time $O(d \beta^{-3} \log^4 n )$, where $d$ is the number of features and $n$ the maximum size of the dataset. This is optimal up to polylogarithmic factors, as any dynamic algorithm must have update time in $\Omega(d)$. Similar guarantees hold for the variance and information gain, for classification and regression, and even for boosted trees. This shows that many popular decision trees such as ID3 or C4.5 can be efficiently be made dynamic, answering an open question of Bressan, Damay and Sozio (AAAI 2023). We also show that, under the 3SUM conjecture or the Orthogonal Vectors Hypothesis, the update time must be polynomial in $1/\beta$.