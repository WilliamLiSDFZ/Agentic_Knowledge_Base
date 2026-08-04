---
title: "Bounded and Uniform Energy-based Out-of-distribution Detection for Graphs"
source: "https://proceedings.mlr.press/v235/yang24n.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24n/yang24n.pdf"
categories: ['anomaly-and-out-of-distribution-detection', 'graph-neural-networks-and-topology']
tags: ['out-of-distribution-detection', 'graph-neural-networks', 'energy-based']
venue: "ICML 2024"
tldr: "A bounded and uniform energy-based framework for improving out-of-distribution detection in graph neural networks."
---

# Bounded and Uniform Energy-based Out-of-distribution Detection for Graphs

**Source**: [https://proceedings.mlr.press/v235/yang24n.html](https://proceedings.mlr.press/v235/yang24n.html)

**TLDR**: A bounded and uniform energy-based framework for improving out-of-distribution detection in graph neural networks.

## Abstract

Given the critical role of graphs in real-world applications and their high-security requirements, improving the ability of graph neural networks (GNNs) to detect out-of-distribution (OOD) data is an urgent research problem. The recent work GNNSAFE proposes a framework based on the aggregation of negative energy scores that significantly improves the performance of GNNs to detect node-level OOD data. However, our study finds that score aggregation among nodes is susceptible to extreme values due to the unboundedness of the negative energy scores and logit shifts, which severely limits the accuracy of GNNs in detecting node-level OOD data. In this paper, we propose NODESAFE: reducing the generation of extreme scores of nodes by adding two optimization terms that make the negative energy scores bounded and mitigate the logit shift. Experimental results show that our approach dramatically improves the ability of GNNs to detect OOD data at the node level, e.g., in detecting OOD data induced by Structure Manipulation, the metric of FPR95 (lower is better) in scenarios without (with) OOD data exposure are reduced from the current SOTA by 28.4% ( 22.7% ). The code is available via https://github.com/ShenzhiYang2000/NODESAFE-Bounded-and-Uniform-Energy-based-Out-of-distribution-Detection-for-Graphs.