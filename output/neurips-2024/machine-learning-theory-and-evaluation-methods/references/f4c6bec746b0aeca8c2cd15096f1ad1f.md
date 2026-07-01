---
title: "Weak Supervision Performance Evaluation via Partial Identification"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/f4c6bec746b0aeca8c2cd15096f1ad1f-Abstract-Conference.html"
categories: ['machine-learning-theory-and-evaluation-methods']
tags: ['weak-supervision', 'partial-identification', 'performance-evaluation']
venue: "NeurIPS 2024"
tldr: "Proposes a partial identification approach to evaluate model performance under programmatic weak supervision without ground truth labels."
---

# Weak Supervision Performance Evaluation via Partial Identification

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/f4c6bec746b0aeca8c2cd15096f1ad1f-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/f4c6bec746b0aeca8c2cd15096f1ad1f-Abstract-Conference.html)

**TLDR**: Proposes a partial identification approach to evaluate model performance under programmatic weak supervision without ground truth labels.

## Abstract

Programmatic Weak Supervision (PWS) enables supervised model training without direct access to ground truth labels, utilizing weak labels from heuristics, crowdsourcing, or pre-trained models. However, the absence of ground truth complicates model evaluation, as traditional metrics such as accuracy, precision, and recall cannot be directly calculated. In this work, we present a novel method to address this challenge by framing model evaluation as a partial identification problem and estimating performance bounds using Fréchet bounds. Our approach derives reliable bounds on key metrics without requiring labeled data, overcoming core limitations in current weak supervision evaluation techniques. Through scalable convex optimization, we obtain accurate and computationally efficient bounds for metrics including accuracy, precision, recall, and F1-score, even in high-dimensional settings. This framework offers a robust approach to assessing model quality without ground truth labels, enhancing the practicality of weakly supervised learning for real-world applications.