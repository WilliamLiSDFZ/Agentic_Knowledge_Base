---
title: "ByMI: Byzantine Machine Identification with False Discovery Rate Control"
source: "https://proceedings.mlr.press/v235/qian24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/qian24b/qian24b.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['byzantine-fault-tolerance', 'distributed-learning', 'hypothesis-testing', 'false-discovery-rate', 'robust-estimation']
venue: "ICML 2024"
tldr: "A framework for identifying Byzantine machines in distributed learning with statistical false discovery rate guarantees."
---

# ByMI: Byzantine Machine Identification with False Discovery Rate Control

**Source**: [https://proceedings.mlr.press/v235/qian24b.html](https://proceedings.mlr.press/v235/qian24b.html)

**TLDR**: A framework for identifying Byzantine machines in distributed learning with statistical false discovery rate guarantees.

## Abstract

Various robust estimation methods or algorithms have been proposed to hedge against Byzantine failures in distributed learning. However, there is a lack of systematic approaches to provide theoretical guarantees of significance in detecting those Byzantine machines. In this paper, we develop a general detection procedure, ByMI, via error rate control to address this issue, which is applicable to many robust learning problems. The key idea is to apply the sample-splitting strategy on each worker machine to construct a score statistic integrated with a general robust estimation and then to utilize the symmetry property of those scores to derive a data-driven threshold. The proposed method is dimension insensitive and p-value free with the help of the symmetry property and can achieve false discovery rate control under mild conditions. Numerical experiments on both synthetic and real data validate the theoretical results and demonstrate the effectiveness of our proposed method on Byzantine machine identification.