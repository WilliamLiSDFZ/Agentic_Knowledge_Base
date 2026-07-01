---
title: "The Many Faces of Optimal Weak-to-Strong Learning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/5cc19d8570ebe171ffad101fef1e4dde-Abstract-Conference.html"
categories: ['machine-learning-theory-and-evaluation-methods', 'deep-learning-optimization-and-generalization-theory']
tags: ['boosting', 'weak-to-strong-learning', 'sample-complexity', 'voting-classifiers']
venue: "NeurIPS 2024"
tldr: "Presents a new sample-optimal boosting algorithm with provably optimal sample complexity for combining weak classifiers."
---

# The Many Faces of Optimal Weak-to-Strong Learning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/5cc19d8570ebe171ffad101fef1e4dde-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/5cc19d8570ebe171ffad101fef1e4dde-Abstract-Conference.html)

**TLDR**: Presents a new sample-optimal boosting algorithm with provably optimal sample complexity for combining weak classifiers.

## Abstract

Boosting is an extremely successful idea, allowing one to combine multiple low accuracy classifiers into a much more accurate voting classifier. In this work, we present a new and surprisingly simple Boosting algorithm that obtains a provably optimal sample complexity. Sample optimal Boosting algorithms have only recently been developed, and our new algorithm has the fastest runtime among all such algorithms and is the simplest to describe: Partition your training data into 5 disjoint pieces of equal size, run AdaBoost on each, and combine the resulting classifiers via a majority vote. In addition to this theoretical contribution, we also perform the first empirical comparison of the proposed sample optimal Boosting algorithms. Our pilot empirical study suggests that our new algorithm might outperform previous algorithms on large data sets.