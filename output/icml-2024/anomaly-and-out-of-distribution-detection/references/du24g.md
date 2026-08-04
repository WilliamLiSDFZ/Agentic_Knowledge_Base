---
title: "When and How Does In-Distribution Label Help Out-of-Distribution Detection?"
source: "https://proceedings.mlr.press/v235/du24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/du24g/du24g.pdf"
categories: ['anomaly-and-out-of-distribution-detection']
tags: ['out-of-distribution-detection', 'in-distribution-labels', 'anomaly-detection', 'classifier']
venue: "ICML 2024"
tldr: "An analysis of when and how in-distribution label information helps out-of-distribution detection, providing both theoretical and empirical insights."
---

# When and How Does In-Distribution Label Help Out-of-Distribution Detection?

**Source**: [https://proceedings.mlr.press/v235/du24g.html](https://proceedings.mlr.press/v235/du24g.html)

**TLDR**: An analysis of when and how in-distribution label information helps out-of-distribution detection, providing both theoretical and empirical insights.

## Abstract

Detecting data points deviating from the training distribution is pivotal for ensuring reliable machine learning. Extensive research has been dedicated to the challenge, spanning classical anomaly detection techniques to contemporary out-of-distribution (OOD) detection approaches. While OOD detection commonly relies on supervised learning from a labeled in-distribution (ID) dataset, anomaly detection may treat the entire ID data as a single class and disregard ID labels. This fundamental distinction raises a significant question that has yet to be rigorously explored: when and how does ID label help OOD detection? This paper bridges this gap by offering a formal understanding to theoretically delineate the impact of ID labels on OOD detection. We employ a graph-theoretic approach, rigorously analyzing the separability of ID data from OOD data in a closed-form manner. Key to our approach is the characterization of data representations through spectral decomposition on the graph. Leveraging these representations, we establish a provable error bound that compares the OOD detection performance with and without ID labels, unveiling conditions for achieving enhanced OOD detection. Lastly, we present empirical results on both simulated and real datasets, validating theoretical guarantees and reinforcing our insights.